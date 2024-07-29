#!/usr/bin/env bash

path=$1

if [ -f "$path" ]; then
	echo  "$path est un fichier"
elif [ -d "$path" ]; then
        echo  "$path est un répertoir"
else
	echo "$path n'est pas reconnu"
fi

