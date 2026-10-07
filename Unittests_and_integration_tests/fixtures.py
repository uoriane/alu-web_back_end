#!/usr/bin/env python3
"""Fixtures for GithubOrgClient integration tests.
"""

TEST_PAYLOAD = [
    (
        {"repos_url": "https://api.github.com/orgs/google/repos"},
        [
            {
                "id": 7697149,
                "name": "episodes.dart",
                "full_name": "google/episodes.dart",
                "license": {
                    "key": "bsd-3-clause",
                    "name": "BSD 3-Clause \"New\" or \"Revised\" License"
                }
            },
            {
                "id": 7776515,
                "name": "cpp-netlib",
                "full_name": "google/cpp-netlib",
                "license": {
                    "key": "bsl-1.0",
                    "name": "Boost Software License 1.0"
                }
            },
            {
                "id": 7968417,
                "name": "dagger",
                "full_name": "google/dagger",
                "license": {
                    "key": "apache-2.0",
                    "name": "Apache License 2.0"
                }
            }
        ],
        ["episodes.dart", "cpp-netlib", "dagger"],
        ["dagger"]
    )
]
