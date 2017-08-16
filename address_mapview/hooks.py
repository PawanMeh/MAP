# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "address_mapview"
app_title = "Mapview"
app_publisher = "Sangram Patil"
app_description = "Address Mapview"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "patil.sangram01@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/css/mapview.desk.min.css"
app_include_js = "/assets/js/mapview.desk.min.js"

# include js, css files in header of web template
# web_include_css = "/assets/address_mapview/css/address_mapview.css"
# web_include_js = "/assets/address_mapview/js/address_mapview.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Address" : "public/js/address.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "address_mapview.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "address_mapview.install.before_install"
# after_install = "address_mapview.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "address_mapview.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Address": {
		"validate": "address_mapview.custom.address.get_lat_lon"
	}
}

fixtures = ['Custom Field', 'Property Setter']

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"address_mapview.tasks.all"
# 	],
# 	"daily": [
# 		"address_mapview.tasks.daily"
# 	],
# 	"hourly": [
# 		"address_mapview.tasks.hourly"
# 	],
# 	"weekly": [
# 		"address_mapview.tasks.weekly"
# 	]
# 	"monthly": [
# 		"address_mapview.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "address_mapview.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "address_mapview.event.get_events"
# }

