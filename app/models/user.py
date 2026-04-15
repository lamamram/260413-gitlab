from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)

    # Relation avec Employee (un utilisateur peut avoir un employee)
    employee = relationship("Employee", back_populates="user", uselist=False)
