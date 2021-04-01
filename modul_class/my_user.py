### 9.11

from user import User, Admin

my_user = Admin('oleksandr', 'naumov', 'ukraine', 'california')

my_user.greet_user()
my_user.privileges.show_privileges()