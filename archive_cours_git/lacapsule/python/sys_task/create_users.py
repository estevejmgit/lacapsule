#!/usr/bin/python3

import subprocess
import crypt
import pwd
import grp

# list of errors 
errors = []

# encPass = crypt.crypt("myPass","22")

# subprocess.run("groupadd group100 && useradd -p " + encPass + " -g group100 myuser3 && usermod -aG sudo myuser3", shell=True)

def create_group(group):
    # if group exists should return True
    try:
        subprocess.run(f"groupadd {group}", shell=True)
        return True
    except Exception as e:
        errors.append(f"Grooup {group} cannot be created")
        return False


def create_user(user):
    myUser = user[0]
    myGroup = user[1]
    myPass = user[2]
    myRoot = user[3]
    
    create_group(myGroup)

    try:
        subprocess.run(f"useradd -g {myGroup} {myUser}", shell=True)
    except Exception as e:
        errors.append(f"Cannot create user {myUser} !")
        return False
    
    # Set password using chpasswd
    try:
        # pass couple user/password to the chpasswd command with |
        subprocess.run(f"echo {myUser}:{myPass} | chpasswd", shell=True)
    except Exception as e:
        errors.append(f"Cannot set password for user {myUser} !")
        return False
    
    if myRoot == "true":
        set_sudo(myUser)


def set_sudo(username):
    try:
        subprocess.run(f"usermod -aG sudo {username}", shell=True)
        return True
    except:
        errors.append(f"Cannot make user {username} sudo !")
        return False
   

# execute script
with open('./assets/users.csv', 'r') as csv:
    cpt = 0
    users = []
    for line in csv:
        # 1ere ligne du csv avec nom colonne à ignorer
        if cpt > 0:
            user = line.rstrip().split(", ")
            create_user(user)
        cpt += 1
    
    print(errors)

