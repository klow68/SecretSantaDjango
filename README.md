# SecretSantaDjango
A Secret Santa web interface with the following functionnalities :
- only 1 user has to register
- emails are send to all participants to confirm their participation
- In each Santa group you can indicate the price, a date, a place, a theme
- Each participant can tell things they like to do to make the Santa/Satan job easier
- user registered use by default the things they like if it's saved in the profile

raw TODO list

- add bootstrap in the project
- use get_text for UI language

test case :

Simple case :
DONE : création d'un utilisateur
DONE : l'utilisateur crée un groupe secret santa
DONE : ajout des email des participant
TODO : suppression du groupe
TODO : envoie des invitations par email
TODO : création des utilisateurs (si pas de compte + set prénom nom au premier login)
TODO : envoie des emails avec mdp (si création sinon juste mail avec nom du groupe)
TODO : validation de participation de tout les utilisateur
TODO : envoie un email a tout les participants avec le nom de la personne



Goal :
création d'un utilisateur
l'utilisateur crée un groupe secret santa (TODO later : de l'année courante avec une date et un lieu (si déjà connue) , montant maximum (possibilité de changé la date et le lieu avec renvoie d'email pour les participants))
ajout des email des participant

possibilité du créateur de crée des champs personnalisé avec une limite de 20 avec le choix pour l'utilisateur de refusé la diffusion

réception de l'email avec un code personnalisé, les personnes ajoutes leur centre d'interêt et valide leur participation et le nom des personnes sur lesquels elle ne doivent pas tombé
une fois que tout les participant on valider ou refusé (le créateur/groupe peut voir le statut de des validations)
Mail a tout le monde si il n'y a pas de solution suite au nom des personnes sur lesquel elle ne peuvent pas tombé 
validation du créateur on non de l'envoie de l'email si il y a un refus

envoie du mail a tout le monde : 

Avec les infos -> choisi par le créateur

Joyeux Secret Santa

possibilité d'ajouter des tags de centre d'intérêt
possibilité de modifier le groupe
possibilité de supprimer le groupe


requirements : 
account requirements : 
	pip install django-user-accounts (https://django-user-accounts.readthedocs.io)
	pip install django-appconf
	pip install pytz

use of js for dynamic formset from : 
https://github.com/elo80ka/django-dynamic-formset

For local test email, run the command :
`$ python -m smtpd -n -c DebuggingServer localhost:1025`

