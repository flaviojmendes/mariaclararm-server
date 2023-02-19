

import json
from model import FamilyModel, ListModel



def confirm_family(family: FamilyModel):
    json_data = None
    with open('list.json') as json_file:
        json_data = json.load(json_file)        
        for db_family in json_data:
            if db_family["name"] == family.dict()["name"]:
                db_family["people"] = family.dict()["people"]
                break
    with open("list.json", "w") as outfile:
        json_object = json.dumps(json_data, indent=4)
        outfile.write(json_object)


    
def get_list():
    with open('list.json') as json_file:
        json_data = json.load(json_file)    
        return json_data
    
    
