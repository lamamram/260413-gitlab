# job test interfaces

## composants

* on va utiliser le conteneur php classique du pipeline
  - en partageant le cache des dépendances
* on va ajouter un **conteneur dynamique** selenium `selenium/standalone-firefox:133.0-geckodriver-0.35` en tant que serveur
* on a besoin en plus du `geckodriver` entre le client et le serveur

## installation du serveur

*  en manuel
```bash
docker run \
       --name selenium \
       -d --restart unless-stopped \
       selenium/standalone-firefox:133.0-geckodriver-0.35
```

* ou dans gitlab avec un **service** à la volée puisque le serveur est complètement
* configuré depuis le client

```yaml
services:
  - name: selenium/standalone-firefox:133.0-geckodriver-0.35
    alias: selenium-server
```

## installation du driver

* avant de lancer les tests
  - décompresser le driver dans le conteneur
  - l'installer en exécution dans le PATH
  - côté client selenium => utiiser le nom du conteneur comme url !
  - utiliser l'option **headless**

* attention au scope: différencier les tests E2E et les tests Unit et IT