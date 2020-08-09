import requests
import json

def query(type, id, scorevalue_min=0):

    url = "https://platform-api.opentargets.io/v3/platform/public/association/filter"

    params = {type: id,
            "size": "10000",
            "direct": "True",
            "scorevalue_min": scorevalue_min}

    res = requests.get(url, params=params).json()

    d = {}
    for index, record in enumerate(res["data"]):
        d[index + 1] = {"disease_id": record["id"].split("-")[1],
                "target_id": record["id"].split("-")[0],
                "association_score.overall": record['association_score']["overall"]}

    return d

def export(dictionary, filename):
    with open(filename, "w") as outfile:  
        json.dump(dictionary, outfile) 

