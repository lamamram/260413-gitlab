from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    seniority = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

    # Relation avec User (un employee est lié à un seul utilisateur)
    user = relationship("User", back_populates="employee")

    def get_seniority(self) -> int:
        """Retourne l'ancienneté de l'employé."""
        return self.seniority
