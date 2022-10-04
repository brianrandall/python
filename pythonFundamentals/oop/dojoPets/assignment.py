from ninja import Ninja
from petClass import Pet

brian = Ninja('brian', 'randall', 'dog', 'burritos', 'pizza')
larry = Pet('larry', 'dog', 'sleeping')

print(larry.energy)
larry.play()
brian.walk()

# 