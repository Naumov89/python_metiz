
from usser import User
from addmin import Admin

my_user = Admin('alex', 'naumov', 'ukraine', 'california')

my_user.discribe_user()
my_user.privileges.show_privileges()