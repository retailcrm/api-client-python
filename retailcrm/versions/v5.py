# coding=utf-8

"""
API Client version 5
"""

import json

from retailcrm.versions.base import Base


class Client(Base):
    """retailCRM API client"""

    apiVersion = 'v5'

    def __init__(self, crm_url, api_key):
        Base.__init__(self, crm_url, api_key, self.apiVersion)

    def costs(self, filters=None, limit=20, page=1):
        """
        :param filters:
        :param limit:
        :param page:
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/costs')

    def cost_create(self, cost, site=None):
        """
        :param cost:
        :param site:
        :return: Response
        """
        self.parameters['cost'] = json.dumps(cost)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/costs/create')

    def costs_delete(self, ids):
        """
        :param ids:
        :return: Response
        """
        self.parameters['ids'] = json.dumps(ids)

        return self.post('/costs/delete')

    def costs_upload(self, costs):
        """
        :param costs:
        :return: Response
        """
        self.parameters['costs'] = json.dumps(costs)

        return self.post('/costs/upload')

    def cost(self, uid):
        """
        :param uid:
        :return: Response
        """

        return self.get('/costs/' + str(uid))

    def cost_delete(self, uid):
        """
        :param uid:
        :return: Response
        """

        return self.post('/costs/' + str(uid) + '/delete')

    def cost_edit(self, cost, site=None):
        """
        :param cost:
        :param site:
        :return: Response
        """
        self.parameters['cost'] = json.dumps(cost)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/costs/' + str(cost['id']) + '/edit')

    def custom_fields(self, filters=None, limit=20, page=1):
        """
        :param filters:
        :param limit:
        :param page:
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/custom-fields')

    def custom_dictionaries(self, filters=None, limit=20, page=1):
        """
        :param filters:
        :param limit:
        :param page:
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/custom-fields/dictionaries')

    def custom_dictionary_create(self, dictionary):
        """
        :param dictionary:
        :return: Response
        """
        self.parameters['customDictionary'] = json.dumps(dictionary)

        return self.post('/custom-fields/dictionaries/create')

    def custom_dictionary(self, code):
        """
        :param code:
        :return: Response
        """

        return self.get('/custom-fields/dictionaries/' + str(code))

    def custom_dictionary_edit(self, dictionary):
        """
        :param dictionary:
        :return: Response
        """
        self.parameters['customDictionary'] = json.dumps(dictionary)

        return self.post('/custom-fields/dictionaries/' + str(dictionary['code']) + '/create')

    def custom_field_create(self, field):
        """
        :param field:
        :return: Response
        """
        self.parameters['customField'] = json.dumps(field)

        return self.post('/custom-fields/' + str(field['entity']) + '/create')

    def custom_field(self, code, entity):
        """
        :param code:
        :param entity:
        :return: Response
        """

        return self.get('/custom-fields/' + str(entity) + '/' + str(code))

    def custom_field_edit(self, field):
        """
        :param field:
        :return: Response
        """

        entity = str(field['entity'])
        code = str(field['code'])
        self.parameters['customField'] = json.dumps(field)

        return self.post('/custom-fields/' + entity + '/' + code + '/create')

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

    def customers_combine(self, customers, result):
        """
        :param customers: array of object
        :param result: object
        :return: Response
        """
        self.parameters['customers'] = json.dumps(customers)
        self.parameters['resultCustomer'] = json.dumps(result)

        return self.post('/customers/combine')

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

    def customers_history(self, filters=None, limit=20, page=1):
        """
        :param filters:
        :param limit:
        :param page:
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/customers/history')

    def customer_notes(self, filters=None, limit=20, page=1):
        """
        :param filters:
        :param limit:
        :param page:
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/customers/notes')

    def customer_note_create(self, note, site=None):
        """
        :param note: object
        :param site: string
        :return: Response
        """
        self.parameters['note'] = json.dumps(note)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers/notes/create')

    def customer_note_delete(self, uid):
        """
        :param uid: string
        :return: Response
        """

        return self.post('/customers/notes/' + str(uid) + '/delete')

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

        return self.post('/customers/' + str(customer[uid_type]) + '/edit')

    def delivery_tracking(self, code, status_update):
        """
        :param code:
        :param status_update:
        :return: Response
        """
        self.parameters['statusUpdate'] = json.dumps(status_update)

        return self.post('/delivery/generic/' + str(code) + '/tracking')

    def delivery_shipments(self, filters=None, limit=20, page=1):
        """
        :param filters:
        :param limit:
        :param page:
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/delivery/shipments')

    def delivery_shipment_create(self, shipment, delivery_type, site=None):
        """
        :param shipment:
        :param delivery_type:
        :param site:
        :return: Response
        """
        self.parameters['deliveryShipment'] = json.dumps(shipment)
        self.parameters['deliveryType'] = delivery_type

        if site is not None:
            self.parameters['site'] = site

        return self.post('/delivery/shipment/create')

    def delivery_shipment(self, uid):
        """
        :param uid:
        :return: Response
        """

        return self.get('/delivery/shipments/' + str(uid))

    def delivery_shipment_edit(self, shipment, site=None):
        """
        :param shipment:
        :param site:
        :return: Response
        """
        self.parameters['deliveryShipment'] = json.dumps(shipment)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/delivery/shipment/' + shipment['id'] + '/edit')

    def integration_module(self, code):
        """
        :param code:
        :return: Response
        """

        return self.get('/integration-modules/' + str(code))

    def integration_module_edit(self, configuration):
        """
        :param configuration::
        :return: Response
        """
        self.parameters['integrationModule'] = json.dumps(configuration)

        return self.post('/integration-modules/' + str(configuration['code'])) + '/edit'

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

    def orders_combine(self, order, result_order, technique='ours'):
        """
        :param order: object
        :param result_order: object
        :param technique: string
        :return: Response
        """
        self.parameters['technique'] = technique
        self.parameters['order'] = json.dumps(order)
        self.parameters['resultOrder'] = json.dumps(result_order)

        return self.post('/orders/combine')

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

    def orders_history(self, filters=None, limit=20, page=1):
        """
        :param filters:
        :param limit:
        :param page:
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/orders/history')

    def order_payment_create(self, payment, site=None):
        """
        :param payment: object
        :param site: string
        :return: Response
        """
        self.parameters['payment'] = json.dumps(payment)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/orders/payments/create')

    def order_payment_delete(self, uid):
        """
        :param uid: string
        :return: Response
        """

        return self.post('/orders/payments/' + str(uid) + '/delete')

    def order_payment_edit(self, payment, uid_type='externalId', site=None):
        """
        :param payment: object
        :param uid_type: string
        :param site: string
        :return: Response
        """
        self.parameters['payment'] = json.dumps(payment)

        if site is not None:
            self.parameters['site'] = site

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        return self.post('/orders/payments/' + str(payment[uid_type]) + '/edit')

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

    def cost_groups(self):
        """
        :return: Response
        """

        return self.get('/reference/cost-groups')

    def cost_groups_edit(self, cost_group):
        """
        :param cost_group:
        :return: Response
        """
        self.parameters['costGroup'] = json.dumps(cost_group)

        return self.post('/reference/cost-groups/' + cost_group['code'] + '/edit')

    def cost_items(self):
        """
        :return: Response
        """

        return self.get('/reference/cost-items')

    def cost_items_edit(self, cost_item):
        """
        :param cost_item:
        :return: Response
        """
        self.parameters['costItem'] = json.dumps(cost_item)

        return self.post('/reference/delivery-services/' + cost_item['code'] + '/edit')

    def countries(self):
        """
        :return: Response
        """

        return self.get('/reference/countries')

    def couriers(self):
        """
        :return: Response
        """

        return self.get('/reference/couriers')

    def couriers_create(self, courier):
        """
        :param courier:
        :return: Response
        """
        self.parameters['courier'] = json.dumps(courier)

        return self.post('/reference/couriers/create')

    def couriers_edit(self, courier):
        """
        :param courier:
        :return: Response
        """
        self.parameters['courier'] = json.dumps(courier)

        return self.post('/reference/couriers/' + courier['code'] + '/edit')

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

    def legal_entities(self):
        """
        :return: Response
        """

        return self.get('/reference/legal-entities')

    def legal_entities_edit(self, legal_entity):
        """
        :param legal_entity:
        :return: Response
        """
        self.parameters['legalEntity'] = json.dumps(legal_entity)

        return self.post('/reference/legal-entities/' + legal_entity['code'] + '/edit')

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

    def price_types(self):
        """
        :return: Response
        """

        return self.get('/reference/price-types')

    def price_types_edit(self, price_type):
        """
        :param price_type:
        :return: Response
        """
        self.parameters['priceType'] = json.dumps(price_type)

        return self.post('/reference/price-types/' + price_type['code'] + '/edit')

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

    def segments(self, filters=None, limit=20, page=1):
        """
        :param filters:
        :param limit:
        :param page:
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/segments')

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

    def prices_upload(self, prices):
        """
        :param prices:
        :return: Response
        """
        self.parameters['prices'] = json.dumps(prices)

        return self.post('/store/prices/upload')

    def product_groups(self, filters=None, limit=20, page=1):
        """
        :param filters: array
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/store/product-groups')

    def products(self, filters=None, limit=20, page=1):
        """
        :param filters: array
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/store/products')

    def products_properties(self, filters=None, limit=20, page=1):
        """
        :param filters: array
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/store/products/properties')

    def tasks(self, filters=None, limit=20, page=1):
        """
        :param filters:
        :param limit:
        :param page:
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/tasks')

    def task_create(self, task, site=None):
        """
        :param task: object
        :param site: string
        :return: Response
        """
        self.parameters['task'] = json.dumps(task)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/tasks/create')

    def task(self, uid):
        """
        :param uid: string
        :return: Response
        """

        return self.get('/tasks/' + str(uid))

    def task_edit(self, task, site=None):
        """
        :param task: object
        :param site: string
        :return: Response
        """
        self.parameters['task'] = json.dumps(task)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/tasks/' + str(task['id']) + '/edit')

    def telephony_call_event(self, event):
        """
        :param event:
        :return: Response
        """
        self.parameters['event'] = json.dumps(event)

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

    def user_groups(self, limit=20, page=1):
        """
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/user-groups')

    def users(self, filters=None, limit=20, page=1):
        """
        :param filters: array
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/users')

    def user(self, uid):
        """
        :param uid:
        :return: Response
        """

        return self.get('/users/' + str(uid))

    def user_status(self, uid, status):
        """
        :param uid:
        :param status:
        :return: Response
        """

        self.parameters['status'] = status

        return self.post('/users/' + str(uid) + '/status')
