#Codigo para hacer un heatmap en el que el eje x es posicion y el y los 20 tipos de aa. Se necesita una columna con el deltadeltaG para colorear


def heatmap(metodos,guardar,titulo,nombre):
    result=df.pivot(index="aa",columns="n",values=metodos)
    result = result.sort_index(axis=0)  # Ordenar índices del resultado
    result = result.sort_index(axis=1)  # Ordenar columnas del resultado
    
    fig, ax = plt.subplots(figsize=(60,7)) 
   
    colores=["#2902D7","#9481EB","#CAC0F5","#EA8080","#D40000"]
    heatmap=sns.heatmap(result,ax=ax,cmap=colores, center=0,vmin=-4,vmax=4,linewidths=.6,linecolor="white",cbar_kws={"orientation": "vertical", "pad": 0.02,'ticks': [-4,-2,0, 2, 4]})
    mut=df["aa"].tolist()
    aa=df["aa"].unique().tolist()
    aa.sort()
    wt=df["wt"].tolist()
    n=df["n"].tolist()
    
            # Agregar rectángulo con la posición y color especificados
    for i in range(len(mut)):
        if mut[i]==wt[i]:
            y=aa.index(wt[i])
            coord=(n[i]-9,y)

            rect = Rectangle(coord, 1, 1, fill=False, edgecolor='yellow', lw=2)
            ax.add_patch(rect)
                
    ax.tick_params(axis='both', which='both', labelsize=20)
    ax.set_xlabel("", fontsize=16)  # Tamaño del título del eje x
    ax.set_ylabel("Aminoácido", fontsize=20)  
    heatmap.tick_params(right=True,left=True, labelright=True, rotation=0)

    cbar = heatmap.collections[0].colorbar
    cbar.ax.tick_params(labelsize=16)
    plt.xticks(rotation=90)
    plt.yticks(rotation=0)
    # Agregar título a la barra de valores
    cbar.set_label("ΔΔG\ (kcal/mol)", fontsize=20)
    heatmap.set_title(titulo, fontsize=20)
    if guardar:
        plt.savefig(nombre, transparent=True,bbox_inches='tight')
    plt.show()
