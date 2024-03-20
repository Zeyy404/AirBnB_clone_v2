#!/usr/bin/python3
""" Test suite for the console"""

import unittest
import os
import sys
import models
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
from unittest.mock import create_autospec


class TestHBNBCommand(unittest.TestCase):
    """Test the console module"""
    def setUp(self):
        """Set up for tests"""
        self.cmd = HBNBCommand()

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_fs_create(self):
        """Tests the create method with the file storage."""
        self.cmd.do_create("Base name=\"example\" age=25")
        created_instance = self.cmd.storage.all().values()
        self.assertTrue(len(created_instance) == 1)
        instance = created_instance[0]
        self.assertEqual(instance.__class__.__name__, "Base")
        self.assertEqual(instance.name, "example")
        self.assertEqual(instance.age, 25)

    def tearDown(self):
        """Clean up storage after each test"""
        self.cmd.storage.reset()
