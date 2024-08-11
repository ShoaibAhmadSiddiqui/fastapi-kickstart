from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import Model


class User(Model):
    __tablename__ = "users"
    id: UUID = Column(UUID(as_uuid=True), primary_key=True)
    first_name = Column(String(100), index=True)
    last_name = Column(String(100), nullable=True)
    email = Column(String(256), unique=True, index=True)
    password = Column(String(256))
