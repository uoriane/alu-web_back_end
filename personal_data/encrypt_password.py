#!/usr/bin/env python3
"""
Module for password hashing and validation using bcrypt.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Expects a password string and returns a salted, hashed password byte string.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that the provided password matches the hashed password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
