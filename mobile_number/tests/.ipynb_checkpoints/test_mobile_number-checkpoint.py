# -*- coding: utf-8 -*-

# import unittest
from odoo.tests import common
# import logging

# _logger = logging.getLogg


class TestModule(common.TransactionCase):
    
#     at_install = True
#     post_install = True
    
    def setUp(self):
        super(TestModule, self).setUp()
        #Add Test Setup Code Here
        
        
    def test_data(self):
        #Add Test Code Here
        
        # Create a New Location with the Test
        test_location_1 = self.env['stock.location'].create({
            'name': 'Location_1',
            'usage':'internal'
        })
        
        # Create a Another Location
        test_location_2 = self.env['stock.location'].create({
            'name': 'Location_2',
            'usage':'storage'
        })
        
        # Check if the usage of the two created locations are the same
        
        # Assert functions are used to check whether the operation’s output is True or False
        self.assertEqual(test_location_1.usage, test_location_2.usage, msg='TEST FAILED')
        
    
#     if __name__ == '__main__':
#         unittest.main()