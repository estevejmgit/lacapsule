#!/bin/bash

# Vérifie si un paramètre a été passé
if [ -z "$1" ]; then
  echo "Usage: $0 \"NAME <EMAIL>\""
  exit 1
fi

# Extraction de l'email
EMAIL=$(echo "$1" | grep -oP '(?<=<).*(?=>)')

# Vérifie si l'email contient "@"
if [[ "$EMAIL" == *"@"* ]]; then
  echo "Valid address"
else
  echo "Invalid address"
  exit 1
fi
