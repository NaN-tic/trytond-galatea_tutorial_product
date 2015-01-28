# This file is part galatea_tutorial_product module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import PoolMeta

__all__ = ['GalateaTutorialProductTemplate', 'GalateaTutorial']
__metaclass__ = PoolMeta


class GalateaTutorialProductTemplate(ModelSQL, ModelView):
    'Galatea - Tutorial'
    __name__ = 'galatea.tutorial-product.template'
    _table = 'galatea_tutorial_product_template_rel'
    tutorial = fields.Many2One('galatea.tutorial', 'Tutorial',
            ondelete='CASCADE', select=True, required=True)
    template = fields.Many2One('product.template', 'Product Template',
            ondelete='CASCADE', select=True, required=True)


class GalateaTutorial:
    __name__ = 'galatea.tutorial'
    products = fields.Many2Many('galatea.tutorial-product.template',
            'tutorial', 'template', 'Product Templates')
