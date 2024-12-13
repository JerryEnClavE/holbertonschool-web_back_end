#!/usr/bin/env python3
"""
Return a list of all documents in a collection
"""

def list_all(mongo_colletion):
    """Return a list of all documents in a collection"""
    documents = []
    for doc in mongo_colletion.find({}):
        documents.append(doc)
    return documents
