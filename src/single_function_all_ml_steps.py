from sklearn import neighbors, datasets

import logging
import random
import threading
import time


iris = None
knn = None

def load_data():
    global iris
    while(True):
        logging.info("Loading Data")
        iris = datasets.load_iris()
        logging.info("Data Loading Complete")
        time.sleep(24)


def train_model():
    global iris
    global knn
    while(True):
        if(iris == None):
            logging.info('\tWaiting for data to load')
            time.sleep(3)
            continue
        logging.info("\tTrain Model Start")
        X, y = iris.data, iris.target
        knn = neighbors.KNeighborsClassifier(n_neighbors=1)
        knn.fit(X, y)
        logging.info("\tTrain Model Complete")
        time.sleep(24)


def get_inference(query):
    global iris
    global knn
    if(knn == None):
        logging.info('\t\tWaiting for model to load')
        time.sleep(3)
        return
    logging.info(f'\t\tProviding inference for {query}')
    logging.info(f'\t\tInference Value: {iris.target_names[knn.predict(query)]}')
    logging.info(f'\t\tProvided inference for {query}')

def simulate_inference_request():
    while(True):
        get_inference([[3, 5, 4, 2]])
        time.sleep(5)


def store_user_feedback(query_id, score):
    logging.info(f'\t\t\tStoring score {query_id} = {score}')
    time.sleep(0.2)
    logging.info(f'\t\t\tStored score for {query_id} = {score}')

def listen_to_user_feedback():
    while(True):
        store_user_feedback(random.random(), random.random())
        time.sleep(5)



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
