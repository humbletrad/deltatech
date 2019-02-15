# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2016 Deltatech All Rights Reserved
#                    Dorin Hongu <dhongu(@)gmail(.)com       
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
{
    "name": "Deltatech Fast Purchase",
    'version': '10.0.1.0.0',
    "author": "Terrabit, Dorin Hongu",
    "website": "www.terrabit.ro",
    'summary': 'Achizitie rapida',

    "description": """
 
Features:
---------
 - Buton in comanda de aprovizionare pentru a face pasii de confirmare, receptie si facturare
 - Buton in repetie pentru a introduce direct factura


    """,
    "category": "Generic Modules/Stock",
    "depends": ["base", "purchase","stock"],

    "images": ['images/main_screenshot.png'], "license":"LGPL-3","data": ['purchase_view.xml','stock_view.xml'],
    "active": False,
    "installable": True,
}
