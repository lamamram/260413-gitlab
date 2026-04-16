# exécuter un client IA (opencode) via un Composant GitLab CI/CD

## Objectif

L'objectif de ce composant est de démontrer comment exécuter un client d'intelligence artificielle (IA) appelé "opencode" dans le cadre d'un pipeline GitLab CI/CD. Ce composant peut être utilisé pour automatiser des tâches telles que l'analyse de code, la génération de rapports, ou toute autre opération que le client IA est capable de réaliser.

## plan

1. chercher le composant [https://gitlab.com/nagyv/gitlab-opencode](https://gitlab.com/nagyv/gitlab-opencode) et l'implanter dans notre groupe de projets

2. configurer le composant pour qu'il puisse être utilisé dans notre pipeline

  * ajouter le dossier .opencode à la racine de notre projet pour charger les 
    - commandes slash personnalisées
    - les SKILLS personnalisés (compétences spécifiques à notre projet)
  
  * on doit créer une variables cachées $OPENCODE_AUTH_JSON qui contient le chemin vers un fichier json d'authentification

  * configurer le modèle et les droits d'usage du composant