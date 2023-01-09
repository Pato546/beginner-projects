#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from expand import expanded_form
import unittest


class TestExpandedForm(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertEqual(expanded_form(10001), '10000 + 1')
        self.assertEqual(expanded_form('5904590'), '5000000 + 900000 + 4000 + 500 + 90')

    def test_invalid_numbers(self):
        self.assertEqual(expanded_form('10000g'), '10000g is not a number')
        self.assertEqual(expanded_form('abcd'), 'abcd is not a number')

    def test_digits_in_words(self):
        self.assertEqual(expanded_form('thirty four'), '30 + 4')
        self.assertEqual(expanded_form('two million four hundred and eight'), '2000000 + 400 + 8')

    def __str__(self):
        return 'TestExpandedForm'


unittest.main()


