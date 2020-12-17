# coding=utf-8


"""
RetailCRM API client v3 tests
"""

from urllib.parse import urlencode
import unittest
import os
import retailcrm
import pook
import json


class TestVersion3(unittest.TestCase):
    """
    TestClass for v3
    """

    __header = {'Server': 'nginx/1.16.0', 'Content-Type': 'application/json; charset=UTF-8'}

    __customer = {
        'id': 9717,
        'externalId': 'c-111111111',
        'createdAt': '2020-04-09 16:55:59',
        'vip': 'false',
        'bad': 'false',
        'site': 'test-org',
        'marginSumm': 28180,
        'totalSumm': 28180,
        'averageSumm': 28180,
        'ordersCount': 1,
        'customFields': [],
        'personalDiscount': 0,
        'address': {
            'id': 5667,
            'text': 'MAY'
        },
        'firstName': 'Аа',
        'lastName': 'Аа',
        'phones': [],
        'contragentType': 'individual'
    }

    __order = {
        'slug': 5604,
        'summ': 0,
        'id': 5604,
        'number': '5604A',
        'externalId': '5603',
        'orderType': 's789',
        'orderMethod': 'shopping-cart',
        'countryIso': 'RU',
        'createdAt': '2020-04-07 15:44:24',
        'statusUpdatedAt': '2020-04-07 15:44:24',
        'totalSumm': 0,
        'prepaySum': 0,
        'purchaseSumm': 0,
        'markDatetime': '2020-04-07 15:44:24',
        'call': 'false',
        'expired': 'false',
        'customer': {
            'id': 9711,
            'createdAt': '2020-04-07 15:44:24',
            'vip': 'false',
            'bad': 'false',
            'site': '127-0-0-1-8080',
            'marginSumm': 0,
            'totalSumm': 0,
            'averageSumm': 0,
            'ordersCount': 1,
            'customFields': [],
            'personalDiscount': 0,
            'email': '',
            'phones': [],
            'contragentType': 'individual'
        },
        'contragentType': 'individual',
        'delivery': {
            'cost': 0,
            'netCost': 0,
            'address': {}
        },
        'site': '127-0-0-1-8080',
        'status': 'new',
        'items': [],
        'fromApi': 'true',
        'shipped': 'false',
        'customFields': []
    }

    __pack = {
        'id': 122,
        'purchasePrice': 0,
        'quantity': 1,
        'store': '7777z',
        'item': {
            'id': 7632,
            'order': {
                'id': 5608
            },
            'offer': {
                'externalId': 's789'
            }
        }
    }

    def setUp(self):
        """
        Setup
        """

        self.client = retailcrm.v3(os.getenv('RETAILCRM_URL'), os.getenv('RETAILCRM_KEY'))

    @staticmethod
    def dictionaryEncode(key, dictionary):
        return urlencode({key: json.dumps(dictionary)})

    @pook.on
    def test_wrong_api_url(self):
        """
        V3 Test wrong api url
        """

        (pook.get('https://epoqq.retailcrm.pro' + '/api/v3/statistic/update')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(404)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'errorMsg': 'Account does not exist.'
                }
        )
        )

        client = retailcrm.v3('https://epoqq.retailcrm.pro', os.getenv('RETAILCRM_KEY'))
        response = client.statistic_update()
        pook.off()

        self.assertIsNot(response.is_successful(), True)
        self.assertEqual(response.get_error_msg(), 'Account does not exist.')

    @pook.on
    def test_wrong_api_key(self):
        """
        V3 Test wrong api key
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/statistic/update')
         .headers({'X-API-KEY': 'XXXX'})
         .reply(200)
         .headers(self.__header)
         .json({'errorMsg': 'Wrong "apiKey" value.'})
         )

        client = retailcrm.v3(os.getenv('RETAILCRM_URL'), 'XXXX')
        response = client.statistic_update()
        pook.off()

        self.assertEqual(response.get_error_msg(), 'Wrong "apiKey" value.')

    @pook.on
    def test_missing_api_key(self):
        """
        V3 Test missing api key
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/statistic/update')
         .headers({'X-API-KEY': None})
         .reply(200)
         .headers(self.__header)
         .json({'errorMsg': '"apiKey" is missing.'})
         )

        client = retailcrm.v3(os.getenv('RETAILCRM_URL'), None)
        response = client.statistic_update()
        pook.off()

        self.assertEqual(response.get_error_msg(), '"apiKey" is missing.')

    @pook.on
    def test_api_versions(self):
        """
        V3 Test api-versions method
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/api-versions')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'versions': ['3.0', '4.0', '5.0']})
         )

        response = self.client.api_versions()
        pook.off()

        self.assertTrue(response.is_successful(), True)

    @pook.on
    def test_api_credentials(self):
        """
        V3 Test api-credentials method
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/credentials')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'credentials': [], 'siteAccess': 'access_full'})
         )

        response = self.client.api_credentials()
        pook.off()

        self.assertTrue(response.is_successful(), True)

    @pook.on
    def test_customers(self):
        """
        V3 Test method customers
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/customers')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[bad]': 'false', 'filter[contragentType]': 'individual'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': 20,
                        'totalCount': 4342,
                        'currentPage': 1,
                        'totalPageCount': 87
                    },
                    'customers': [self.__customer]
                }
        )
        )

        response = self.client.customers({'bad': 'false', 'contragentType': 'individual'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customers_create(self):
        """
        V3 Test method customers_create
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/customers/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('customer', self.__customer))
         .reply(201)
         .headers(self.__header)
         .json({'success': 'true', 'id': 7777})
         )

        response = self.client.customer_create(self.__customer)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customers_fix_external_ids(self):
        """
        V3 Test method customers_fix_external_ids
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/customers/fix-external-ids')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('customers', self.__customer['externalId']))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.customers_fix_external_ids(self.__customer['externalId'])
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customers_upload(self):
        """
        V3 Test method customers_upload
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/customers/upload')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .body(self.dictionaryEncode('customers', self.__customer))
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'uploadedCustomers': [
                        {
                            'id': 9717,
                            'externalId': 'c-983344770'
                        }
                    ]
                }
        )
        )

        response = self.client.customers_upload(self.__customer)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customer(self):
        """
        V3 Test method customer
        """

        uid = str(self.__customer['externalId'])

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/customers/' + uid)
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'customers': self.__customer})
         )

        response = self.client.customer(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customers_edit(self):
        """
        V3 Test method customers_edit
        """

        uid = str(self.__customer['externalId'])

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/customers/' + uid + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('customer', self.__customer))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'id': 9717})
         )

        response = self.client.customer_edit(self.__customer)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_orders(self):
        """
        V3 Test method orders
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/orders')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[bad]': 'false', 'filter[contragentType]': 'individual'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': 20,
                        'totalCount': 2444,
                        'currentPage': 1,
                        'totalPageCount': 49
                    },
                    'orders': [self.__order]
                }
        )
        )

        response = self.client.orders({'bad': 'false', 'contragentType': 'individual'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_orders_create(self):
        """
        V3 Test method orders_create
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/orders/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('order', self.__order))
         .reply(201)
         .headers(self.__header)
         .json({'success': 'true', 'id': 7777, 'order': self.__order})
         )

        response = self.client.order_create(self.__order)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_orders_fix_external_ids(self):
        """
        V3 Test method orders_fix_external_ids
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/orders/fix-external-ids')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('orders', self.__order['externalId']))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.orders_fix_external_ids(self.__order['externalId'])
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_orders_history(self):
        """
        V3 Test method orders_history
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/orders/history')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'startDate': '2020-01-07', 'endDate': '2020-04-12'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'generatedAt': '2020-04-12 15:44:24',
                    'orders': [self.__order]
                }
        )
        )

        response = self.client.orders_history('2020-01-07', '2020-04-12')
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_orders_statuses(self):
        """
        V3 Test method orders_statuses
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/orders/statuses')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'ids[]': '5604', 'externalIds[]': '5603'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'orders': [
                        {
                            'id': 5604,
                            'externalId': '5603',
                            'status': 'new',
                            'group': 'new'
                        }
                    ]
                }
        )
        )

        response = self.client.orders_statuses([5604], [5603])
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_orders_upload(self):
        """
        V3 Test method orders_upload
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/orders/upload')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .body(self.dictionaryEncode('orders', self.__order))
            .reply(201)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'uploadedOrders': [
                        {
                            'id': 5604,
                            'externalId': '5603'
                        }
                    ],
                    'orders': [self.__order]
                }
        )
        )

        response = self.client.orders_upload(self.__order)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_order(self):
        """
        V3 Test method order
        """

        uid = str(self.__order['externalId'])

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/orders/' + uid)
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'orders': self.__order})
         )

        response = self.client.order(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_orders_edit(self):
        """
        V3 Test method orders_edit
        """

        uid = str(self.__order['externalId'])

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/orders/' + uid + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('order', self.__order))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'id': 5604, 'order': self.__order})
         )

        response = self.client.order_edit(self.__order)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_packs(self):
        """
        V3 Test method packs
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/orders/packs')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[store]': '7777z'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': 20,
                        'totalCount': 1,
                        'currentPage': 1,
                        'totalPageCount': 1
                    },
                    'packs': [self.__pack]
                }
        )
        )

        response = self.client.packs({'store': '7777z'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_packs_create(self):
        """
        V3 Test method packs_create
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/orders/packs/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('pack', {'store': '7777z', 'quantity': 1, 'itemId': 7632}))
         .reply(201)
         .headers(self.__header)
         .json({'success': 'true', 'id': 7777})
         )

        response = self.client.pack_create({'store': '7777z', 'quantity': 1, 'itemId': 7632})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_packs_history(self):
        """
        V3 Test method packs_history
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/orders/packs/history')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[startDate]': '2016-01-07', 'filter[endDate]': '2020-04-12'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'generatedAt': '2020-04-17 13:08:48',
                    'history': [
                        {
                            'id': 777,
                            'createdAt': '2018-04-13 15:46:06',
                            'created': 'true',
                            'field': 'store',
                            'newValue': {
                                'code': 'zzz'
                            },
                            'pack': {
                                'id': 678,
                                'quantity': 1,
                                'store': {'code': 'zzz'},
                                'item': {
                                    'id': 222,
                                    'order': {'id': 6677},
                                    'offer': {'externalId': '333'}
                                }
                            },
                            'source': 'api'
                        }
                    ]
                }
        )
        )

        response = self.client.packs_history({'startDate': '2016-01-07', 'endDate': '2020-04-12'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_pack(self):
        """
        V3 Test method pack
        """

        uid = str(self.__pack['id'])

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/orders/packs/' + uid)
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'pack': self.__pack})
         )

        response = self.client.pack(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_packs_delete(self):
        """
        V3 Test method packs_delete
        """

        uid = str(self.__pack['id'])

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/orders/packs/' + uid + '/delete')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.pack_delete(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_pack_edit(self):
        """
        V3 Test method pack_edit
        """

        uid = str(self.__pack['id'])

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/orders/packs/' + uid + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('pack', self.__pack))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'id': 5604})
         )

        response = self.client.pack_edit(self.__pack)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_countries(self):
        """
        V3 Test method countries
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/reference/countries')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'countriesIso': ['RU', 'UA', 'BY', 'KZ']})
         )

        response = self.client.countries()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_delivery_services(self):
        """
        V3 Test method delivery_services
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/reference/delivery-services')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'deliveryServices': {
                        '0tq6d': {
                            'name': '57jij',
                            'code': '0tq6d'
                        },
                        'a080k': {
                            'name': 's789',
                            'code': 'a080k'
                        },
                        'a6zgf': {
                            'name': 'eu8ss',
                            'code': 'a6zgf'
                        }
                    }
                }
        )
        )

        response = self.client.delivery_services()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_delivery_services_edit(self):
        """
        V3 Test method delivery_services_edit
        """

        service = {'code': 'a080k', 'name': 's789'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/reference/delivery-services/' + service['code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('deliveryService', service))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.delivery_services_edit(service)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_delivery_types(self):
        """
        V3 Test method delivery_types
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/reference/delivery-types')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(201)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'deliveryTypes': {
                        '1kp52': {
                            'name': 's789',
                            'code': '1kp52',
                            'defaultCost': 300,
                            'defaultNetCost': 0,
                            'paymentTypes': [
                                'cash',
                                'bank-card'
                            ],
                            'deliveryServices': [],
                            'defaultForCrm': 'false'
                        },
                        's789': {
                            'name': '1s0ei',
                            'code': 's789',
                            'defaultCost': 300,
                            'defaultNetCost': 0,
                            'paymentTypes': [
                                'cash',
                                'bank-card'
                            ],
                            'deliveryServices': [],
                            'defaultForCrm': 'false'
                        }
                    }
                }
        )
        )

        response = self.client.delivery_types()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_delivery_types_edit(self):
        """
        V3 Test method delivery_types_edit
        """

        delivery_type = {'code': 's789', 'name': '1s0ei'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/reference/delivery-types/' + delivery_type['code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('deliveryType', delivery_type))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.delivery_types_edit(delivery_type)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_order_methods(self):
        """
        V3 Test method order_methods
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/reference/order-methods')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'orderMethods': {
                        '1b4os': {
                            'name': '19le4',
                            'code': '1b4os',
                            'defaultForCrm': 'false',
                            'defaultForApi': 'false',
                            'isFromPos': 'false'
                        },
                        '44cmd': {
                            'name': '1tdf4',
                            'code': '44cmd',
                            'defaultForCrm': 'false',
                            'defaultForApi': 'false',
                            'isFromPos': 'false'
                        },
                        'zoc5q': {
                            'name': '1y0cp',
                            'code': 'zoc5q',
                            'defaultForCrm': 'false',
                            'defaultForApi': 'false',
                            'isFromPos': 'false'
                        }
                    }
                }
        )
        )

        response = self.client.order_methods()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_order_methods_edit(self):
        """
        V3 Test method order_methods_edit
        """

        method = {'code': 'zoc5q', 'name': '1y0cp'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/reference/order-methods/' + method['code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('orderMethod', method))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.order_methods_edit(method)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_order_types(self):
        """
        V3 Test method order_types
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/reference/order-types')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'orderTypes': {
                        's789': {
                            'name': 'test',
                            'code': 's789',
                            'defaultForCrm': 'true',
                            'defaultForApi': 'true',
                            'ordering': 990
                        },
                        'b7e20': {
                            'name': 'vwt5f',
                            'code': 'b7e20',
                            'defaultForCrm': 'false',
                            'defaultForApi': 'false',
                            'ordering': 990
                        }
                    }
                }
        )
        )

        response = self.client.order_types()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_order_types_edit(self):
        """
        V3 Test method order_types_edit
        """

        order_type = {'code': 's789', 'name': 'test'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/reference/order-types/' + order_type['code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('orderType', order_type))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.order_types_edit(order_type)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_payment_statuses(self):
        """
        V3 Test method payment_statuses
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/reference/payment-statuses')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'paymentStatuses': {
                        'invoice': {
                            'name': 'Выставлен счет',
                            'code': 'invoice',
                            'defaultForCrm': 'false',
                            'defaultForApi': 'false',
                            'paymentComplete': 'false',
                            'ordering': 20,
                            'paymentTypes': [
                                'bank-card',
                                'bank-transfer',
                                'credit',
                                'cash',
                                'e-money'
                            ]
                        },
                        'payment-start': {
                            'name': 'Платеж проведен',
                            'code': 'payment-start',
                            'defaultForCrm': 'false',
                            'defaultForApi': 'false',
                            'paymentComplete': 'false',
                            'ordering': 30,
                            'paymentTypes': [
                                'bank-card',
                                'bank-transfer',
                                'credit',
                                'cash',
                                'e-money'
                            ]
                        }
                    }
                }
        )
        )

        response = self.client.payment_statuses()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_payment_statuses_edit(self):
        """
        V3 Test method payment_statuses_edit
        """

        status = {'code': 'payment-start', 'name': 'Платеж проведен'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/reference/payment-statuses/' + status['code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('paymentStatus', status))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.payment_statuses_edit(status)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_payment_types(self):
        """
        V3 Test method payment_types
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/reference/payment-types')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'paymentTypes': {
                        '056a3e': {
                            'name': 'TestPaymentType-056a3e',
                            'code': '056a3e',
                            'defaultForCrm': 'false',
                            'defaultForApi': 'false',
                            'deliveryTypes': [],
                            'paymentStatuses': []
                        },
                        '238c06': {
                            'name': 'TestPaymentType-238c06',
                            'code': '238c06',
                            'defaultForCrm': 'false',
                            'defaultForApi': 'false',
                            'deliveryTypes': [],
                            'paymentStatuses': []
                        }
                    }
                }
        )
        )

        response = self.client.payment_types()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_payment_types_edit(self):
        """
        V3 Test method payment_types_edit
        """

        payment_type = {'code': '238c06', 'name': 'TestPaymentType-238c06'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/reference/payment-types/' + payment_type['code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('paymentType', payment_type))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.payment_types_edit(payment_type)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_product_statuses(self):
        """
        V3 Test method product_statuses
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/reference/product-statuses')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'productStatuses': {
                        'confirming': {
                            'code': 'confirming',
                            'ordering': 20,
                            'createdAt': '2018-04-10 12:33:58',
                            'cancelStatus': 'false',
                            'name': 'Подтверждение наличия'
                        },
                        'in-reserve': {
                            'code': 'in-reserve',
                            'ordering': 30,
                            'createdAt': '2018-04-10 12:33:58',
                            'cancelStatus': 'false',
                            'name': 'В резерве'
                        }
                    }
                }
        )
        )

        response = self.client.product_statuses()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_product_statuses_edit(self):
        """
        V3 Test method product_statuses_edit
        """

        status = {'code': 'in-reserve', 'name': 'В резерве'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/reference/product-statuses/' + status['code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('productStatus', status))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.product_statuses_edit(status)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_sites(self):
        """
        V3 Test method sites
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/reference/sites')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'sites': {
                        'sites': {
                            'name': 'XXX',
                            'url': 'http://url',
                            'code': 'code',
                            'defaultForCrm': 'false',
                            'ymlUrl': 'http://url',
                            'loadFromYml': 'true',
                            'catalogUpdatedAt': '2020-04-03 13:56:26',
                            'catalogLoadingAt': '2020-04-13 08:50:55',
                            'countryIso': 'RU'
                        }
                    }
                }
        )
        )

        response = self.client.sites()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_sites_edit(self):
        """
        V3 Test method sites_edit
        """

        site = {'code': 'code', 'name': 'XXX'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/reference/sites/' + site['code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('site', site))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.sites_edit(site)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_status_groups(self):
        """
        V3 Test method status_groups
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/reference/status-groups')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'statusGroups': {
                        'new': {
                            'name': 'Новый',
                            'code': 'new',
                            'ordering': 10,
                            'process': 'false',
                            'statuses': [
                                'new',
                                'rake-status'
                            ]
                        },
                        'approval': {
                            'name': 'Согласование',
                            'code': 'approval',
                            'ordering': 20,
                            'process': 'true',
                            'statuses': [
                                'availability-confirmed',
                                'offer-analog',
                                'client-confirmed',
                                'prepayed'
                            ]
                        }
                    }
                }
        )
        )

        response = self.client.status_groups()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_statuses(self):
        """
        V3 Test method statuses
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/reference/statuses')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'statuses': {
                        'new': {
                            'name': 'Новый',
                            'code': 'new',
                            'ordering': 10,
                            'group': 'new'
                        },
                        'rake-status': {
                            'name': 'Rake status',
                            'code': 'rake-status',
                            'ordering': 990,
                            'group': 'new'
                        }
                    }
                }
        )
        )

        response = self.client.statuses()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_statuses_edit(self):
        """
        V3 Test method statuses_edit
        """

        status = {'code': 'new', 'name': 'Новый'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/reference/statuses/' + status['code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('status', status))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.statuses_edit(status)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_stores(self):
        """
        V3 Test method stores
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/reference/stores')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'stores': [
                        {
                            'type': 'store-type-warehouse',
                            'inventoryType': 'integer',
                            'code': 'lca46',
                            'name': 'new'
                        },
                        {
                            'type': 'store-type-warehouse',
                            'inventoryType': 'integer',
                            'code': 'q6w5i',
                            'name': 's789'
                        }
                    ]
                }
        )
        )

        response = self.client.stores()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_stores_edit(self):
        """
        V3 Test method stores_edit
        """

        store = {'code': 'q6w5i', 'name': 's789'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/reference/stores/' + store['code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('store', store))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.stores_edit(store)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_inventories(self):
        """
        V3 Test method inventories
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/store/inventories')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[site]': 'https://help.ru'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination':
                        {
                            'limit': 20,
                            'totalCount': 34,
                            'currentPage': 1,
                            'totalPageCount': 2
                        },
                    'offers': [
                        {
                            'externalId': 'werew',
                            'quantity': 102
                        },
                        {
                            'externalId': '46',
                            'quantity': 0
                        },
                        {
                            'externalId': '33',
                            'quantity': 0
                        }]
                }
        )
        )

        response = self.client.inventories({'site': 'https://help.ru'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_inventories_upload(self):
        """
        V3 Test method inventories_upload
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/store/inventories/upload')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .body(self.dictionaryEncode('offers', {'externalId': 's789', 'id': 5603}))
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'processedOffersCount': 0,
                    'notFoundOffers': {
                        'externalId': 's789',
                        'xmlId': 9999
                    }
                }
        )
        )

        response = self.client.inventories_upload({'externalId': 's789', 'id': 5603})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_telephony_call_event(self):
        """
        V3 Test method telephony_call_event
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/telephony/call/event')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(urlencode({'hangupStatus': 'busy', 'phone': '+799999999', 'code': 'c2321', 'type': 'hangup'}))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.telephony_call_event('+799999999', 'hangup', 'c2321', 'busy')
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_telephony_calls_upload(self):
        """
        V3 Test method telephony_calls_upload
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/telephony/calls/upload')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .body(self.dictionaryEncode('calls', {}))
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'processedCallsCount': 5555,
                    'duplicateCalls': []
                }
        )
        )

        response = self.client.telephony_calls_upload({})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_telephony_manager(self):
        """
        V3 Test method telephony_manager
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v3/telephony/manager')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'phone': '+79999999999'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'manager': {
                        'id': 777,
                        'firstName': 'yyy',
                        'lastName': 'xxxx',
                        'patronymic': 's789',
                        'email': 'mail@retailcrm.pro',
                        'code': 'ccc7'
                    },
                    'customer': {
                        'id': 888,
                        'externalId': '5406',
                        'firstName': 'ccc',
                        'lastName': 's789',
                        'patronymic': 's789',
                        'email': 'mail@retailcrm.pro',
                        'code': 'ccc7',
                        'phones': [{'number': '+71111111111'}]
                    },
                    'links': {
                        'newOrderLink': 'https://newOrderLink.ru',
                        'lastOrderLink': 'https://lastOrderLink.ru',
                        'newCustomerLink': 'https://newCustomerLink.ru',
                        'customerLink': 'https://customerLink.ru',
                    }
                }
        )
        )

        response = self.client.telephony_manager('+79999999999')
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_telephony_settings(self):
        """
        V3 Test method telephony_settings
        """

        code = 'xxx'

        (
            pook.post(os.getenv('RETAILCRM_URL') + '/api/v3/telephony/settings/' + code)
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .body(urlencode({
                'code': code,
                'clientId': '123x',
                'makeCallUrl': 'url',
                'active': 'active',
                'name': 'name',
                'image': 'url_image'}))
            .reply(201)
            .headers(self.__header)
            .json({'success': 'true'})
        )

        response = self.client.telephony_settings(code, '123x', 'url', 'active', 'name', 'url_image')
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def statistic_update(self):
        """
        V3 Test method statistic_update
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/statistic/update')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.statistic_update()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)
