from frappe import _

def get_data():
	return [
		{
			"label": _("Automation"),
			"icon": "icon-paper-clip",
			"items": [
				{
					"type": "doctype",
					"name": "User Share Settings",
					"doctype": "User Share Settings",
				},
				{
					"type": "doctype",
					"name": "User Permission Settings",
					"doctype": "User Permission Settings",
				},
				{
					"type": "doctype",
					"name": "Shipway Settings",
					"doctype": "Shipway Settings",
				},
			]
		}
	]
