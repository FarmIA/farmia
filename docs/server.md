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
**Ne partagez à personne votre clé privée**