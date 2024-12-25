from sqlalchemy.orm import Session
from app import models, schemas


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(
        title=item.title,
        description=item.description,
        completed=item.completed
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_items(db: Session):
    return db.query(models.Item).all()


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def update_item(db: Session, item_id: int, item: schemas.ItemCreate):
    db_item = get_item(db, item_id)
    if db_item:
        for key, value in item.model_dump().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int):
    db_item = get_item(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    return False
