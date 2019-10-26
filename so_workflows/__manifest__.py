{

    'name':'Sale Order WorkFlows',
    'description' : 'SO WorkFlows',
    'author' : 'Hafeez Brothers',
    
    'depends' : [
                   'base', 'product','sale',
                ],
    'data' :[   
                
                'views/sale_cust.xml',
                'security/hr_user_rights.xml'
            ],
    'installable' : True,
    'price':40.00,
    'currency':'EUR', 


}
