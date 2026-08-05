from flask import Flask, request, jsonify, render_template, send_from_directory, Response, redirect, url_for, send_file

from files import readfile_write, create_first_output
import pandas as pd
import uuid
import os
import openpyxl
from sampledata import read_write
from files import merge_file
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

# api
# webpage interface
# uploaad file  *
# download page *
# analytic
# row id *
# Check json values according to columns and rows
# Remove extra unnamed indexes

@app.route("/", methods=['GET'])
def index():
    if request.method == 'GET':
        # get data for merged table
        # Gwt data m db
        if os.path.isfile("./output/output.xlsx") == False:
            create_first_output()
        merge_table_df = pd.read_excel(os.path.join("./output", "output.xlsx"))
        merge_table_df = merge_table_df.to_dict()
        return render_template('indexlayout.html', merge_table_df=merge_table_df, new_table_df={})
# Add the column wise table view for each file
@app.route('/data', methods=['GET','POST'])
def receive_data():
    if request.method == 'POST':
        datafile = request.files["file"]
        # primary_key = request.form.get("primary_key")
        # column_name = request.form.get("column_name")

        #Return All column names or table view
        #Upload a file and Create the merged table when the button is clicked
        # merged_df, filename, status = readfile_write(datafile)
        # merged_df_columns = merged_df.columns.tolist()
        #Create output file when call the merge for the first time

        new_table_df, status = readfile_write(datafile)
        # new_table_df = pd.read_excel(datafile)
        new_table = new_table_df.columns.tolist()
        print("New Table Columns",new_table)
        table_json = new_table_df.to_dict()
        print("New table json",table_json)
        merge_table_df = pd.read_excel(os.path.join("./output", "output.xlsx"))
        merge_table_columns = merge_table_df.columns.tolist()
        print("Merged Table Columns",merge_table_columns)
        # status = True
        # second time return columns of the previous merged table and new table
        if status:
            return render_template("indexlayout.html", new_table = new_table or {}, new_table_df=table_json, merged_table_columns=merge_table_columns, merge_table_df=merge_table_df.to_dict())
        else:
            return render_template("indexlayout.html", message = "Please select .xlsx file")
        # filelist = os.path.

        # else:
        #     return render_template('index.html', message="Please select .xlsx file")
        # readfile_write(datafile)  # Call the function to process the received data
    # Append the content to the file
    # Process the received data

#Merge files when add button clicked on the html page
@app.route("/merge-data", methods=["GET","POST"])
def merge_data():
    # if request.method == 'POST':
        # data = request.json['data']
        # print("Add_Data")
        # print("Adding Data")
        # print("data",data)
        # # if os.
        # filename = read_write(data)
        # print(filename)
        #
        new_table = ''
        columns_new = request.json['columns_new']
        columns_merge = request.json['columns_merge']
        new_table = request.json['new_table']
        # # merged_table = request.json['merged_table']
        data = request.json
        print("Request values",columns_new, columns_merge,new_table)
        # # new_table = pd.read_excel('./files/products.xlsx')
        # # new_table = new_table.drop(columns=['Unnamed: 0'])
        # # Convert df to file
        # new_table_file = new_table.to_excel("./files")
        columns = [[columns_new],[columns_merge]]
        merged_df, filename = merge_file(new_table, columns)
        #Save Excel file when merged to download
        # merged_df = pd.read_excel("./files/products.xlsx")
        response = Response(
            merged_df.to_json(),
            mimetype='application/json',
            headers={"Content-Disposition": "attachment;filename='output.json"}

        )
        # return render_template('indexlayout.html', merged_df=merged_df, filename=filename or {})
        return response


        # return render_template("download.html", filelist = filename )


# @app.route("/add-data", methods=["GET"])
# def add_data():
#         # data = request.json['data']
#         # print("Add_Data")
#         # print("Adding Data")
#         # print("data",data)
#         # # if os.
#         # filename = read_write(data)
#         # print(filename)
#         return redirect(url_for("download_output_file"))
# Can return Json response
# @app.route('/download/<filename>', methods=['GET'])
# def download_file(filename):
#     if request.method == 'GET':
#         return send_from_directory('./output', filename, download_name="output.xslx")@app.route('/download/<filename>', methods=['GET'])

@app.route('/download', methods=['GET'])
def download_output_file():
    if request.method == 'GET':
        return send_from_directory('./output', 'output.xlsx', download_name="output.xslx")
if __name__ == '__main__':
    app.run(debug=True)