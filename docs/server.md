# Ici on va parler de la partie serveur (UPDATE 2025)

## A partir du setup jusqu'à l'utilisation

Premièrement il vous faudra une machine sur laquelle le serveur va tourner. Cette machine peut etre un ordinateur dans la salle, un ordinateur d'un membre, une machine virtuelle (MiNET ou non). Attention cependant pour les machines virtuelles, il vous faudra un stockage important.  
Dans notre cas (2024-2025), on a trouvé un ordinateur en demandant à notre tuteur sinon vous avez aussi le projecteur mais +galère.  

## Mettre l'OS sur la machine vierge

Il vous faudra une clé bootable avec l'OS que vous voulez installer. Nous on a choisi *Debian 12* car je connais cette distribution et qu'elle a fait ses preuves. Je vous laisse trouver comment faire pour obtenir une clé bootable.  
Ensuite il faut donc booter l'ordi sur la clé, suivre les étapes de l'installeur graphique.  
Mais en gros les étapes sont :  
- Le choix de la langue (osef choisissez celle que vous voulez, l'anglais c'est cool pour chercher les bugs sur internet)
- le choix de la langue du clavier (ça c'est plus important)
- La configuration réseau automatique (si ça marhce pas à cause de la connexion au serveur DHCP, demandez à la DISI)
- La détermination du nom de la machine (nous on a choisit farmia, prévenez la DISI)
- Le renseignement du nom de domaine (Donné par la DISI, nous c'était `telecom-sudparis.eu`)
- Le renseignement du mot de passe `root`
- Le renseignement d'un premier user (vous en ajouterez d'autres par la suite)
- le choix des packages à installer (installez au moins le serveur ssh, pour l'interface graphique c'est pas du tout obligatoire mais ça peut être confortable et désactivable pour sauvegarder les ressources de l'ordi)
- installer `grub` (c'est plutot important pour éviter des galères)  

Voilà en gros c'est tout !  
Le serveur devrait redémarrer et vous êtes partis. GG

## La préparation du joli serveur

Nous on a installé Debian 12 dessus sans interface graphique (et oui logique c'est un serveur).  

### 1. La première étape est de mettre un serveur `ssh` dessus
En gros on veut permettre aux utilisateurs du serveur de se connecter à distance au serveur via le protocole `ssh`.  
Pour se faire si un serveur ssh n'est pas deja installé sur la machine :  
Sur le serveur :  
```
apt install openssh-server
```

La celui ou celle qui est en train de faire cette installation va avoir le privilège d'être le ou la première à mettre sa clé ssh dessus.  
> Mais c'est quoi une clé ssh ?  

En gros c'est une paire de clé, une privé, une publique, qui permet d'assurer l'authentification d'un ordinateur.  
Il vous faut donc générer une paire de clé sur l'ordinateur client (votre ordi).  
Sur votre ordi :  
```
ssh-keygen -t ed25519
```
Ensuite suivez les instructions (mettez un code).  
### **Ne partagez à personne votre clé privée**

Ensuite il faut l'envoyer sur le serveur : 
```
ssh-copy-id -i path/to/sshkey <user>@<serveurIP>
```

D'ailleurs pour connaitre l'IP du serveur : 
```
ip -4 addr
```

Ensuite il faut vérifier que vous avez accès à distance au serveur :  
```
ssh -i path/to/sshkey <user>@<serveurIP>
```

Si la connexion est établie. C'est super bravo. Mais c'est pas fini.  

Maintenant il va falloir se protéger des vilains méchants qui veulent s'introduire chez vous.  
> Comment faire ? 

Et bien leur fermer la porte au nez bien sur !  
En gros le risque c'est que tout le monde peut essayer de se connecter sur le server avec un nom d'utilisateur et un mot de passe. Le problème c'est que ça, ça se bruteforce. Pas cool ...  
Il faut donc éviter ça, et interdire les connexions par mots de passe tout simplement.  
On va donc se rendre dans les fichiers de configuration du serveur ssh.  

On cherche et on modifie dans le fichier `/etc/ssh/sshd_config` les lignes 
```
PasswordAuthentication no
PermitEmptyPasswords no
```
Après avoir fait ça il faut relancer le service ssh :  
```
systemctl restart ssh
```
ou
```
service ssh restart
```

Bravo les champions. Vous avez maintenant accès au serveur à distance ... **tant que vous êtes sur le campus** ... le firewall du campus vous empêche d'y accéder depuis l'extérieur. Mais c'est déjà bien.  

Vous pouvez ajouter le serveur à votre `.ssh/config` en ajoutant ses lignes sur vos ordis :
```
### Serveur Farmia
Host farmia
  User <user>
  IdentityFile <path/to/sshkey>
  HostName <IP Serveur>
```

Vous pouvez alors vous connecter avec :
```
ssh farmia
```
