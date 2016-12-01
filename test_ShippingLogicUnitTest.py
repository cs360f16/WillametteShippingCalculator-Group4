#!/usr/bin/python3

################################
# File Name:	test_ShippingLogicUnitTest.py
# Author:		Mason Rausten
# Date:			11/17/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		Unittest for SaleItem
################################


import unittest
from ShippingLogic import ShippingLogic


class TestShippingLogic(unittest.TestCase):
    def setUp(self):
        """ the text fixture, necessary setup for the tests to run
        """
        self.theShipping = ShippingLogic()

    def tearDown(self):
        """ nothing to tear down here
        If your test created a database or built a network connection
        you might delete the database or close the network connection
        here. You might also close files you opened, close your
        TK windows if this is GUI program, or kill threads if this is
        a multithreaded application
        """
        pass  # nothing to do

    def test_getName(self):
        self.assertEqual(self.theShipping.getName(), 'Standard')