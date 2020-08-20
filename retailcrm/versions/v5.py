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
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/costs')

    def cost_create(self, cost, site=None):
        """
        :param cost: object
        :param site: string
        :return: Response
        """
        self.parameters['cost'] = json.dumps(cost)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/costs/create')

    def costs_delete(self, ids):
        """
        :param ids: array of integers
        :return: Response
        """
        self.parameters['ids'] = json.dumps(ids)

        return self.post('/costs/delete')

    def costs_upload(self, costs):
        """
        :param costs: array of objects
        :return: Response
        """
        self.parameters['costs'] = json.dumps(costs)

        return self.post('/costs/upload')

    def cost(self, uid):
        """
        :param uid: string
        :return: Response
        """

        return self.get('/costs/' + str(uid))

    def cost_delete(self, uid):
        """
        :param uid: string
        :return: Response
        """

        return self.post('/costs/' + str(uid) + '/delete')

    def cost_edit(self, cost, site=None):
        """
        :param cost: object
        :param site: string
        :return: Response
        """
        self.parameters['cost'] = json.dumps(cost)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/costs/' + str(cost['id']) + '/edit')

    def custom_fields(self, filters=None, limit=20, page=1):
        """
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/custom-fields')

    def custom_dictionaries(self, filters=None, limit=20, page=1):
        """
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/custom-fields/dictionaries')

    def custom_dictionary_create(self, dictionary):
        """
        :param dictionary: object
        :return: Response
        """
        self.parameters['customDictionary'] = json.dumps(dictionary)

        return self.post('/custom-fields/dictionaries/create')

    def custom_dictionary(self, code):
        """
        :param code: string
        :return: Response
        """

        return self.get('/custom-fields/dictionaries/' + str(code))

    def custom_dictionary_edit(self, dictionary):
        """
        :param dictionary: object
        :return: Response
        """
        self.parameters['customDictionary'] = json.dumps(dictionary)

        return self.post('/custom-fields/dictionaries/' + str(dictionary['code']) + '/edit')

    def custom_field_create(self, field):
        """
        :param field: object
        :return: Response
        """
        self.parameters['customField'] = json.dumps(field)

        return self.post('/custom-fields/' + str(field['entity']) + '/create')

    def custom_field(self, code, entity):
        """
        :param code: string
        :param entity: string
        :return: Response
        """

        return self.get('/custom-fields/' + str(entity) + '/' + str(code))

    def custom_field_edit(self, field):
        """
        :param field: object
        :return: Response
        """

        entity = str(field['entity'])
        code = str(field['code'])
        self.parameters['customField'] = json.dumps(field)

        return self.post('/custom-fields/' + entity + '/' + code + '/edit')

    def customers(self, filters=None, limit=20, page=1):
        """
        :param filters: object
        :param limit: integer
        :param page: integer
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
        :param customer: object
        :param site: string
        :return: Response
        """
        self.parameters['customer'] = json.dumps(customer)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers/create')

    def customers_fix_external_ids(self, customers, site=None):
        """
        :param customers: array of objects
        :param site: string
        :return: Response
        """
        self.parameters['customers'] = json.dumps(customers)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers/fix-external-ids')

    def customers_history(self, filters=None, limit=20, page=1):
        """
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/customers/history')

    def customer_notes(self, filters=None, limit=20, page=1):
        """
        :param filters: object
        :param limit: integer
        :param page: integer
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
        :param uid: integer
        :return: Response
        """

        return self.post('/customers/notes/' + str(uid) + '/delete')

    def customers_upload(self, customers, site=None):
        """
        :param customers: array of objects
        :param site: string
        :return: Response
        """
        self.parameters['customers'] = json.dumps(customers)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers/upload')

    def customer(self, uid, uid_type='externalId', site=None):
        """
        :param uid: string
        :param uid_type: string
        :param site: string
        :return: Response
        """
        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if site is not None:
            self.parameters['site'] = site

        return self.get('/customers/' + str(uid))

    def customer_edit(self, customer, uid_type='externalId', site=None):
        """
        :param customer: object
        :param uid_type: string
        :param site: string
        :return: Response
        """
        self.parameters['customer'] = json.dumps(customer)

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers/' + str(customer[uid_type]) + '/edit')

    def customers_corporate(self, filters=None, limit=20, page=1):
        """
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/customers-corporate')

    def customers_combine_corporate(self, customers, result):
        """
        :param customers: array of object
        :param result: object
        :return: Response
        """
        self.parameters['customers'] = json.dumps(customers)
        self.parameters['resultCustomer'] = json.dumps(result)

        return self.post('/customers-corporate/combine')

    def customer_corporate_create(self, customer_corporate, site=None):
        """
        :param customer_corporate: object
        :param site: string
        :return: Response
        """
        self.parameters['customerCorporate'] = json.dumps(customer_corporate)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers-corporate/create')

    def customers_corporate_fix_external_ids(self, customers_corporate, site=None):
        """
        :param customers_corporate: array of objects
        :param site: string
        :return: Response
        """
        self.parameters['customersCorporate'] = json.dumps(customers_corporate)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers-corporate/fix-external-ids')

    def customers_corporate_history(self, filters=None, limit=20, page=1):
        """
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/customers-corporate/history')

    def customer_corporate_notes(self, filters=None, limit=20, page=1):
        """
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/customers-corporate/notes')

    def customer_corporate_note_create(self, note, site=None):
        """
        :param note: object
        :param site: string
        :return: Response
        """
        self.parameters['note'] = json.dumps(note)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers-corporate/notes/create')

    def customer_corporate_note_delete(self, uid):
        """
        :param uid: integer
        :return: Response
        """

        return self.post('/customers-corporate/notes/' + str(uid) + '/delete')

    def customers_corporate_upload(self, customers_corporate, site=None):
        """
        :param customers_corporate: array of objects
        :param site: string
        :return: Response
        """
        self.parameters['customersCorporate'] = json.dumps(customers_corporate)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers-corporate/upload')

    def customer_corporate(self, uid, uid_type='externalId', site=None):
        """
        :param uid: string
        :param uid_type: string
        :param site: string
        :return: Response
        """
        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if site is not None:
            self.parameters['site'] = site

        return self.get('/customers-corporate/' + str(uid))

    def customer_corporate_addresses(self, uid, uid_type='externalId', limit=20, page=1, filters=None, site=None):
        """
        :param filters: object
        :param uid: string
        :param uid_type: string
        :param site: string
        :param limit: integer
        :param page: integer
        :return: Response
        """

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if site is not None:
            self.parameters['site'] = site

        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/customers-corporate/' + str(uid) + '/addresses')

    def customer_corporate_addresses_create(self, address, uid_type='externalId', site=None):
        """
        :param address: object
        :param uid_type: string
        :param site: string
        :return: Response
        """
        self.parameters['address'] = json.dumps(address)

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers-corporate/' + str(address[uid_type]) + '/addresses/create')

    def customer_corporate_addresses_edit(self,
                                          uid_corporate,
                                          address,
                                          uid_type='externalId',
                                          entity_by='externalId',
                                          site=None):
        """
        :param address: object
        :param uid_corporate: string
        :param uid_type: string
        :param entity_by: string
        :param site: string
        :return: Response
        """
        self.parameters['address'] = json.dumps(address)

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if entity_by != 'externalId':
            self.parameters['entityBy'] = entity_by

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers-corporate/' +
                         str(uid_corporate) +
                         '/addresses/' +
                         str(address[entity_by]) +
                         '/edit')

    def customer_corporate_companies(self, uid, uid_type='externalId', limit=20, page=1, filters=None, site=None):
        """
        :param filters: object
        :param uid: string
        :param uid_type: string
        :param site: string
        :param limit: integer
        :param page: integer
        :return: Response
        """

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if site is not None:
            self.parameters['site'] = site

        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/customers-corporate/' + str(uid) + '/companies')

    def customer_corporate_companies_create(self, company, uid_type='externalId', site=None):
        """
        :param company: object
        :param uid_type: string
        :param site: string
        :return: Response
        """
        self.parameters['company'] = json.dumps(company)

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers-corporate/' + str(company[uid_type]) + '/companies/create')

    def customer_corporate_companies_edit(self,
                                          uid_corporate,
                                          company,
                                          uid_type='externalId',
                                          entity_by='externalId',
                                          site=None):
        """
        :param company: object
        :param uid_corporate: string
        :param uid_type: string
        :param entity_by: string
        :param site: string
        :return: Response
        """
        self.parameters['company'] = json.dumps(company)

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if entity_by != 'externalId':
            self.parameters['entityBy'] = entity_by

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers-corporate/' +
                         str(uid_corporate) + '/companies/' + str(company[entity_by]) + '/edit')

    def customer_corporate_contacts(self, uid, uid_type='externalId', limit=20, page=1, filters=None, site=None):
        """
        :param filters: object
        :param uid: string
        :param uid_type: string
        :param site: string
        :param limit: integer
        :param page: integer
        :return: Response
        """

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if site is not None:
            self.parameters['site'] = site

        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/customers-corporate/' + str(uid) + '/contacts')

    def customer_corporate_contacts_create(self, contact, uid_type='externalId', site=None):
        """
        :param contact: object
        :param uid_type: string
        :param site: string
        :return: Response
        """
        self.parameters['contact'] = json.dumps(contact)

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers-corporate/' + str(contact[uid_type]) + '/contacts/create')

    def customer_corporate_contacts_edit(self,
                                         uid_corporate,
                                         contact,
                                         uid_type='externalId',
                                         entity_by='externalId',
                                         site=None):
        """
        :param contact: object
        :param uid_corporate: string
        :param uid_type: string
        :param entity_by: string
        :param site: string
        :return: Response
        """
        self.parameters['contact'] = json.dumps(contact)

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if entity_by != 'externalId':
            self.parameters['entityBy'] = entity_by

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers-corporate/' +
                         str(uid_corporate) + '/contacts/' + str(contact[entity_by]) + '/edit')

    def customer_corporate_edit(self, customer_corporate, uid_type='externalId', site=None):
        """
        :param customer_corporate: object
        :param uid_type: string
        :param site: string
        :return: Response
        """
        self.parameters['customersCorporate'] = json.dumps(customer_corporate)

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers-corporate/' + str(customer_corporate[uid_type]) + '/edit')

    def delivery_tracking(self, code, status_update):
        """
        :param code: string
        :param status_update: array of objects
        :return: Response
        """
        self.parameters['statusUpdate'] = json.dumps(status_update)

        return self.post('/delivery/generic/' + str(code) + '/tracking')

    def delivery_shipments(self, filters=None, limit=20, page=1):
        """
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/delivery/shipments')

    def delivery_shipment_create(self, shipment, site=None):
        """
        :param shipment: object
        :param site: string
        :return: Response
        """
        self.parameters['deliveryShipment'] = json.dumps(shipment)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/delivery/shipments/create')

    def delivery_shipment(self, uid):
        """
        :param uid: string
        :return: Response
        """

        return self.get('/delivery/shipments/' + str(uid))

    def delivery_shipment_edit(self, shipment, site=None):
        """
        :param shipment: object
        :param site: string
        :return: Response
        """
        self.parameters['deliveryShipment'] = json.dumps(shipment)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/delivery/shipment/' + str(shipment['id']) + '/edit')

    def files(self, filters=None, limit=20, page=1):
        """
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/files')

    def files_upload(self, file, site=None):
        """
        :param file: objects
        :param site: string
        :return: Response
        """

        self.parameters['file'] = json.dumps(file)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/files/upload')

    def file(self, uid):
        """
        :param uid: integer
        :return: Response
        """
        return self.get('/files/' + str(uid))

    def files_delete(self, uid):
        """
        :param uid: integer
        :return: Response
        """

        return self.post('/files/' + str(uid) + '/delete')

    def files_download(self, uid):
        """
        :param uid: integer
        :return: Response
        """

        return self.get('/files/' + str(uid) + '/download')

    def files_edit(self, file):
        """
        :param file: object
        :return: Response
        """
        self.parameters['file'] = json.dumps(file)

        return self.post('/files/' + str(file['id']) + '/edit')

    def integration_module(self, code):
        """
        :param code: integer
        :return: Response
        """

        return self.get('/integration-modules/' + str(code))

    def integration_module_edit(self, configuration):
        """
        :param configuration: object
        :return: Response
        """
        self.parameters['integrationModule'] = json.dumps(configuration)

        return self.post('/integration-modules/' + str(configuration['code']) + '/edit')

    def orders(self, filters=None, limit=20, page=1):
        """
        :param filters: object
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
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/orders/history')

    def order_links_create(self, link, site=None):
        """
        :param link: object
        :param site: string
        :return: Response
        """
        self.parameters['link'] = json.dumps(link)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/orders/links/create')

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
        if uid_type != 'externalId':
            self.parameters['by'] = uid_type
        if site is not None:
            self.parameters['site'] = site

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
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/orders/packs')

    def pack_create(self, pack):
        """
        :param pack: object
        :return: Response
        """
        self.parameters['pack'] = json.dumps(pack)

        return self.post('/orders/packs/create')

    def packs_history(self, filters=None, limit=20, page=1):
        """
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/orders/packs/history')

    def pack(self, uid):
        """
        :param uid: integer
        :return: Response
        """

        return self.get('/orders/packs/' + str(uid))

    def pack_delete(self, uid):
        """
        :param uid: integer
        :return: Response
        """

        return self.post('/orders/packs/' + str(uid) + '/delete')

    def payment_check(self, check):
        """
        :param check: object
        :return: Response
        """
        self.parameters['check'] = json.dumps(check)

        return self.post('/payment/check')

    def payment_create_invoice(self, create_invoice):
        """
        :param create_invoice: object
        :return: Response
        """
        self.parameters['createInvoice'] = json.dumps(create_invoice)

        return self.post('/payment/create-invoice')

    def payment_update_invoice(self, update_invoice):
        """
        :param update_invoice: object
        :return: Response
        """
        self.parameters['updateInvoice'] = json.dumps(update_invoice)

        return self.post('/payment/update-invoice')

    def pack_edit(self, pack):
        """
        :param pack: object
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
        :param cost_group: array of objects
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
        :param cost_item: array of objects
        :return: Response
        """
        self.parameters['costItem'] = json.dumps(cost_item)

        return self.post('/reference/cost-groups/' + cost_item['code'] + '/edit')

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
        :param courier: array of objects
        :return: Response
        """
        self.parameters['courier'] = json.dumps(courier)

        return self.post('/reference/couriers/create')

    def couriers_edit(self, courier):
        """
        :param courier: object
        :return: Response
        """
        self.parameters['courier'] = json.dumps(courier)

        return self.post('/reference/couriers/' + str(courier['id']) + '/edit')

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
        :param delivery_type: object
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
        :param legal_entity: object
        :return: Response
        """
        self.parameters['legalEntity'] = json.dumps(legal_entity)

        return self.post('/reference/legal-entities/' + legal_entity['code'] + '/edit')

    def mg_channels(self):
        """
        :return: Response
        """

        return self.get('/reference/mg-channels')

    def order_methods(self):
        """
        :return: Response
        """

        return self.get('/reference/order-methods')

    def order_methods_edit(self, order_method):
        """

        :param order_method: object
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
        :param order_type: object
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
        :param payment_status: object
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
        :param payment_type: object
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
        :param price_type: object
        :return: Response
        """
        self.parameters['priceTypes'] = json.dumps(price_type)

        return self.post('/reference/price-types/' + price_type['code'] + '/edit')

    def product_statuses(self):
        """
        :return: Response
        """

        return self.get('/reference/product-statuses')

    def product_statuses_edit(self, product_status):
        """
        :param product_status: object
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
        :param site: object
        :return: Response
        """
        self.parameters['site'] = json.dumps(site)

        return self.post('/reference/sites/' + site['code'] + '/edit')

    def status_groups(self):
        """
        :return Response
        """

        return self.get('/reference/status-groups')

    def statuses(self):
        """
        :return: Response
        """

        return self.get('/reference/statuses')

    def statuses_edit(self, status):
        """
        :param status: object
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
        :param store: object
        :return: Response
        """
        self.parameters['store'] = json.dumps(store)

        return self.post('/reference/stores/' + store['code'] + '/edit')

    def units(self):
        """
        :return: Response
        """

        return self.get('/reference/units')

    def units_edit(self, units):
        """
        :param units: object
        :return: Response
        """
        self.parameters['units'] = json.dumps(units)

        return self.post('/reference/units/' + units['code'] + '/edit')

    def segments(self, filters=None, limit=20, page=1):
        """
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/segments')

    def inventories(self, filters=None, limit=20, page=1):
        """
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/store/inventories')

    def inventories_upload(self, offers, site=None):
        """
        :param offers: array of objects
        :param site: string
        :return: Response
        """
        if site is not None:
            self.parameters['site'] = site

        self.parameters['offers'] = json.dumps(offers)

        return self.post('/store/inventories/upload')

    def prices_upload(self, prices):
        """
        :param prices: array of objects
        :return: Response
        """
        self.parameters['prices'] = json.dumps(prices)

        return self.post('/store/prices/upload')

    def product_groups(self, filters=None, limit=20, page=1):
        """
        :param filters: object
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
        :param filters: object
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
        :param filters: object
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
        :param filters: object
        :param limit: integer
        :param page: integer
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
        :param event: object
        :return: Response
        """
        self.parameters['event'] = json.dumps(event)

        return self.post('/telephony/call/event')

    def telephony_calls_upload(self, calls):
        """
        :param calls: array of objects
        :return: Response
        """
        self.parameters['calls'] = json.dumps(calls)

        return self.post('/telephony/calls/upload')

    def telephony_manager(self, phone, details=True, ignore_status=True):
        """
        :param phone: string
        :param details: string
        :param ignore_status: string
        :return: Response
        """
        self.parameters['phone'] = phone
        self.parameters['details'] = details
        self.parameters['ignoreStatus'] = ignore_status

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
        :param filters: object
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
        :param uid: integer
        :return: Response
        """

        return self.get('/users/' + str(uid))

    def user_status(self, uid, status):
        """
        :param uid: integer
        :param status: string
        :return: Response
        """

        self.parameters['status'] = status

        return self.post('/users/' + str(uid) + '/status')

    def statistic_update(self):
        """
        :return: Response
        """

        return self.get('/statistic/update')
