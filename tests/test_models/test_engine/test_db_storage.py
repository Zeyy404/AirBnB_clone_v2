#!/usr/bin/python3
''' module for file_storage tests '''
import unittest
import MySQLdb
from models.user import User
from models import storage
from datetime import datetime
import os


class TestDBStorage(unittest.TestCase):
