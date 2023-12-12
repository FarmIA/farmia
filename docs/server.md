# Ici on va parler de la partie serveur

## A partir du setup jusqu'à l'utilisation

## Le setup

Premièrement il vous faudra une machine sur laquelle le serveur va tourner. Cette machine peut etre un ordinateur dans la salle, un ordinateur d'un membre, une machine virtuelle (MiNET ou non). Attention cependant pour les machines virtuelles, il vous faudra un stockage important.  
Dans notre cas (2024), on a trouvé un super ordinateur de MiNET. On a installé Debian 12 dessus sans interface graphique (et oui logique c'est un serveur).  

### 1. La première étape est de mettre un serveur `ssh` dessus
En gros on veut permettre aux utilisateurs du serveur de se connecter à distance au serveur via le protocole `ssh`.  
Pour se faire :  
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
ssh-copy-id -h
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
service ssh restart
```