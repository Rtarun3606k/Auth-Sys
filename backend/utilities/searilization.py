def serialize_doc(doc):
    """
    Convert MongoDB document to JSON-serializable format.
    """
    if doc:
        doc['_id'] = str(doc['_id'])
    return doc