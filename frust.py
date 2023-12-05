#Voy a calcular el zscore de cada posicion para relacionar con la frustracion.
def frust(df,metodo):
    n=df["n"].unique().tolist()
    for i in range(len(n)):
        df_c=df[df["n"]==n[i]]
        prom=df_c[metodo].mean()
        sd=df_c[metodo].std()
        zscore=(df_c[metodo]-prom)/sd
        df.loc[df["n"] == n[i], "zscore"] = zscore.tolist()
    zscore=df[df["aa"]==df["wt"]]
    zscore["zscore"].to_csv("/home/solcanale/calculos nuevos con alphafold/Noviembre 2023/frustracion/"+metodo+"_frust.txt",sep="\t",index=False,header=None)
