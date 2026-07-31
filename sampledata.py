import os
from functools import reduce

# from itertools import count
#
#
import pandas as pd
# from pandas.core.interchange import column

from database import insert_data, get_data
#
# # df1 = pd.read_excel("./sample/customers.xlsx")
# # print(df1)
# # df2 = pd.read_excel("./sample/order_items.xlsx")
# # print(df2)
# # df3 = pd.read_excel("./sample/orders.xlsx")
# # print(df3)
# # df4 = pd.read_excel("./sample/products.xlsx")
# # print(df4)
#
# # insert_data(df1, "customers")
# # insert_data(df2, "order_items")
# # insert_data(df3, "orders")
# #
# # insert_data(df4, "products")
#
def read_write(data):
    # list = os.listdir(os.path.join("./sample"))
    dic = {

    }
    count = 0
    # with os.scandir("./files") as entries:
    #     for file in entries:
    #         dic["df"+str(count)] = pd.read_excel(file)
    #         count = count + 1
    arr = data
    print(arr)
    # arr =[('./files/customers.xlsx', 'customer_id', 'customer_id'), ('./files/orders.xlsx', 'customer_id', 'order_id'), ('./files/order_items.xlsx', 'order_id', 'product_id'), ('./files/products.xlsx', 'product_id', 'product_id')]
    merge =[]
    for file in arr.values():
        dic['df'+str(count)] = [pd.read_excel(file[0]), file[1], file[2]]
        count +=1
    # dic = arr

    # print(dic)
    main_data = dic['df0']
    merge_df = {0:main_data[0]}
    # print(main_data)
    count = 0
    for value in dic.keys():
        print(value)
        merge_df[0] = merge_df[0].merge(dic[value][0], left_on=main_data[2], right_on=dic[value][1], how="outer", suffixes=("_x", "_y"))
        # merge_df[0].set_index('customer_id', inplace=True)
        merge_df[0].rename(columns={'Unnamed: 0': 'new_index_name_'+str(count)}, inplace=True)

        # merge.append(merge_df)

        # main_data[0] = merge_df
        # main_data[1] = dic['df1'][2]
        # main_data[2] = dic['df1'][2]

    pd.set_option('display.max_columns', 20)
    print(merge_df)


#     list = [dic['df0'],dic['df1']]
#     print('Data \n',dic.values())
#     df = reduce(lambda left, right : pd.merge(left[0][0], right[0][0], left_on=left[0][2], right_on=right[0][1] ,how='outer'), dic.values())
#     print("dataframe \n",df)
# #
#
#     # dic={
#     #     'df0': pd.read_excel("./sample/customers.xlsx"),
#     #     'df1': pd.read_excel("./sample/orders.xlsx"),
#     #     'df2': pd.read_excel("./sample/order_items.xlsx"),
#     #     'df3': pd.read_excel("./sample/products.xlsx"),
#     #     'df4': pd.read_excel("./sample/order_remarks.xlsx"),
#     # }
#     # dic = read_write()
#     # df_merge = dic["df0"].merge(dic["df1"], left_on='customer_id', right_on='customer_id', how='outer')
#     #
#     # # print("Data frame",df_merge)
#     #
#     # df_merge1 = df_merge.merge(dic["df2"], left_on='order_id', right_on='order_id', how='outer')
#     # pd.set_option('display.max_columns', 10)
#     # # print("Data frame 1",df_merge1)
#     #
#     # df_merge2 = df_merge1.merge(dic["df3"], left_on='product_id', right_on='product_id', how='outer')
#     # # print("Data frame 2", df_merge2)
#     # df_merge3 = df_merge2.merge(dic["df4"], left_on=['customer_id','order_id'], right_on=['customer_id','order_id'], how='outer')
#     # # print(df_merge3.groupby('customer_id').head())
#     # dic_name = dic['df0'].to_dict()
#     # # print(dic_name)
#     # dic_name = {'cus_name': {1: 'Alice', 2: 'Bob', 3: 'Charlie', 4: 'Diana', 5: 'Ethan', 6: 'Fiona'},
#     #             'city':{1: 'New York', 2: 'Chicago', 3: 'Dallas', 4: 'Seattle', 5: 'Boston', 6: 'Miami'}}
#     # # print(dic_name)
#     # df_merge3['customer_name'] = df_merge3['customer_id'].map(dic_name['cus_name'])
#     # df_merge3['city'] = df_merge3['customer_id'].map(dic_name['city'])
#     # # df_merge3.set_index('customer_name')
#     # # print(df_merge3)
#     # # df_merge4 = df_merge3
#     # # df_merge5 = df_merge4.reset_index()
#     # # print(df_merge3.to_string(index=False))
#     # # df_merge5 = df_merge3.to_string(index=False)
#     # # print(df_merge3)
#     # # print(df_merge3.drop( columns=df_merge3.iloc[]))
#     # df_merge4 = df_merge3.drop_duplicates()
#     # # print(df_merge3)
#
#     # index = df_merge3['customer_id, customer_name,      city,  order_id,  order_date,  product_id, quantity, product_name,     category,                  remarks ']
    df_cleaned = merge_df[0].loc[:, ~merge_df[0].columns.duplicated()]
    filename = "output.xlsx"
#     # pr
    df_cleaned.drop_duplicates()
    df_cleaned.to_excel(os.path.join("./output/",filename), index=False)
    insert_data(df_cleaned, "Full Table 6")
    return filename
#
# read_write(data)
# # print(read_write())
#
# #
# # df = pd.read_excel("./sample/order_remarks.xlsx")
# # print(df.head())
# # insert_data(df, "order_remarks")
# # print(read_write())
# # insert_data(df_merge2, "Merged Table pd")