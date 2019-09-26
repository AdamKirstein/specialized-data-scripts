import pandas as pd 
import numpy as np 
from openpyxl import load_workbook


#get col names and add to empty df 
def get_columns(emptycol):
    #search in list for "empty df"
    emptycol =  [i for i in data if len(i)==0]
    # assign column names to object
    emptycol= keys
    #make the empty dataframe into a dataframe from list
    emptycol = pd.DataFrame(emptycol)
    # column names get put into rows, so need to transpose to make them columns
    emptycol = emptycol.T
    # extract the values and make them columns
    emptycol.columns = emptycol.values[0]
    emptycol = emptycol.reset_index(drop = True)
    # assign the row values to nan
    emptycol[emptycol.notna()] = np.nan
    # remove those nan values to be left with just column names
    emptycol.dropna(inplace=True)
    return emptycol
    
    
    
  def update_sheet(i, emptycol):
    book = load_workbook('testbook.xlsx')
    writer = pd.ExcelWriter('testbook.xlsx', engine='openpyxl') 
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    emptycol.reset_index(drop=True)
    emptycol.to_excel(writer,sheet_name = i, index=False)
    writer.save()


xls = pd.ExcelFile('testbook.xlsx')

# all sheets in wkbk
sheets = xls.sheet_names
emptycol = []
datalist = []

for i in sheets:
    #this one is used for extracting the sheet name 
    data= xls.parse(i)
    #this one to get list of all the data in workbook
    datalist.append(xls.parse(i))
    #get the column names
    keys=datalist[0].keys()
    keys = list(keys)
    #assign columns
    emptycol = get_columns(emptycol)
    #applying logic to data to find the empty sheet, if found bring columns to blank 
    if data.columns.empty: 
        update_sheet(i, emptycol)
        break
