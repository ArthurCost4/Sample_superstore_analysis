import pandas as pd
from pathlib import Path

pasta_atual = Path(__file__).resolve().parent
caminho_arquivo = pasta_atual.parent / 'raw' / 'sample_-_superstore.xls'

# Você pode até definir o índice direto na leitura:
df = pd.read_excel(caminho_arquivo, index_col='Order ID')

print(df.head())
print(df.info())