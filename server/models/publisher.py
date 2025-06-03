"""
Publisher model for the Tailspin Toys crowdfunding platform.

This module defines the Publisher model representing game publishers
who create games available for crowdfunding.
"""
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Publisher(BaseModel):
    """
    Model representing a game publisher.
    
    Stores publisher information including name and description,
    with a one-to-many relationship to games.
    """
    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one publisher has many games
    games = relationship("Game", back_populates="publisher")

    @validates('name')
    def validate_name(self, key, name):
        """
        Validate the publisher name field.
        
        Args:
            key: The field name being validated
            name: The name value to validate
            
        Returns:
            str: The validated name
        """
        return self.validate_string_length('Publisher name', name, min_length=2)

    @validates('description')
    def validate_description(self, key, description):
        """
        Validate the publisher description field.
        
        Args:
            key: The field name being validated
            description: The description value to validate
            
        Returns:
            str: The validated description
        """
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)

    def __repr__(self):
        """
        Return a string representation of the Publisher object.
        
        Returns:
            str: String representation including publisher name
        """
        return f'<Publisher {self.name}>'

    def to_dict(self):
        """
        Convert the Publisher object to a dictionary for JSON serialization.
        
        Returns:
            dict: Dictionary representation of the publisher with all fields
                 including game count
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }