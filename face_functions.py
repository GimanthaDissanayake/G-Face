import pickle
from db_functions import write_data, read_data


########################################################
# Function to read face encodings from the database
########################################################
def load_from_db():
    result = read_data()
    return result


########################################################
# Function to write face encodings to the database
########################################################
def write_to_db(name, encoding):
    serialized_encoding = pickle.dumps(encoding)
    result = write_data(name, serialized_encoding)
    return result
