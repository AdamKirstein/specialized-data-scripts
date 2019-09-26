import pandas as pd 
import numpy as np 


def create_column_list_pairs(columns_to_change, new_columns):
    old_columns = columns_to_change
    new_columns = new_columns
    dictionary = dict(zip(old_columns, new_columns))  
    df_output = columns_to_change.rename(columns = dictionary)
    for i in df.columns:
        if i not in dictionary.keys():
            print("the following columns are no longer present in the dataframe : {}".format(i))
    return df_output


def reorder_columns(df_output, order_list):
    desired_order_list = order_list
    reordered = {k: df_output.columns[k] for k in desired_order_list}
    reordered = list(reordered.values())
    df_output = df_output[reordered]
    return df_output

def calculate_weights(df_output, columns_to_weight,weight):
    columns_to_weight = columns_to_weight
    weight = weight
    col_to_weight = df_output.loc[:, df_output.columns.str.contains('|'.join(columns_to_weight))]
    weight = df_output.loc[:, df_output.columns.str.contains('|'.join(weight))]

    for column in col_to_weight:
        for j in weight: 
            df_output['weighted_'+'{}'.format(column)] = np.array(col_to_weight[column]) * weight[j]
    return df_output
    
    df = pd.read_csv("test1.csv")
# specify column names. these can be any columns you want to have reformatted. 
# note: any column in a dateframe not added here will not be included in the output.  a print will show which are 
# excluded 
columns_to_change = df[df.columns[0:3]]
# give names to new columns here. Length here must equate to the amount of columns specified above 
new_columns = ['col1 new name', 'col 2 new name', 'col 3 new name']
# apply function to rename and filter columns
new_df = create_column_list_pairs(columns_to_change, new_columns)


# provid the order you want the columns to be reformatted. 
# note they are going by index which for python is 0 index. So the first column is 0. 
# if i want to completely reverse the order of my columns that go [1,2,3,4,5,6]
# i would specify my order [5,4,3,2,1,0]
# the amount of indices must match the number of columns you specified 
order_list =[1,0,2]
# apply reformat function 
new_df=reorder_columns(new_df, order_list)

columns_to_weight=['col 2 new name', 'col1 new name']
weight = ['col 3 new name']
new_df = calculate_weights(new_df,columns_to_weight,weight)
