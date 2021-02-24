from reg_demo import config

TRAIN_DATA_PATH = config.DATA_PATH / 'train.txt'

def get_data():
    with open (TRAIN_DATA_PATH, 'r') as data_file:
        contents = data_file.read().strip()
        return contents

def write_data(*, new_contents = "new_contents"):
    with open(TRAIN_DATA_PATH, 'w') as data_file:
        data_file.write(new_contents)