# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2012-2014 E-MIPS (http://www.e-mips.com.ar)
#    Copyright (c) 2014 Aconcagua Team (http://www.proyectoaconcagua.com.ar)
#    All Rights Reserved. See AUTHORS for details.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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

from osv import osv, fields


class account_fiscal_position (osv.osv):
    _name = "account.fiscal.position"
    _inherit = "account.fiscal.position"
    _description = ""
    _columns = {
        'local' : fields.boolean('Local Fiscal Rules', help="Check this if it corresponds to apply local fiscal rules, like invoice number validation, etc"),
        'denomination_id' : fields.many2one('invoice.denomination','Denomination', required=True),
        'denom_supplier_id' : fields.many2one('invoice.denomination','Denomination', required=True),
    }

    _defaults = {
        'local': True,
    }
account_fiscal_position()