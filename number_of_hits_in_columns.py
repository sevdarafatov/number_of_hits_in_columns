import pandas as pd
df = pd.read_csv(r'deneme_excel.csv', sep=';')
df
df["prot_coords"].value_counts()
hits=len(df)-256973
hits
