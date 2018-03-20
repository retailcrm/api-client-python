# coding=utf-8


"""
retailCRM API client v4 tests
"""

import unittest
import os
import retailcrm


class TestVersion4(unittest.TestCase):
    """
    TestClass for v4
    """

    def setUp(self):
        """
        Setup
        """
        self.client = retailcrm.v4(
            os.getenv('RETAILCRM_URL'), os.getenv('RETAILCRM_KEY'))

    def test_wrong_api_url(self):
        """
        V4 Test wrong api url
        """
        client = retailcrm.v4(
            'https://epoqwieqwpoieqpwoeiqpwoeiq.retailcrm.ru', '98sdf9sj8fsd9fjs9dfjs98')
        response = client.statistic_update()

        self.assertTrue(response.is_successful(), False)
        self.assertEqual(response.get_error_msg(), 'Account does not exist.')

    def test_wrong_api_key(self):
        """
        V4 Test wrong api key
        """
        client = retailcrm.v3(os.getenv('RETAILCRM_URL'),
                              '98sdf9sj8fsd9fjs9dfjs98')
        response = client.statistic_update()

        self.assertEqual(response.get_error_msg(), 'Wrong "apiKey" value.')

    def test_missing_api_key(self):
        """
        V4 Test missing api key
        """
        client = retailcrm.v4(os.getenv('RETAILCRM_URL'), None)
        response = client.statistic_update()

        self.assertEqual(response.get_error_msg(), '"apiKey" is missing.')

    def test_api_versions(self):
        """
        V4 Test api-versions method
        """
        response = self.client.api_versions()

        self.assertTrue(response.is_successful(), True)

    def test_api_credentials(self):
        """
        V4 Test api-credentials method
        """
        response = self.client.api_credentials()

        self.assertTrue(response.is_successful(), True)
