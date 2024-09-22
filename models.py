from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

db = SQLAlchemy()

class UserTabel(db.Model):
    code: Mapped[int] = mapped_column(unique=True,primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()
    date:Mapped[str] = mapped_column(default=datetime.now())


class UserChat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[int] = mapped_column()
    name: Mapped[str] = mapped_column()
    chat: Mapped[str] = mapped_column()
    tag: Mapped[str] = mapped_column()
    date:Mapped[str] = mapped_column(default=datetime.now())