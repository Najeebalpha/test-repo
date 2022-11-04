import os

def move_collection(from_URL, to_URL, database_name, collection_name, temp_filename='temp.json'):
    """
    Copy collection from one Mongo cluster to another.
    """
    from_URL = os.getenv[from_URL]
    to_URL = os.getenv[to_URL]
    os.system(f'mongoexport --uri {from_URL} --collection {collection_name} --type {temp_filename} --out temp.json 2>/dev/null')
    os.system(f'mongoimport --uri {to_URL} --collection {collection_name} --type {temp_filename} --file temp.json 2>/dev/null')
    os.system(f'rm {temp_filename}')

