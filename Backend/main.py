from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import get_connection
from models import Filter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/search")
def search(filter: Filter):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT id, brand, model, cpu_brand, cpu_generation,
           ram, storage_size, storage_type, price, store, url
    FROM laptops
    WHERE 1=1
    """

    params = []

    if filter.ram:
        query += " AND ram >= %s"
        params.append(filter.ram)

    if filter.storage_size:
        query += " AND storage_size >= %s"
        params.append(filter.storage_size)

    if filter.storage_type:
        query += " AND storage_type = %s"
        params.append(filter.storage_type)

    if filter.cpu_brand:
        query += " AND cpu_brand = %s"
        params.append(filter.cpu_brand)

    if filter.cpu_generation:
        query += " AND cpu_generation >= %s"
        params.append(filter.cpu_generation)

    if filter.max_price:
        query += " AND price <= %s"
        params.append(filter.max_price)

    query += " ORDER BY price ASC LIMIT 50"

    cursor.execute(query, params)

    rows = cursor.fetchall()

    result = []

    for row in rows:
        result.append({
            "id": row[0],
            "brand": row[1],
            "model": row[2],
            "cpu": f"{row[3]} Gen {row[4]}",
            "ram": row[5],
            "storage": f"{row[6]} {row[7]}",
            "price": float(row[8]),
            "store": row[9],
            "url": row[10]
        })

    cursor.close()
    conn.close()

    return result