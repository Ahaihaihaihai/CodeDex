class restaurant:
    name = ''
    category = ''
    rating = 0.0
    delivery = False

bobs_burgers = restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Dinner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

王仔 = restaurant()
王仔.name = '王仔滷味'
王仔.category = '滷味'
王仔.rating = 5.0
王仔.delivery = False

sevel = restaurant()
sevel.name = '7-11'
sevel.category = 'Conveniences Store'
sevel.rating = 4.3
sevel.delivery = True

print(vars(bobs_burgers))
print(vars(王仔))
print(vars(sevel))