from flask import Flask, request, jsonify, render_template, send_from_directory

import sampledata
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
        return render_template('index.html')
#
@app.route('/data', methods=['GET','POST'])
def receive_data():
    if request.method == 'POST':
        datafile = request.files["file"]

        readfile_write(datafile)
        filelist = os.listdir(os.path.join("./files"))
        return render_template("index.html", filelist = filelist)
        # filelist = os.path.

        # else:
        #     return render_template('index.html', message="Please select .xlsx file")
        # readfile_write(datafile)  # Call the function to process the received data
    # Append the content to the file
    # Process the received data


@app.route("/add-data", methods=["GET","POST"])
def add_data():
    filename = read_write()
    return render_template("index.html", filelist = filename)
    # return render_template("download.html", filename=filename)
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    if request.method == 'GET':
        return send_from_directory('./output', filename, download_name="output.xslx")
if __name__ == '__main__':
    app.run(debug=True)