"""
googleapilib 单元测试
"""

from unittest import TestCase

from shicong.api.google import geocode


class GoogleTestCase(TestCase):
    def test_geocode(self):
        print(geocode(*(str(22.616390222222222), str(114.06048583333333))))