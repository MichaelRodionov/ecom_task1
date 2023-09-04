from json import JSONDecodeError

from fastapi import FastAPI, Request, HTTPException

from src import client, service

# ----------------------------------------------------------------
# init fastapi
app = FastAPI()


# ----------------------------------------------------------------
@app.post('/results')
async def get_attrs(request: Request):
    try:
        params = await request.json()
    except JSONDecodeError:
        raise HTTPException(status_code=400, detail='category_id and product_id are required')
    category_id, product_id = params.get('category_id'), params.get('product_id')

    query = (
        "select ca.attribute_id, ca.attribute_name, ca.description, ca.required, "
        "ca.dictionary_value, ca.data_type, pa.value "
        "from categories c "
        "join category_attrs ca "
        "on c.category_id=ca.category_id "
        "left join product_attr pa "
        "on ca.attribute_id = pa.attribute_id "
        f"where c.category_id = '{category_id}' and pa.product_id = '{product_id}'"
    )

    try:
        objects = client.query(query).result_rows
        result = service.get_results(objects)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
