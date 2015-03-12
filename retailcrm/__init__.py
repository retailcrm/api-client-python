import requests
import json


class Client:
    """RetailCrm API client"""

    apiVersion = '3'

    def __init__(self, crmUrl, apiKey):
        self.apiUrl = crmUrl + '/api/v' + self.apiVersion + '/'
        self.apiKey = apiKey
        self.parameters = {'apiKey': apiKey}

    def requestApi(self, url, method='GET', format='json'):

        # TODO: catch http exceptions
        if method == 'GET':
            result = requests.get(url, params=self.parameters)
        elif method == 'POST':
            result = requests.post(url, data=self.parameters)

        statusCode = result.status_code
        r = result.json()

        # reset params dict
        self.parameters = {'apiKey': self.apiKey}

        if statusCode > 400 or r.has_key('success') and r['success'] == False:
            #TODO: raise ApiException
            pass

        if r.has_key('generatedAt'):
            self.generatedAt = r['generatedAt']
            del r['generatedAt']

        del r['success']

        return r

    def getErrorMessage(self, response):
        if type(response) is not dict: return ''
        err = ''

        if response.has_key('message'):
            err = response['message']
        elif response.has_key('error'):
            err = response['error']['message']
        elif response.has_key('errorMsg'):
            err = response['errorMsg']

        if len(err) == 0: return 'Application Error'

        return err

    def orderGet(self, id, by='externalId'):
        url = self.apiUrl + 'orders/' + str(id)

        if by != 'externalId':
            self.parameters['by'] = by

        return self.requestApi(url)

    def orderCreate(self, order):
        dataJson = json.dumps(order)
        self.parameters['order'] = dataJson

        url = self.apiUrl + 'orders/create'
        return self.requestApi(url, 'POST')

    def orderEdit(self, order):
        dataJson = json.dumps(order)
        self.parameters['order'] = dataJson

        url = self.apiUrl + 'orders/' + str(order['externalId']) + '/edit'
        return self.requestApi(url, 'POST')

    def orderUpload(self, orders):
        dataJson = json.dumps(orders)
        self.parameters['orders'] = dataJson

        url = self.apiUrl + 'orders/' + str(order['externalId']) + '/edit'
        result = self.requestApi(url, 'POST')

        if type(result) is dict and result.has_key('uploadedOrders'):
            return result['uploadedOrders']
        else:
            return result

    def orderFixExternalIds(self, orders):
        dataJson = json.dumps(orders)
        self.parameters['orders'] = dataJson

        url = self.apiUrl + 'orders/fix-external-ids'
        return self.requestApi(url, 'POST')

    def orderHistory(self, startDate='', endDate='', limit=100, offset=0):
        url = self.apiUrl + 'orders/history'
        self.parameters['startDate'] = startDate
        self.parameters['endDate'] = endDate
        self.parameters['limit'] = limit
        self.parameters['offset'] = offset

        return self.requestApi(url)

    def customerGet(self, id, by='externalId'):
        url = self.apiUrl + 'customers/' + str(id)

        if by != 'externalId':
            self.parameters['by'] = by

        return self.requestApi(url)

    def customers(self, phone=None, email=None, fio=None, limit=200, offset=0):
        url = self.apiUrl + 'customers'

        if email:
            self.parameters['email'] = email
        if phone:
            self.parameters['phone'] = phone
        if fio:
            self.parameters['fio'] = fio

        self.parameters['limit'] = limit
        self.parameters['offset'] = offset

        return self.requestApi(url)

    def customerCreate(self, customer):
        dataJson = json.dumps(customer)
        self.parameters['customer'] = dataJson

        url = self.apiUrl + 'customers/create'
        return self.requestApi(url, 'POST')

    def customerEdit(self, customer):
        dataJson = json.dumps(customer)
        self.parameters['customer'] = dataJson

        url = self.apiUrl + 'customers/' + customer['externalId'] + '/edit'
        return self.requestApi(url, 'POST')

    def customerUpload(self, customers):
        dataJson = json.dumps(customers)
        self.parameters['customers'] = dataJson

        url = self.apiUrl + 'customers/upload'
        result = self.requestApi(url, 'POST')

        if type(result) is dict and result.has_key('uploaded'):
            return result['uploaded']
        else:
            return result

    def deliveryTypesList(self):
        url = self.apiUrl + 'reference/delivery-types'
        return self.requestApi(url)

    def deliveryTypeEdit(self, deliveryType):
        dataJson = json.dumps(deliveryType)
        self.parameters['deliveryType'] = dataJson

        url = self.apiUrl + 'reference/delivery-types/' + deliveryType['code'] + '/edit'
        return self.requestApi(url, 'POST')

    def deliveryServicesList(self):
        url = self.apiUrl + 'reference/delivery-services'
        return self.requestApi(url)

    def deliveryServiceEdit(self, deliveryService):
        dataJson = json.dumps(deliveryService)
        self.parameters['deliveryService'] = dataJson

        url = self.apiUrl + 'reference/delivery-services/' + deliveryService['code'] + '/edit'
        return self.requestApi(url, 'POST')

    def paymentTypesList(self):
        url = self.apiUrl + 'reference/payment-types'
        return self.requestApi(url)

    def paymentTypesEdit(self, paymentType):
        dataJson = json.dumps(paymentType)
        self.parameters['paymentType'] = dataJson

        url = self.apiUrl + 'reference/payment-types/' + paymentType['code'] + '/edit'
        return self.requestApi(url, 'POST')

    def orderTypesList(self):
        url = self.apiUrl + 'reference/order-types'
        return self.requestApi(url)

    def orderTypesEdit(self, orderType):
        dataJson = json.dumps(orderType)
        self.parameters['orderType'] = dataJson

        url = self.apiUrl + 'reference/order-types/' + orderType['code'] + '/edit'
        return self.requestApi(url, 'POST')

    def orderMethodsList(self):
        url = self.apiUrl + 'reference/order-methods'
        return self.requestApi(url)

    def orderMethodsEdit(self, orderMethod):
        dataJson = json.dumps(orderMethod)
        self.parameters['orderMethod'] = dataJson

        url = self.apiUrl + 'reference/order-methods/' + orderMethod['code'] + '/edit'
        return self.requestApi(url, 'POST')

    def orderStatusesList(self):
        url = self.apiUrl + 'reference/statuses'
        return self.requestApi(url)

    def orderStatusEdit(self, status):
        dataJson = json.dumps(orderStatuse)
        self.parameters['status'] = dataJson

        url = self.apiUrl + 'reference/statuses/' + status['code'] + '/edit'
        return self.requestApi(url, 'POST')
