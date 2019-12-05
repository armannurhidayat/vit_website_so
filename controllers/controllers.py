# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class VitWebsiteSo(http.Controller):

	@http.route('/vit/so/', type='http', auth='public', website=True)
	def index(self, **kw):
		# Mengambil semua data yang ada di model sale.order
		sale_orders = request.env['sale.order'].search([])

		return request.render("vit_website_so.index", { # vit_website_so nama addons
			'sale_orders' : sale_orders # Pasrsing data
		})


	@http.route('/vit/so_ajax/', type='http', auth='public', website=True)
	def index_ajax(self, **kw):

		return request.render("vit_website_so.index_ajax", {
		})

	# Load Data Ajax dari sale.order
	@http.route('/vit/load_ajax/', type='http', auth='public', website=True)
	def load_ajax(self, **kw):
		sale_orders = request.env['sale.order'].search([])

		result = {}
		result['data'] = []

		for so in sale_orders:
			result['data'].append([
				so.name,
				so.confirmation_date if so.confirmation_date else '',
				so.partner_id.name,
				so.user_id.name,
				so.amount_total,
				so.invoice_status
			])

		return json.dumps(result, default=str)


	@http.route('/vit/so_chart/', type='http', auth='public', website=True)
	def index_chart(self, **kw):
		sale_orders = request.env['sale.order'].search([])

		return request.render("vit_website_so.index_chart", {
			'sale_orders' : sale_orders # Pasrsing data
		})