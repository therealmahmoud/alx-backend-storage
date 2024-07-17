#!/usr/bin/env python3
""" Task 11."""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic."""
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [search for search in mongo_collection.find(topic_filter)]
