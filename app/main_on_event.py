from fastapi import FastAPI

from app.util import MysqlDB

mysql_db = MysqlDB()

app = FastAPI()


# 注册启动和关闭事件
# @app.on_event("startup")
# async def startup_event():
#     await mysql_db.connect_to_mysql()
#
#
# @app.on_event("shutdown")
# async def shutdown_event():
#     await mysql_db.close_mysql_connection()


@app.get("/predict")
async def predict():
    sql = "SELECT t.* FROM xiaoe_testing_platform.django_migrations t LIMIT 501"
    result = mysql_db.mysql_get_sql_result(sql)
    return {"message": "Connection OK", "result": result}


items = {}


@app.on_event("startup")
async def startup_event():
    items["foo"] = {"name": "Fighters"}
    items["bar"] = {"name": "Tenders"}


@app.get("/items/{item_id}")
async def read_items(item_id: str):
    return items[item_id]
