#codigo para hacer un scatterplot. ojo con las opciones

def plot_scatter_e(nombre, etiquetas, save, netiquetas,general, *x):    
    fig, ax = plt.subplots(figsize=(20, 6))
    colors = ["black", "red","blue","black","black"]
    facecolors = ["none", "red","blue","orange","none"]
    marker=[".",".",".",".","d"]
    col=["effect_prediction_independent_x","effect_prediction_independent_y","effect_prediction_independent","prom_est","ddg foldx alphafold"]
    for i in range(0, len(x), 3):
        if x[i].name==col[0] or x[i].name==col[1] or x[i].name==col[2]:
            xlabel="Ev Independent"
        elif x[i].name==col[3]:
            xlabel="Promedio Estructurales"
        elif x[i].name==col[4]:
            xlabel="Foldx"
        if x[i+1].name==col[0] or x[i+1].name==col[1] or x[i+1].name==col[2]:
            ylabel="Ev Independent"
        elif x[i+1].name==col[3]:
            ylabel="Promedio Estructurales"
        elif x[i+1].name==col[4]:
            ylabel="Foldx"
        if general:
            xlabel="Metodos estructurales"
            ylabel="Metodos secuencia"
            if x[i].name=="ddG Fireprot":
                xlabel="Experimental"
                ylabel="Promedio Predicho"
            elif x[i].name=="mutantes":
                xlabel="mutantes"
                ylabel="Promedio Predicho"
                lineas=np.arange(0,len(x[1]))
                for xc in lineas:
                    plt.axvline(x=xc,color="black",alpha=0.3,linestyle='dotted')
            
    
        ax.scatter(x[i], x[i+1], facecolors=facecolors[i//3], edgecolors=colors[i//3],s=80,label=x[i+2],marker=marker[i//3])

        ax.set_ylabel(f'{ylabel}\n$\\bf{{ΔΔG\ (kcal/mol)}}$', color="black", fontsize=12)
        ax.set_xlabel(f'$\\bf{{ΔΔG\ (kcal/mol)}}$\n{xlabel}', color="black", fontsize=12)
        ax.set_xlabel("Mutantes", color="black", fontsize=12)
        if etiquetas:
            for j, e in enumerate(netiquetas):
                color = colors[i//2] if len(x) > 2 else "black"  # Color negro cuando len(x) < 2 y etiquetas es verdadero
                plt.text(x[i].iloc[j], x[i+1].iloc[j], netiquetas.iloc[j], color=color, fontsize=9)

    if etiquetas and len(x) > 3:
        if x[1].name=="prom_est":
            ylabel="Promedio Estructurales"
        ax2 = ax.twinx()
        ax2.set_ylabel(f'$\\bf{{ΔΔG\ (kcal/mol)}}$\n{ylabel}', color=colors[0], fontsize=12)
    plt.xticks(rotation=90)
    plt.legend()
    if save:
        plt.savefig(nombre, transparent=True, bbox_inches='tight', dpi=1000)
    
    plt.show()
    
