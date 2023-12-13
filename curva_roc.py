
from sklearn.metrics import roc_curve, roc_auc_score, precision_recall_curve, auc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from ANALISIS_BENCHMARK import regresion,grafico_colores,l
from datos_normalizados import df_r


y_true=df_r["ddG Fireprot"]

y_pred_proba=df_r["ddG foldx"]
y_pred_proba_p=df_r["ddG PopMusic"]
y_pred_proba_e=df_r["effect_prediction_epistatic"]
y_pred_proba_i=df_r["effect_prediction_independent"]

df_r["y_binary"] = (y_true > 0).astype(int)

y_binary=df_r["y_binary"]
# y_pred_proba_c=df_r["y_pred_proba"]

# Suponiendo que y_true e y_pred_proba son tus etiquetas reales y probabilidades predichas, respectivamente
fpr, tpr, _ = roc_curve(y_binary, y_pred_proba)
fpr_e, tpr_e, _c = roc_curve(y_binary, y_pred_proba_e)
fpr_i, tpr_i, _p = roc_curve(y_binary, y_pred_proba_i)
fpr_p, tpr_p, _p = roc_curve(y_binary, y_pred_proba_p)
#precision, recall, _ = precision_recall_curve(y_binary, y_pred_proba)

# Calcula el área bajo la curva (AUC) para ROC y PR
roc_auc = roc_auc_score(y_binary, y_pred_proba)
roc_auc_e= roc_auc_score(y_binary, y_pred_proba_e)
roc_auc_i = roc_auc_score(y_binary, y_pred_proba_i)
roc_auc_p = roc_auc_score(y_binary, y_pred_proba_p)
# pr_auc = auc(recall, precision)

# Grafica la curva ROC
plt.figure(figsize=(8, 8))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve Foldx(AUC = {roc_auc:.2f})')
plt.plot(fpr_e, tpr_e, color='red', lw=2, label=f'ROC curve EV epistatic (AUC = {roc_auc_e:.2f})')
plt.plot(fpr_i, tpr_i, color='blue', lw=2, label=f'ROC curve EV independent (AUC = {roc_auc_i:.2f})')
plt.plot(fpr_p, tpr_p, color='black', lw=2, label=f'ROC curve PopMusic (AUC = {roc_auc_p:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()

# # Grafica la curva PR
# plt.figure(figsize=(8, 8))
# plt.plot(recall, precision, color='darkgreen', lw=2, label=f'PR curve (AUC = {pr_auc:.2f})')
# plt.xlabel('Recall')
# plt.ylabel('Precision')
# plt.title('Precision-Recall (PR) Curve')
# plt.legend(loc='lower right')
# plt.show()

