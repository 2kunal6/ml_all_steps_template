import logging
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


def simulate_inference_request(query):
    while(True):
        logging.info(f'Providing inference for {query}')
        time.sleep(0.2)
        logging.info(f'Provided inference for {query}')


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("ML Model Deployed")

    load_data_thread = threading.Thread(target=load_data, daemon = True)
    load_data_thread.start()

    logging.info("Start Training")

    train_model_thread = threading.Thread(target=train_model, daemon = True)
    train_model_thread.start()

    logging.info("Simulating Inference Requests")
    simulate_inference_request_thread = threading.Thread(target=simulate_inference_request('xxx'), daemon = True)
    simulate_inference_request_thread.start()

    while True:
        pass
