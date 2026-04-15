"""Script pour initialiser la base de données SQLite avec les modèles SQLAlchemy."""

from app.models.database import Base, engine
from app.models.user import User
from app.models.employee import Employee


def init_database() -> None:
    """
    Crée toutes les tables dans la base de données selon les modèles SQLAlchemy.

    Cette fonction:
    - Supprime toutes les tables existantes (DROP)
    - Recrée toutes les tables selon les modèles définis
    """
    print("Initialisation de la base de données...")

    # Supprimer toutes les tables existantes
    print("Suppression des tables existantes...")
    Base.metadata.drop_all(bind=engine)

    # Créer toutes les tables selon les modèles
    print("Création des tables...")
    Base.metadata.create_all(bind=engine)

    print("Base de données initialisée avec succès!")
    print(f"Tables créées: {', '.join(Base.metadata.tables.keys())}")


def create_tables_if_not_exists() -> None:
    """
    Crée les tables uniquement si elles n'existent pas déjà.

    Contrairement à init_database(), cette fonction ne supprime pas
    les tables existantes.
    """
    print("Vérification et création des tables manquantes...")
    Base.metadata.create_all(bind=engine)
    print("Vérification terminée!")


if __name__ == "__main__":
    # Par défaut, initialise complètement la base de données
    init_database()
