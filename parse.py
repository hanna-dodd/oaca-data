import pandas as pd
import os
import xlrd

def parse_files():
    
    directory = 'data'
    df = pd.DataFrame({"id": [], "citations_wos": [], "citations_all": [], "open_access": [], "year": [], "language": []})
    
    for filename in os.listdir(directory):
        
        path = directory + "/" + filename
        wb = xlrd.open_workbook(path)
        sh = wb.sheet_by_index(0)
        
        id = ""
        citations_wos = ""
        citations_all = ""
        open_access = ""
        year = ""
        language = ""
        
        for rx in range(sh.nrows):
            
            id = sh.cell_value(rowx=rx,colx=70)
            citations_wos = sh.cell_value(rowx=rx,colx=33)
            citations_all = sh.cell_value(rowx=rx,colx=34)
            open_access = sh.cell_value(rowx=rx,colx=66)
            year = sh.cell_value(rowx=rx,colx=46)
            language = sh.cell_value(rowx=rx,colx=12)
            
            row = {"id": id, "citations_wos": citations_wos, "citations_all": citations_all, "open_access": open_access, "year": year, "language": language}
            df = df._append(row, ignore_index=True)
            
    print(df.head())
    csv = "wos.csv"
    df.to_csv(csv, index=False)

parse_files()