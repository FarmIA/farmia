# Ici on va parler de la partie serveur

## A partir du setup jusqu'à l'utilisation

## Le setup

Premièrement il vous faudra une machine sur laquelle le serveur va tourner. Cette machine peut etre un ordinateur dans la salle, un ordinateur d'un membre, une machine virtuelle (MiNET ou non). Attention cependant pour les machines virtuelles, il vous faudra un stockage important.  
Dans notre cas (2024), on a trouvé un super ordinateur de MiNET. On a installé Debian 12 dessus sans interface graphique (et oui logique c'est un serveur).  

### 1. La première étape est de mettre un serveur `ssh` dessus
En gros on veut permettre aux utilisateurs du server de se connecter à distance au server via le protocole `ssh`.  
Pour se faire :  
Sur le server  ```apt install openssh-server```