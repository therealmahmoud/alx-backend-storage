#!/usr/bin/env python3
"Task 8."


def list_all(mongo_collection):
    """ Lists all documents in a collection."""
    return [res for res in mongo_collection.collection.find()]
