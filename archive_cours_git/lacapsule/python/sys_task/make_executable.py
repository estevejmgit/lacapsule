#!/usr/bin/python3
import os
import sys
import pwd
import grp

# check si 3 args après l'appel du fichier
if len(sys.argv) < 4:
    print("Usage : make_executable.py <file> <user> <group>")
    # On quitte le script si il manque un argument
    sys.exit(1)


file = sys.argv[1]
user_id = pwd.getpwnam(sys.argv[2]).pw_uid
group_id = grp.getgrnam(sys.argv[3]).gr_gid

# print("file : {} / userid : {} / group_id : {}".format(file, user_id, group_id))

os.chown(file, user_id, group_id)
os.chmod(file, 0o755)

