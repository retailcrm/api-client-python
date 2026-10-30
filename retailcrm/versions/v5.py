# coding=utf-8

"""
API Client version 5
"""

import json
from urllib.parse import quote

from retailcrm.versions.base import Base


class Client(Base):
    """RetailCRM API client"""

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

    def customer_subscription(self, uid, subscriptions, uid_type='externalId', site=None):
        """
        :param uid: string
        :param subscriptions: array of objects
        :param uid_type: string
        :param site: string
        :return: Response
        """
        self.parameters['subscriptions'] = json.dumps(subscriptions)

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if site is not None:
            self.parameters['site'] = site

        return self.post('/customers/' + str(uid) + '/subscriptions')

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

        return self.post("".join(
            [
                '/customers-corporate/',
                str(uid_corporate),
                '/addresses/',
                str(address[entity_by]),
                '/edit'
            ]
        ))

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

        return self.post("".join(
            [
                '/customers-corporate/',
                str(uid_corporate),
                '/companies/',
                str(company[entity_by]),
                '/edit'
            ]
        ))

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

        return self.post("".join(
            [
                '/customers-corporate/',
                str(uid_corporate),
                '/contacts/',
                str(contact[entity_by]),
                '/edit'
            ]
        ))

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

    def customer_interaction_cart_clear(self, site, cart, siteBy='code'):
        """
        :param site: string
        :param cart: object
        :param siteBy: string
        :return: Response
        """
        self.parameters['cart'] = json.dumps(cart)

        if siteBy != 'code':
            self.parameters['siteBy'] = siteBy

        return self.post('/customer-interaction/' + str(site) + '/cart/clear')

    def customer_interaction_cart_set(self, site, cart, siteBy='code'):
        """
        :param site: string
        :param cart: object
        :param siteBy: string
        :return: Response
        """
        self.parameters['cart'] = json.dumps(cart)

        if siteBy != 'code':
            self.parameters['siteBy'] = siteBy

        return self.post('/customer-interaction/' + str(site) + '/cart/set')

    def customer_interaction_cart(self, site, customer_id, uid_type='externalId', siteBy='code'):
        """
        :param site: string
        :param customer_id: string
        :param uid_type: string
        :param siteBy: string
        :return: Response
        """
        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if siteBy != 'code':
            self.parameters['siteBy'] = siteBy

        return self.get('/customer-interaction/' + str(site) + '/cart/' + str(customer_id))

    def customer_interaction_favorites(self, site, customer_id, uid_type='externalId', siteBy='code'):
        """
        :param site: string
        :param customer_id: string
        :param uid_type: string
        :param siteBy: string
        :return: Response
        """
        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if siteBy != 'code':
            self.parameters['siteBy'] = siteBy

        return self.get('/customer-interaction/' + str(site) + '/favorites/' + str(customer_id))

    def customer_interaction_favorites_add(self, site, customer_id, favorite, uid_type='externalId', siteBy='code'):
        """
        :param site: string
        :param customer_id: string
        :param favorite: object
        :param uid_type: string
        :param siteBy: string
        :return: Response
        """
        self.parameters['favorite'] = json.dumps(favorite)

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if siteBy != 'code':
            self.parameters['siteBy'] = siteBy

        return self.post('/customer-interaction/' + str(site) + '/favorites/' + str(customer_id) + '/add')

    def customer_interaction_favorite_remove(self, site, customer_id, favorite, uid_type='externalId', siteBy='code'):
        """
        :param site: string
        :param customer_id: string
        :param favorite: object
        :param uid_type: string
        :param siteBy: string
        :return: Response
        """
        self.parameters['favorite'] = json.dumps(favorite)

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if siteBy != 'code':
            self.parameters['siteBy'] = siteBy

        return self.post('/customer-interaction/' + str(site) + '/favorites/' + str(customer_id) + '/remove')

    def delivery_calculate(self, deliveryTypeCodes, order):
        """
        :param deliveryTypeCodes: array of strings
        :param order: object
        :return: Response
        """
        self.parameters['deliveryTypeCodes'] = json.dumps(deliveryTypeCodes)

        self.parameters['order'] = json.dumps(order)

        return self.post('/delivery/calculate')

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
        :param file: bytes, a binary file object, or a legacy dictionary
        :param site: string
        :return: Response
        """

        if isinstance(file, (bytes, bytearray)) or hasattr(file, 'read'):
            return self.post_file('/files/upload', file)

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
        :param code: string
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

    def integration_module_update_scopes(self, code, requires):
        """
        :param code: string
        :param requires: object
        :return: Response
        """
        self.parameters['requires'] = json.dumps(requires)

        return self.post('/integration-modules/' + str(code) + '/update-scopes')

    def loyalty_account_create(self, site, loyalty_account):
        """
        :param site: string
        :param loyalty_account: object
        :return: Response
        """
        self.parameters['site'] = site
        self.parameters['loyaltyAccount'] = json.dumps(loyalty_account)

        return self.post('/loyalty/account/create')

    def loyalty_account(self, uid):
        """
        :param uid: integer
        :return: Response
        """

        return self.get('/loyalty/account/' + str(uid))

    def loyalty_account_activate(self, uid):
        """
        :param uid: integer
        :return: Response
        """

        return self.post('/loyalty/account/' + str(uid) + '/activate')

    def loyalty_account_bonus_charge(self, uid, amount, comment):
        """
        :param uid: integer
        :param amount: float
        :param comment: string
        :return: Response
        """
        self.parameters['amount'] = amount
        self.parameters['comment'] = comment

        return self.post('/loyalty/account/' + str(uid) + '/bonus/charge')

    def loyalty_account_bonus_credit(self, uid, amount, activation_date, expire_date, comment):
        """
        :param uid: integer
        :param amount: float
        :param activation_date: date (Y-m-d)
        :param expire_date: date (Y-m-d)
        :param comment: string
        :return: Response
        """
        self.parameters['amount'] = amount
        self.parameters['activationDate'] = activation_date
        self.parameters['expireDate'] = expire_date
        self.parameters['comment'] = comment

        return self.post('/loyalty/account/' + str(uid) + '/bonus/credit')

    def loyalty_account_bonus_operations(self, uid, filters=None, limit=20, page=1):
        """
        :param uid: integer
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/loyalty/account/' + str(uid) + '/bonus/operations')

    def loyalty_account_bonus_details(self, uid, status, filters=None, limit=20, page=1):
        """
        :param uid: integer
        :param status: string
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/loyalty/account/' + str(uid) + '/bonus/' + str(status) + '/details')

    def loyalty_account_edit(self, uid, loyalty_account):
        """
        :param uid: integer
        :param loyalty_account: object
        :return: Response
        """
        self.parameters['loyaltyAccount'] = json.dumps(loyalty_account)

        return self.post('/loyalty/account/' + str(uid) + '/edit')

    def loyalty_accounts(self, filters=None, limit=20, page=1):
        """
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/loyalty/accounts')

    def loyalty_bonus_operations(self, filters=None, limit=20, cursor=None):
        """
        :param filters: object
        :param limit: integer
        :param cursor: string
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit

        if cursor:
            self.parameters['cursor'] = cursor

        return self.get('/loyalty/bonus/operations')

    def loyalty_calculate(self, order, site=None, bonuses=0):
        """
        :param order: object
        :param site: string
        :param bonuses: float
        :return: Response
        """
        self.parameters['order'] = json.dumps(order)

        if site is not None:
            self.parameters['site'] = site

        self.parameters['bonuses'] = bonuses

        return self.post('/loyalty/calculate')

    def loyalty_loyalties(self, filters=None, limit=20, page=1):
        """
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/loyalty/loyalties')

    def loyalty_loyalty(self, uid):
        """
        :param uid: integer
        :return: Response
        """

        return self.get('/loyalty/loyalties/' + str(uid))

    def notifications_send(self, notification):
        """
        :param notification: object
        :return: Response
        """
        self.parameters['notification'] = json.dumps(notification)

        return self.post('/notifications/send')

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

    def orders_loyalty_apply(self, order, site=None, bonuses=0):
        """
        :param order: object
        :param site: string
        :param bonuses: float
        :return: Response
        """
        self.parameters['order'] = json.dumps(order)

        if site is not None:
            self.parameters['site'] = site

        if bonuses != 0:
            self.parameters['bonuses'] = bonuses

        return self.post('/orders/loyalty/apply')

    def orders_loyalty_cancel_bonus_operations(self, order, site=None):
        """
        :param order: object
        :param site: string
        :return: Response
        """
        self.parameters['order'] = json.dumps(order)

        if site is not None:
            self.parameters['site'] = site

        return self.post('/orders/loyalty/cancel-bonus-operations')

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

    def orders_delivery_cancel(self, uid, uid_type='externalId', force='false'):
        """
        :param uid: string
        :param uid_type: string
        :param force: string
        """
        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        self.parameters['force'] = force

        return self.post('/orders/' + str(uid) + '/delivery/cancel')

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

    def orders_plates_print(self, uid, plate_id, uid_type='externalId', site=None):
        """
        :param uid: string
        :param plate_id: integer
        :param uid_type: string
        :param site: string
        :return: Response
        """
        if site is not None:
            self.parameters['site'] = site

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        return self.get('/orders/' + str(uid) + '/plates/' + str(plate_id) + '/print')

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

    def pack_edit(self, pack):
        """
        :param pack: object
        :return: Response
        """
        self.parameters['pack'] = json.dumps(pack)

        return self.post('/orders/packs/' + str(pack['id']) + '/edit')

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

    def payment_invoice_import(self, invoice):
        """
        :param invoice: object
        :return: Response
        """
        self.parameters['invoice'] = json.dumps(invoice)

        return self.post('/payment/invoice/import')

    def payment_invoice(self, uid):
        """
        :param uid: string
        :return: Response
        """

        return self.get('/payment/invoice/' + str(uid))

    def payment_update_invoice(self, update_invoice):
        """
        :param update_invoice: object
        :return: Response
        """
        self.parameters['updateInvoice'] = json.dumps(update_invoice)

        return self.post('/payment/update-invoice')

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

        return self.post('/reference/cost-items/' + cost_item['code'] + '/edit')

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

    def currencies(self):
        """
        :return: Response
        """

        return self.get('/reference/currencies')

    def currencies_create(self, currency):
        """
        :param currency: object
        :return: Response
        """
        self.parameters['currency'] = json.dumps(currency)

        return self.post('/reference/currencies/create')

    def currencies_edit(self, currency):
        """
        :param currency: object
        :return: Response
        """
        self.parameters['currency'] = json.dumps(currency)

        return self.post('/reference/currencies/' + str(currency['id']) + '/edit')

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

    def subscriptions(self):
        """
        :return: Response
        """

        return self.get('/reference/subscriptions')

    def subscriptions_edit(self, channel, code, subscription):
        """
        :param channel: string
        :param code: string
        :param subscription: object
        :return: Response
        """
        self.parameters['subscription'] = json.dumps(subscription)

        return self.post('/reference/subscriptions/' + str(channel) + '/' + str(code) + '/edit')

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

    def settings(self):
        """
        :return: Response
        """

        return self.get('/settings')

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

    def offers(self, filters=None, limit=20, page=1):
        """
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/store/offers')

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

    def product_groups_create(self, productGroup):
        """
        :param productGroup: object
        :return: Response
        """
        self.parameters['productGroup'] = json.dumps(productGroup)

        return self.post('/store/product-groups/create')

    def product_groups_edit(self, uid, productGroup, uid_type='externalId', site=None):
        """
        :param uid: string
        :param productGroup: object
        :param uid_type: string
        :param site: string
        :return: Response
        """
        self.parameters['productGroup'] = json.dumps(productGroup)

        if uid_type != 'externalId':
            self.parameters['by'] = uid_type

        if site is not None:
            self.parameters['site'] = site

        return self.post('/store/product-groups/' + str(uid) + '/edit')

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

    def products_batch_create(self, products):
        """
        :param products: array of objects
        :return: Response
        """
        self.parameters['products'] = json.dumps(products)

        return self.post('/store/products/batch/create')

    def products_batch_edit(self, products):
        """
        :param products: array of objects
        :return: Response
        """
        self.parameters['products'] = json.dumps(products)

        return self.post('/store/products/batch/edit')

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

    def products_properties_values(self, filters=None, limit=20, page=1):
        """
         :param filters: object
         :param limit: integer
         :param page: integer
         :return: Response
         """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/store/products/properties/values')

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

    def tasks_history(self, filters=None, limit=20, page=1):
        """
        :param filters: object
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['filter'] = filters
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/tasks/history')

    def task(self, uid):
        """
        :param uid: string
        :return: Response
        """

        return self.get('/tasks/' + str(uid))

    def tasks_comments(self, uid, limit=20, page=1):
        """
        :param uid: string
        :param limit: integer
        :param page: integer
        :return: Response
        """
        self.parameters['limit'] = limit
        self.parameters['page'] = page

        return self.get('/tasks/' + str(uid) + '/comments')

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

    def verification_sms_confirm(self, verification):
        """
        :param verification: object
        :return: Response
        """
        self.parameters['verification'] = json.dumps(verification)

        return self.post('/verification/sms/confirm')

    def verification_sms_status(self, check_id):
        """
        :param check_id: string
        :return: Response
        """

        return self.get('/verification/sms/' + str(check_id) + '/status')

    def web_analytics_client_ids_upload(self, client_ids):
        """
        :param client_ids: array of objects
        :return: Response
        """
        self.parameters['clientIds'] = json.dumps(client_ids)

        return self.post('/web-analytics/client-ids/upload')

    def web_analytics_sources_upload(self, sources):
        """
        :param sources: array of objects
        :return: Response
        """
        self.parameters['sources'] = json.dumps(sources)

        return self.post('/web-analytics/sources/upload')

    def web_analytics_visits_upload(self, visits):
        """
        :param visits: array of objects
        :return: Response
        """
        self.parameters['visits'] = json.dumps(visits)

        return self.post('/web-analytics/visits/upload')

    def statistic_update(self):
        """
        :return: Response
        """

        return self.get('/statistic/update')

    def knowledge_base_sections(self):
        """Return all sections without pagination."""
        return self.get('/knowledge-base/sections')

    def knowledge_base_section_create(self, section):
        """Create a section from name and optional parentId fields."""
        self.parameters['section'] = json.dumps(section)
        return self.post('/knowledge-base/sections/create')

    def knowledge_base_section_edit(self, uid, section):
        """Update supplied fields only; parentId=0 or None moves to the root."""
        self.parameters['section'] = json.dumps(section)
        return self.post('/knowledge-base/sections/' + quote(str(uid), safe='') + '/edit')

    def knowledge_base_section_delete(self, uid):
        """Delete a section together with its subsections and documents."""
        return self.post('/knowledge-base/sections/' + quote(str(uid), safe='') + '/delete')

    def knowledge_base_documents(self, filters=None, limit=20, cursor=None):
        """List documents using cursor pagination, including Markdown and file URLs.

        Pass pagination.nextCursor as cursor; an empty nextCursor ends the list.

        Filters: ids, externalIds, sectionId, directOnly, availableForCopilot,
        hasFile, search. directOnly without sectionId selects root documents.
        """
        self.parameters['filter'] = {
            name: int(value) if isinstance(value, bool) else value
            for name, value in (filters or {}).items()
        }
        self.parameters['limit'] = limit
        if cursor is not None:
            self.parameters['cursor'] = cursor
        return self.get('/knowledge-base/documents')

    def knowledge_base_document(self, uid, uid_type='externalId'):
        """Get a document by externalId (default) or internal id."""
        if uid_type != 'externalId':
            self.parameters['by'] = uid_type
        return self.get('/knowledge-base/documents/' + quote(str(uid), safe=''))

    def knowledge_base_document_create(self, document):
        """Create a document. Attach an original file through files_edit."""
        self.parameters['document'] = json.dumps(document)
        return self.post('/knowledge-base/documents/create')

    def knowledge_base_document_edit(self, uid, document, uid_type='externalId'):
        """Update only supplied fields, preserving False, zero, empty text and None."""
        self.parameters['document'] = json.dumps(document)
        if uid_type != 'externalId':
            self.parameters['by'] = uid_type
        return self.post('/knowledge-base/documents/' + quote(str(uid), safe='') + '/edit')

    def knowledge_base_document_delete(self, uid, uid_type='externalId'):
        """Delete a document by externalId (default) or internal id."""
        if uid_type != 'externalId':
            self.parameters['by'] = uid_type
        return self.post('/knowledge-base/documents/' + quote(str(uid), safe='') + '/delete')

    def knowledge_base_documents_history(self, filters=None, limit=20, page=1):
        """Read changes using sinceId, documentId, startDate and endDate filters.

        Content changes contain hashes rather than text. Sections have no history.
        """
        self.parameters['filter'] = filters or {}
        self.parameters['limit'] = limit
        self.parameters['page'] = page
        return self.get('/knowledge-base/documents/history')
