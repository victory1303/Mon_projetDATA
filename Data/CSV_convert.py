import pandas as pd
#lecture du fichier excel
df = pd.read_excel('data_DSE_mpox_week47 2._ange.xlsx',engine='openpyxl')
#sauvegarder en tant que CSV
df.to_csv('data_DSE_mpox_week47 2._ange.csv', index=False,  sep=',')