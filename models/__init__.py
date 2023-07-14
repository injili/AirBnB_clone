"""
modified __init__ to create a unique FileStorage instance
"""
from .file_storage import FileStorage
storage = FileStorage()
storage.reload()

