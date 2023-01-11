#########################################################
# Voici le README du site de la ferme des trois chênes. #
#########################################################

L'intéret de ce site est de représenter graphiquement des données utiles pour la ferme des trois chênes.


##Pré-requis## :

    Voci les modules à télécharger pour pouvoir lancer notre site web :
        - Flask 1.1.2

    Installation :
        Voici les commandes installation des modules utilisés :
            - $pip install Flask


##Démarage## :

    Pour démarrer notre site il faut lancer avec python le fichier `main.py`. Nous vous conseillons d'exécuter dans votre cmd les commandes suivantes:

    $ cd la-ferme-des-3-chenes

    pour ce situer dans le fichier `la-ferme-des-3-chenes` qui est le dossier contenant les fichiers du site
    Apres ça vous pouvez lancer le site internet avec cette commande:

    $ python main.py

    Quand vous aurez exécuté ce fichier, une adresse de type `http://127.0.0.1:5000/` apparaîtra dans votre cmd.
    Il vous suffit de copier cette adresse et de la coller dans votre navigateur web préféré. Si tout c'est bien passé vous voilà sur la page d'accueil de
    notre site.



##Arborescence des fichiers## :

    - \la-ferme-des-3-chenes -> est la racine du site. C'est ici que vous trouverez le fichier main.py ainsi que les fichiers python permettant l'extraction des données.

    - \la-ferme-des-3-chenes\data -> C'est ici que nous créons notre base de donnée p2.sqlite . La base de donnée est remplie en exécutant le fichier data_insert.py
                                     Le fichier sql_schema.py permet de créer les tables (vide) de la base de données, ce fichier est éxécuter lors de l'exécution
                                     de data_insert.py .


    -\la-ferme-des-3-chenes\static -> C'est ici que se trouve nos fichier css ainsi que les images présentes sur le site.

    -\la-ferme-des-3-chenes\templates -> C'est ici que vous trouverez tous les fichiers html des pages du site. Le fichier layout.html est la base de notre site il est donc présent dans
                                         tous les fichiers html du site.

##Auteurs##
    Ce site a été créé par le groupe P2_1B_2 composé de :

        - Dekens, Alba
        - Fraipont, Arthur
        - Gourgue, Julien
        - Hogge, Jacques