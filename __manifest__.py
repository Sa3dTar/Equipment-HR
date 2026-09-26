{
    'name': 'Human Resource For Medical',
    'version': '18.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Manages medical equipment, meters, preventive maintenance rules, work orders, and technician certifications',
    'description': """
        Custom Odoo 18 module for comprehensive medical equipment management:
        - Equipment Inventory and Meter Logs tracking.
        - Preventive Maintenance Rules linked to product models.
        - Work Orders management with downtime calculation and technician assignment.
        - Technician Certifications and HR employee integration.
    """,
    'author': 'Saad Tarek',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'hr',
        'stock',
        'my_inventory',
        'purchase',
        'my_purchase',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/equipment_work_order.xml',
        'views/equipment_preventive_rule.xml',
        'views/certification.xml',
        'views/hr_employee.xml',
        'views/menuitem.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}