"""
Created on Thu Jan  4 14:14:40 2024

@author: solcanale
"""
from sklearn.ensemble import GradientBoostingClassifier
from datos_normalizados import df_t,df_g
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

df_2=df_t[df_t["Unnamed: 0"] == 'csp'] 
df_t=df_t[df_t["Unnamed: 0"] != 'csp'] 

features=df_t[["ddG foldx","effect_prediction_epistatic"]]
labels=(df_t["ddG Fireprot"]> 0).astype(int)


# Seleccionar el número de folds para la validación cruzada
n_splits = 4
kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)

# Inicializar listas para almacenar las métricas de cada fold
all_accuracy_scores = []
all_precision_scores = []
all_recall_scores = []
all_f1_scores = []
all_confusion_matrices = []
# Iterar sobre los folds
for train_index, test_index in kf.split(features):
    X_train, X_test = features.iloc[train_index], features.iloc[test_index]
    y_train, y_test = labels.iloc[train_index], labels.iloc[test_index]

    # Inicializar y entrenar el modelo LogisticRegression
    # model = RandomForestClassifier(random_state=15)
    model=GradientBoostingClassifier(random_state=15) ## con este modelo anda mejor
    model.fit(X_train, y_train)

    # Establecer el umbral de decisión (ajusta según tus necesidades)
    threshold = 0.95

    # Hacer predicciones en el conjunto de prueba
    predictions = (model.predict_proba(X_test)[:, 1] > threshold).astype(int)

    # Calcular y almacenar métricas para este fold
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

    all_accuracy_scores.append(accuracy)
    all_precision_scores.append(precision)
    all_recall_scores.append(recall)
    all_f1_scores.append(f1)
    
    y_pred = model.predict(X_test)
    # Calcular la matriz de confusión para este fold
    cm = confusion_matrix(y_test, y_pred)

    # Almacenar la matriz de confusión en la lista
    all_confusion_matrices.append(cm)

# Calcular la matriz de confusión promedio sobre todos los folds
average_confusion_matrix = np.mean(all_confusion_matrices, axis=0)

# Imprimir la matriz de confusión promedio
print("Average Confusion Matrix:")
print(average_confusion_matrix)
# [[TN, FP]
#  [FN, TP]]

# Calcular y mostrar las métricas globales
global_accuracy = sum(all_accuracy_scores) / n_splits
global_precision = sum(all_precision_scores) / n_splits
global_recall = sum(all_recall_scores) / n_splits
global_f1 = sum(all_f1_scores) / n_splits

print(f"Global Accuracy: {global_accuracy}")
print(f"Global Precision: {global_precision}")
print(f"Global Recall: {global_recall}")
print(f"Global F1 Score: {global_f1}")

###pruebo el modelo con la proteina que saque 
#### da 1 la precision
X_pred=df_2[["ddG foldx","effect_prediction_epistatic"]]
y_test=(df_2["ddG Fireprot"]> 0).astype(int)
predictions_model = model.predict(X_pred)
predictions_model_adjusted = (model.predict_proba(X_pred)[:, 1] > .95).astype(int)
df_2['foldx_epis'] = predictions_model_adjusted
cm = confusion_matrix(y_test, predictions_model_adjusted)
print(cm,precision_score(y_test, predictions_model_adjusted))


#pruebo con gh10
df_g["ddG foldx"]=df_g["ddg foldx alphafold"]
X_pred=df_g[["ddG foldx","effect_prediction_epistatic"]]
predictions_model = model.predict(X_pred)

# predictions_model3 = model3.predict(X_pred.iloc[:,[0,2]])

df_g['foldx_epis'] = predictions_model
# Ajustar el umbral para el modelo 1
threshold_model = 0.95 # Ajusta el umbral según tus necesidades
predictions_model_adjusted = (model.predict_proba(X_pred)[:, 1] > threshold_model).astype(int)


# Agregar las predicciones ajustadas al DataFrame original
df_g['foldx_epis_adjusted'] = predictions_model_adjusted
# df_g['foldx_ind_adjusted'] = predictions_model3_adjusted
h=df_g[["ddG foldx","effect_prediction_epistatic","mutant","foldx_epis_adjusted"]]
h = h[h['mutant'].apply(lambda x: x[0] != x[-1])]
print(sum(h["foldx_epis_adjusted"]))
# esto da muy bien. dan las mutaciones que obtuve antes y algunas mas 


####PARA VER QUE KFOLD ES MEJOR

# Seleccionar el número de folds para la validación cruzada
n_splits = 4
kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)

# Inicializar variables para el seguimiento del mejor modelo
best_precision = 0
best_model = None
best_confusion_matrix = None
best_fold_indices = None
best_ytrain=None
# Iterar sobre los folds
for fold_num, (train_index, test_index) in enumerate(kf.split(features), 1):
    X_train, X_test = features.iloc[train_index], features.iloc[test_index]
    y_train, y_test = labels.iloc[train_index], labels.iloc[test_index]

    # Inicializar y entrenar el modelo GradientBoostingClassifier
    model = GradientBoostingClassifier(random_state=15)
    model.fit(X_train, y_train)

    # Establecer el umbral de decisión (ajustar según tus necesidades)
    threshold = 0.9

    # Hacer predicciones en el conjunto de prueba
    predictions = (model.predict_proba(X_test)[:, 1] > threshold).astype(int)

    # Calcular precisión para este fold
    precision = precision_score(y_test, predictions)

    # Actualizar el mejor modelo si se encuentra una precisión mayor
    if precision > best_precision:
        best_precision = precision
        best_model = model
        best_confusion_matrix = confusion_matrix(y_test, predictions)
        best_fold_indices = test_index
        best_ytrain= predictions
# Imprimir la precisión del mejor modelo
print("Best Precision:", best_precision)



# Proyectar el mejor modelo en tus datos
X_best_fold = features.iloc[best_fold_indices]
y_best_fold = df_t["ddG Fireprot"].iloc[best_fold_indices]
best_fold_data = pd.concat([X_best_fold, y_best_fold], axis=1)
# Obtener la columna "mutant" del DataFrame original df_t para el mejor fold
mutant_column_best_fold = df_t["mutant"].iloc[best_fold_indices]
prot = df_t["Unnamed: 0"].iloc[best_fold_indices]

# Agregar la columna "mutant" al DataFrame best_fold_data
best_fold_data["mutant"] = mutant_column_best_fold.values
best_fold_data["prot"] = prot.values
best_fold_data["true"] = best_ytrain



# Imprimir la matriz de confusión del mejor modelo
print("Best Confusion Matrix:")
print(best_confusion_matrix)
