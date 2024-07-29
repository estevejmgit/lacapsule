#!/usr/bin/env bash

# Récupérer le chemin du fichier passé en paramètre
FILE=$1

# Vérifier si le fichier existe
if [ ! -e "$FILE" ]; then
  echo "Le fichier $FILE n'existe pas."
else
    # Vérifier les droits d'exécution de l'utilisateur courant sur le fichier
    if [ -x "$FILE" ]; then
        echo "L'utilisateur courant a les droits d'exécution sur $FILE."
    else
        echo "L'utilisateur courant n'a pas les droits d'exécution sur $FILE."
    fi
fi