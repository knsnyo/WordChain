import pandas as pd
from glob import glob
import re

def write(before):
    p = re.compile("[^0-9]")
    if before is not None:
        before = before.replace("-", "")
        before = before.replace("^", "")
        after = before.replace(":", "")
        after = "".join(p.findall(after))
        return after

files = glob('전체 내려받기_우리말샘_xls_20211102/*.xls')

df = pd.DataFrame()
for file in files:
    data = pd.read_excel(file, sheet_name = 'Sheet0')
    df = df.append(data)

new_data = df[['어휘', '품사']]
new_data = new_data[new_data['품사']=='명사']
new_data['어휘'] = new_data['어휘'].apply(write)
new_data.to_csv('noun_dictionary.csv', index=False)