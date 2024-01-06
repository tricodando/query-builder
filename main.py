from database.generator.data import Database
from database.seed import seed

# seed()

db = Database()

users = db.user.findMany()

print(users)