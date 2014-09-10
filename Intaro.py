import requests

class IntaroApy:
  """Intaro Api wrapper"""

  apiVersion = '3'

  def __init__(self, crmUrl, apiKey):
    self.apiUrl = crmUrl + '/api/v' + IntaroApy.apiVersion + '/'
    self.apiKey = apiKey
    self.parameters = { 'apiKey': apiKey }

  def requestApi(self, url, method='GET', format='json'):
    
    #TODO: catch http exceptions
    if method == 'GET':
      result = requests.get(url, params=self.parameters)
    elif method == 'POST':
      result = requests.post(url, data=self.parameters)

    statusCode = result.status_code
    r = result.json()

    # reset params dict
    self.parameters = { 'apiKey': self.apiKey }

    if statusCode > 400 or r.has_key('success') and r['success'] == False :
      #TODO: ApiException
      pass

    if r.has_key('generatedAt') :
      self.generatedAt = r['generatedAt']
      del r['generatedAt']

    del r['success']

    return r

  def orderGet(self, id, by='externalId') :
    url = self.apiUrl + 'orders/' + str(id)

    if by != 'externalId' :
      self.parameters['by'] = by

    return self.requestApi(url)

