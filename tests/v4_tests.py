# coding=utf-8


"""
RetailCRM API client v4 tests
"""

from urllib.parse import urlencode
import unittest
import os
import retailcrm
import pook
import json


class TestVersion4(unittest.TestCase):
    """
    TestClass for v4
    """
    __header = {'Server': 'nginx/1.16.0', 'Content-Type': 'application/json; charset=UTF-8'}

    __customer = {
        'id': 9717,
        'externalId': 'c-34234',
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
        'slug': 3425,
        'summ': 0,
        'id': 3425,
        'number': '5604A',
        'externalId': '5603',
        'orderType': 'individual',
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
                'externalId': 'x2342'
            }
        }
    }

    def setUp(self):
        """
        Setup
        """

        self.client = retailcrm.v4(
                os.getenv('RETAILCRM_URL'), os.getenv('RETAILCRM_KEY'))

    @staticmethod
    def dictionaryEncode(key, dictionary):
        return urlencode({key: json.dumps(dictionary)})

    @pook.on
    def test_wrong_api_url(self):
        """
        V4 Test wrong api url
        """

        (pook.get('https://epoqq.retailcrm.pro' + '/api/v4/statistic/update')
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

        client = retailcrm.v4('https://epoqq.retailcrm.pro', os.getenv('RETAILCRM_KEY'))
        response = client.statistic_update()
        pook.off()

        self.assertIsNot(response.is_successful(), True)
        self.assertEqual(response.get_error_msg(), 'Account does not exist.')

    @pook.on
    def test_wrong_api_key(self):
        """
        V4 Test wrong api key
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/statistic/update')
         .headers({'X-API-KEY': 'XXXX'})
         .reply(200)
         .headers(self.__header)
         .json({'errorMsg': 'Wrong "apiKey" value.'})
         )

        client = retailcrm.v4(os.getenv('RETAILCRM_URL'), 'XXXX')
        response = client.statistic_update()
        pook.off()

        self.assertEqual(response.get_error_msg(), 'Wrong "apiKey" value.')

    @pook.on
    def test_missing_api_key(self):
        """
        V4 Test missing api key
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/statistic/update')
         .headers({'X-API-KEY': None})
         .reply(200)
         .headers(self.__header)
         .json({'errorMsg': '"apiKey" is missing.'})
         )

        client = retailcrm.v4(os.getenv('RETAILCRM_URL'), None)
        response = client.statistic_update()
        pook.off()

        self.assertEqual(response.get_error_msg(), '"apiKey" is missing.')

    @pook.on
    def test_customers(self):
        """
        V4 Test method customers
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/customers')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[online]': 'No', 'filter[contragentType]': 'individual'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': 20,
                        'totalCount': 4347,
                        'currentPage': 1,
                        'totalPageCount': 87
                    },
                    'customers': [self.__customer]
                }
        )
        )

        response = self.client.customers({'online': 'No', 'contragentType': 'individual'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customers_create(self):
        """
        V4 Test method customers_create
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/customers/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('customer', self.__customer))
         .reply(201)
         .headers(self.__header)
         .json({'success': 'true', 'id': 7117})
         )

        response = self.client.customer_create(self.__customer)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customers_fix_external_ids(self):
        """
        V4 Test method customers_fix_external_ids
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/customers/fix-external-ids')
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
    def test_customers_history(self):
        """
        V4 Test method customers_history
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/customers/history')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params(
                {
                    'filter[sinceId]': '1111',
                    'filter[startDate]': '2016-01-07',
                    'filter[endDate]': '2020-04-12'
                }
        )
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'generatedAt': '2020-04-15 17:43:12',
                    'history': [
                        {
                            'id': 7018,
                            'createdAt': '2018-04-11 09:01:26',
                            'created': 'true',
                            'source': 'api',
                            'field': 'id',
                            'apiKey': {
                                'current': 'false'
                            },
                            'oldValue': 'null',
                            'newValue': 4949,
                            'customer': {
                                'id': 4949,
                                'externalId': 'x2342',
                                'createdAt': '2018-04-11 09:01:26',
                                'vip': 'false',
                                'bad': 'false',
                                'site': 'retailcrm-ru',
                                'contragent': {
                                    'contragentType': 'individual'
                                },
                                'marginSumm': 0,
                                'totalSumm': 0,
                                'averageSumm': 0,
                                'ordersCount': 0,
                                'customFields': [],
                                'personalDiscount': 0,
                                'cumulativeDiscount': 0,
                                'firstName': 'XXX',
                                'lastName': 'XXX',
                                'patronymic': 'XXX',
                                'email': 'xxx@example.com'
                            }
                        }
                    ]
                }
        )
        )

        response = self.client.customers_history(
                {
                    'sinceId': '1111',
                    'startDate': '2016-01-07',
                    'endDate': '2020-04-12'
                }
        )
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customers_upload(self):
        """
        V4 Test method customers_upload
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/customers/upload')
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
        V4 Test method customer
        """

        uid = str(self.__customer['externalId'])

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/customers/' + uid)
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
        V4 Test method customers_edit
        """

        uid = str(self.__customer['externalId'])

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/customers/' + uid + '/edit')
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
    def test_delivery_setting(self):
        """
        V4 Test method delivery_setting
        """

        code = 'zzz'

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/delivery/generic/setting/' + code)
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'configuration': {
                        'actions': {},
                        'payerType': [
                            'sender'
                        ],
                        'platePrintLimit': 100,
                        'rateDeliveryCost': 'true',
                        'allowPackages': 'false',
                        'codAvailable': 'false',
                        'selfShipmentAvailable': 'false',
                        'duplicateOrderProductSupported': 'false',
                        'availableCountries': [],
                        'requiredFields': [],
                        'statusList': [
                            {
                                'code': 's789',
                                'name': 'sss',
                                'isEditable': 'true'
                            },
                            {
                                'code': 'crmDeleted',
                                'name': 'Удален',
                                'isEditable': 'false'
                            }
                        ],
                        'name': 'test',
                        'code': 'zzz',
                        'availableShipmentCountries': []
                    }
                }
        )
        )

        response = self.client.delivery_setting(code)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_delivery_setting_edit(self):
        """
        V4 Test method delivery_setting_edit
        """

        configuration = {
            'payerType': ['sender'],
            'statusList': [
                {
                    'code': 's789',
                    'name': 'sss',
                    'isEditable': 'true'
                }
            ],
            'name': 'test',
            'code': 'zzz'
        }

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/delivery/generic/setting/' + configuration['code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('configuration', configuration))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'code': 'generic.zzz'})
         )

        response = self.client.delivery_setting_edit(configuration)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_delivery_tracking(self):
        """
        V4 Test method delivery_tracking
        """

        code = 'zzz'
        tracking = {
            'deliveryId': '777z',
            'history': [
                {
                    'code': '888',
                    'updatedAt': '2020-04-12',
                    'comment': 'Good'
                }
            ]
        }

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/delivery/generic/' + code + '/tracking')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('statusUpdate', tracking))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.delivery_tracking(code, tracking)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_marketplace_setting_edit(self):
        """
        V4 Test method marketplace_setting_edit
        """

        code = 'May'
        configuration = {'name': 'Test123', 'code': code, 'configurationUrl': 'https://may.cat.ru'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/marketplace/external/setting/' + code + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('configuration', configuration))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        self.client.marketplace_setting_edit(configuration)
        pook.off()

    @pook.on
    def test_orders(self):
        """
        V4 Test method orders
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/orders')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[city]': 'Moscow', 'filter[contragentType]': 'individual'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': 20,
                        'totalCount': 2464,
                        'currentPage': 1,
                        'totalPageCount': 50
                    },
                    'orders': [self.__order]
                }
        )
        )

        response = self.client.orders({'city': 'Moscow', 'contragentType': 'individual'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_orders_create(self):
        """
        V4 Test method orders_create
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/orders/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('order', self.__order))
         .reply(201)
         .headers(self.__header)
         .json({'success': 'true', 'id': 8888, 'order': self.__order})
         )

        response = self.client.order_create(self.__order)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_orders_fix_external_ids(self):
        """
        V4 Test method orders_fix_external_ids
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/orders/fix-external-ids')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('orders', (self.__order['externalId'])))
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
        V4 Test method orders_history
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/orders/history')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params(
                {
                    'filter[sinceId]': '1111',
                    'filter[startDate]': '2016-01-07',
                    'filter[endDate]': '2020-04-12'
                }
        )
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'generatedAt': '2020-04-16 11:03:00',
                    'history': [
                        {
                            'id': 7887,
                            'createdAt': '2018-04-11 09:01:29',
                            'created': 'true',
                            'source': 'api',
                            'field': 'status',
                            'apiKey': {
                                'current': 'false'
                            },
                            'oldValue': 'null',
                            'newValue': {
                                'code': 'new'
                            },
                            'order': {
                                'slug': 9090,
                                'summ': 0,
                                'id': 9090,
                                'number': '9090A',
                                'externalId': 'x353',
                                'orderType': 'eshop-individual',
                                'orderMethod': 'shopping-cart',
                                'createdAt': '2018-04-11 09:01:29',
                                'statusUpdatedAt': '2018-04-11 09:01:29',
                                'totalSumm': 0,
                                'prepaySum': 0,
                                'purchaseSumm': 0,
                                'markDatetime': '2018-04-11 09:01:29',
                                'lastName': 'xxxx',
                                'firstName': 'xxxx',
                                'patronymic': 'xxxx',
                                'email': 'maymayslt@example.com',
                                'call': 'false',
                                'expired': 'false',
                                'customer': {
                                    'id': 5544,
                                    'isContact': 'false',
                                    'createdAt': '2018-04-11 09:01:29',
                                    'vip': 'false',
                                    'bad': 'false',
                                    'site': 'retailcrm-ru',
                                    'contragent': {
                                        'contragentType': 'individual'
                                    },
                                    'marginSumm': 0,
                                    'totalSumm': 0,
                                    'averageSumm': 0,
                                    'ordersCount': 1,
                                    'customFields': [],
                                    'personalDiscount': 0,
                                    'cumulativeDiscount': 0,
                                    'address': {
                                        'id': 3322
                                    },
                                    'lastName': 'xxxx',
                                    'firstName': 'xxxx',
                                    'patronymic': 'xxxx',
                                    'email': 'maymays@example.com',
                                    'phones': []
                                },
                                'contragent': {
                                    'contragentType': 'individual'
                                },
                                'delivery': {
                                    'cost': 0,
                                    'netCost': 0,
                                    'address': {
                                        'id': 2477,
                                        'countryIso': ''
                                    }
                                },
                                'site': 'retailcrm-ru',
                                'status': 'new',
                                'items': [],
                                'fromApi': 'true',
                                'shipped': 'false',
                                'customFields': []
                            }
                        }
                    ]
                }
        )
        )

        response = self.client.orders_history(
                {
                    'sinceId': '1111',
                    'startDate': '2016-01-07',
                    'endDate': '2020-04-12'
                }
        )
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_orders_statuses(self):
        """
        V4 Test method orders_statuses
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/orders/statuses')
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
        V4 Test method orders_upload
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/orders/upload')
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
        V4 Test method order
        """

        uid = str(self.__order['externalId'])

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/orders/' + uid)
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
        V4 Test method orders_edit
        """

        uid = str(self.__order['externalId'])

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/orders/' + uid + '/edit')
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
        V4 Test method packs
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/orders/packs')
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
        V4 Test method packs_create
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/orders/packs/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('pack', self.__pack))
         .reply(201)
         .headers(self.__header)
         .json({'success': 'true', 'id': 7777})
         )

        response = self.client.pack_create(self.__pack)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_packs_history(self):
        """
        V4 Test method packs_history
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/orders/packs/history')
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
                                'code': 'eee'
                            },
                            'pack': {
                                'id': 678,
                                'quantity': 1,
                                'store': {'code': 'eee'},
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
        V4 Test method pack
        """

        uid = str(self.__pack['id'])

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/orders/packs/' + uid)
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
        V4 Test method packs_delete
        """

        uid = '7777'

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/orders/packs/' + uid + '/delete')
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
        V4 Test method pack_edit
        """

        uid = str(self.__pack['id'])

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/orders/packs/' + uid + '/edit')
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
        V4 Test method countries
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/reference/countries')
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
        V4 Test method delivery_services
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/reference/delivery-services')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'deliveryServices': {
                        'hp5kc': {
                            'name': '8305u',
                            'code': 'hp5kc',
                            'active': 'true'
                        },
                        'hmo8s': {
                            'name': 'j456',
                            'code': 'hmo8s',
                            'active': 'true'
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
        V4 Test method delivery_services_edit
        """

        service = {'code': 'hmo8s', 'name': 'g4562'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/reference/delivery-services/' + service['code'] + '/edit')
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
        V4 Test method delivery_types
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/reference/delivery-types')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(201)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'deliveryTypes': {
                        '1kp52': {
                            'name': 'xas',
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
                        'wer': {
                            'name': '1s0ei',
                            'code': 'd452',
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
        V4 Test method delivery_types_edit
        """

        delivery_type = {'code': 'x345', 'name': '1s0ei'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/reference/delivery-types/' + delivery_type['code'] + '/edit')
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
        V4 Test method order_methods
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/reference/order-methods')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'orderMethods': {
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
        V4 Test method order_methods_edit
        """

        method = {'code': 'zoc5q', 'name': '1y0cp'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/reference/order-methods/' + method['code'] + '/edit')
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
        V4 Test method order_types
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/reference/order-types')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'orderTypes': {
                        's234': {
                            'name': 'test',
                            'code': 's234',
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
        V4 Test method order_types_edit
        """

        order_type = {'code': 's234', 'name': 'test'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/reference/order-types/' + order_type['code'] + '/edit')
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
        V4 Test method payment_statuses
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/reference/payment-statuses')
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
                            'ordering': 14,
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
        V4 Test method payment_statuses_edit
        """

        status = {'code': 'payment-start', 'name': 'Платеж проведен'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/reference/payment-statuses/' + status['code'] + '/edit')
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
        V4 Test method payment_types
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/reference/payment-types')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'paymentTypes': {
                        '056a3e': {
                            'name': 'TestPaymentType-056a3e',
                            'code': '2345',
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
        V4 Test method payment_types_edit
        """

        payment_type = {'code': '238c06', 'name': 'TestPaymentType-238c06'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/reference/payment-types/' + payment_type['code'] + '/edit')
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
        V4 Test method product_statuses
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/reference/product-statuses')
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
        V4 Test method product_statuses_edit
        """

        status = {'code': 'in-reserve', 'name': 'В резерве'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/reference/product-statuses/' + status['code'] + '/edit')
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
        V4 Test method sites
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/reference/sites')
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
        V4 Test method sites_edit
        """

        site = {'code': 'code', 'name': 'XXX'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/reference/sites/' + site['code'] + '/edit')
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
        V4 Test method status_groups
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/reference/status-groups')
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
                            'ordering': 23,
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
        V4 Test method statuses
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/reference/statuses')
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
        V4 Test method statuses_edit
        """

        status = {'code': 'new', 'name': 'Новый'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/reference/statuses/' + status['code'] + '/edit')
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
        V4 Test method stores
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/reference/stores')
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
                            'name': 'u532'
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
        V4 Test method stores_edit
        """

        store = {'code': 'q6w5i', 'name': 'u245'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/reference/stores/' + store['code'] + '/edit')
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
        V4 Test method inventories
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/store/inventories')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[site]': 'https://retailcrm.pro'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': 20,
                        'totalCount': 621,
                        'currentPage': 1,
                        'totalPageCount': 32
                    },
                    'offers': [
                        {
                            'id': 33937,
                            'externalId': 'werew',
                            'site': 'https://retailcrm.pro',
                            'quantity': 102
                        },
                        {
                            'id': 33933,
                            'externalId': '46',
                            'site': 'https://retailcrm.pro',
                            'quantity': 0
                        }
                    ]
                }
        )
        )

        response = self.client.inventories({'site': 'https://retailcrm.pro'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_inventories_upload(self):
        """
        V4 Test method inventories_upload
        """

        inventories = {'externalId': '5603', 'id': 5603}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/store/inventories/upload')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .body(self.dictionaryEncode('offers', inventories))
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'processedOffersCount': 0,
                    'notFoundOffers': {
                        'externalId': 'u234',
                        'xmlId': 9999
                    }
                }
        )
        )

        response = self.client.inventories_upload(inventories)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_prices_upload(self):
        """
        V4 Test method prices_upload
        """

        price = [{'price': 999, 'externalId': 'werew'}]

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/store/prices/upload')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .body(self.dictionaryEncode('prices', price))
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'processedOffersCount': 0,
                    'notFoundOffers': [
                        {
                            'externalId': 'werew'
                        }
                    ]
                }
        )
        )

        response = self.client.prices_upload(price)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_products(self):
        """
        V4 Test method products
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/store/products')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[priceType]': 'base', 'filter[active]': '1'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': 20,
                        'totalCount': 558,
                        'currentPage': 1,
                        'totalPageCount': 28
                    },
                    'products': [
                        {
                            'minPrice': 100,
                            'maxPrice': 100,
                            'id': 25804,
                            'name': 'sds',
                            'manufacturer': 'asdas',
                            'offers': [
                                {
                                    'name': 'sdfsdf',
                                    'price': 100,
                                    'id': 33937,
                                    'externalId': 'werew',
                                    'article': 'ewrwrew',
                                    'prices': [
                                        {
                                            'priceType': 'base',
                                            'price': 100,
                                            'ordering': 991
                                        }
                                    ],
                                    'weight': 44
                                }
                            ],
                            'active': 'true',
                            'quantity': 102,
                            'markable': 'false'
                        }
                    ]
                }
        )
        )

        response = self.client.products({'priceType': 'base', 'active': 1})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_store_setting(self):
        """
        V4 Test method store_setting
        """

        code = 'xxx'

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/store/setting/' + code)
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params(code)
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'configuration': {
                        'actions': [
                            {
                                'code': 'ccc',
                                'url': 'https://test'
                            }
                        ],
                        'code': 'xxx',
                        'active': 'true',
                        'name': 'test',
                        'baseUrl': '/'
                    }
                }
        )
        )

        response = self.client.store_setting(code)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_store_setting_edit(self):
        """
        V4 Test method store_setting_edit
        """

        setting = {
            'code': 'xxx',
            'name': 'test',
            'actions': [
                {
                    'code': 'ccc',
                    'url': 'https://test'
                }
            ]
        }

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/store/setting/' + setting['code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('configuration', setting))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.store_setting_edit(setting)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_telephony_call_event(self):
        """
        V4 Test method telephony_call_event
        """

        call_event = {'phone': '+799999999', 'type': 'out'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/telephony/call/event')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('event', call_event))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'false', 'errorMsg': 'Telephony not enabled'})
         )

        response = self.client.telephony_call_event(call_event)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_telephony_calls_upload(self):
        """
        V4 Test method telephony_calls_upload
        """

        call = {'phone': '79999999999', 'type': 'out'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/telephony/calls/upload')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('calls', call))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'false', 'errorMsg': 'Telephony not enabled or not supports calls upload'}
               )
         )

        response = self.client.telephony_calls_upload(call)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_telephony_manager(self):
        """
        V4 Test method telephony_manager
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/telephony/manager')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params('+79999999999')
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'manager': {
                        'id': 777,
                        'firstName': 'yyy',
                        'lastName': 'xxxx',
                        'patronymic': 'www',
                        'email': 'mail@retailcrm.pro',
                        'code': 'ccc7'
                    },
                    'customer': {
                        'id': 888,
                        'externalId': '5406',
                        'firstName': 'ccc',
                        'lastName': 'zzz',
                        'patronymic': 'sss',
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
    def test_telephony_setting(self):
        """
        V4 Test method telephony_setting
        """

        code = 'www'

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/telephony/setting/' + code)
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params(code)
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'configuration': {
                        'makeCallUrl': 'https://retailcrm.pro',
                        'allowEdit': 'false',
                        'inputEventSupported': 'false',
                        'outputEventSupported': 'false',
                        'additionalCodes': [],
                        'externalPhones': [],
                        'code': 'www',
                        'active': 'false',
                        'name': 'telephony.company.www'
                    }
                }
        )
        )

        response = self.client.telephony_setting(code)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_telephony_setting_edit(self):
        """
        V4 Test method telephony_setting_edit
        """

        configuration = {
            'code': 'www',
            'clientId': '5604',
            'makeCallUrl': 'https://retailcrm.pro'
        }

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v4/telephony/setting/' + configuration['code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('configuration', configuration))
         .reply(201)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.telephony_setting_edit(configuration)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_user_groups(self):
        """
        V4 Test method user_groups
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/user-groups')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': 20,
                        'totalCount': 2,
                        'currentPage': 1,
                        'totalPageCount': 1
                    },
                    'groups': [
                        {
                            'name': 'Менеджеры',
                            'code': 'manager',
                            'isManager': 'true',
                            'isPosManager': 'false',
                            'isDeliveryMen': 'false',
                            'deliveryTypes': [],
                            'breakdownOrderTypes': ['xxx', 'yyy', 'zzz'],
                        },
                        {
                            'name': 'Руководители',
                            'code': 'director',
                            'isManager': 'false',
                            'isPosManager': 'false',
                            'isDeliveryMen': 'false',
                            'deliveryTypes': ['xxx'],
                            'breakdownOrderTypes': ['yyy'],
                            'breakdownSites': [],
                            'breakdownOrderMethods': ['zzz'],
                            'grantedOrderTypes': ['ccc']
                        }
                    ]
                }
        )
        )

        response = self.client.user_groups()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_users(self):
        """
        V4 Test method users
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/users')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[status]': 'online', 'filter[isManager]': 'false'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': 20,
                        'totalCount': 7,
                        'currentPage': 1,
                        'totalPageCount': 1
                    },
                    'users': [
                        {
                            'id': 777,
                            'createdAt': '2020-04-05 11:23:46',
                            'active': 'true',
                            'email': 'mail@retailcrm.pro',
                            'firstName': 'yyy',
                            'lastName': 'xxxx',
                            'status': 'free',
                            'online': 'true',
                            'isAdmin': 'true',
                            'isManager': 'false',
                            'groups': []
                        }
                    ]
                }
        )
        )

        response = self.client.users({'status': 'online', 'isManager': 'false'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_user(self):
        """
        V4 Test method user
        """

        uid = 777

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v4/users/' + str(uid))
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'user': {
                        'id': 777,
                        'createdAt': '2020-04-05 11:23:46',
                        'active': 'true',
                        'email': 'mail@retailcrm.pro',
                        'firstName': 'yyy',
                        'lastName': 'xxxx',
                        'status': 'free',
                        'online': 'true',
                        'isAdmin': 'true',
                        'isManager': 'false',
                        'groups': []
                    }
                }
        )
        )

        response = self.client.user(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def statistic_update(self):
        """
        V4 Test method statistic_update
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/statistic/update')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.statistic_update()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)
