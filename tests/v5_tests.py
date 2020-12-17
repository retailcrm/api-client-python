# coding=utf-8

"""
RetailCRM API client v5 tests
"""

from urllib.parse import urlencode
import unittest
import os
import retailcrm
import pook
import json


class TestVersion5(unittest.TestCase):
    """
    TestClass for v5
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
                'externalId': 'y6642'
            }
        }
    }

    __cost = {
        'id': 635,
        'dateFrom': '2020-01-30',
        'dateTo': '2020-01-30',
        'summ': 2,
        'costItem': 'delivery-cost',
        'createdAt': '2020-01-30 16:43:36',
        'order': {
            'id': 4798,
            'number': '16',
            'externalId': '16'
        },
        'sites': [
            'prestashop'
        ]
    }

    __file = {
        'id': 30,
        'filename': 'API upload 18-09-2019 13:14:00',
        'type': 'application/pdf',
        'createdAt': '2019-09-18 13:14:00',
        'size': 124225,
        'attachment': [
            {
                'order': {
                    'id': 7777,
                    'number': '7777A',
                    'site': 'hhhh'
                }
            }
        ]
    }

    __customer_corporate = {
        'type': 'customer_corporate',
        'id': 9084,
        'externalId': 'cc_9',
        'nickName': 'Test',
        'mainAddress': {
            'id': 3995,
            'name': 'Test'
        },
        'createdAt': '2020-02-14 13:49:21',
        'vip': 'false',
        'bad': 'false',
        'site': 'opencart',
        'tags': [],
        'marginSumm': 0,
        'totalSumm': 0,
        'averageSumm': 0,
        'ordersCount': 0,
        'costSumm': 0,
        'customFields': [],
        'personalDiscount': 0,
        'ainCustomerContact': {
            'id': 33,
            'customer': {
                'id': 9083,
                'externalId': '9'
            },
            'companies': []
        },
        'mainCompany': {
            'id': 31,
            'name': 'Test'
        }
    }

    __task = {
        'id': 433,
        'text': 'test task edited',
        'commentary': 'test commentary',
        'complete': 'false',
        'phone': '+79185550000',
        'performerId': 15
    }

    def setUp(self):
        """
        Setup
        """

        self.client = retailcrm.v5(os.getenv('RETAILCRM_URL'), os.getenv('RETAILCRM_KEY'))

    @staticmethod
    def dictionaryEncode(key, dictionary):
        return urlencode({key: json.dumps(dictionary)})

    @pook.on
    def test_wrong_api_url(self):
        """
        V5 Test wrong api url
        """

        (pook.get('https://epoqq.retailcrm.pro' + '/api/v5/statistic/update')
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

        client = retailcrm.v5('https://epoqq.retailcrm.pro', os.getenv('RETAILCRM_KEY'))
        response = client.statistic_update()
        pook.off()

        self.assertIsNot(response.is_successful(), True)
        self.assertEqual(response.get_error_msg(), 'Account does not exist.')

    @pook.on
    def test_wrong_api_key(self):
        """
        V5 Test wrong api key
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/statistic/update')
         .headers({'X-API-KEY': 'XXXX'})
         .reply(200)
         .headers(self.__header)
         .json({'errorMsg': 'Wrong "apiKey" value.'})
         )

        client = retailcrm.v5(os.getenv('RETAILCRM_URL'), 'XXXX')
        response = client.statistic_update()
        pook.off()

        self.assertEqual(response.get_error_msg(), 'Wrong "apiKey" value.')

    @pook.on
    def test_missing_api_key(self):
        """
        V5 Test missing api key
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/statistic/update')
         .headers({'X-API-KEY': None})
         .reply(200)
         .headers(self.__header)
         .json({'errorMsg': '"apiKey" is missing.'})
         )

        client = retailcrm.v5(os.getenv('RETAILCRM_URL'), None)
        response = client.statistic_update()
        pook.off()

        self.assertEqual(response.get_error_msg(), '"apiKey" is missing.')

    @pook.on
    def test_api_versions(self):
        """
        V5 Test api-versions method
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
        V5 Test api-credentials method
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
    def test_costs(self):
        """
        V5 Test method costs
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/costs')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': 20,
                        'totalCount': 6,
                        'currentPage': 1,
                        'totalPageCount': 1
                    },
                    'costs': [self.__cost]
                }
        )
        )

        response = self.client.costs()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_costs_create(self):
        """
        V5 Test method costs_create
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/costs/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('cost', self.__cost))
         .reply(201)
         .headers(self.__header)
         .json({'success': 'true', 'id': 7117})
         )

        response = self.client.cost_create(self.__cost)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_costs_delete(self):
        """
        V5 Test method costs_delete
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/costs/delete')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .body(self.dictionaryEncode('ids', [555, 666, 777]))
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'count': 3,
                    'notRemovedIds': []
                }
        )
        )

        response = self.client.costs_delete([555, 666, 777])
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_costs_upload(self):
        """
        V5 Test method costs_upload
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/costs/upload')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('costs', [self.__cost]))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'uploadedCosts': [555]})
         )

        response = self.client.costs_upload([self.__cost])
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_cost(self):
        """
        V5 Test method cost
        """

        uid = str(self.__cost['id'])

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/costs/' + uid)
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'cost': self.__cost})
         )

        response = self.client.cost(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_costs_delete_v5(self):
        """
        V5 Test method costs_delete
        """

        uid = '7777'

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/costs/' + uid + '/delete')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.cost_delete(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_costs_edit(self):
        """
        V5 Test method cost_edit
        """

        uid = str(self.__cost['id'])

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/costs/' + uid + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('cost', self.__cost))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'id': 7777})
         )

        response = self.client.cost_edit(self.__cost)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_custom_fields(self):
        """
        V5 Test method custom_fields
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/custom-fields')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[entity]': 'customer'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': 20,
                        'totalCount': 66,
                        'currentPage': 1,
                        'totalPageCount': 4
                    },
                    'customFields': [
                        {
                            'name': 'xxxx',
                            'code': 'test',
                            'required': 'false',
                            'inFilter': 'true',
                            'inList': 'true',
                            'inGroupActions': 'false',
                            'type': 'text',
                            'entity': 'order',
                            'ordering': 50,
                            'displayArea': 'delivery',
                            'viewMode': 'editable'
                        }
                    ]
                }
        )
        )

        response = self.client.custom_fields({'entity': 'customer'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_custom_dictionaries(self):
        """
        V5 Test method custom_dictionaries
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/custom-fields/dictionaries')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[name]': 'test223'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': 20,
                        'totalCount': 67,
                        'currentPage': 1,
                        'totalPageCount': 1
                    },
                    'customDictionaries': [
                        {
                            'name': 'test223',
                            'code': 'test2',
                            'elements': [
                                {
                                    'name': 'test3',
                                    'code': 'test3',
                                    'ordering': 50
                                }
                            ]
                        }
                    ]
                }
        )
        )

        response = self.client.custom_dictionaries({'name': 'test223'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_custom_dictionary_create(self):
        """
        V5 Test method custom_dictionary_create
        """

        custom_dictionary = {
            'name': 'test',
            'code': 'test',
            'elements': [{'name': 'fear', 'code': 'e456'}]
        }

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/custom-fields/dictionaries/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('customDictionary', custom_dictionary))
         .reply(201)
         .headers(self.__header)
         .json({'success': 'true', 'code': 'test'})
         )

        response = self.client.custom_dictionary_create(custom_dictionary)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_custom_dictionary(self):
        """
        V5 Test method custom_dictionary
        """

        uid = '777'

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/custom-fields/dictionaries/' + uid)
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'customDictionary': {
                        'name': 'test223',
                        'code': 'test2',
                        'elements': [
                            {
                                'name': 'test3',
                                'code': 'test3',
                                'ordering': 50
                            }
                        ]
                    }
                }
        )
        )

        response = self.client.custom_dictionary(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_custom_dictionary_edit(self):
        """
        V5 Test method custom_dictionary_edit
        """

        custom_dictionary = {
            'name': 'test',
            'code': 'test',
            'elements': [{'name': 'fear', 'code': 'e456'}]
        }

        (pook.post("".join(
            [
                os.getenv('RETAILCRM_URL'),
                '/api/v5/custom-fields/dictionaries/',
                custom_dictionary['code'],
                '/edit'
            ]))
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('customDictionary', custom_dictionary))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'code': 'test'}))

        response = self.client.custom_dictionary_edit(custom_dictionary)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_custom_field_create(self):
        """
        V5 Test method custom_field_create
        """

        custom_field = {
            'name': 'test',
            'code': 'test',
            'type': 'text',
            'entity': 'customer'
        }

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/custom-fields/' + custom_field['entity'] + '/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('customField', custom_field))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'code': 'test'})
         )

        response = self.client.custom_field_create(custom_field)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_custom_field(self):
        """
        V5 Test method custom_field
        """

        entity = 'customer'
        code = 'test'

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/custom-fields/' + entity + '/' + code)
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'customField': {
                        'name': 'test',
                        'code': 'test',
                        'required': 'false',
                        'inFilter': 'true',
                        'inList': 'true',
                        'inGroupActions': 'false',
                        'type': 'text',
                        'entity': 'customer',
                        'ordering': 50,
                        'viewMode': 'editable'
                    }
                }
        )
        )

        response = self.client.custom_field(code, entity)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_custom_field_edit(self):
        """
        V5 Test method custom_field_edit
        """

        custom_field = {
            'name': 'test',
            'ordering': 5555,
            'displayArea': 'customer',
            'entity': 'customer',
            'code': 'test'
        }

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/custom-fields/' + custom_field['entity'] + '/' + custom_field[
            'code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('customField', custom_field))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'code': 'test'})
         )

        response = self.client.custom_field_edit(custom_field)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customers(self):
        """
        V5 Test method customers
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/customers')
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
    def test_customers_combine(self):
        """
        V5 Test method customers_combine
        """

        customer = {'id': 5604}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers/combine')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.customers_combine(customer, customer)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customers_create(self):
        """
        V5 Test method customers_create
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers/create')
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
        V5 Test method customers_fix_external_ids
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers/fix-external-ids')
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
        V5 Test method customers_history
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/customers/history')
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
                                'externalId': 'c456',
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
    def test_customers_notes(self):
        """
        V5 Test method customers_notes
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/customers/notes')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[createdAtFrom]': '2020-04-18', 'filter[createdAtTo]': '2020-04-21'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': 20,
                        'totalCount': 3,
                        'currentPage': 1,
                        'totalPageCount': 1
                    },
                    'notes': [
                        {
                            'customer': {
                                'site': 'retailcrm-ru',
                                'id': 5604,
                                'type': 'customer'
                            },
                            'id': 279,
                            'text': 'test',
                            'createdAt': '2020-04-20 13:02:35'
                        }
                    ]
                }
        )
        )

        response = self.client.customer_notes({'createdAtFrom': '2020-04-18', 'createdAtTo': '2020-04-21'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customer_note_create(self):
        """
        V5 Test method customer_note_create
        """

        note = {'managerId': 23, 'text': 'test', 'customer': {'id': 5604}}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers/notes/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('note', note))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'id': 2222})
         )

        response = self.client.customer_note_create(note)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customer_note_delete(self):
        """
        V5 Test method customer_note_delete
        """

        uid = '279'

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers/notes/' + uid + '/delete')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.customer_note_delete(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customers_upload(self):
        """
        V5 Test method customers_upload
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers/upload')
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
        V5 Test method customer
        """

        uid = str(self.__customer['externalId'])

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/customers/' + uid)
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
        V5 Test method customers_edit
        """

        uid = str(self.__customer['externalId'])

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers/' + uid + '/edit')
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
    def test_customers_corporate(self):
        """
        V5 Test customers_corporate
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[vip]': 'false', 'filter[companyName]': 'Test'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': 20,
                        'totalCount': 128,
                        'currentPage': 1,
                        'totalPageCount': 7
                    },
                    'customersCorporate': [self.__customer_corporate]
                }
        )
        )

        response = self.client.customers_corporate({'vip': 'false', 'companyName': 'Test'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customers_combine_corporate(self):
        """
        V5 Test method customers_combine_corporate
        """

        customer = {'id': 5604}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/combine')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.customers_combine_corporate(customer, customer)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customer_corporate_create(self):
        """
        V5 Test method customer_corporate_create
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('customerCorporate', self.__customer_corporate))
         .reply(201)
         .headers(self.__header)
         .json({'success': 'true', 'id': 7117})
         )

        response = self.client.customer_corporate_create(self.__customer_corporate)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def customers_corporate_fix_external_ids(self):
        """
        V5 Test method customers_corporate_fix_external_ids
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/fix-external-ids')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('customerCorporate', self.__customer_corporate['externalId']))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.customers_corporate_fix_external_ids(self.__customer_corporate['externalId'])
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customers_history_v5(self):
        """
        V5 Test method customers_corporate_history
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/history')
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
                            'id': 1,
                            'createdAt': '2019-10-14 14:57:21',
                            'created': 'true',
                            'source': 'user',
                            'user': {'id': 15},
                            'field': 'id',
                            'oldValue': 'null',
                            'newValue': 7484,
                            'customer': {
                                'type': 'customer_corporate',
                                'id': 7484,
                                'nickName': 'Inventive',
                                'createdAt': '2019-10-14 14:57:21',
                                'managerId': 15,
                                'vip': 'false',
                                'bad': 'false',
                                'site': 'samsung',
                                'marginSumm': 0,
                                'totalSumm': 0,
                                'averageSumm': 0,
                                'ordersCount': 0,
                                'customFields': [],
                                'personalDiscount': 0,
                                'cumulativeDiscount': 0
                            }
                        }
                    ]
                }
        )
        )

        response = self.client.customers_corporate_history(
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
    def test_customer_corporate_notes(self):
        """
        V5 Test method customer_corporate_notes
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/notes')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[createdAtFrom]': '2020-04-18', 'filter[createdAtTo]': '2020-04-21'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': 20,
                        'totalCount': 3,
                        'currentPage': 1,
                        'totalPageCount': 1
                    },
                    'notes': [
                        {
                            'customer': {
                                'site': 'retailcrm-ru',
                                'id': 5604,
                                'type': 'customer_corporate'
                            },
                            'id': 279,
                            'text': 'test',
                            'createdAt': '2020-04-29 13:02:35'
                        }
                    ]
                }
        )
        )

        response = self.client.customer_corporate_notes({'createdAtFrom': '2020-04-18', 'createdAtTo': '2020-04-21'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customer_corporate_note_create(self):
        """
        V5 Test method customer_corporate_note_create
        """

        note = {'managerId': 23, 'text': 'test', 'customer': {'id': 5604}}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/notes/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('note', note))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'id': 2222})
         )

        response = self.client.customer_corporate_note_create(note)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customer_corporate_note_delete(self):
        """
        V5 Test method customer_corporate_note_delete
        """

        uid = '279'

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/notes/' + uid + '/delete')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.customer_corporate_note_delete(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customers_corporate_upload(self):
        """
        V5 Test method customers_corporate_upload
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/upload')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .body(self.dictionaryEncode('customersCorporate', self.__customer_corporate))
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

        response = self.client.customers_corporate_upload(self.__customer_corporate)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customer_corporate(self):
        """
        V5 Test method customer_corporate
        """

        uid = str(self.__customer_corporate['externalId'])

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/' + uid)
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'customerCorporate': self.__customer_corporate})
         )

        response = self.client.customer_corporate(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customer_corporate_addresses(self):
        """
        V5 Test method customer_corporate_addresses
        """

        uid = str(self.__customer_corporate['externalId'])

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/' + uid + '/addresses')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params(uid)
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'addresses': [{
                        'id': 3995,
                        'text': '123123, Russian Federation, Moscow, Kubuntu 14',
                        'isMain': 'true',
                        'name': 'Test'
                    }],
                    'pagination': {
                        'limit': 20,
                        'totalCount': 1,
                        'currentPage': 1,
                        'totalPageCount': 1
                    }
                }
        )
        )

        response = self.client.customer_corporate_addresses(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customer_corporate_addresses_create(self):
        """
        V5 Test method customer_corporate_addresses_create
        """

        address = {'isMain': 'true', 'name': 'Test', 'externalId': 'cc_9'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/' + address['externalId'] + '/addresses/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('address', address))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'id': 9717}))

        response = self.client.customer_corporate_addresses_create(address)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customer_corporate_addresses_edit(self):
        """
        V5 Test method customer_corporate_addresses_edit
        """

        uid = str(self.__customer_corporate['externalId'])
        address = {'isMain': 'true', 'name': 'Test', 'externalId': 'ccc8'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/' + uid + '/addresses/' + address[
            'externalId'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('address', address))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'id': '7777'})
         )

        response = self.client.customer_corporate_addresses_edit(uid, address)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customer_corporate_companies(self):
        """
        V5 Test method customer_corporate_companies
        """

        uid = str(self.__customer_corporate['externalId'])

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/' + uid + '/companies')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params(uid)
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    "success": 'true',
                    "companies": [
                        {
                            "isMain": 'true',
                            "id": 31,
                            "customer": {
                                "site": "test",
                                "id": 9084,
                                "externalId": "cc_9",
                                "type": "customer_corporate"
                            },
                            "active": 'true',
                            "name": "Test",
                            "createdAt": "2020-02-14 16:49:21",
                            "contragent": {
                                "contragentType": "legal-entity"
                            },
                            "marginSumm": 0,
                            "totalSumm": 0,
                            "averageSumm": 0,
                            "ordersCount": 0,
                            "costSumm": 0,
                            "customFields": []
                        }
                    ],
                    "pagination": {
                        "limit": 20,
                        "totalCount": 1,
                        "currentPage": 1,
                        "totalPageCount": 1
                    }
                }
        )
        )

        response = self.client.customer_corporate_companies(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customer_corporate_companies_create(self):
        """
        V5 Test method customer_corporate_companies_create
        """

        company = {'isMain': 'true', 'name': 'TestN', 'externalId': 'cc_9'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/' + company['externalId'] + '/companies/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('company', company))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'id': 9717})
         )

        response = self.client.customer_corporate_companies_create(company)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customer_corporate_companies_edit(self):
        """
        V5 Test method customer_corporate_companies_edit
        """

        uid = str(self.__customer_corporate['externalId'])
        company = {'isMain': 'true', 'name': 'TestN', 'externalId': 'ccc9'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/' + uid + '/companies/' + company[
            'externalId'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('company', company))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'id': 7777})
         )

        response = self.client.customer_corporate_companies_edit(uid, company)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customer_corporate_contacts(self):
        """
        V5 Test method customer_corporate_contacts
        """

        uid = str(self.__customer_corporate['externalId'])

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/' + uid + '/contacts')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params(uid)
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'contacts': [
                        {
                            'isMain': 'true',
                            'id': 33,
                            'customer': {
                                'id': 9083,
                                'externalId': '9',
                                'site': 'opencart'
                            },
                            'companies': []
                        }
                    ],
                    'pagination': {
                        'limit': 20,
                        'totalCount': 1,
                        'currentPage': 1,
                        'totalPageCount': 1
                    }
                }
        )
        )

        response = self.client.customer_corporate_contacts(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customer_corporate_contacts_create(self):
        """
        V5 Test method customer_corporate_contacts_create
        """

        contact = {'isMain': 'true', 'name': 'TestM', 'externalId': 'cc_9'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/' + contact['externalId'] + '/contacts/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('contact', contact))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'id': 9717})
         )

        response = self.client.customer_corporate_contacts_create(contact)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customer_corporate_contacts_edit(self):
        """
        V5 Test method customer_corporate_contacts_edit
        """

        uid = str(self.__customer_corporate['externalId'])
        contact = {'isMain': 'true', 'name': 'TestM', 'externalId': 'cc_10'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/' + uid + '/contacts/' + contact[
            'externalId'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('contact', contact))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'id': '7777'})
         )

        response = self.client.customer_corporate_contacts_edit(uid, contact)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_customer_corporate_edit(self):
        """
        V5 Test method customer_corporate_edit
        """

        uid = str(self.__customer_corporate['externalId'])

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/customers-corporate/' + uid + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('customersCorporate', self.__customer_corporate))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'id': '9717'})
         )

        response = self.client.customer_corporate_edit(self.__customer_corporate)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_delivery_tracking(self):
        """
        V5 Test method delivery_tracking
        """

        code = 'zzz'
        delivery_id = {
            'deliveryId': '777z',
            'history': [
                {
                    'code': '888',
                    'updatedAt': '2020-04-12',
                    'comment': 'Good'
                }
            ]
        }

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/delivery/generic/' + code + '/tracking')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('statusUpdate', delivery_id))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.delivery_tracking(code, delivery_id)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_delivery_shipments(self):
        """
        V5 Test delivery_shipments
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/delivery/shipments')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[stores]': 'test'})
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
                    'deliveryShipments': [
                        {
                            'integrationCode': 'xxx',
                            'id': 1,
                            'externalId': '10471460',
                            'deliveryType': 'osj97',
                            'store': 'test',
                            'managerId': 23,
                            'status': 'processing',
                            'date': '2020-03-31',
                            'time': {
                                'from': '13:00',
                                'to': '18:00'
                            },
                            'orders': [
                                {
                                    'id': 5596,
                                    'number': '5596C'
                                }
                            ],
                            'extraData': []
                        }
                    ]
                }
        )
        )

        response = self.client.delivery_shipments({'stores': 'test'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_delivery_shipment_create(self):
        """
        V5 Test method delivery_shipment_create
        """

        delivery_shipment = {'status': 'cancelled', 'store': 'test'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/delivery/shipments/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('deliveryShipment', delivery_shipment))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'id': 5555, 'status': 'cancelled'})
         )

        response = self.client.delivery_shipment_create(delivery_shipment)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_delivery_shipment(self):
        """
        V5 Test method delivery_shipment
        """

        uid = '10471460'

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/delivery/shipments/' + uid)
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'deliveryShipments':
                        {
                            'integrationCode': 'xxx',
                            'id': 1,
                            'externalId': '10471460',
                            'deliveryType': 'osj97',
                            'store': 'test',
                            'managerId': 23,
                            'status': 'processing',
                            'date': '2020-03-31',
                            'time': {
                                'from': '13:00',
                                'to': '18:00'
                            },
                            'orders': [
                                {
                                    'id': 5596,
                                    'number': '5596C'
                                }
                            ],
                            'extraData': []
                        }
                }
        )
        )

        response = self.client.delivery_shipment(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_delivery_shipment_edit(self):
        """
        V5 Test method delivery_shipment_edit
        """

        delivery_shipment = {
            'integrationCode': 'xxx',
            'id': 1,
            'externalId': '10471460',
            'deliveryType': 'osj97',
            'store': 'test',
            'managerId': 23,
            'status': 'processing',
            'date': '2020-03-31',
            'time': {
                'from': '13:00',
                'to': '18:00'
            },
            'orders': [
                {
                    'id': 5596,
                    'number': '5596C'
                }
            ],
            'extraData': []
        }
        uid = delivery_shipment['id']

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/delivery/shipment/' + str(uid) + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('deliveryShipment', delivery_shipment))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'id': 5555, 'status': 'cancelled'})
         )

        response = self.client.delivery_shipment_edit(delivery_shipment)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_files(self):
        """
        V5 Test method files
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/files')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[sizeFrom]': '1'})
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
                    'files': [self.__file]
                }
        )
        )

        response = self.client.files({'sizeFrom': '1'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_files_upload(self):
        """
        V5 Test method files_upload
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/files/upload')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('file', self.__file))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'file': {'id': 92}})
         )

        response = self.client.files_upload(self.__file)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_file(self):
        """
        V5 Test method file
        """

        uid = str(self.__file['id'])

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/files/' + uid)
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'file': self.__file})
         )

        response = self.client.file(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_files_delete(self):
        """
        V5 Test method files_delete
        """

        uid = '7777'

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/files/' + uid + '/delete')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.files_delete(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_files_download(self):
        """
        V5 Test method files_download
        """

        uid = '7777'

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/files/' + uid + '/download')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .params(uid)
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.files_download(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_files_edit(self):
        """
        V5 Test method files_edit
        """

        uid = '30'

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/files/' + uid + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('file', self.__file))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.files_edit(self.__file)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_integration_module(self):
        """
        V5 Test method integration_module
        """

        code = 'xxx'

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/integration-modules/' + code)
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params(code)
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': '20',
                        'totalCount': '4347',
                        'currentPage': '1',
                        'totalPageCount': '87'
                    },
                    'integrationModule': {
                        'success': 'true',
                        'integrationModule': {
                            'code': 'xxx',
                            'integrationCode': 'xxx',
                            'active': 'true',
                            'freeze': 'false',
                            'name': 'test',
                            'native': 'false',
                            'actions': {},
                            'availableCountries': [],
                            'integrations': {
                                'store': {
                                    'actions': [
                                        {
                                            'code': 'ccc',
                                            'url': 'https://test'
                                        }
                                    ]
                                }
                            }
                        }
                    }
                }
        )
        )

        response = self.client.integration_module(code)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_integration_module_edit(self):
        """
        V5 Test method integration_module_edit
        """

        integration_module = {'code': 'xxx', 'integrationCode': 'xxx'}
        uid = 'xxx'

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/integration-modules/' + uid + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('integrationModule', integration_module))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.integration_module_edit(integration_module)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_orders(self):
        """
        V5 Test method orders
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/orders')
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
    def test_orders_combine(self):
        """
        V5 Test method orders_combine
        """

        order = {'id': 5604}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/orders/combine')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.orders_combine(order, order, 'merge')
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_orders_create(self):
        """
        V5 Test method orders_create
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/orders/create')
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
        V5 Test method orders_fix_external_ids
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/orders/fix-external-ids')
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
        V5 Test method orders_history
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/orders/history')
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
                                'externalId': 'v4321',
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
        V5 Test method orders_statuses
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/orders/statuses')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'ids[]': '5604', 'externalIds[]': '5603'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'orders': [
                        {
                            'id': '5604',
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
        V5 Test method orders_upload
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/orders/upload')
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
        V5 Test method order
        """

        uid = str(self.__order['externalId'])

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/orders/' + uid)
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
    def test_order_links_create(self):
        """
        V5 Test method order_links_create
        """

        link = {
            "comment": "test",
            "orders": [
                {
                    "id": 5604,
                    "externalId": 5603,
                    "number": 1
                },
                {
                    "id": 5605,
                    "externalId": 5601,
                    "number": 1
                }
            ]
        }

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/orders/links/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('link', link))
         .reply(201)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.order_links_create(link)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_order_payment_create(self):
        """
        V5 Test method payment_create
        """

        payment = {'order': {'externalId': '5603'}, 'type': 'bank-card'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/orders/payments/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('payment', payment))
         .reply(201)
         .headers(self.__header)
         .json({'success': 'true', 'id': 7777})
         )

        response = self.client.order_payment_create(payment)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_order_payment_delete(self):
        """
        V5 Test method order_payment_delete
        """

        uid = '7777'

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/orders/payments/' + uid + '/delete')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.order_payment_delete(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_order_payment_edit(self):
        """
        V5 Test method order_payment_edit
        """

        payment = {
            'externalId': '5603',
            'order': [
                {
                    'id': 5604,
                    'externalId': '5603',
                    'number': 1
                }
            ],
            'type': 'bank-card'
        }
        uid = str(self.__order['externalId'])

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/orders/payments/' + uid + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('payment', payment))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'payment': payment})
         )

        response = self.client.order_payment_edit(payment)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_orders_statuses_v5(self):
        """
        V5 Test method orders_statuses
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/orders/statuses')
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
    def test_orders_upload_v5(self):
        """
        V5 Test method orders_upload
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/orders/upload')
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
    def test_order_v5(self):
        """
        V5 Test method order
        """

        uid = str(self.__order['externalId'])

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/orders/' + uid)
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
        V5 Test method orders_edit
        """

        uid = str(self.__order['externalId'])

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/orders/' + uid + '/edit')
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
        V5 Test method packs
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/orders/packs')
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
        V5 Test method packs_create
        """

        packs_create = {'store': '7777z', 'quantity': 1, 'itemId': 7632}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/orders/packs/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('pack', packs_create))
         .reply(201)
         .headers(self.__header)
         .json({'success': 'true', 'id': 7777})
         )

        response = self.client.pack_create(packs_create)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_packs_history(self):
        """
        V5 Test method packs_history
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/orders/packs/history')
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
        V5 Test method pack
        """

        uid = str(self.__pack['id'])
        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/orders/packs/' + uid)
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
        V5 Test method packs_delete
        """

        uid = '7777'

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/orders/packs/' + uid + '/delete')
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
        V5 Test method pack_edit
        """

        uid = str(self.__pack['id'])

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/orders/packs/' + uid + '/edit')
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
    def test_payment_check(self):
        """
        V5 Test method payment_check
        """

        check = {'invoiceUuid': '577', 'amount': 1, 'currency': 'RU'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/payment/check')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('check', check))
         .reply(201)
         .headers(self.__header)
         .json({'success': 'true', 'result': {'success': 'true'}})
         )

        response = self.client.payment_check(check)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_payment_create_invoice(self):
        """
        V5 Test method payment_create_invoice
        """

        create_invoice = {'paymentId': 578, 'returnUrl': 'https://test.ru'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/payment/create-invoice')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('createInvoice', create_invoice))
         .reply(201)
         .headers(self.__header)
         .json({'success': 'true', 'result': {'link': 'https://test.ru'}})
         )

        response = self.client.payment_create_invoice(create_invoice)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_payment_update_invoice(self):
        """
        V5 Test method payment_update_invoice
        """

        update_invoice = {'invoiceUuid': '577', 'paymentId': '5304'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/payment/update-invoice')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('updateInvoice', update_invoice))
         .reply(201)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.payment_update_invoice(update_invoice)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_cost_groups(self):
        """
        V5 Test method cost_groups
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/cost-groups')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'costGroups': [
                        {
                            'code': 'cost-gr-example',
                            'name': 'CostGroup-example',
                            'ordering': 990,
                            'active': 'true',
                            'color': '#da5c98'
                        },
                        {
                            'code': 'cost-gr-lst7',
                            'name': 'CostGroup-lst7',
                            'ordering': 990,
                            'active': 'true',
                            'color': '#da5c98'
                        }
                    ]
                }
        )
        )

        response = self.client.cost_groups()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_cost_groups_edit(self):
        """
        V5 Test method cost_groups_edit
        """

        group = {'code': 'cost-gr-example', 'color': '#da5c98', 'ordering': 990, 'name': 'CostGroup-lst7'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/reference/cost-groups/' + group['code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('costGroup', group))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.cost_groups_edit(group)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_cost_items(self):
        """
        V5 Test method cost_items
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/cost-items')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'costItems': [
                        {
                            'code': 'cost-it-example',
                            'name': 'CostItem-example',
                            'group': 'cost-gr-example',
                            'ordering': 990,
                            'active': 'true',
                            'appliesToOrders': 'true',
                            'type': 'const',
                            'appliesToUsers': 'false'
                        },
                        {
                            'code': 'cost-it-1',
                            'name': 'CostItem-1',
                            'group': 'cost-gr-1',
                            'ordering': 990,
                            'active': 'true',
                            'appliesToOrders': 'true',
                            'type': 'const',
                            'appliesToUsers': 'false'
                        }
                    ]
                }
        )
        )

        response = self.client.cost_items()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_cost_items_edit(self):
        """
        V5 Test method cost_items_edit
        """

        item = {'code': 'cost-it-example', 'name': 'CostItem-example', 'ordering': 990, 'active': 'true'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/reference/cost-groups/' + item['code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('costItem', item))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.cost_items_edit(item)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_countries(self):
        """
        V5 Test method countries
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/countries')
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
    def test_couriers(self):
        """
        V5 Test method couriers
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/couriers')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'couriers': [
                        {
                            'id': 55,
                            'firstName': 'Jean',
                            'lastName': 'Doe',
                            'patronymic': 'M.',
                            'active': 'true',
                            'email': 'r9z4o@example.com'
                        },
                        {
                            'id': 57,
                            'firstName': 'John',
                            'lastName': 'Doe',
                            'patronymic': 'H.',
                            'active': 'true',
                            'email': 'oflf9@example.com'
                        }
                    ]
                }
        )
        )

        response = self.client.couriers()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_couriers_create(self):
        """
        V5 Test method couriers_create
        """

        courier = {
            'id': 55,
            'firstName': 'John',
            'lastName': 'Doe',
            'patronymic': 'H.',
            'active': 'true',
            'email': 'r9z4o@example.com'
        }

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/reference/couriers/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('courier', courier))
         .reply(201)
         .headers(self.__header)
         .json({'success': 'true', 'id': '8888'})
         )

        response = self.client.couriers_create(courier)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_couriers_edit(self):
        """
        V5 Test method couriers_edit
        """

        courier = {
            'id': 55,
            'firstName': 'John',
            'lastName': 'Doe',
            'patronymic': 'H.',
            'active': 'true',
            'email': 'r9z4o@example.com'
        }

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/reference/couriers/' + str(courier['id']) + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('courier', courier))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.couriers_edit(courier)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_delivery_services(self):
        """
        V5 Test method delivery_services
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/delivery-services')
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
                            'name': 'k1233',
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
        V5 Test method delivery_services_edit
        """

        service = {'code': 'hmo8s', 'name': 'x345'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/reference/delivery-services/' + service['code'] + '/edit')
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
        V5 Test method delivery_types
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/delivery-types')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(201)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'deliveryTypes': {
                        '1kp52': {
                            'name': 'c435',
                            'code': 'd345',
                            'defaultCost': 300,
                            'defaultNetCost': 0,
                            'paymentTypes': [
                                'cash',
                                'bank-card'
                            ],
                            'deliveryServices': [],
                            'defaultForCrm': 'false'
                        },
                        'example-code': {
                            'name': '1s0ei',
                            'code': 'example-code',
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
        V5 Test method delivery_types_edit
        """

        delivery_type = {'code': 'example-code', 'name': '1s0ei'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/reference/delivery-types/' + delivery_type['code'] + '/edit')
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
    def test_legal_entities(self):
        """
        V5 Test method legal_entities
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/legal-entities')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'legalEntities': [
                        {
                            'contragentType': 'legal-entity',
                            'legalName': 'Test LegalEntity-0aca34',
                            'code': '0aca34',
                            'countryIso': 'RU'
                        },
                        {
                            'contragentType': 'legal-entity',
                            'legalName': 'Test LegalEntity-2e8913',
                            'code': '2e8913',
                            'countryIso': 'RU'
                        }
                    ]
                }
        )
        )

        response = self.client.legal_entities()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_legal_entities_edit(self):
        """
        V5 Test method legal_entities_edit
        """

        legal = {
            'contragentType': 'legal-entity',
            'legalName': 'Test LegalEntity-0aca34',
            'code': '0aca34',
            'countryIso': 'RU'
        }

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/reference/legal-entities/' + legal['code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('legalEntity', legal))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.legal_entities_edit(legal)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_mg_channels(self):
        """
        V5 Test method mg_channels
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/mg-channels')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'mgChannels': [
                        {
                            'id': 1,
                            'externalId': 1,
                            'type': 'telegram',
                            'active': 'false'
                        },
                        {
                            'id': 2,
                            'externalId': 268,
                            'type': 'telegram',
                            'active': 'false'
                        }
                    ]
                }
        )
        )

        response = self.client.mg_channels()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_order_methods(self):
        """
        V5 Test method order_methods
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/order-methods')
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
        V5 Test method order_methods_edit
        """

        method = {'code': 'zoc5q', 'name': '1y0cp'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/reference/order-methods/' + method['code'] + '/edit')
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
        V5 Test method order_types
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/order-types')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'orderTypes': {
                        'example-code': {
                            'name': 'test',
                            'code': 'example-code',
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
        V5 Test method order_types_edit
        """

        order_type = {'code': 'example-code', 'name': 'test'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/reference/order-types/' + order_type['code'] + '/edit')
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
        V5 Test method payment_statuses
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/payment-statuses')
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
        V5 Test method payment_statuses_edit
        """

        status = {'code': 'payment-start', 'name': 'Платеж проведен'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/reference/payment-statuses/' + status['code'] + '/edit')
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
        V5 Test method payment_types
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/payment-types')
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
        V5 Test method payment_types_edit
        """

        payment_type = {'code': '238c06', 'name': 'TestPaymentType-238c06'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/reference/payment-types/' + payment_type['code'] + '/edit')
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
    def test_price_types(self):
        """
        V5 Test method price_types
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/price-types')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'priceTypes': [
                        {
                            'id': 174,
                            'code': 'sample_v5_price_code',
                            'name': 'Sample v5 price type',
                            'active': 'true',
                            'default': 'false',
                            'geo': [],
                            'groups': [],
                            'ordering': 500
                        },
                        {
                            'id': 170,
                            'code': 'l6u5c',
                            'name': 's50sa',
                            'active': 'false',
                            'default': 'false',
                            'geo': [],
                            'groups': [],
                            'ordering': 990
                        }
                    ]
                }
        )
        )

        response = self.client.price_types()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_price_types_edit(self):
        """
        V5 Test method price_types_edit
        """

        price_type = {
            'id': 174,
            'code': 'sample_v5_price_code',
            'name': 'Sample v5 price type',
            'active': 'true',
            'default': 'false',
            'geo': [],
            'groups': [],
            'ordering': 500
        }

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/reference/price-types/' + price_type['code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('priceTypes', price_type))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.price_types_edit(price_type)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_product_statuses(self):
        """
        V5 Test method product_statuses
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/product-statuses')
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
        V5 Test method product_statuses_edit
        """

        status = {'code': 'in-reserve', 'name': 'В резерве'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/reference/product-statuses/' + status['code'] + '/edit')
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
        V5 Test method sites
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/sites')
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
        V5 Test method sites_edit
        """

        site = {'code': 'code', 'name': 'XXX'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/reference/sites/' + site['code'] + '/edit')
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
        V5 Test method status_groups
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/status-groups')
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
        V5 Test method statuses
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/statuses')
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
        V5 Test method statuses_edit
        """

        status = {'code': 'new', 'name': 'Новый'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/reference/statuses/' + status['code'] + '/edit')
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
        V5 Test method stores
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/stores')
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
                            'name': 's344'
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
        V5 Test method stores_edit
        """

        store = {'code': 'q6w5i', 'name': 's234f'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/reference/stores/' + store['code'] + '/edit')
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
    def test_units(self):
        """
        V5 Test method units
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/reference/units')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'units': {
                        'pc': {
                            'code': 'pc',
                            'name': 'Штука',
                            'sym': 'шт.',
                            'default': 'true',
                            'active': 'true'
                        },
                        'kg': {
                            'code': 'kg',
                            'name': 'Килограмм',
                            'sym': 'кг',
                            'default': 'false',
                            'active': 'true'
                        }
                    }
                }
        )
        )

        response = self.client.units()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_units_edit(self):
        """
        V5 Test method units_edit
        """

        units = {
            'code': 'pc',
            'name': 'Штука',
            'sym': 'шт.',
            'default': 'true',
            'active': 'true'
        }

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/reference/units/' + units['code'] + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('units', units))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.units_edit(units)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_segments(self):
        """
        V5 Test method segments
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/segments')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[active]': 'true'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'segments': [
                        {
                            'id': 34,
                            'code': 'no-sex',
                            'name': 'Пол не указан',
                            'createdAt': '2018-04-10 12:34:30',
                            'isDynamic': 'true',
                            'customersCount': 1290,
                            'active': 'true'
                        },
                        {
                            'id': 33,
                            'code': 'women',
                            'name': 'Women',
                            'createdAt': '2018-04-10 12:34:30',
                            'isDynamic': 'true',
                            'customersCount': 0,
                            'active': 'true'
                        }
                    ]
                }
        )
        )

        response = self.client.segments({'active': 'true'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_inventories(self):
        """
        V5 Test method inventories
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/store/inventories')
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
                            'externalId': '89387',
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
        V5 Test method inventories_upload
        """

        offer = {'externalId': '89387', 'id': 33937}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/store/inventories/upload')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .body(self.dictionaryEncode('offers', offer))
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'processedOffersCount': 0,
                    'notFoundOffers': {
                        'externalId': '89387',
                        'id': 33937,
                        'xmlId': 9999
                    }
                }
        )
        )

        response = self.client.inventories_upload(offer)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_prices_upload(self):
        """
        V5 Test method prices_upload
        """

        price = [{'price': 999, 'externalId': '89387'}]

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/store/prices/upload')
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
                            'externalId': 'x2342'
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
    def test_product_groups(self):
        """
        V5 Test method product_groups
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/store/product-groups')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[active]': 'true'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': 20,
                        'totalCount': 115,
                        'currentPage': 1,
                        'totalPageCount': 6
                    },
                    'productGroup': [
                        {
                            'site': '127-0-0-1-8080',
                            'id': 2171,
                            'name': 'Cameras',
                            'externalId': '33',
                            'active': 'true'
                        },
                        {
                            'site': 'localhost-8080',
                            'id': 2133,
                            'name': 'Cameras',
                            'externalId': '33',
                            'active': 'true'
                        }
                    ]
                }
        )
        )

        response = self.client.product_groups({'active': 'true'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_products(self):
        """
        V5 Test method products
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/store/products')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[active]': 'true'})
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
                            'groups': [
                                {
                                    'id': 2171,
                                    'externalId': '33'
                                }
                            ],
                            'manufacturer': 'asdas',
                            'offers': [
                                {
                                    'name': 'example',
                                    'price': 100,
                                    'images': [],
                                    'id': 33937,
                                    'externalId': '89387',
                                    'article': 'x3421',
                                    'prices': [
                                        {
                                            'priceType': 'base',
                                            'price': 100,
                                            'ordering': 991
                                        }
                                    ],
                                    'weight': 44,
                                    'length': 324,
                                    'width': 33,
                                    'height': 432,
                                    'unit': {
                                        'code': 'pc',
                                        'name': 'Штука',
                                        'sym': 'шт.'
                                    }
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

        response = self.client.products({'active': 'true'})
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_products_properties(self):
        """
        V5 Test method products_properties
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/store/products/properties')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[active]': 'true'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': 20,
                        'totalCount': 24,
                        'currentPage': 1,
                        'totalPageCount': 2
                    },
                    'properties': [
                        {
                            'sites': [
                                'samsung'
                            ],
                            'code': 'type',
                            'name': 'Тип'
                        },
                        {
                            'sites': [
                                'samsung'
                            ],
                            'code': 'vendor_country',
                            'name': 'Страна производителя'
                        },
                        {
                            'sites': [
                                'samsung'
                            ],
                            'code': 'vendor_address',
                            'name': 'Юр. адрес производителя'
                        },
                        {
                            'sites': [
                                'samsung'
                            ],
                            'code': 'color',
                            'name': 'color'
                        }
                    ]
                }
        )
        )

        response = self.client.products_properties({'active': 'true'})
        pook.off()

        self.assertTrue(response.is_successful(), True)

    @pook.on
    def test_tasks(self):
        """
        V5 Test method tasks
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/tasks')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params({'filter[performers]': '15'})
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'pagination': {
                        'limit': 20,
                        'totalCount': 139,
                        'currentPage': 1,
                        'totalPageCount': 7
                    },
                    'tasks': [
                        {
                            'id': 433,
                            'text': 'test task edited',
                            'commentary': 'test commentary',
                            'datetime': '2020-02-20 05:01',
                            'createdAt': '2020-02-20 01:01:28',
                            'complete': 'false',
                            'performer': 15,
                            'performerType': 'user'
                        },
                        {
                            'id': 432,
                            'text': 'test task edited',
                            'commentary': 'test commentary',
                            'datetime': '2020-02-20 05:00',
                            'createdAt': '2020-02-20 01:00:07',
                            'complete': 'false',
                            'performer': 15,
                            'performerType': 'user'
                        }
                    ]
                }
        )
        )

        response = self.client.tasks({'performers': '15'})
        pook.off()

        self.assertTrue(response.is_successful(), True)

    @pook.on
    def test_task_create(self):
        """
        V5 Test method task_create
        """

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/tasks/create')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('task', self.__task))
         .reply(201)
         .headers(self.__header)
         .json({'success': 'true', 'id': 434})
         )

        response = self.client.task_create(self.__task)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_task(self):
        """
        V5 Test method task
        """

        uid = str(self.__task['id'])

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/tasks/' + uid)
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'task': self.__task})
         )

        response = self.client.task(uid)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_task_edit(self):
        """
        V5 Test method task_edit
        """

        uid = str(self.__task['id'])

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/tasks/' + uid + '/edit')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body(self.dictionaryEncode('task', self.__task))
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true', 'id': '433', 'task': self.__task})
         )

        response = self.client.task_edit(self.__task)
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def test_telephony_call_event(self):
        """
        V5 Test method telephony_call_event
        """

        call_event = {'phone': '+799999999', 'type': 'out'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/telephony/call/event')
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
        V5 Test method telephony_calls_upload
        """

        call = {'phone': '79999999999', 'type': 'out'}

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/telephony/calls/upload')
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
        V5 Test method telephony_manager
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/telephony/manager')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .params('+79999999999')
            .reply(200)
            .headers(self.__header)
            .json(
                {
                    'success': 'true',
                    'manager': {
                        'id': 777,
                        'firstName': 'John',
                        'lastName': 'Doe',
                        'patronymic': 'H.',
                        'email': 'mail@retailcrm.pro',
                        'code': 'ccc7'
                    },
                    'customer': {
                        'id': 888,
                        'externalId': '5406',
                        'firstName': 'John',
                        'lastName': 'Doe',
                        'patronymic': 'H.',
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
    def test_user_groups(self):
        """
        V5 Test method user_groups
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/user-groups')
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
        V5 Test method users
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/users')
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
        V5 Test method user
        """

        uid = '777'

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/users/' + uid)
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
    def test_user_status(self):
        """
        V5 Test method user_status
        """

        uid = '777'

        (pook.post(os.getenv('RETAILCRM_URL') + '/api/v5/users/' + uid + '/status')
         .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
         .body('status=free')
         .reply(200)
         .headers(self.__header)
         .json({'success': 'true'})
         )

        response = self.client.user_status(uid, 'free')
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)

    @pook.on
    def statistic_update(self):
        """
        V5 Test method statistic_update
        """

        (pook.get(os.getenv('RETAILCRM_URL') + '/api/v5/statistic/update')
            .headers({'X-API-KEY': os.getenv('RETAILCRM_KEY')})
            .reply(200)
            .headers(self.__header)
            .json({'success': 'true'}))

        response = self.client.statistic_update()
        pook.off()

        self.assertTrue(response.is_successful(), True)
        self.assertTrue(response.get_status_code() < 400, True)
