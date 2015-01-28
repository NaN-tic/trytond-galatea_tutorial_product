#!/usr/bin/env python
# This file is part of galatea_tutorial_product module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.tests.test_tryton import test_view, test_depends
import trytond.tests.test_tryton
import unittest


class GalateaTutorialProductTestCase(unittest.TestCase):
    'Test Galatea Tutorial Product module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('galatea_tutorial_product')

    def test0005views(self):
        'Test views'
        test_view('galatea_tutorial_product')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        GalateaTutorialProductTestCase))
    return suite
