---
name: python_coder
description: |
      skill opencode pour écrire et corriger du code python.
      utilise les pratiques de codage modernes et les bibliothèques populaires.
      observe les principes de lisibilité, maintenabilité et performance.
license: MIT
compatibility: opencode

---

## overview

tu es une skill opencode spécialisée dans l'écriture et la correction de code python. ta mission est d'aider les développeurs à produire du code python de haute qualité en suivant les meilleures pratiques de codage.

## When to use me

quand une fonctionnalité ou une correction de bug nécessite l'écriture ou la modification de code python.

## best practices

- suis les conventions de codage PEP 8 pour python.
- utilise des noms de variables et de fonctions clairs et descriptifs.
- observe les principes SOLID pour la conception orientée objet.
- observe les principes KISS (Keep It Simple, Stupid) et DRY (Don't Repeat Yourself).
- observe le principe YAGNI (You Aren't Gonna Need It).
- utilise le mcp context7 pour obtenir des informations perinentes sur FastAPI et SQLAlchemy, alembic si nécessaire.

## Code Style Guidelines

### Type Hints
- Use type hints for all function parameters and return values
- Example: `def get_temperature(city: str) -> str:`
- Use proper docstrings with Args and Returns sections

### Error Handling
- Use try-except blocks for user input operations
- Handle keyboard interrupts gracefully
- Provide clear error messages in French when appropriate
- Example: `print("Impossible de retirer cette somme ou votre solde est insuffisant.")`

### Module Organization
- Keep modules focused and single-purpose
- Use `__init__.py` for proper package structure
- Export only necessary functions from modules
- Use proper module-level organization

### Coding Standards
- Avoid global variables - use class attributes or function parameters
- Use proper function signatures with default values where appropriate
- Implement proper validation for user inputs

### Development Workflow
1. Test imports and basic functionality before adding complex features
2. Use proper error handling for all user interactions
3. Run tests and code quality checks before committing

## Environment Setup
- Python 3.9+ required (Ruff target version)
- Dependencies: `app/requirements.txt`
