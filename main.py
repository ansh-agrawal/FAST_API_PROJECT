from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Simple FastAPI App", version="1.0.0")


class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)


items_db: list[dict[str, int | str | float]] = []
next_item_id = 1


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello from FastAPI"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/items")
def list_items() -> list[dict[str, int | str | float]]:
    return items_db


@app.post("/items")
def create_item(item: ItemCreate) -> dict[str, int | str | float]:
    global next_item_id

    new_item = {
        "id": next_item_id,
        "name": item.name,
        "price": item.price,
        "message": "Item created",
    }
    items_db.append(new_item)
    next_item_id += 1

    return new_item
