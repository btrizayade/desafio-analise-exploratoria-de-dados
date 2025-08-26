import pandas as pd

# carregar a base de dados
df = pd.read_csv("desafio1/netflix daily top 10.csv")

# 1. tipos de dados disponíveis
print("\ndados disponíveis:")
print(df.dtypes)

# 2. período da análise feita
print("\nperíodo da análise feita:")
if "As of" in df.columns:
    df["As of"] = pd.to_datetime(df["As of"], errors="coerce")
    print("início:", df["As of"].min())
    print("fim:", df["As of"].max())
else:
    print("nenhuma coluna de data encontrada.")

# 3. tamanho da base de dados
print("\ntamanho da base de dados:")
print("n° linhas:", df.shape[0])
print("n° colunas:", df.shape[1])

# 4. verificar dados nulos
print("\nvalores nulos por coluna:")
print(df.isnull().sum())

# 5. outliers (IQR)
print("\noutliers:")
for col in df.select_dtypes(include=['int64','float64']).columns:
    q1, q3 = df[col].quantile([0.25, 0.75])
    iqr = q3 - q1
    li, ls = q1 - 1.5*iqr, q3 + 1.5*iqr
    outliers = df[(df[col] < li) | (df[col] > ls)]
    print(f"outliers={len(outliers)}")
