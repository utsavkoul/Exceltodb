import pandas as pd
from pathlib import Path
import os
from database import insert_data
import uuid
from database import insert_dictionary

dictionary = {
            'fe298e06-1ccc-4a47-8f35-9c99a3518ece': {'./files/orders.xlsx':'orders_id'},
        }
def readfile_write(file, column_name, primary_key, dictionary=dictionary):
    # for file in files:
        count = 0


        if file.filename.endswith(".xlsx"):

            df = pd.read_excel(file)
            print(file.filename)
            if os.path.exists("./files") == False:
                os.mkdir("./files")
            # filename = f'{uuid.uuid4()}.xlsx'
            df.to_excel(os.path.join("./files/",file.filename))
            # file.save(os.path.join("./files"))
            # dictionary["file2"] ={os.path.join("./files/", file.filename): column_name}
            files = insert_dictionary([os.path.join("./files/", file.filename), column_name, primary_key])
            print(files)

            return files, True
        elif file.filename.endswith(".csv"):
            df = pd.read_csv(file)
            if os.path.exists("./files") == False:
                os.mkdir("./files")
            filename = f'{file.filename}.xlsx'
            df.to_excel(os.path.join("./files/", filename))
            # dictionary[str(uuid.uuid4())] = [os.path.join("./files/", file.filename), column_name]
            files = insert_dictionary([os.path.join("./files/", file.filename), column_name, primary_key])

            return files, True
        else:
            # raise ValueError("Unsupported file format. Please provide a .xlsx or .csv file.")
            return False



# def writefile(data):
#     file_path = os.path.join("C:\\Users\\hyped\\OneDrive\\Documents\\Excettodb\\", "output.xlsx")
#
#     if os.path.isfile(file_path):
#         # File exists — append with overlay
#         with pd.ExcelWriter(file_path, mode="a", if_sheet_exists='overlay', engine="openpyxl") as file:
#             start_row = file.sheets["Sheet1"].max_row
#             data.to_excel(file, sheet_name="Sheet1", startrow=start_row, header=False, index=False)
#     else:
#         # File doesn't exist — create new
#         with pd.ExcelWriter(file_path, mode="w", engine="openpyxl") as file:
#             data.to_excel(file, index=False)
#
#
#     with open(file_path, 'r') as file:
#         df = pd.read_excel(file_path)
#         insert_data(df)  # Call the function to insert data into the database
#

# listoffiles = ["savefiles/Copy of Vrinda Store Data Analysis.xlsx",
#                "savefiles/Sales.csv"]

# readfile_write(listoffiles)
