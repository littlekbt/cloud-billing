# -*- coding: utf-8 -*- 

from __future__ import print_function
import boto3
import csv
import time
import pandas as pd
import datetime

# unit_id, key, secret_keyをもらう。
def handler(event, context):
  session = boto3.Session(profile_name='s3')
  s3      = session.client('s3')
  now = datetime.datetime.today()

  with open('tmp.csv', 'w') as data:
    month = now.month
    month  = str(month) if month >= 10 else "0" + str(month)
    s3.download_fileobj("littlekbt-billing-report", "603023411334-aws-billing-csv-"+str(now.year)+"-"+month+".csv", data)

  unit_id  = 1
  pd_datas = pd.read_csv('tmp.csv')

  insert(collect_datas(unit_id, pd_datas, now))

def collect_datas(unit_id, pd_datas, date):
  datas = []
  datas.append(total(unit_id, pd_datas, date))
  datas += resource(unit_id, pd_datas, date)
  datas += resource_usage_type(unit_id, pd_datas, date)
  
  return datas

def total(unit_id, pd_datas, date):
  key = '.'.join(['aws', 'total', str(date.year), str(date.month), str(date.day), str(date.hour)])
  return mk_item(unit_id, date, {'resource_key': key, 'resource': 'aws.total', 'value': format(round(pd_datas['TotalCost'].max(), 3), ".15g")})

def resource(unit_id, pd_datas, date):
  d = pd_datas.groupby('ProductCode')['TotalCost'].sum()
  m = []
  for index in d.index:
    key = '.'.join(['aws', index, str(date.year), str(date.month), str(date.day), str(date.hour)])
    m.append(mk_item(unit_id, date, {'resource_key': key, 'resource': '.'.join(['aws', index]), 'value': format(round(d[index], 3), ".15g")}))

  return m

def resource_usage_type(unit_id, pd_datas, date):
  d = pd_datas.groupby(["ProductCode", "UsageType"])['TotalCost'].sum()
  m = []
  for index in d.index:
    key = '.'.join(['aws', index[0], index[1], str(date.year), str(date.month), str(date.day), str(date.hour)])
    m.append(mk_item(unit_id, date, {'resource_key': key, 'resource': '.'.join(['aws', index[0], index[1]]), 'value': format(round(d[index], 3), ".15g")}))
    
  return m

def mk_item(unit_id, date, data):
  default = {'unit_id': unit_id, 'timestamp': int(time.mktime(date.timetuple()))}
  default.update(data)
  return default

def insert(datas):
  dynamodb = boto3.resource(
    'dynamodb', 
    region_name='ap-northeast-1', 
  )

  table = dynamodb.Table("cloud_billings")

  with table.batch_writer() as batch:
    for data in datas:
      response = table.put_item(
        Item = data
      )
