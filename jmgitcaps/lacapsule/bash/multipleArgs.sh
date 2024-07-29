#!/usr/bin/env bash

# Vérifie s'il y a au moins un argument
if [ "$#" -eq 0 ]; then
    echo "Usage: $0 /path/to/file_or_folder [additional paths...]"
    exit 1
fi

# Boucle sur tous les arguments fournis
for path in "$@"; do
    if [ -f "$path" ]; then
        echo "$path est un fichier"
    elif [ -d "$path" ]; then
        echo "$path est un répertoire"
    else
        echo "$path n'est pas reconnu"
    fi
done
