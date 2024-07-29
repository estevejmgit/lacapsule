#!/bin/bash

# Vérifie si un argument a été passé
if [ -z "$1" ]; then
  echo "Usage: $0 <maximum_size>"
  exit 1
fi

MAX_SIZE=$1
EXCEEDING_FILES=$(find . -type f -size +"$MAX_SIZE")

# Vérifie s'il y a des fichiers qui dépassent la taille maximale
if [ -n "$EXCEEDING_FILES" ]; then
  echo "Des fichiers dépassent la taille maximale de $MAX_SIZE :"
  exit 1
else
  echo "Aucun fichier ne dépasse la taille maximale de $MAX_SIZE."
fi
