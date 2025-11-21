from fastapi import FastAPI
from static_products import products
from static_product_model import StaticProductModel

app = FastAPI()


@app.get("/")
def greet():
    return "Welcome to the FastAPI!"


@app.get("/products")
def get_all_products():
    return products


@app.get("/products/{id}")
def view_product(id: int):
    for product in products:
        if product.id == id:
            return product

    return "Product not found"


@app.post("/products")
def store_product(product: StaticProductModel):
    products.append(product)
    return product


@app.put("/products/{id}")
def update_product(id: int, product: StaticProductModel):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Updated successfully"

    return "Product not found."


@app.delete("/products/{id}")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product deleted successfully"

    return "Product not found"
