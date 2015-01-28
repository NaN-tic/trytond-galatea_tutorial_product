# This file is part of galatea_tutorial_product module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .tutorial import *

def register():
    Pool.register(
        GalateaTutorialProductTemplate,
        GalateaTutorial,
        module='galatea_tutorial_product', type_='model')
