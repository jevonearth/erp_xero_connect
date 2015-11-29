from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
            {
                "label": _("Setup"),
                "icon": "icon-star",
                "items": [
                    {
                        "type": "doctype",
                        "name": "Xero Settings",
                        "description": _("Connect ERPNext with Xero"),
                        "hide_count": True
                        }
                    ]
                }
            ]

