from database.generator.data import Database

db = Database()

def seed():
  db.user.delete()
  db.user.create({
    'id': '1',
    'email': 'johndoe@gmail.com',
    'senha': '123'
  })
  db.user.create({
    'id': '2',
    'email': 'janetdoe@gmail.com',
    'senha': '456'
  })