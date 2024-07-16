#!/usr/bin/env python3
"""Task 10."""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name."""
    res = mongo_collection.update({name}, [topics])
    return res
