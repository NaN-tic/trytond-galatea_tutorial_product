# This file is part galatea_tutorial_product module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

__all__ = ['GalateaTutorialProductTemplate', 'GalateaTutorial']
__metaclass__ = PoolMeta


class GalateaTutorialProductTemplate(ModelSQL, ModelView):
    'Galatea Tutorial - Product Template'
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
    esale_products_by_shop = fields.Function(fields.Many2Many(
        'product.template', None, None, 'Products by Shop'),
        'get_esale_products_by_shop')

    def get_esale_products_by_shop(self, name):
        '''Get all products by shop
        (context or user shop preferences)'''
        templates = [] # ids
        if not self.products:
            return templates

        pool = Pool()
        transaction = Transaction()

        shop = None
        if Transaction().context.get('shop'):
            SaleShop = pool.get('sale.shop')
            shop = SaleShop(transaction.context.get('shop'))
        if not shop:
            return templates

        for template in self.products:
            if shop in template.esale_saleshops:
                templates.append(template.id)
        return templates
