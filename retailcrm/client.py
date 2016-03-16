# coding=utf-8
import requests
import json
from response import Response


class Client(object):
    """retailCRM API client"""

    apiVersion = '3'

    def __init__(self, crm_url, api_key):
        self.apiUrl = crm_url + '/api/v' + self.apiVersion + '/'
        self.apiKey = api_key
        self.parameters = {'apiKey': api_key}

    def make_request(self, url, method='GET'):
        """
        :param url: string
        :param method: string
        :return: Response
        """
        global result
        if method == 'GET':
            result = requests.get(url, params=self.parameters)
        elif method == 'POST':
            result = requests.post(url, data=self.parameters)

        response_code = result.status_code
        response_body = result.json()

        return Response(response_code, response_body)

    def orders(self, filters, limit=20, page=1):
        """
        :param filters: array
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page
        url = self.apiUrl + 'orders'

        return self.make_request(url)

    def orders_get(self, uid, by='externalId', site=None):
        """
        :param uid: string
        :param by: string
        :param site: string
        :return: Response
        """
        url = self.apiUrl + 'orders/' + str(uid)

        if site is not None:
            self.parameters['site'] = site

        if by != 'externalId':
            self.parameters['by'] = by

        return self.make_request(url)

    def orders_create(self, order, site=None):
        """

        :param order:
        :param site:
        :return:
        """
        data_json = json.dumps(order)
        self.parameters['order'] = data_json

        if site is not None:
            self.parameters['site'] = site

        url = self.apiUrl + 'orders/create'

        return self.make_request(url, 'POST')

    def orders_edit(self, order, site=None):
        """

        :param order:
        :param site:
        :return:
        """
        data_json = json.dumps(order)
        self.parameters['order'] = data_json

        if site is not None:
            self.parameters['site'] = site

        url = self.apiUrl + 'orders/' + str(order['externalId']) + '/edit'

        return self.make_request(url, 'POST')

    def orders_upload(self, orders, site=None):
        """

        :param orders:
        :param site:
        :return:
        """
        data_json = json.dumps(orders)
        self.parameters['orders'] = data_json

        if site is not None:
            self.parameters['site'] = site

        url = self.apiUrl + 'orders/upload'

        return self.make_request(url, 'POST')

    def orders_fix_external_ids(self, orders, site=None):
        """

        :param orders:
        :param site:
        :return:
        """
        data_json = json.dumps(orders)
        self.parameters['orders'] = data_json

        if site is not None:
            self.parameters['site'] = site

        url = self.apiUrl + 'orders/fix-external-ids'

        return self.make_request(url, 'POST')

    def orders_statuses(self, ids, external_ids):
        """

        :param ids:
        :param external_ids:
        :return:
        """
        self.parameters['ids'] = ids
        self.parameters['externalIds'] = external_ids
        url = self.apiUrl + 'orders/statuses'

        return self.make_request(url)

    def orders_history(self, start_date=None, end_date=None, limit=100, offset=0, skip_my_changes=True):
        """

        :param start_date:
        :param end_date:
        :param limit:
        :param offset:
        :param skip_my_changes:
        :return:
        """
        self.parameters['startDate'] = start_date
        self.parameters['endDate'] = end_date
        self.parameters['limit'] = limit
        self.parameters['offset'] = offset
        self.parameters['skipMyChanges'] = skip_my_changes
        url = self.apiUrl + 'orders/history'

        return self.make_request(url)

    def customers(self, filters, limit=20, page=0):
        """

        :param filters:
        :param limit:
        :param page:
        :return:
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page
        url = self.apiUrl + 'customers'

        return self.make_request(url)

    def customers_get(self, uid, by='externalId', site=None):
        """

        :param uid:
        :param by:
        :param site:
        :return:
        """
        url = self.apiUrl + 'customers/' + str(uid)

        if by != 'externalId':
            self.parameters['by'] = by

        if site is not None:
            self.parameters['site'] = site

        return self.make_request(url)

    def customers_create(self, customer, site=None):
        """

        :param customer:
        :param site:
        :return:
        """
        data_json = json.dumps(customer)
        self.parameters['customer'] = data_json

        if site is not None:
            self.parameters['site'] = site

        url = self.apiUrl + 'customers/create'

        return self.make_request(url, 'POST')

    def customers_edit(self, customer, site=None):
        """

        :param customer:
        :param site:
        :return:
        """
        data_json = json.dumps(customer)
        self.parameters['customer'] = data_json

        if site is not None:
            self.parameters['site'] = site

        url = self.apiUrl + 'customers/' + customer['externalId'] + '/edit'
        return self.make_request(url, 'POST')

    def customers_upload(self, customers, site=None):
        """

        :param customers:
        :param site:
        :return:
        """
        data_json = json.dumps(customers)
        self.parameters['customers'] = data_json

        if site is not None:
            self.parameters['site'] = site

        url = self.apiUrl + 'customers/upload'

        return self.make_request(url, 'POST')

    def customers_fix_external_ids(self, customers, site=None):
        """

        :param customers:
        :param site:
        :return:
        """
        data_json = json.dumps(customers)
        self.parameters['customers'] = data_json

        if site is not None:
            self.parameters['site'] = site

        url = self.apiUrl + 'customers/fix-external-ids'

        return self.make_request(url, 'POST')

    def inventories(self, filters, limit=20, page=1):
        """

        :param filters:
        :param limit:
        :param page:
        :return:
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page
        url = self.apiUrl + 'store/inventories'

        return self.make_request(url)

    def inventories_upload(self, offers):
        """

        :param offers:
        :return:
        """
        data_json = json.dumps(offers)
        self.parameters['offers'] = data_json
        url = self.apiUrl + 'store/inventories/upload'

        return self.make_request(url, 'POST')

    def packs(self, filters, limit=20, page=1):
        """

        :param filters:
        :param limit:
        :param page:
        :return:
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page
        url = self.apiUrl + 'orders/packs'

        return self.make_request(url)

    def packs_get(self, uid):
        """

        :param uid:
        :return:
        """
        url = self.apiUrl + 'orders/packs/' + str(uid)

        return self.make_request(url)

    def packs_create(self, pack):
        """

        :param pack:
        :return:
        """
        data_json = json.dumps(pack)
        self.parameters['pack'] = data_json
        url = self.apiUrl + 'orders/packs/create'

        return self.make_request(url, 'POST')

    def packs_edit(self, pack, uid):
        """

        :param pack:
        :param uid:
        :return:
        """
        data_json = json.dumps(pack)
        self.parameters['pack'] = data_json
        url = self.apiUrl + 'orders/packs/' + str(uid) + '/edit'

        return self.make_request(url, 'POST')

    def packs_delete(self, uid):
        """

        :param uid:
        :return:
        """
        url = self.apiUrl + 'orders/packs/' + str(uid) + '/delete'

        return self.make_request(url, 'POST')

    def packs_history(self, filters, limit=20, page=1):
        """

        :param filters:
        :param limit:
        :param page:
        :return:
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page
        url = self.apiUrl + 'orders/packs/history'

        return self.make_request(url)

    def countries(self):
        """

        :return:
        """
        url = self.apiUrl + 'reference/countries'

        return self.make_request(url)

    def delivery_types(self):
        """

        :return:
        """
        url = self.apiUrl + 'reference/delivery-types'

        return self.make_request(url)

    def delivery_types_edit(self, delivery_type):
        """

        :param delivery_type:
        :return:
        """
        data_json = json.dumps(delivery_type)
        self.parameters['deliveryType'] = data_json
        url = self.apiUrl + 'reference/delivery-types/' + delivery_type['code'] + '/edit'

        return self.make_request(url, 'POST')

    def delivery_services(self):
        """

        :return:
        """
        url = self.apiUrl + 'reference/delivery-services'

        return self.make_request(url)

    def delivery_services_edit(self, delivery_service):
        """

        :param delivery_service:
        :return:
        """
        data_json = json.dumps(delivery_service)
        self.parameters['deliveryService'] = data_json
        url = self.apiUrl + 'reference/delivery-services/' + delivery_service['code'] + '/edit'

        return self.make_request(url, 'POST')

    def payment_types(self):
        """

        :return:
        """
        url = self.apiUrl + 'reference/payment-types'

        return self.make_request(url)

    def payment_types_edit(self, payment_type):
        """

        :param payment_type:
        :return:
        """
        data_json = json.dumps(payment_type)
        self.parameters['paymentType'] = data_json
        url = self.apiUrl + 'reference/payment-types/' + payment_type['code'] + '/edit'

        return self.make_request(url, 'POST')

    def payment_statuses(self):
        """

        :return:
        """
        url = self.apiUrl + 'reference/payment-statuses'

        return self.make_request(url)

    def payment_statuses_edit(self, payment_status):
        """

        :param payment_status:
        :return:
        """
        data_json = json.dumps(payment_status)
        self.parameters['paymentStatus'] = data_json
        url = self.apiUrl + 'reference/payment-statuses/' + payment_status['code'] + '/edit'

        return self.make_request(url, 'POST')

    def product_statuses(self):
        """

        :return:
        """
        url = self.apiUrl + 'reference/product-statuses'

        return self.make_request(url)

    def product_statuses_edit(self, product_status):
        """

        :param product_status:
        :return:
        """
        data_json = json.dumps(product_status)
        self.parameters['productStatus'] = data_json
        url = self.apiUrl + 'reference/product-statuses/' + product_status['code'] + '/edit'

        return self.make_request(url, 'POST')

    def order_types(self):
        """

        :return:
        """
        url = self.apiUrl + 'reference/order-types'

        return self.make_request(url)

    def order_types_edit(self, order_type):
        """

        :param order_type:
        :return:
        """
        data_json = json.dumps(order_type)
        self.parameters['orderType'] = data_json
        url = self.apiUrl + 'reference/order-types/' + order_type['code'] + '/edit'

        return self.make_request(url, 'POST')

    def order_methods(self):
        """

        :return:
        """
        url = self.apiUrl + 'reference/order-methods'

        return self.make_request(url)

    def order_methods_edit(self, order_method):
        """

        :param order_method:
        :return:
        """
        data_json = json.dumps(order_method)
        self.parameters['orderMethod'] = data_json
        url = self.apiUrl + 'reference/order-methods/' + order_method['code'] + '/edit'

        return self.make_request(url, 'POST')

    def status_groups(self):
        """
        :return
        """
        url = self.apiUrl + 'reference/status-groups'

        return self.make_request(url)

    def statuses(self):
        """

        :return:
        """
        url = self.apiUrl + 'reference/statuses'

        return self.make_request(url)

    def statuses_edit(self, status):
        """

        :param status:
        :return:
        """
        data_json = json.dumps(status)
        self.parameters['status'] = data_json
        url = self.apiUrl + 'reference/statuses/' + status['code'] + '/edit'

        return self.make_request(url, 'POST')

    def stores(self):
        """

        :return:
        """
        url = self.apiUrl + 'reference/stores'

        return self.make_request(url)

    def stores_edit(self, store):
        """

        :param store:
        :return:
        """
        data_json = json.dumps(store)
        self.parameters['status'] = data_json
        url = self.apiUrl + 'reference/stores/' + store['code'] + '/edit'

        return self.make_request(url, 'POST')

    def statistic_update(self):
        """
        :return
        """
        url = self.apiUrl + 'statistic/update'

        return self.make_request(url)

    def telephony_call_event(self, phone, call_type, code, status):
        """

        :param phone:
        :param call_type:
        :param code:
        :param status:
        :return:
        """
        self.parameters['hangupStatus'] = status
        self.parameters['phone'] = phone
        self.parameters['code'] = code
        self.parameters['type'] = call_type
        url = self.apiUrl + 'telephony/call/event'

        return self.make_request(url, 'POST')

    def telephony_calls_upload(self, calls):
        """

        :param calls:
        :return:
        """
        data_json = json.dumps(calls)
        self.parameters['calls'] = data_json
        url = self.apiUrl + 'telephony/calls/upload'

        return self.make_request(url, 'POST')

    def telephony_settings(self, code, client_id, make_call_url, active, name, image):
        """

        :param code:
        :param client_id:
        :param make_call_url:
        :param active:
        :param name:
        :param image:
        :return:
        """
        self.parameters['code'] = code
        self.parameters['clientId'] = client_id
        self.parameters['makeCallUrl'] = make_call_url
        self.parameters['active'] = active
        self.parameters['name'] = name
        self.parameters['image'] = image
        url = self.apiUrl + 'telephony/settings/' + str(code)

        return self.make_request(url, 'POST')

    def telephony_manager(self, phone, details=True):
        """

        :param phone:
        :param details:
        :return:
        """
        self.parameters['phone'] = phone
        self.parameters['details'] = details
        url = self.apiUrl + 'telephony/manager'

        return self.make_request(url)
