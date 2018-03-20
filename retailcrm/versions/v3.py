# coding=utf-8

"""
API Client version 3
"""

import json

from retailcrm.versions.base import Base


class Client(Base):
    """retailCRM API client"""

    apiVersion = 'v3'

    def __init__(self, crm_url, api_key):
        Base.__init__(self, crm_url, api_key, self.apiVersion)

    def customers(self, filters=None, limit=20, page=1):
        """
        :param filters:
        :param limit:
        :param page:
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/customers')

    def customer_create(self, customer, site=None):
        """
        :param customer:
        :param site:
        :return: Response
        """
        self.parameters['customer'] = json.dumps(customer)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers/create')

    def customers_fix_external_ids(self, customers, site=None):
        """
        :param customers:
        :param site:
        :return: Response
        """
        self.parameters['customers'] = json.dumps(customers)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers/fix-external-ids')

    def customers_upload(self, customers, site=None):
        """
        :param customers:
        :param site:
        :return: Response
        """
        self.parameters['customers'] = json.dumps(customers)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers/upload')

    def customer(self, uid, uid_type='externalId', site=None):
        """
        :param uid:
        :param uid_type:
        :param site:
        :return: Response
        """
        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if site is not None:
            self.parameters['site'] = site

        return self.get('/customers/' + str(uid))

    def customer_edit(self, customer, uid_type='externalId', site=None):
        """
        :param customer:
        :param uid_type:
        :param site:
        :return: Response
        """
        self.parameters['customer'] = json.dumps(customer)

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers/' + customer[uid_type] + '/edit')

    def orders(self, filters=None, limit=20, page=1):
        """
        :param filters: array
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/orders')

    def order_create(self, order, site=None):
        """
        :param order: object
        :param site: string
        :return: Response
        """
        self.parameters['order'] = json.dumps(order)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/orders/create')

    def orders_fix_external_ids(self, orders, site=None):
        """
        :param orders: object
        :param site: string
        :return: Response
        """
        self.parameters['orders'] = json.dumps(orders)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/orders/fix-external-ids')

    def orders_history(self, start=None, end=None, limit=100, offset=0, skip=True):
        """
        :param start:
        :param end:
        :param limit:
        :param offset:
        :param skip:
        :return: Response
        """
        self.parameters['startDate'] = start
        self.parameters['endDate'] = end
        self.parameters['limit'] = limit
        self.parameters['offset'] = offset
        self.parameters['skipMyChanges'] = skip

        return self.get('/orders/history')

    def orders_statuses(self, ids, external_ids):
        """
        :param ids: array
        :param external_ids: array
        :return: Response
        """
        self.parameters['ids'] = ids
        self.parameters['externalIds'] = external_ids

        return self.get('/orders/statuses')

    def orders_upload(self, orders, site=None):
        """
        :param orders: object
        :param site: string
        :return: Response
        """
        self.parameters['orders'] = json.dumps(orders)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/orders/upload')

    def order(self, uid, uid_type='externalId', site=None):
        """
        :param uid: string
        :param uid_type: string
        :param site: string
        :return: Response
        """
        if site is not None:
            self.parameters['site'] = site

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        return self.get('/orders/' + str(uid))

    def order_edit(self, order, uid_type='externalId', site=None):
        """
        :param order: object
        :param uid_type: string
        :param site: string
        :return: Response
        """
        self.parameters['order'] = json.dumps(order)

        if site is not None:
            self.parameters['site'] = site

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        return self.post('/orders/' + str(order[uid_type]) + '/edit')

    def packs(self, filters=None, limit=20, page=1):
        """
        :param filters:
        :param limit:
        :param page:
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/orders/packs')

    def pack_create(self, pack):
        """
        :param pack:
        :return: Response
        """
        self.parameters['pack'] = json.dumps(pack)

        return self.post('/orders/packs/create')

    def packs_history(self, filters=None, limit=20, page=1):
        """
        :param filters:
        :param limit:
        :param page:
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/orders/packs/history')

    def pack(self, uid):
        """
        :param uid:
        :return: Response
        """

        return self.get('/orders/packs/' + str(uid))

    def pack_delete(self, uid):
        """
        :param uid:
        :return: Response
        """

        return self.post('/orders/packs/' + str(uid) + '/delete')

    def pack_edit(self, pack):
        """
        :param pack:
        :return: Response
        """
        self.parameters['pack'] = json.dumps(pack)

        return self.post('/orders/packs/' + str(pack['id']) + '/edit')

    def countries(self):
        """
        :return: Response
        """

        return self.get('/reference/countries')

    def delivery_services(self):
        """
        :return: Response
        """

        return self.get('/reference/delivery-services')

    def delivery_services_edit(self, delivery_service):
        """
        :param delivery_service:
        :return: Response
        """
        self.parameters['deliveryService'] = json.dumps(delivery_service)

        return self.post('/reference/delivery-services/' + delivery_service['code'] + '/edit')

    def delivery_types(self):
        """
        :return: Response
        """

        return self.get('/reference/delivery-types')

    def delivery_types_edit(self, delivery_type):
        """
        :param delivery_type:
        :return: Response
        """
        self.parameters['deliveryType'] = json.dumps(delivery_type)

        return self.post('/reference/delivery-types/' + delivery_type['code'] + '/edit')

    def order_methods(self):
        """
        :return: Response
        """

        return self.get('/reference/order-methods')

    def order_methods_edit(self, order_method):
        """

        :param order_method:
        :return: Response
        """
        self.parameters['orderMethod'] = json.dumps(order_method)

        return self.post('/reference/order-methods/' + order_method['code'] + '/edit')

    def order_types(self):
        """
        :return: Response
        """

        return self.get('/reference/order-types')

    def order_types_edit(self, order_type):
        """
        :param order_type:
        :return: Response
        """
        self.parameters['orderType'] = json.dumps(order_type)

        return self.post('/reference/order-types/' + order_type['code'] + '/edit')

    def payment_statuses(self):
        """
        :return: Response
        """

        return self.get('/reference/payment-statuses')

    def payment_statuses_edit(self, payment_status):
        """
        :param payment_status:
        :return: Response
        """
        self.parameters['paymentStatus'] = json.dumps(payment_status)

        return self.post('/reference/payment-statuses/' + payment_status['code'] + '/edit')

    def payment_types(self):
        """
        :return: Response
        """

        return self.get('/reference/payment-types')

    def payment_types_edit(self, payment_type):
        """
        :param payment_type:
        :return: Response
        """
        self.parameters['paymentType'] = json.dumps(payment_type)

        return self.post('/reference/payment-types/' + payment_type['code'] + '/edit')

    def product_statuses(self):
        """
        :return: Response
        """

        return self.get('/reference/product-statuses')

    def product_statuses_edit(self, product_status):
        """
        :param product_status:
        :return: Response
        """
        self.parameters['productStatus'] = json.dumps(product_status)

        return self.post('/reference/product-statuses/' + product_status['code'] + '/edit')

    def sites(self):
        """
        :return: Response
        """

        return self.get('/reference/sites')

    def sites_edit(self, site):
        """
        :param site:
        :return: Response
        """
        self.parameters['site'] = json.dumps(site)

        return self.post('/reference/sites/' + site['code'] + '/edit')

    def status_groups(self):
        """
        :return
        """

        return self.get('/reference/status-groups')

    def statuses(self):
        """
        :return: Response
        """

        return self.get('/reference/statuses')

    def statuses_edit(self, status):
        """
        :param status:
        :return: Response
        """
        self.parameters['status'] = json.dumps(status)

        return self.post('/reference/statuses/' + status['code'] + '/edit')

    def stores(self):
        """
        :return: Response
        """

        return self.get('/reference/stores')

    def stores_edit(self, store):
        """
        :param store:
        :return: Response
        """
        self.parameters['status'] = json.dumps(store)

        return self.post('/reference/stores/' + store['code'] + '/edit')

    def inventories(self, filters=None, limit=20, page=1):
        """
        :param filters:
        :param limit:
        :param page:
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/store/inventories')

    def inventories_upload(self, offers):
        """
        :param offers:
        :return: Response
        """
        self.parameters['offers'] = json.dumps(offers)

        return self.post('/store/inventories/upload')

    def telephony_call_event(self, phone, call_type, code, status):
        """
        :param phone:
        :param call_type:
        :param code:
        :param status:
        :return: Response
        """
        self.parameters['hangupStatus'] = status
        self.parameters['phone'] = phone
        self.parameters['code'] = code
        self.parameters['type'] = call_type

        return self.post('/telephony/call/event')

    def telephony_calls_upload(self, calls):
        """
        :param calls:
        :return: Response
        """
        self.parameters['calls'] = json.dumps(calls)

        return self.post('/telephony/calls/upload')

    def telephony_manager(self, phone, details=True):
        """
        :param phone:
        :param details:
        :return: Response
        """
        self.parameters['phone'] = phone
        self.parameters['details'] = details

        return self.get('/telephony/manager')

    def telephony_settings(self, code, client_id, make_call_url, active, name, image):
        """
        :param code:
        :param client_id:
        :param make_call_url:
        :param active:
        :param name:
        :param image:
        :return: Response
        """
        self.parameters['code'] = code
        self.parameters['clientId'] = client_id
        self.parameters['makeCallUrl'] = make_call_url
        self.parameters['active'] = active
        self.parameters['name'] = name
        self.parameters['image'] = image

        return self.post('/telephony/settings/' + str(code))
