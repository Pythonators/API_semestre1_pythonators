import pandas as pd
df_json = pd.read_json('Avaliacao.json')
df_json.to_excel('Pasta1.xlsx')