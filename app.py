from flask import Flask, request,jsonify
import json

app = Flask(__name__)

@app.route('/postJSON', methods = ["POST"])
def receive_json():
     # Get the JSON object from the request
    json_object = request.json

    # Load the existing JSON data from the file
    with open('config1.json', 'r') as file:
        existing_data = json.load(file)

    # Add the new JSON object to the list
    existing_data.append(json_object)

    # Write the updated JSON data back to the file
    with open('config1.json', 'w') as file:
        json.dump(existing_data, file, indent=4)

    return jsonify({'message': 'JSON object added successfully'})


@app.route('/send_entity/<source_name>/<id>', methods = ["GET"])

def send_entity(source_name,id):
    req_data = None
    with open("config1.json","r") as file:
        data = json.load(file)
        for i in range(len(data)):
            if data[i]["source_name"] == source_name:
                for j in range(len(data[i]["entities"])):   
                    if int(data[i]["entities"][j]["id"]) == int(id):
                        req_data = data[i]["entities"][j]
                        break
                break
    if req_data is not None:
        return req_data
    else:
        return "Entity not found"
   


if  __name__ == "__main__":
    app.run()


