#!/usr/bin/python3

import subprocess
import sys

errors = []

if len(sys.argv) < 2:
    print("Veuillez fournir un nom de user.")
    # On quitte le script si il manque un argument
    sys.exit(1)

def delete_group(groupname):
    try:
        subprocess.run(f"groupdel {groupname}", shell=True)
        return True
    except Exception as e:
        errors.append(f"Group {groupname} cannot be deleted")
        return False

def delete_user(username):
    try:
        subprocess.run(f"userdel {username}", shell=True)
        return True
    except Exception as e:
        errors.append(f"User {username} cannot be deleted")
        return False



# execute script
delete_user(sys.argv[1])
delete_group(sys.argv[1])