import connexion
import six
import pymongo
from swagger_server import util
from AuthCore.sdb import mongo
import uuid

db = mongo.MongoDBInterface("lfvde")
db.select_table("SOCIAL_DISCUSS", "CLASSIFY_DATA")


# def content_db():
#     client = pymongo.MongoClient(
#         "mongodb+srv://root:root@cluster0.lfvde.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#     return client


def insert_db(data):
    key = str(uuid.uuid4())
    result = db.__insert__(key, data)
    return result


def select_all_db():
    return db.dump()


def to_csv_from_list_of_json(json_list):
    text = ""
    for line in json_list:
        row = []
        for k, v in line.items():
            row.append(str(v).replace(",", ".."))
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
    # mongo_client = content_db()
    db_result = insert_db(insert_data)
    print(f"db_result: {db_result}")
    print(f"insert_data: {insert_data}")
    # data["db_result"] = str(db_result)
    return "ok"


def get_data():  # noqa: E501

    # mongo_client = content_db()
    data = select_all_db()
    return to_csv_from_list_of_json([line for line in data])
