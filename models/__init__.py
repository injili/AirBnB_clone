#!/usr/bin/python3
"""
modified __init__ to create a unique FileStorage instance
"""

from  models.engine import file_storage
storage = file_storage.FileStorage()
storage.reload()

