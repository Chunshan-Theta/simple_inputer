import connexion
import six
import pymongo
from swagger_server import util

def content_db():
    client = pymongo.MongoClient(
        "mongodb+srv://root:root@cluster0.lfvde.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    return client

def insert_db(client,data):
    result = client.insert_one(data)
    return result

def select_all_db(client):
    return client.find()

def to_csv_from_list_of_json(json_list):
    text = ""
    for line in json_list:
        row = []
        for k, v in line.items():
            row.append(str(v).replace(",",".."))
        text += ",".join(row)
        text += "\n"
    return text

def add_data(content, label):  # noqa: E501
    """輸入資料

     # noqa: E501

    :param content: ID of pet that needs to be updated
    :type content: str
    :param label: ID of pet that needs to be updated
    :type label: str

    :rtype: None
    """
    insert_data = {
        "content": content,
        "label": label
    }
    mongo_client = content_db()
    db_result = insert_db(mongo_client['SOCIAL_DISCUSS']['CLASSIFY_DATA'], insert_data)
    print(f"db_result: {db_result}")
    print(f"insert_data: {insert_data}")
    # data["db_result"] = str(db_result)
    return "ok"

def get_data():  # noqa: E501

    mongo_client = content_db()
    data = select_all_db(mongo_client['SOCIAL_DISCUSS']['CLASSIFY_DATA'])
    return to_csv_from_list_of_json([line for line in data])