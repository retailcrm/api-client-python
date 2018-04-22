# coding=utf-8


"""
retailCRM API client v5 tests
"""

import unittest
import os
import retailcrm


class TestVersion5(unittest.TestCase):
    """
    TestClass for v5
    """

    def setUp(self):
        """
        Setup
        """
        self.client = retailcrm.v5(
            os.getenv('RETAILCRM_URL'), os.getenv('RETAILCRM_KEY'))

    def test_wrong_api_url(self):
        """
        V5 Test wrong api url
        """
        client = retailcrm.v5(
            'https://epoqwieqwpoieqpwoeiqpwoeiq.retailcrm.ru', '98sdf9sj8fsd9fjs9answer98')
        response = client.statistic_update()

        self.assertTrue(response.is_successful(), False)
        self.assertEqual(response.get_error_msg(), 'Account does not exist.')

    def test_wrong_api_key(self):
        """
        V5 Test wrong api key
        """
        client = retailcrm.v5(os.getenv('RETAILCRM_URL'), '98sdf9sj8fsd9fjs9answer98')
        response = client.statistic_update()

        self.assertEqual(response.get_error_msg(), 'Wrong "apiKey" value.')

    def test_missing_api_key(self):
        """
        V5 Test missing api key
        """
        client = retailcrm.v5(os.getenv('RETAILCRM_URL'), None)
        response = client.statistic_update()

        self.assertEqual(response.get_error_msg(), '"apiKey" is missing.')

    def test_api_versions(self):
        """
        V5 Test api-versions method
        """
        response = self.client.api_versions()

        self.assertTrue(response.is_successful(), True)

    def test_api_credentials(self):
        """
        V5 Test api-credentials method
        """
        response = self.client.api_credentials()

        self.assertTrue(response.is_successful(), True)

    # def test_telephony_calls_upload(self):
    #     """
    #     V5 Test telephony calls upload
    #     """
    #
    #     calls = [
    #         {
    #             'date': '2018-04-20 22:10:00',
    #             'type': 'in',
    #             'phone': '+79999999999',
    #             'userId': os.getenv('RETAILCRM_USER'),
    #             'result': 'answered'
    #          },
    #         {
    #             'date': '2018-04-20 22:10:00',
    #             'type': 'out',
    #             'phone': '+79999999999',
    #             'userId': os.getenv('RETAILCRM_USER'),
    #             'result': 'answered'
    #         }
    #     ]
    #
    #     response = self.client.telephony_calls_upload(calls)
    #
    #     self.assertTrue(response.is_successful(), True)
    #     self.assertTrue(response.get_status_code() < 400, True)

    def test_set_user_status(self):
        response = self.client.user_status(os.getenv('RETAILCRM_USER'), 'dinner')

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)
