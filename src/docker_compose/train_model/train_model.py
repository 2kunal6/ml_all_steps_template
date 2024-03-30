from sklearn import neighbors, datasets

import logging
import os
import pickle
import time


logging.basicConfig(level = logging.INFO)


data_file_path = 'data/iris.pkl'
model_file_path = 'data/model.pkl'

# TODO: Do this using cron
while(True):
    if not os.path.exists(data_file_path):
        logging.info('\tWaiting for data to load')
        time.sleep(3)

    with open(data_file_path, 'rb') as bunch:
        df = pickle.load(bunch)

    logging.info("\tTrain Model Start")
    X, y = df.data, df.target
    knn = neighbors.KNeighborsClassifier(n_neighbors=1)
    knn.fit(X, y)
    logging.info("\tTrain Model Complete")


    logging.info("\tSaving model as pickle file")
    if os.path.exists(model_file_path):
        os.remove(model_file_path)
    pickle.dumps(knn, model_file_path)
    logging.info("\tSaved model as pickle file")


    time.sleep(24)
