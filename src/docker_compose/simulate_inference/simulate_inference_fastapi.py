from fastapi import FastAPI

import json
import pickle
import time
import uvicorn


model_file_path = 'data/model.pkl'
last_model_update_time = None

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/predict')
def read_item(prompt):
    global last_model_update_time
    if(last_model_update_time == None or int(time.time() - last_model_update_time) >= 24):
        model = pickle.load(open(model_file_path, 'rb'))
        last_model_update_time = time.time()
    prompt = eval(prompt)
    return str(model.predict(prompt))


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
