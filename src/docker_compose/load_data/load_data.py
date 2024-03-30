from sklearn import neighbors, datasets

import logging
import os
import pickle
import time


logging.basicConfig(level = logging.INFO)


data_file_path = 'data/iris.pkl'

# TODO: Do this using cron
while(True):
    logging.info("Loading Data")
    iris = datasets.load_iris()

    if os.path.exists(data_file_path):
        os.remove(data_file_path)
    with open(data_file_path, 'wb') as bunch:
        pickle.dump(iris, bunch, protocol=pickle.HIGHEST_PROTOCOL)

    logging.info("Data Loading Complete")
    time.sleep(24)
