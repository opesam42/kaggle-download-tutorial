import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# https://www.kaggle.com/datasets/srinivasav22/sales-transactions-dataset?select=Train.xlsx
handle = 'srinivasav22/sales-transactions-dataset'

#download all files in dataset
api.dataset_download_files(handle, path='./', unzip=True)

#download specific file in dataset
api.dataset_download_file(handle, file_name='Test.xlsx')