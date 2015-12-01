# This file is part of the galatea_tutorial_product module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class GalateaTutorialProductTestCase(ModuleTestCase):
    'Test Galatea Tutorial Product module'
    module = 'galatea_tutorial_product'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        GalateaTutorialProductTestCase))
    return suite