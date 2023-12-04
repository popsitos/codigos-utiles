def boxplot(data,save,name):
    names = ["Foldx\nEpistatic", "Foldx\nIndependent","Promedio estructural\nEpistatic", "Promedio estructural\nIndependent"]
    #names = ["Foldx\nIndependent","Promedio estructural\nEpistatic", "Promedio estructural\nIndependent"]

    fig, ax = plt.subplots(figsize=(12, 7))
    
    
    # Crear el boxplot
    bp = ax.boxplot(data)
    
    # Crear un arreglo de valores x dispersos
    num_datasets = len(data)
    
    x_values = np.arange(1, num_datasets + 1)
    
    # Agregar puntos para los datos con dispersión en x
    for i, dataset in enumerate(data):
        x_scatter = x_values[i] + np.random.normal(0, 0.04, len(dataset))  # Introducir dispersión en x
        ax.scatter(x_scatter, dataset, color='red', marker='.', s=10)
    # Configuración de etiquetas y título
    ax.set_xticks(x_values)
    
    ax.set_xticklabels(names,fontsize=14)
    
    ax.set_ylabel('$\\bf{ΔΔG\ (kcal/mol)}$\nPromedio predicho',fontsize=14)
    ax.set_title("ind per>80")
    if save:
        plt.savefig(name, transparent=True,bbox_inches='tight',dpi=1000)
    plt.show()
