from flask import Flask, request, jsonify
from files import readfile_write
app = Flask(__name__)


@app.route('/data', methods=['POST'])
def receive_data(fileslist=None):
    datafile = request.get_json()
    for data in datafile:
        fileslist.append(data.filepath)
    readfile_write(fileslist)  # Call the function to process the received data

    # Append the content to the file
    # Process the received data
    return jsonify({"message": "Data received successfully", "received_data": datafile})


if __name__ == '__main__':
    app.run(debug=True)