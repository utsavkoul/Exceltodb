import os
from itertools import count

import pandas as pd

from database import insert_data

# df1 = pd.read_excel("./sample/customers.xlsx")
# print(df1)
# df2 = pd.read_excel("./sample/order_items.xlsx")
# print(df2)
# df3 = pd.read_excel("./sample/orders.xlsx")
# print(df3)
# df4 = pd.read_excel("./sample/products.xlsx")
# print(df4)

# insert_data(df1, "customers")
# insert_data(df2, "order_items")
# insert_data(df3, "orders")
#
# insert_data(df4, "products")

def read_write():
    # list = os.listdir(os.path.join("./sample"))
    dic = {}
    count = 0
    with os.scandir("./sample") as entries:
        for file in entries:
            dic["df"+str(count)] = pd.read_excel(file)
            count = count + 1





    dic = read_write()
    df_merge = dic["df0"].merge(dic["df1"], left_on='customer_id', right_on='customer_id', how='outer')

    # print("Data frame",df_merge)

    df_merge1 = df_merge.merge(dic["df2"], left_on='order_id', right_on='order_id', how='outer')
    pd.set_option('display.max_columns', 10)
    # print("Data frame 1",df_merge1)

    df_merge2 = df_merge1.merge(dic["df3"], left_on='product_id', right_on='product_id', how='outer')
    # print("Data frame 2", df_merge2)
    filename = "output.xlsx"
    df_merge2.to_excel(filename)
    insert_data(df_merge2, "Full Table")
    return filename


# insert_data(df_merge2, "Merged Table pd")