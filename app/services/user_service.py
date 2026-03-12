from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password
from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)
    
    def create_user(self, user_data: UserCreate) -> User:
        """Has business logic - keep in service"""
        # Check if exists
        existing = self.user_repo.get_by_email(user_data.email)  # Call repo directly!
        if existing:
            raise ValueError("Email already registered")
        
        # Hash password (business logic)
        hashed_password = hash_password(user_data.password)
        
        # Create user
        new_user = User(
            email=user_data.email,
            password_hash=hashed_password,
            name=user_data.name,
            phone=user_data.phone
        )
        
        try:
            return self.user_repo.create(new_user)
        except IntegrityError:
            self.db.rollback()
            raise ValueError("Email already exists")
    
