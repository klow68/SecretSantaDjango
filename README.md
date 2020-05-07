# SecretSantaDjango
A Secret Santa web interface with the following functionnalities :
- only 1 user has to register
- emails are send to all participants to confirm their participation
- In each Santa group you can indicate the price, a date, a place, a theme
- Each participant can tell things they like to do to make the Santa/Satan job easier
- user registered use by default the things they like if it's saved in the profile

raw TODO list

- add bootstrap in the project

test case :
création d'un utilisateur
l'utilisateur crée un groupe secret santa de l'année courante avec une date et un lieu (si déjà connue) , montant maximum (possibilité de changé la date et le lieu avec renvoie d'email pour les participants)
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


For local test email, run the command :
`$ python -m smtpd -n -c DebuggingServer localhost:1025`

