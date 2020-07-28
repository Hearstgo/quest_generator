# quest_generator
Un générateur de quêtes
Python 3.8

le but est de générer des quêtes afin d'apporter une grande variété dans les RPG.
Le principe de ce générateur est très simple, il génère des quête parmis les catégories suivantes :
-chasse 
(collecte ou escorte pas encore développées.)

Parmis les catégorie de quêtes, le générateur utilise des "tag", chaque tag représentant une sous-catégorie de quête, une sorte de ligne narrative.
Par exemple : pour le tag "carnivore", les quêtes seront du genre :

Nom : Aider Le fermier
Type : kill
difficulte : difficile
Niveau : 23
Description : Le fermier demande de l'aide d'un valeureux guerrrier pour chasser les Loups qui déciment ses vaches.
Vous pourrez trouver les Loups dans le val. Tuez-en 25
Récompense : ['11 or 97 argent 73 cuivre ', "chapeau d'Hestia"]
statut : 0/25

Il suffit alors de rajouter dans le dictionaire quetes_kill (dans cet exemple car on parle d'une quête de chasse) d'autres possibilité de scénarios.
la description de cet exemple à été généré à partir du paterns suivant :
description = giver+" "+ask_help+" pour chasser les "+objectif+" qui déciment ses "+animaux_passif+". Vous pourrez trouver les "+objectif+" "+lieux+". Tuez-en "+nb

Il suffit donc de rajouter des paterns de nom de quête ou de descriptions aux tags, ou encore d'ajouter des tags afin de multiplier les possibilités.
