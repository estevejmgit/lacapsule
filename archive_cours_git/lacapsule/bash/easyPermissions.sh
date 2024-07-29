#!/usr/bin/env bash

echo "Entrez les fichiers à chmoder séparé par un espace: "
read paths

echo "Quel droit pour les fichiers : "
read right

# Boucle sur tous les arguments fournis
for path in $paths; do
    if [ -f "$path" ]; then
        echo "$path est un fichier ! "
        chmod $right $path 
        echo "Nouveau droits : $right ! "
    elif [ -d "$path" ]; then
        echo "$path est un répertoire"
    else
        echo "$path n'est pas reconnu"
    fi
done