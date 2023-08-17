from odoo import http

class Motorcycle_Compare(http.Controller):
    @http.route('/motorcycle/compare/', auth='public', website=True)
    def motorcycle_compare(self, **kw):
        motorcycles = http.request.env['product.template'].search([('detailed_type', '=', 'motorcycle')])
        return http.request.render('motorcycle_compare.motorcycle_compare_website', {
            'motorcycles': motorcycles,
        })