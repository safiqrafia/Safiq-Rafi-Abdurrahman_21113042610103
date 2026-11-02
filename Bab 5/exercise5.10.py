

current_users = ["admin", "mike", "Sarah", "JHON", "linda"]

new_users = ["Jhon", "LINDA", "Jane", "Ken", "Paul"]

current_users_lower = [username.lower() for username in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken!.")
        continue
    print(f"{new_user} is available!.")