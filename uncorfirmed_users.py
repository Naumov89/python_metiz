
uncorfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while uncorfirmed_users:
    current_users = uncorfirmed_users.pop()
    print(f"Verifing user: {current_users.title()}.")
    confirmed_users.append(current_users)

print(f"\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())