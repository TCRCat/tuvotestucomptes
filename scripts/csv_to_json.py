# -*- coding: utf-8 -*-
import pandas as pd
import json
import datetime

df_vots = pd.read_csv('../data/votscdr.csv',na_values="-")

# Fer join amb meses
df_meses = pd.read_csv('../data/meses.csv', dtype={"COD_PROV":str})
df_join = pd.merge(df_vots, df_meses, how='left', left_on='codimesa', right_on='CODI_MESA')

# Generar vots per mesa
with open('../data/vots_per_mesa.json','w') as vots_file:
    vots_file.write(json.dumps(json.loads(df_join.to_json(orient='records')), indent=4))
    print 'vots_per_mesa.json generat!'

# Generar vots per municipi
df_vots_per_municipi = df_join.groupby(['COD_PROV','CODI_MUNICIPI','MUNICIPI','COMARCA'],as_index=False)[
    u'vnuls', u'vblancs', u'verc', u'vjxc', u'vcup', u'vpsc', u'vcs', u'vppc', u'vcom', u'vpacma', u'vdialeg', u'vpumjust', u'vrecortes', u'vfamilia',
    u'vdn', u'vpfiv', u'vconver', u'vunidos', u'vcilus', u'cens'].sum()

with open('../data/vots_per_municipi.json','w') as vots_file:
    vots_file.write(json.dumps(json.loads(df_vots_per_municipi.to_json(orient='records')), indent=4))
    print 'vots_per_municipi.json generat!'

# Generar estat recompte
with open('../data/estat_recompte.json','w') as estat_file:
    estat_recompte = {
        "ultima_actualitzacio": datetime.datetime.strptime(df_vots['datetime'].max(), '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y %H:%M:%S'),
        "total_meses": len(df_vots),
        "meses_fetes": len(df_vots[df_vots['hihavots']==1]),
        "percentatge": "{0:.2f}%".format(float(len(df_vots[df_vots['hihavots']==1]))*100/float(len(df_vots)))
    }
    estat_file.write(json.dumps(estat_recompte, indent=4))
    print 'estat_recompte.json generat!'
