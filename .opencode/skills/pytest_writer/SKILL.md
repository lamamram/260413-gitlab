---
name: pytest_writer
description: |
  Skill spécialisée dans la génération de tests unitaires ou d'intégration en utilisant le framework pytest pour les projets Python.
license: MIT
compatibility: opencode
metadata:
  workflow: github
permission:
  write: allow
  edit: allow
  glob: allow
  grep: allow
  bash:
    pytest *: allow
---

## overview

Cette skill permet de générer automatiquement des tests unitaires ou d'intégration pour des projets Python en utilisant le framework pytest. 
utilise le pattern AAAC (Arrange, Act, Assert, Cleanup) pour structurer les tests de manière claire et efficace.

## best practices

* commencer avec les test unitaires : classes métiers, models
* MUST, IMPORTANT avant de passer aux tests d'intégration en utilisant des monkeypatch des modèles dans pytest: routes

## commands pytest

* utiliser l'option `-s` si le prompt demande un debug.

## procédures

### installer les fixtures

1. créer un fichier `conftest.py` dans le répertoire des `app\tests` s'il n'existe pas déjà.
2. déplacer les fixtures communes dans ce fichier pour qu'elles soient accessibles à tous les tests.
3. supprimer les fixtures inutiles

### touver les edges cases 

* écrivez les test cases en fonction du prompt fourni
  + spécifiez des fixtures paramétrables
  + en trouvant les edge cases et un cas favorable

## When to use me

Utilisez cette skill lorsque vous avez besoin de générer des tests automatisés pour votre code Python afin d'assurer sa qualité et sa robustesse.


## Documentation

* Examples: dans `./examples/*.md`
