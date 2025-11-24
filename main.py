from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from static_products import products
from static_product_model import StaticProductModel
from database import session, engine
import product_model
from sqlalchemy.orm import Session

app = FastAPI()

# You need to add CORS Middleware like this when you use this API from different PORT like 3000 or 5000 etc...
app.add_middleware(
    CORSMiddleware, allow_origins=["http://localhost:3000"], allow_methods=["*"]
)

product_model.Base.metadata.create_all(bind=engine)


def db_conn():
    db = session()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db = session()

    if db.query(product_model.ProductModel).count == 0:
        for product in products:
            db.add(product_model.ProductModel(**product.model_dump()))

        db.commit()


# Just call this function if you want to create default records into 'products' TABLE from 'static_products.py' file.
init_db()


@app.get("/")
def greet():
    return "Welcome to the FastAPI!"


@app.get("/products")
def get_all_products(db: Session = Depends(db_conn)):
    return db.query(product_model.ProductModel).all()


@app.get("/products/{id}")
def view_product(id: int, db: Session = Depends(db_conn)):
    product = (
        db.query(product_model.ProductModel)
        .filter(product_model.ProductModel.id == id)
        .first()
    )
    if product:
        return product

    return "Product not found"


@app.post("/products")
def store_product(product: StaticProductModel, db: Session = Depends(db_conn)):
    db.add(product_model.ProductModel(**product.model_dump()))
    db.commit()
    return product


@app.put("/products/{id}")
def update_product(
    id: int, product: StaticProductModel, db: Session = Depends(db_conn)
):
    get_product = (
        db.query(product_model.ProductModel)
        .filter(product_model.ProductModel.id == id)
        .first()
    )
    if get_product:
        get_product.name = product.name
        get_product.description = product.description
        get_product.price = product.price
        get_product.quantity = product.quantity
        db.commit()
        return "Product Updated successfully"

    return "Product not found."


@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(db_conn)):
    product = (
        db.query(product_model.ProductModel)
        .filter(product_model.ProductModel.id == id)
        .first()
    )

    if product:
        db.delete(product)
        db.commit()
        return "Product deleted successfully"

    return "Product not found"
