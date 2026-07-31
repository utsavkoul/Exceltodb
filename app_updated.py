from flask import Flask, request, jsonify, render_template, send_from_directory


from files import readfile_write
import pandas as pd
import uuid
import os
import openpyxl
from sampledata import read_write

app = Flask(__name__, template_folder='templates')

# api
# webpage interface
# uploaad file
# download page
# analytic
# row id


@app.route("/", methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html', dictionary={})
#
@app.route('/data', methods=['GET','POST'])
def receive_data():
    if request.method == 'POST':
        datafile = request.files["file"]
        primary_key = request.form["primary_key"]
        column_name = request.form.get("column_name")


        dictionary, status = readfile_write(datafile,column_name,primary_key)
        filelist = os.listdir("./files")
        if status:
            return render_template("index.html", dictionary = dictionary or {})
        else:
            return render_template("index.html", message = "Please select .xlsx file")
        # filelist = os.path.

        # else:
        #     return render_template('index.html', message="Please select .xlsx file")
        # readfile_write(datafile)  # Call the function to process the received data
    # Append the content to the file
    # Process the received data


@app.route("/add-data", methods=["GET","POST"])
def add_data():
        data = request.json['data']
        print("Add_Data")
        print("Adding Data")
        print("data",data)
        # if os.
        filename = read_write(data)
        print(filename)
        return render_template("download.html", filelist = filename )
    # else:
    #
    #     return render_template("download.html", filename=filename)
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    if request.method == 'GET':
        return send_from_directory('./output', filename, download_name="output.xslx")
if __name__ == '__main__':
    app.run(debug=True)