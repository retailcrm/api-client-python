# coding=utf-8

"""
Response class
"""


class Response(object):
    """
    API response class
    """

    def __init__(self, code, body):
        self.__status_code = code
        self.__response_body = body

    def get_status_code(self):
        """
        :return: integer
        """
        return self.__status_code

    def get_response(self):
        """
        :return: string
        """
        return self.__response_body

    def is_successful(self):
        """
        :return: boolean
        """
        return int(self.__status_code) < 400

    def get_error_msg(self):
        """
        :return: string
        """
        return self.__response_body['errorMsg']

    def get_errors(self):
        """
        :return: collection
        """

        errors = self.__response_body.get('errors', {})

        return errors
