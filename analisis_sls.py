#el orimer argumento es la salida de EV, la segunda la salida de MSA, tercero Foldx, cuarto PopMusic
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd




m="aWt_cBLS_pH5.A00" #ruta de archivo
#columna 0 tiempo
#columna 1 IR eliminar
#columna 3 90 restar blanco 
#columna 4 UV

def leer(n):
    df1=pd.read_csv(n, header=None,engine='python', skiprows=21,sep= "\t")
    df1.rename(columns={df1.columns[0]:'time',df1.columns[1]:'IR',df1.columns[3]:'dispersion',df1.columns[4]:'uv'}, inplace=True)
    df1=df1.filter(["time","dispersion","uv"])

    blanco=df1["dispersion"].iloc[0:40]
    blanco=blanco.mean()


    ###para que no agarre la ultima fila que tiene 0
    largo=len(df1.index)-1

    uv=df1["uv"].iloc[0:largo]
    time=df1["time"].iloc[0:largo]
    disp=df1["dispersion"].iloc[0:largo]

    disp=(disp-blanco)/100 #divido 100 para todos menos mut3 ph7 que es 500
    uv=uv/100




    ###para el nombre del pico
    x=df1[df1["uv"] == df1["uv"].max()] 
    return disp,uv,time,x

disp,uv,time,x=leer(m)


    ###para los maximos de los ejes 
maxuv=uv.max()+0.5
maxdisp=disp.max()+1


### todo lo que sigue es para que setee los parametros segun los datos
if m=="Mut3_pH5.A00":
    pm="327 kDa"
    pm2="200 kDa"
    y1=uv.max()+0.35
    y2=disp.max()-2.5
    ytick=[0,2,4,6,8]
    miny=-0.6
    title="Mut3 pH 5"
elif m=="Mut3 pH 7.A00":
    disp=disp/5
    uv=uv/5
    maxuv=uv.max()+0.5
    maxdisp=disp.max()+1
    pm="330 kDa"
    pm2=""
    y1=uv.max()+0.35
    y2=disp.max()-2.5
    ytick=[0,2,4,6,8]
    miny=-0.8
    title="Mut3 pH 7"
elif m=="Awt cBLS pH 7.A00":
    pm="328 kDa"
    pm2=""
    y1=uv.max()+0.43
    y2=disp.max()-2.5
    ytick=[0,2,4,6,8]
    miny=-0.8
    title="WT pH 7"
elif m=="aWt_cBLS_pH5.A00":
    pm="314 kDa"
    pm2="192 kDa"
    y1=uv.max()+0.38
    y2=disp.max()-2.3
    ytick=[0,2,4,6,8]
    miny=-0.5     
    title="WT pH 5"
elif m=="Asor cBLS pH 7.A00":
    pm="188 kDa"
    pm2=""
    y1=uv.max()+0.2
    y2=disp.max()-2.3
    ytick=[0,1,2,3,4,5]
    miny=-0.4 
    title="Sor pH 7"
elif m=="aSor_BLS_pH5.A00":
    pm="192 kDa"
    pm2=""
    y1=uv.max()+0.35
    y2=disp.max()-2.3
    ytick=[0,1,2,3,4,5]
    miny=-0.4 
    title="sor pH 5"
#######################################################


###grafico
fig, ax1 = plt.subplots(figsize=(5,4)) ##5,4 lindo

color = 'tab:red'
ax1.set_xlabel('Time (min)', fontsize=12)
ax1.spines[['top']].set_visible(False)
ax1.set_ylabel('UV$_{280}$ (AU)', color=color, fontsize=12)
ax1.plot(time, uv, color=color)

ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim([-0.1,maxuv])
plt.xticks([0, 20, 40, 60])  
plt.yticks([0,0.2,0.4,0.6,0.8,1])
plt.text(x["time"]-2,y1,pm)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'black'
ax2.set_ylabel('SLS (AU)', color=color, fontsize=12)  # we already handled the x-label with ax1
ax2.plot(time, disp,color=color)

ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim([miny,maxdisp])
ax2.spines[['top']].set_visible(False)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.yticks(ytick)
plt.text(x["time"]+2,y2,pm2)

plt.draw()
ax2.set_title(title)
o=m.replace(".A00",".png")
plt.savefig(o, transparent=True, dpi=500)
plt.show()
