# soft_desk_project

***

Ce projet est entièrement codé en python 3.

SoftDesk API, est une API developpée en Python 3 à l'aide de [Django REST framework](https://www.django-rest-framework.org) permettant de faire remonter et de suivre des problème tehcniques.
Cette API a été créer dans le cadre de mes études lors de ma formation sur le site 
[OpenClassrooms](https://openclassrooms.com/).

L'API permet le suivi de problème sur trois plateformes (site web, application android et application IOS).
Elle permet principalement à un utilisateur de créer divers projets, d'ajouter des utilisateurs à des projets
spécifiques, de créer des problèmes au sein des projets et d'attribuer des libellés à ces problèmes en fonction 
de leurs priorités, de balises, etc.


## Table des matières
1. [Informations génerales](#informations-generales)
2. [Installation/usage](#installation-usage)

***

## Informations Generales

Ce projet utilise les frameworks [django](https://docs.djangoproject.com/fr/3.2/) et [django-REST](https://www.django-rest-framework.org/). Le système d'authentification est basé sur l'authentification JWT, pour cela, le projet utilise [simple-JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html).

Dans django, le projet utilise deux applications (en dehors des applications django pré-installées) :

*	**api**: l'application qui est l'application principale et qui gère tout le système de projet, contributeur, problèmes et commentaires.

*	**accounts**: l'application qui gère le système de connexion et de création de compte utilisateur.

L'ensemble des packages et dépendances à installer pour pouvoir lancer le projet sont notés dans le fichier 'requirements.txt' présent à la racine du projet.

En dehors du système de connexion, l'API est accessible aux utilisateurs connéctés uniquement.

La synthaxe du code respecte les directives de la PEP 8 (vérification avec flake-8). Un rapport flake8 est disponible dans le repertoire flake-report à la racine du projet.

Pour information, actuellement, le parametre DEBUG présent dans le fichier src/soft_desk_API/settings.py a pour valeur "True". En cas de mise en production il sera nécessaire de le passer à "False".

## Installation Usage

Tout d'abord il faut cloner le projet depuis github grâce à la commande suivante :

```
$ git clone https://github.com/npaillasson/soft_desk_project.git
```

Il est ensuite recommandé de créer un environement virtuel avec venv afin d'installer tous les packages et dépendances nécéssaires au fonctionnement du projet :

```
$ python3 -m venv env
```

Utilisez ensuite la commande suivante pour activer l'environnement :
```
$ source env/bin/activate
```

ou sous Windows:
```
> env\Scripts\activate
```

Vous pouvez ensuite installer les packages nécéssaire grace à pip et au fichier requirements.txt :
```
$ pip install -r requirements.txt
```

Pour lancer le serveur exécuter la commande suivante :
```
$ python3 src/manage.py runserver
```

Vous pouvez ensuite réaliser des requêtes à l'API à partir de POSTMAN ou du logiciel de votre choix.

Pour désactiver l'environnement virtuel, utilisez la commande suivante :
```
$ deactivate
```

Ou sous Windows:
```
> env\Scripts\deactivate
```

Pour créer un rapport de conformité à la pep 8 vous pouvez utiliser la commande suivante à la racine du projet :

```
$ flake8 --format=html --htmldir=flake-report --max-line-length=119 --exclude='src/*/migrations/*.py' src/
```
