from frappe import _

def get_data():
	config = [
		{
			"label": _("Accounts Receivable"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Carrier Tracking",
					"description": _("Track Shipments sent via Courier"),
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "DN To Be Billed",
					"doctype": "Sales Invoice",
				},
			]
		},
		{
			"label": _("Accounts Payable"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "PR to be Billed",
					"doctype": "Purchase Invoice",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Sales Partner Commission Details",
					"doctype": "Sales Invoice",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "TOD Sales Invoice",
					"doctype": "Sales Invoice",
				}
			]
		},
		{
			"label": _("Banking and Payments"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "BRC MEIS Tracking",
					"description": _("Track BRC and MEIS Status"),
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "BRC Tracking",
					"doctype": "BRC MEIS Tracking",
				},
			]
		},
	]
	return config
