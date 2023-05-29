import json



def hello(source,id):
    with open("config1.json","r") as file:
        data = json.load(file)
        for i in range(len(data)):
            print("hi")
            if data[i]["source_name"] == source:
                print("hello")
                for j in range(len(data[i]["entities"])):   
                    print("ssup")
                    if int(data[i]["entities"][j]["id"]) == id:
                        print(data[i]["entities"][j])
                        break
            break


hello('sharepoint_source',1)