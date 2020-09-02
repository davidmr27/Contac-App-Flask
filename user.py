from flask_login import UserMixin

class User(UserMixin):
     user = []

     def __init__(self, id, username    ):
          super().__init__()
          self.id = id 
          self.username = username


