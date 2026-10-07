#!/usr/bin/env python3
""" Unit and integration tests for client.py
"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Unit test case for GithubOrgClient class
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ Test that GithubOrgClient.org returns the correct value
        """
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """ Test that _public_repos_url returns expected URL
        """
        with patch.object(
            GithubOrgClient,
            'org',
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                'repos_url': 'https://api.github.com/orgs/google/repos'
            }
            test_client = GithubOrgClient('google')
            self.assertEqual(
                test_client._public_repos_url,
                'https://api.github.com/orgs/google/repos'
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Test GithubOrgClient.public_repos
        """
        test_payload = [
            {"name": "episodes.dart"},
            {"name": "cpp-netlib"},
        ]
        mock_get_json.return_value = test_payload

        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                'https://api.github.com/orgs/google/repos'
            )
            test_client = GithubOrgClient('google')
            res = test_client.public_repos()

            self.assertEqual(res, ["episodes.dart", "cpp-netlib"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test GithubOrgClient.has_license static method
        """
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected
        )


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test case for GithubOrgClient
    """

    @classmethod
    def setUpClass(cls):
        """ Set up class fixtures before running tests
        """
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                mock_resp = Mock()
                mock_resp.json.return_value = route_payload[url]
                return mock_resp
            return Mock()

        cls.get_patcher = patch('requests.get', side_effect=get_payload)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ Tear down class fixtures after tests run
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Integration test for public_repos method
        """
        test_client = GithubOrgClient('google')
        self.assertEqual(test_client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """ Integration test for public_repos with license filtering
        """
        test_client = GithubOrgClient('google')
        self.assertEqual(
            test_client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )


if __name__ == '__main__':
    unittest.main()
