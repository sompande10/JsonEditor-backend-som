import json



share_path = "/Users/sompande/Desktop/JSONeditor/templates/sharepoint.json"
oracle_path = "/Users/sompande/Desktop/JSONeditor/templates/oracle.json"


choice = int(input("Choose one option : 1)Create from existing templates 2) Create a new template. 3)Edit Objects\n"))

if choice == 1:
    print("Create from existing templates chosen")

    db_type = input("Enter DB type: ")
    if db_type == "sharepoint":
        with open(share_path) as f:
            obj = json.load(f)
    print("Enter source details: ")
    source_keys = list(obj.keys())

    obj[source_keys[0]] = input("enter source name: ")
    obj[source_keys[1]] = input("enter source type:")
    obj[source_keys[2]] = input("enter datalake container value:")
    obj[source_keys[3]] = input("Enter source enabled: ")

    print("\n Enter entity values")

    entity_keys = list(obj["entities"])
    print(entity_keys)

    
    # obj["source_name"] = input("Enter source name : ")
    # obj["source_type"] = input("Enter source type : ")
    # obj["datalake_container"] = input("Enter datalake container")

    print(obj)


if choice  == 2:
    print("Create a new template")
if choice  == 3:
    print("Edit existing objects")

