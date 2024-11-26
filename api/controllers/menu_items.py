from sqlalchemy.orm import Session
from ..models.menu_items import MenuItem as MenuItemModel
from ..schemas.menu_items import MenuItemCreate, MenuItemUpdate

def create_menu_item(db: Session, request: MenuItemCreate):
    new_item = MenuItemModel(**request.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def get_all_menu_items(db: Session):
    return db.query(MenuItemModel).all()

def get_menu_item(db: Session, menu_item_id: int):
    return db.query(MenuItemModel).filter(MenuItemModel.id == menu_item_id).first()

def update_menu_item(db: Session, menu_item_id: int, request: MenuItemUpdate):
    item = db.query(MenuItemModel).filter(MenuItemModel.id == menu_item_id).first()
    if item:
        for key, value in request.dict(exclude_unset=True).items():
            setattr(item, key, value)
        db.commit()
        db.refresh(item)
    return item

def delete_menu_item(db: Session, menu_item_id: int):
    item = db.query(MenuItemModel).filter(MenuItemModel.id == menu_item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item
