import pandas as pd
import numpy as np 

df = pd.read_excel("NYX TEST.xlsx", sheet_name ='test')
xls = pd.ExcelFile('NYX TEST.xlsx')

def clean_columns_test(df):
    df = df.dropna()
    df = df.replace('--','0')
    df = df.replace(',','')
    df = df.replace(r'[<%,]', '', regex=True)
    df.iloc[:, [14]] = df.iloc[:, [14]].astype(float)
    df[['Search impr. share', 'Search top IS','Avg. pos.']] = df[['Search impr. share',
                                                                  'Search top IS',
                                                                  'Avg. pos.']] .apply(pd.to_numeric, errors='coerce')
    return df
    
    def read_all_sheets(excel_files):
    sheet_to_df_map = {}
    for sheet_name in xls.sheet_names[-4:]:
        sheet_to_df_map[sheet_name] = xls.parse(sheet_name)
    return sheet_to_df_map
    
    
    all_sheets_dict = read_all_sheets(xls)
    
    
   creitoapicleaned_df= all_sheets_dict['CriteoAPI.Cleaned']
creitoapicleaned_df = creitoapicleaned_df.iloc[:,0:7]
creitoapicleaned_df = creitoapicleaned_df.dropna()
