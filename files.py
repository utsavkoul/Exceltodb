import pandas as pd
from pathlib import Path
import os
from database import insert_data
import uuid
def readfile_write(file):
    # for file in files:
        if file.filename.endswith(".xlsx"):

            df = pd.read_excel(file)
            print(file.filename)
            if os.path.exists("./files") == False:
                os.mkdir("./files")
            # filename = f'{uuid.uuid4()}.xlsx'
            df.to_excel(os.path.join("./files/",file.filename))
            # file.save(os.path.join("./files"))
            return True
        elif file.filename.endswith(".csv"):
            df = pd.read_csv(file)
            if os.path.exists("./files") == False:
                os.mkdir("./files")
            filename = f'{file.filename}.xlsx'
            df.to_excel(os.path.join("./files/", filename))
            return True
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
