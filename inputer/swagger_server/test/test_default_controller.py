# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_add_data(self):
        """Test case for add_data

        輸入資料
        """
        query_string = [('content', 'content_example'),
                        ('label', 'label_example')]
        response = self.client.open(
            '/v1/data',
            method='POST',
            content_type='application/x-www-form-urlencoded',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
