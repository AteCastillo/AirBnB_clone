#!/usr/bin/python3
"""Tests File"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import pep8


class TestFileStorage(unittest.TestCase):
    """Test of Amenity_class"""
    def test_FileStorage(self):
        new = FileStorage()
        self.assertIsInstance(new, FileStorage)
        self.assertEqual(issubclass(new.__class__, FileStorage), True)
        self.assertIs(type(new), FileStorage)

    def test_documentation(self):
        """Check documentation"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)

    def test_pep8_conformance(self):
        '''Test that we conform to PEP8.'''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['../../../models/FileStorage.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_save(self):
        pass

    def test_all(self):
        pass

    def test_reload(self):
        pass

    def test_new(self):
        pass
