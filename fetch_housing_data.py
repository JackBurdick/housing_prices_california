import os
import tarfile
from six.moves import urllib

# original file adapted from linked Textbook in root README.md
# link to github: https://github.com/ageron/handson-ml/blob/master/02_end_to_end_machine_learning_project.ipynb

# URL path specification
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    # create directory if not already created
    if not os.path.exists(housing_path):
        os.makedirs(housing_path)

    # retrieve zip file
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)

    #open and extract
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

if __name__ == "__main__":
    fetch_housing_data()
