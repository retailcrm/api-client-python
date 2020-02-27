# coding=utf-8


"""
retailCRM API client v5 tests
"""

import unittest
import os
import random
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

        self.assertIsNot(response.is_successful(), True)
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

    def test_set_user_status(self):
        response = self.client.user_status(os.getenv('RETAILCRM_USER'), 'dinner')

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    def test_check_order_payment(self):
        rand = random.randint(10000, 99999)
        ex_id = 'test-case-payment' + str(rand)
        order = {
            'firstName': 'John',
            'lastName': 'Doe',
            'phone': '+79000000000',
            'email': 'john@example.com',
            'orderMethod': 'call-request',
            'delivery': {
                'code': 'self-delivery'
            },
            'payments': [
                {
                    'externalId': ex_id,
                    'amount': 100,
                    'type': 'cash'
                }
            ]
        }

        response = self.client.order_create(order)

        response_data = response.get_response()
        payment_id = response_data['order']['payments'][0]['id']
        print(payment_id)

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

        payment_response = self.client.order_payment_edit({'externalId': ex_id, 'status': 'invoice'}, 'externalId')

        self.assertTrue(payment_response.is_successful(), True)
        self.assertTrue(payment_response.get_status_code() < 400, True)

        payment_response = self.client.order_payment_edit({'id': payment_id, 'status': 'paid'})

        self.assertTrue(payment_response.is_successful(), True)
        self.assertTrue(payment_response.get_status_code() < 400, True)
