from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..controllers import menu_items as controller
from ..schemas.menu_items import MenuItem, MenuItemCreate, MenuItemUpdate

router = APIRouter(
    tags=["Menu Items"],
    prefix="/menuitems"
)

@router.post("/", response_model=MenuItem)
def create_menu_item(request: MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create_menu_item(db, request)

@router.get("/", response_model=list[MenuItem])
def get_all_menu_items(db: Session = Depends(get_db)):
    return controller.get_all_menu_items(db)

@router.get("/{menu_item_id}", response_model=MenuItem)
def get_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    return controller.get_menu_item(db, menu_item_id)

@router.put("/{menu_item_id}", response_model=MenuItem)
def update_menu_item(menu_item_id: int, request: MenuItemUpdate, db: Session = Depends(get_db)):
    return controller.update_menu_item(db, menu_item_id, request)

@router.delete("/{menu_item_id}")
def delete_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    return controller.delete_menu_item(db, menu_item_id)
