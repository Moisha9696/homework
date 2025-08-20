from flask_sqlalchemy import SQLAlchemy

# Инициализируем экземпляр SQLAlchemy
db = SQLAlchemy()

# Импортируем все модели
from .posts import Post

__all__ = ['db', 'Post']