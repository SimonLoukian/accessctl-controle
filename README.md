**Vous trouverez ici une explication du code pour le contrôle d'accès.** 
Vous y trouverez la configuration d'une passerelle qui permet de communiquer en RS-485 au travers de TCP/IP
La configuration du de l'EDW 100 est la suivante : 
Adresse IP : 192.168.191.100
Port : 502
Cette adresse permettra de communiquer avec la plateforme sur laquel se trouve un pont bascule, une caméra et une barrière. 
Le but étant à la fin de permettre que la barrière s'active automaatiquement en fonction des données qu'il aura transmi a une base de donnée. 
Sur ce même code vous trouverez un serveur bottle sur le port 5000 et a une adresse IP qui est celle de votre système ( vous pouvez la changer si besoin ). 
Il est relier a une page web dont le code se trouve en HTML dans le programme et cette dite pages web permet à un opérateur de contrôler la barrière 
a sa guise a distance en cas par exemple de problème avec le le contrôle d'accès. 

**Les améliorations a apporter sont les suivantes :** 
- Retirer la configuration du programme et l'inclure dans un fichier yaml.
- Retirer la partie du code html et l'inclure dans un fichier HTML.
- Corriger l'erreur 133 qui s'affiche au travers de la ligne 50 et 51
