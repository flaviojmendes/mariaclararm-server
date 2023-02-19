

import codecs
import json


def loadList():
    people = []
    with open('people.txt') as f:
        lines = f.readlines()
        
        family = {"name": "", "people" : []}
        for line in lines:
            line = line.replace("\n", "") 

            if line == '':
                people.append(family)
                family = {"name": "","people" : []}
            else:
                if family["name"] == "":
                    family["name"] = line
                
                family["people"].append({"name": line})
    with codecs.open("people.json", "w", "utf-8-sig") as temp:
    
        temp.write(json.dumps(people, indent = 4, ensure_ascii=False ) )
        temp.close()


loadList()

