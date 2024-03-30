from sklearn import neighbors, datasets

import logging
import time


logging.basicConfig(level = logging.INFO)

# TODO: Do this using cron
def main():
    while(True):
        logging.info("Loading Data")
        iris = datasets.load_iris()
        logging.info("Data Loading Complete")
        time.sleep(24)


if __name__ == '__main__':
    main()
