{
    'name': 'Purchase Requisition Received',
    'version': '14.0.0',
    'author': 'Taling Tarung',
    'license': 'OPL-1',
    'category': 'My-Custom',
    'website': 'https://t.me/BeyondCode',
    'summary': 'Custom-built Odoo',
    'description': '''
    ''',
    'depends': [
        'purchase',
        'purchase_requisition'
    ],
    'data': [
        'views/purchase_requisition_received.xml',
    ],
    'qweb': [
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}