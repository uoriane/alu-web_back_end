#!/usr/bin/env python3
"""
Module for filtering and logging personal data securely.
"""
import logging
import os
import re
from typing import List, Tuple
import mysql.connector
from mysql.connector.connection import MySQLConnection

PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Returns the log message obfuscated for specified fields using a single regex.
    """
    pattern = f"({'|'.join(fields)})=([^{separator}]*)(?={separator})"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class to filter sensitive values in logs.
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: Tuple[str, ...]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Filter values in incoming log records using filter_datum.
        """
        original_message = super().format(record)
        return filter_datum(
            list(self.fields), self.REDACTION, original_message, self.SEPARATOR
        )


def get_logger() -> logging.Logger:
    """
    Returns a logging.Logger object configured for PII redaction.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> MySQLConnection:
    """
    Returns a connector to the MySQL database using environment variables.
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME", "")

    db_connection = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )
    return db_connection


def main() -> None:
    """
    Retrieves all rows in the users table and displays them under a filtered format.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT name, email, phone, ssn, password, ip, last_login, user_agent FROM users;"
    )
    logger = get_logger()

    fields = ["name", "email", "phone", "ssn", "password", "ip", "last_login", "user_agent"]
    for row in cursor:
        row_str = ";".join([f"{fields[i]}={row[i]}" for i in range(len(fields))]) + ";"
        logger.info(row_str)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
