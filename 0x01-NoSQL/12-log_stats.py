#!/usr/bin/env python3
"""Task 12."""
from pymongo import MongoClient


def main(nginx_collection):
    """Print logs and methods."""
    print(f"{nginx_collection.count_documents({})} logs")
    print("Methoods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        req_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def run():
    """Provides some stats about Nginx logs stored in MongoDB."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    main(client.logs.nginx)


if __name__ == '__main__':
    run()
