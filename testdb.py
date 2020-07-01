from project import db
from project.models import User

user = User.query.get(1)

print(user)
