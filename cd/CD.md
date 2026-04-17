## notes sur le déploiement continu (CD)

### gestion de l'image docker pour le build en utilisant le démon docker du host

> !! l'image docker "docker:xxx-cli" ne contient que la cli, elle donc besoin d'un démon

1. partager la socket unix dans la config `/etc/gitlab-runner/config.toml` du runner
```toml
[[runners]]
  ...
  volumes = ["/var/run/docker.sock:/var/run/docker.sock", "/cache"]
```

2. utiliser une image docker qui contient le démon docker, par exemple `docker:xxx-dind` (docker-in-docker)
  - on créer ce conteneur en utilisant une clé `services` à côté du conteneur du job
  - il faut utiliser TCP et non la socket unix port 2376 TLS
  - de toute façon le runner demande une élévation de privilère pour utiliser le démon docker, il faut ajouter `privileged = true` dans la config du runner

3. installer la vm avec un docker rootless, + un conteneur sidecar qui lui même dind-rootless


### gestion du certifiat auto signé pour le registry privé

* désactiver le vérification tls dans `/etc/docker/daemon.json` du host
```json
{
  "insecure-registries" : ["gitlab.lan.fr:5050"]
}
```

