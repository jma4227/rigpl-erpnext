from frappe import _

def get_data():
	return [
		{
			"label": _("Loans"),
			"icon": "icon-gear",
			"items": [
				{
					"type": "doctype",
					"name": "Employee Advance",
					"description": _("Employee Advance"),
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Employee Loan Analysis",
					"doctype": "Employee Advance",
				},
			]
		},
		{
			"label": _("Payroll"),
			"icon": "icon-gear",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Employee Balances RIGPL",
					"doctype": "Salary Slip",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Salary Structure",
					"doctype": "Salary Structure",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Salary Register",
					"doctype": "Salary Slip",
				}
			]
		},
		{
			"label": _("Attendance"),
			"icon": "icon-gear",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Attendance Performance Analysis",
					"doctype": "Attendance",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Employee Attendance",
					"doctype": "Attendance",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Leave Application Report",
					"doctype": "Leave Application",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "List of Holidays",
					"doctype": "Holiday List",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Monthly Attendance Time Based",
					"doctype": "Attendance",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Roster",
					"doctype": "Roster",
				},
			]
		},
	]
