# qualité

## formatage: convention & style du code

* exemple python avec black

1. ajout dans app/requirements-dev.txt
2. test en local (dans le venv)
  * `python -m black ./app`
3. ajout du fichier de configuration
  * fichier app/pyproject.py.toml
  * `python -m black --config=./app/pyproject.py.toml ./app`
4. ajout de la procédure dans le hook `./git/hooks/pre-commit`
  * ramasser les modifs issues du formatage avec un `git add`
  * ajout l'option **-q**
  * `chmod u+x .git/hooks/pre-commit` 