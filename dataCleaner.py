import pandas as pd 
import numpy as np

fileName = str(input('Raw CSV File Directory: '))
df = pd.read_csv(fileName)
new = df.Info.str.split(", ",expand=True)
df = df.drop('Info', 1)

df['SN'] = new[1]
df['FN'] = new[2]
df['Flags'] = new[3]
df['SSID'] = new[4]

df['SN'] = df['SN'].str[3:]
df['FN'] = df['FN'].str[3:]
df['Flags'] = df['Flags'].str[6:]
df['SSID'] = df['SSID'].str[5:]
SSIDS = df.SSID.unique()
for SSID in SSIDS:
    destinations = df.loc[df['SSID'] == SSID].Destination.unique()
    for mac in destinations:
        df.loc[df.Destination == mac, 'SSID'] = SSID

outputFileName = "{}_cleansed.csv".format(fileName[:-4])
df.to_csv(outputFileName)

print('Process Complete')