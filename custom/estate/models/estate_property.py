from dateutil.relativedelta import relativedelta

from odoo import models, fields

class EstateProperties(models.Model):
    _name = "estate.property"
    _description = "Pluri Select Estate Properties"

    name = fields.Char(string="Title", required=True)
    active = fields.Boolean(default=True)
    description = fields.Text()
    postcode = fields.Char(string="Postcode")
    availability_date = fields.Date(string="Available From", copy=False, default=lambda self:fields.Date.today()+relativedelta(months=3))
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)
    bedroom_count = fields.Integer(string="Bedrooms", default=2)
    living_area_sqm_rounded = fields.Integer(string="Living Area (sqm)")
    facade_count = fields.Integer("Facades")
    has_garage = fields.Boolean("Garage")
    has_garden = fields.Boolean("Garden")
    garden_area_sqm_rounded = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")],
        help="Garden Orientation",
    )
    state = fields.Selection(
        string="State",
        selection=[("new", "New"), ("offer Recieved", "Offer Received"), ("offer Accepted", "Offer Accepted"), ("sold", "Sold"), ("cancelled", "Cancelled")],
        help="in which state the selling is, one of these [New, Offer Received, Offer Accepted, Sold]",
        default="new",
        required=True,
        copy=False,
    )