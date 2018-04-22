# coding=utf-8

"""
API Client base class
"""

import requests

from multidimensional_urlencode import urlencode as query_builder
from retailcrm.response import Response


class Base(object):
    """retailCRM API client"""

    def __init__(self, crm_url, api_key, version):
        self.api_url = crm_url + '/api'
        self.api_key = api_key
        self.api_version = version
        self.parameters = {}

    def get(self, url, version=True):
        """
        Get request
        :param url: string
        :param version: boolean
        :return: Response
        """
        base_url = self.api_url + '/' + self.api_version if version else self.api_url
        requests_url = base_url + url if not self.parameters else base_url + url + "?" + query_builder(self.parameters)
        response = requests.get(requests_url, headers={
            'X-API-KEY': self.api_key})

        return Response(response.status_code, response.json())

    def post(self, url, version=True):
        """
        Post request
        :return: Response
        """
        base_url = self.api_url + '/' + self.api_version if version else self.api_url
        requests_url = base_url + url
        response = requests.post(requests_url, data=self.parameters, headers={
            'X-API-KEY': self.api_key})

        return Response(response.status_code, response.json())

    def api_versions(self):
        """
        :return: Response
        """
        return self.get('/api-versions', False)

    def api_credentials(self):
        """
        :return: Response
        """
        return self.get('/credentials', False)

    def statistic_update(self):
        """
        :return Response
        """
        return self.get('/statistic/update')
