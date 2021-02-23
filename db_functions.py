import pickle
import mysql

# Connect to the database
connection = mysql.connect('localhost', 'root', '', 'g_face')

# Create a cursor for interacting
cursor = connection.cursor()


########################################################
# Read all data from the database table
########################################################
def read_data():
    cursor.execute("""SELECT * FROM face_encodings""")
    rows = cursor.fetchall()
    return rows


########################################################
# Add the information to the database table
########################################################
def write_data(name, encoding):
    return cursor.execute("""INSERT INTO face_encodings(name,encoding) VALUES (%s, %s)""", (name, encoding))
