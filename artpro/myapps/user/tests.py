from django.test import TestCase

# Create your tests here.

from myapps.utils import log
import logging

class TestLog(TestCase):
    def testLog(self):
        #
        self.assertEquals(1,1)
        logging.warning('1=1是ok')
