from frappe import _

def get_data():
	config = [
		{
			"label": _("Reports"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Asset Analysis",
					"doctype": "Asset Category",
				},
			]
		},
	]
	return config
