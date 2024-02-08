import pandas as pd
import psycopg2
import re


## credetial for connections
DATABASE = "vcdw_production__v"
USER = "vcdw_readall_mahajanshreya"
PASSWORD = "hGfSwRFxqYNZqptbp28k8cki6ah6JR"
HOST = "cdw-organon-us.veevanitro.com"
PORT = 5439
# SCHEMA = "symphony_non_retail_report_current__v"
con=psycopg2.connect(dbname = DATABASE, host = HOST, port= PORT, user= USER, password= PASSWORD,)


with open('cummmmm_overall.txt') as f:
    lines = f.read()

with open('cummmmm_vendor.txt') as f:
    lines1 = f.read()

vendor = {'%nex%':['deepintent','doximity','edh','medscape','numedis','pulsepoint','reachmd','sfmc'],'%ont%':['alertmkting','deepintent','doximity','edh','medscape','sfmc'],'%ren%':['deepintent','doximity','healio','medscape','sfmc']}
 
print(vendor)
 
print("Please Enter the table name")
table_nm = input()
 
print("Please Enter the Yearmonth list")
ym_list = input().split(',')

prod_list = ['%nex%','%ont%','%ren%']
df1 = pd.DataFrame()
for j in prod_list:
    for i in ym_list:
        df = pd.read_sql_query(lines.replace('xzxtablexzx',table_nm).replace('xzxprodxzx',j).replace('xzxymxzx',i), con)
        df1 = pd.concat([df1,df])


df1.to_excel('cummulative_overall.xlsx',index=False)
print('First Downloaded')

df2 = pd.DataFrame()
for j in prod_list:
    for k in vendor[j]:
        for i in ym_list:
            df_ = pd.read_sql_query(lines1.replace('xzxtablexzx',table_nm).replace('xzxvendxzx',k).replace('xzxprodxzx',j).replace('xzxymxzx',i), con)
            df2 = pd.concat([df2,df_])

df2.to_excel('cummulative_vendor.xlsx',index=False)
print('Second Downloaded')
