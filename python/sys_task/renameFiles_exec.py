#!/usr/bin/python3

# J'importe le module os
# Le module os c'est le module qui permet  de communiquer avec le systeme via un script en Python
import os
import sys

# check si 3 args après l'appel du fichier
if len(sys.argv) < 4:
    print("Usage : renameFiles.py work_dir prefix suffix")
    # On quitte le script si il manque un argument
    sys.exit(1)

directory = sys.argv[1]
prefix = sys.argv[2]    
suffix = sys.argv[3]

# On parcoure la liste des elements du dossier './test'
for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)
        if os.path.isFile(old_path):
              base, ext = os.path.splitext(filename) # retourne tuple avec 2 éléments : le nom de fichier, ext l'extension              

        if not base.endswith(suffix) and not base.startswith(prefix):
            new_name = f"{prefix}{base}{suffix}{ext}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        else:
              print("Files already renamed")