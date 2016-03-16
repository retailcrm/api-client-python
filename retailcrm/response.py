# coding=utf-8


class Response(object):
    """
    API response class
    """

    def __init__(self, code, body):
        self.response_body = body
        self.status_code = code

    def get_status_code(self):
        """
        :return: integer
        """
        return self.status_code

    def get_response(self):
        """
        :return: dict
        """
        return self.response_body

    def is_successfull(self):
        """
        :return: boolean
        """
        return int(self.status_code) < 400
