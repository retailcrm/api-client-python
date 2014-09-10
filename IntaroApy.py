import requests

class IntaroApy:
  'Intaro Api wrapper'

  apiVersion = '3'

  def __init__(self, crmUrl, apiKey):
    self.crmUrl = crmUrl + '/api/v' + IntaroApy.apiVersion + '/'
    self.apiKey = apiKey
    self.parameters = { 'apiKey': apiKey }

  def requestApi(self, url, method='GET', format='json'):
    
    #TODO: catch http exceptions
    if method == 'GET':
      result = requests.get(url, params=self.parameters)
    else if method == 'POST':
      result = requests.post(url, data=self.parameters)

    statusCode = result.status_code
    r = result.json()

    # reset params dict
    self.parameters = { 'apiKey': apiKey }

    if statusCode > 400 || r.has_key('success') && r['success'] == False :
      #TODO: ApiException

    if r.has_key('generatedAt') :
      self.generatedAt = r['generatedAt']
      del r['generatedAt']

    del r['success']

    return True


