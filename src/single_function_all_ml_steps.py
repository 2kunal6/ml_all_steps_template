import logging
import random
import threading
import time


def load_data():
    while(True):
        logging.info("Loading Data")
        time.sleep(1)
        logging.info("Data Loading Complete")


def train_model():
    while(True):
        logging.info("Train Model Start")
        time.sleep(2)
        logging.info("Train Model Complete")
        logging.info("Saving New Model Complete")


def get_inference(query):
    logging.info(f'Providing inference for {query}')
    time.sleep(0.2)
    logging.info(f'Provided inference for {query}')

def simulate_inference_request():
    while(True):
        get_inference(random.random())
        time.sleep(2)


def store_user_feedback(query_id, score):
    logging.info(f'Storing score {query_id} = {score}')
    time.sleep(0.2)
    logging.info(f'Stored score for {query_id} = {score}')

def listen_to_user_feedback():
    while(True):
        store_user_feedback(random.random(), random.random())
        time.sleep(2)



if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("ML Model Deployed")

    load_data_thread = threading.Thread(target=load_data)
    load_data_thread.start()

    train_model_thread = threading.Thread(target=train_model)
    train_model_thread.start()

    simulate_inference_request_thread = threading.Thread(target=simulate_inference_request)
    simulate_inference_request_thread.start()

    listen_to_user_feedback_thread = threading.Thread(target=listen_to_user_feedback)
    listen_to_user_feedback_thread.start()
