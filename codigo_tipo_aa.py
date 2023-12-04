#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:10:38 2023

@author: solcanale
"""

### a partir de una secuencia crear un archivo con el tipo de residuo en formato ""aa tipo"

seq="GSTLQAAAAESGRYFGTAIAASRLNDGTYTTIANREFNMITAENEMKMDAMQPSRGQFNWSSGDRIVNWARQNGKQVRGHALAWHSQQPGWMQNMEGSALRTAMLDHVTQVASYYRGKIYAWDVVNEAFDDGSSGARRNSNLQRTGNDWIEAAFRAARAADPGAKLCYNDYNTDNWQHAKTQAVYNMVKDFKARGVPIDCVGFQAHFNSGNPVPSNYHTTLQNFADLGVDVQITELDIEGSGSSQAQQYQGVVQACLAVARCTGITVWGVRDTDSWRANGTPLLFDGSGNKKAAYTSVLN"

def tipo_aa(seq):
    res=[]
    basicos=["H","R","K"]
    nopolar=["I","F","L","W","A","M","P","V"]
    polar=["C","N","G","S","Q","T","Y"]
    acido=["D","E"]
    
    for aa in seq:
        if aa in basicos: 
            res.append(aa+" 0")
        elif aa in nopolar:
            res.append(aa+" 1")
        elif aa in polar:
            res.append(aa+" 2")
        elif aa in acido:
            res.append(aa+" -1")
    return res

a=tipo_aa(seq)
with open(r"ruta/al/archivo", 'w') as fp:
    fp.write('\n'.join(a))