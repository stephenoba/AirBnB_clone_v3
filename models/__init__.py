#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    print("using db storage")
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    print("using file storage")
    storage = FileStorage()
storage.reload()
