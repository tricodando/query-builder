from database.generator.build import Build

class User(Build):
  def __init__(self):
    super().__init__('user')