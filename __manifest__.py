{
    'name': 'Sale Manager',
    'version': '13.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Odoo Development Tutorials For Beginners',
    'sequence': '10',
    'license': 'AGPL-3',
    'author': 'NQ Vinh',
    'maintainer': 'Odoo Mates',
    'website': 'odoomates.com',
    'live_test_url': 'https://www.youtube.com/watch?v=BDepk0LhVuI&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=1',
    'depends': ['sale',
                'mail',
                'board',
                'website'],
    'demo': [],
    'data': [
        'views/sale_view.xml'
    ],
    # 'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
