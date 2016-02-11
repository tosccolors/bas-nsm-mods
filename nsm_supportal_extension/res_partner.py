# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright 2014 BAS Solutions
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import osv
from openerp.osv import fields
from openerp.tools.translate import _


class res_partner(osv.osv):
    _inherit = 'res.partner'

#   NOG NIET KLAAR
#    def _get_genexp_portal(self, cr, uid, supplier_id, context={}):
#        partner_obj = self.pool.get('res.partner')
#        rec = self.pool.get('account.analytic.default').account_get(
#            cr, uid, product, partner_id, uid,
#            fields.date.context_today(self, cr, uid, context=context),
#            context=context)

    _columns = {
        'genexp_portal': fields.boolean('Portal Algemene kosten'),
        'analytic_account_ids': fields.many2many('account.analytic.account','partner_analytic_rel','partner_id','analytic_account_id','Titels/Afdelingen'),
    }

#    _defaults = {
#        'genexp_portal': _get_genexp_portal,
#    }

res_partner()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
