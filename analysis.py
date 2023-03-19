import pandas as pd

file_path = "data/API_SP.DYN.TFRT.IN_DS2_en_csv_v2_4901945/API_SP.DYN.TFRT.IN_DS2_en_csv_v2_4901945.csv"
df = pd.read_csv(file_path, index_col=0, skiprows=5)
rows, cols = df.shape
print(f"Created dataframe from csv: {rows} rows, {cols} cols.")

columns = [0]+list(range(4,36))
f_rates = df.iloc[:, columns]

print(f_rates)
