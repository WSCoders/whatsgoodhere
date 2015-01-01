__author__ = 'David Mitchell'
#This script creates an example/test db.

from app import db
from app import MenuCategory, MenuItem

db.drop_all()
db.create_all()

appetizer_category = MenuCategory(name='Appetizers')
entree_category = MenuCategory(name='Entrees')
desert_category = MenuCategory(name='Deserts')
bacon_item = MenuItem(name='Bacon', description='Delicious bacon', category=appetizer_category)
baconz_item = MenuItem(name='Baconz', description='Bacon with Bacon on top, fried in a bacon crust', category=entree_category)
baconIceCream_item = MenuItem(name='Bacon Ice Cream', description='Bacon Ice Cream topped with bacon bits', category=desert_category)

db.session.add_all([appetizer_category, entree_category, desert_category, bacon_item, baconz_item, baconIceCream_item])
db.session.commit()
