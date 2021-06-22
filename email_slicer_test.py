#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email_slicer import email_slicer
import unittest


class TestEmailSlicer(unittest.TestCase):

    def test_valid_email(self):
        self.assertEqual(email_slicer('boatengpato.pb@gmail.com'), ('boatengpato.pb', 'gmail.com'))
        self.assertEqual(email_slicer('boatengpato.pb@yahoo.com'), ('boatengpato.pb', 'yahoo.com'))
        self.assertEqual(email_slicer('boatengpato.pb@outlook.com'), ('boatengpato.pb', 'outlook.com'))

    def test_invalid_email(self):
        self.assertEqual(email_slicer('boatengpato'), 'boatengpato is invalid')
    
    def __str__(self):
        return 'TestEmailSlicer'

unittest.main()
