
# in - v(ect li v spiske)
# not in - ne v (ne vxodit v spisok)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
