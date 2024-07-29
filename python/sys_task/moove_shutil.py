# Importe le module shutil pour la gestion de fichiers et de répertoires.
import shutil  
# Importe le module os pour les opérations système.
import os

source = '/chemin/source'  # Définit le chemin du répertoire source.
destination = '/chemin/destination'  # Définit le chemin du répertoire de destination.
# Parcourt tous les fichiers et répertoires dans le répertoire source.
for filename in os.listdir(source):
    # Vérifie si le fichier se termine par '.png'.
    if filename.endswith('.png'):
        # Crée un nouveau nom de fichier en remplaçant '.png' par '_backup.png'.
        new_name = filename.replace('.png', '_backup.png')
        # Déplace le fichier de source vers destination en renommant le fichier.
        shutil.move(
            os.path.join(source, filename),       # Chemin complet du fichier source.
            os.path.join(destination, new_name)   # Chemin complet du nouveau fichier dans destination.
        )
