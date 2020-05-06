import pandas as pd
def set_opt_expand():
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

def lista_columns():
    filename="/home/tomy/MEGAsync/Programming/Crimes_-_2001_to_present.csv"
    lista=[]
    for chunk in pd.read_csv(filename, chunksize=10):
        for ele in chunk.columns:
            lista.append(ele)
        return lista
        break

print(lista_columns())

# print(lista_columns())