from pydantic import BaseModel


class StaticProductModel(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int


"""
As We've added below code in Model,

`
from pydantic import BaseModel


class StaticProductModel(BaseModel):
`

Now, We don't need to __init__ construct method here. It'll be automatically inherited by 'BaseModel'.
"""

# def __init__(
#     self, id: int, name: str, description: str, price: float, quantity: int
# ):
#     self.id = id
#     self.name = name
#     self.description = description
#     self.price = price
#     self.quantity = quantity
