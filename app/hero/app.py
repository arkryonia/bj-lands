from fastapi import APIRouter

from fastapi.params import Depends
from sqlmodel import Session, select

from app.core.db import create_db_and_tables, get_db
from app.hero import models

hero = APIRouter()

@hero.post("/")
def create_hero(*, db: Session = Depends(get_db), hero: models.HeroCreate):
        hero = models.Hero.from_orm(hero)
        db.add(hero)
        db.commit()
        db.refresh(hero)
        return hero


@hero.get("/")
def read_heroes(db: Session = Depends(get_db)):
        heroes = db.exec(select(models.Hero)).all()
        return heroes