# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Dt4WsYNs2f3Vqzvhy6LYHagzHvNPpyGX
"""

import pandas as pd
fanlar=pd.DataFrame({
    "Fish" :['Aliyev A',"Xalilov D","Turdimatov M",'Raxmatov R',"Xonto'rayev S",
        "Abdullayev M","Jorayeva G","Tillaboyev M","Qurbonova G","D Jalilov"],
    'Fan nomi' :["Suniy intelekt asoslari","Suniy intelekt asoslari" , "Kiber hafsizlik","Kiber hafsizlik", "Ma'lumotlar tuzilmasi va algaritimlar"
      , "Ma'lumotlar tuzilmasi va algaritimlar","Elektronika va sihemalar","Elektronika va sihemalar",
       "Kanpuyuterni tashkil etish","Kanpuyuterni tashkil etish"],
    "Mashg'ulot" :['Amali', "Maruza",'Maruza','Amali','Maruza','Amali','Maruza','Amali','Amali','Maruza' ],
    "Dars o'tish mahorati" :['yaxshi', 'yaxshi','yaxshi','yaxshi','yaxshi','yaxshi','yaxshi','yaxshi','yaxshi','yaxshi' ]
})
print(fanlar)

fanlar.to_excel('681-23-guruh fanlar.xlsx')

fanlar.to_excel('681-23-guruh fanlar.xlsx')
