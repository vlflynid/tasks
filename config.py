import dotenv
from dotenv import load_dotenv
import os

load_dotenv()
HOST = os.environ.get('HOST')
USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')
DATABASE = os.environ.get('DATABASE')

LOGFILE = 'logs.log'

STUDENTS = 'source/students.json'
ROOMS = 'source/rooms.json'

TABLES = {
    'rooms': ['id INT PRIMARY KEY', 'name VARCHAR(255)'],
    'students': ['birthday VARCHAR(255)', 'id INT PRIMARY KEY', 'name VARCHAR(255)', 'room INT', 'sex VARCHAR(1)']
}

ANALYSIS_PATH = 'source/analysis.yaml'



