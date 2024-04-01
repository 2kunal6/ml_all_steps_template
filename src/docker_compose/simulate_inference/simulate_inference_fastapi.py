from fastapi import FastAPI

import pickle
import time
import uvicorn


model_file_path = 'data/model.pkl'
user_feedback_file_path = 'data/user_feedback.txt'
last_model_update_time = None

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/predict')
def predict(prompt):
    global last_model_update_time
    if(last_model_update_time == None or int(time.time() - last_model_update_time) >= 24):
        model = pickle.load(open(model_file_path, 'rb'))
        last_model_update_time = time.time()
    prompt = eval(prompt)
    return str(model.predict(prompt))

@app.get('/store_user_feedback')
def store_user_feedback(user_feedback):
    with open(user_feedback_file_path, 'a+') as f:
        f.write(user_feedback)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
