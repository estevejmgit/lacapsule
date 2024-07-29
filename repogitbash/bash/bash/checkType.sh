#!/usr/bin/env bash

echo "Enter a path to a file or directory: "

read path

if [ -f "$path" ]; then
	echo  "$path est un fichier"
elif [ -d "$path" ]; then
        echo  "$path est un répertoir"
else
	echo "$path n'est pas reconnu"
fi

