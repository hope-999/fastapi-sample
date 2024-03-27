from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/items/{item_id}")
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    base_url = request.base_url
    cookies = request.cookies
    return {"client_host": client_host, "item_id": item_id, "base_url": base_url, "cookies": cookies}
