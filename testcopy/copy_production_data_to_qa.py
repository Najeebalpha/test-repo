import move_collection
databases_to_copy = {'sample_airbnb': ['listingsAndReviews'], 'sample_restaurants': ['neighborhoods', 'restaurants'], 'sample_geospatial': ['shipwrecks']}

def copy_production_data_to_qa():
    """
    Make sure to set the environment variables used as from_url and to_url
    before running this script.
    """
    for db_name, collections in databases_to_copy:
        if 'user_db' in db_name:
            from_url = 'prod_MONGO_URL_USERS'
            to_url = 'qa_MONGO_URL_USERS'
        else:
            from_url = 'prod_MONGO_URL'
            to_url = 'qa_MONGO_URL'
        for collection_name in collections:
            move_collection(from_url, to_url, db_name, collection_name)