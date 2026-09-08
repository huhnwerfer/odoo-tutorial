{
    "name": "Estate",
    "author": "Nikita",
    'license': "LGPL-3",
    "depends": [
        "base",
    ],
    "application": True,
    "data": [
        # securiry
        "security/ir.model.access.csv",

        # views
        "views/estate_menus.xml",
        "views/estate_property/action_views.xml",
        "views/estate_property/list_views.xml",
        "views/estate_property/search_views.xml", 
        "views/estate_property/form_views.xml",
    ]
}

