from pydantic import BaseModel

class Filter(BaseModel):

    ram: int | None = None
    storage_size: int | None = None
    storage_type: str | None = None
    cpu_brand: str | None = None
    cpu_generation: int | None = None
    max_price: float | None = None