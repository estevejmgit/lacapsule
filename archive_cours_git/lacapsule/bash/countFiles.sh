#!/usr/bin/env bash

# REP=$1

ls -l $1 | awk {print $3} | uniq -c | awk '{print $2, $1}'

# # check if file exists -e
# if [ ! -e "$REP" ]; then
#   echo "Le dossier $REP n'existe pas."
#   exit 1
# fi

# # pour chaque file/rep (sur le rep courant - no recursif), si fichier, print un "x" | count le nb de charactères 
# # > un x par fichier, donc 2 x pour deux fichiers etc
# FILECOUNT="$(find $REP -maxdepth 1 -type f  -printf x | wc -c)"

# echo "file count : $FILECOUNT"

# # affiche la liste des fichier et sous-rep ainsi que leur owner
# for entry in "$REP"/*
#   do
#     owner="$(stat -c '%U' $entry)"
#     echo "$entry:$owner"
# done

