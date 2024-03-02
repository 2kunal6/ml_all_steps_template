from fastapi import FastAPI
from inference import get_inference


import uvicorn


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post('/predict')
def read_item(query_str):
    return get_inference(query_str)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
