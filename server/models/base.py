# filepath: server/models/base.py
"""
Base model class providing common functionality for all database models.

This module defines the BaseModel class which serves as the foundation
for all SQLAlchemy models in the application, providing shared validation methods.
"""
from . import db

class BaseModel(db.Model):
    """
    Abstract base class for all database models.
    
    Provides common validation methods and shared functionality
    that all models can inherit and use.
    """
    __abstract__ = True
    
    @staticmethod
    def validate_string_length(field_name, value, min_length=2, allow_none=False):
        """
        Validate the length of a string field.
        
        Args:
            field_name: Name of the field being validated (for error messages)
            value: The string value to validate
            min_length: Minimum required length (default: 2)
            allow_none: Whether to allow None values (default: False)
            
        Returns:
            str: The validated string value
            
        Raises:
            ValueError: If validation fails
        """
        if value is None:
            if allow_none:
                return value
            else:
                raise ValueError(f"{field_name} cannot be empty")
        
        if not isinstance(value, str):
            raise ValueError(f"{field_name} must be a string")
            
        if len(value.strip()) < min_length:
            raise ValueError(f"{field_name} must be at least {min_length} characters")
            
        return value