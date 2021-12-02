with open('input.txt','r') as input:
  planned_course = input.read().splitlines()

def forward(position, amount):
  position['horizontal'] += amount
  position['depth'] += amount * position['aim']
  return position

def down(position, amount):
  position['aim'] += amount
  return position

def up(position, amount):
  position['aim'] -= amount
  return position


position = {
  'horizontal': 0,
  'depth': 0,
  'aim': 0
}
for movement in planned_course:
  direction = movement.split(' ')[0]
  amount = int(movement.split(' ')[1])
  move_options = {
    'forward': forward,
    'down': down,
    'up': up
  }

  position = move_options[direction](position, amount)

print(position['horizontal'] * position['depth'])