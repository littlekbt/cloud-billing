# -*- coding: utf-8 -*- 

from __future__ import print_function
import boto3
import csv
import time
import pandas as pd
import datetime

s3 = boto3.client('s3')

def handler(event, context):
  #with open('tmp.csv', 'w') as data:
  #  s3.download_fileobj("littlekbt-billing-report", "603023411334-aws-billing-csv-2017-08.csv", data)
  pd_datas = pd.read_csv('tmp.csv')
  today = datetime.datetime.today()
  print(total(pd_datas, today))
  print(resources(pd_datas, today))
  print(resource_usage_type(pd_datas, today))


# {aws.total.2017.08.07: 10}
def total(pd_datas, date):
    key = '.'.join(['aws', 'total', str(date.year), str(date.month), str(date.day), str(date.hour)])
    return {key: round(pd_datas['TotalCost'].max(), 3)}

# {aws.s3.2017.08.07: 8,
# aws.lambda.2017.08.07: 7}
def resources(pd_datas, date):
    d = pd_datas.groupby("ProductCode")['TotalCost'].sum()
    return d

# {aws.lambda.Request.2017.08.07: 6,
# aws.s3.USW1-TimedStorage-ByteHrs.2017.08.07: 2}
def resource_usage_type(pd_datas, date):
    d = pd_datas.groupby(["ProductCode", "UsageType"])['TotalCost'].sum()
    return d

# 今度対応する
# {aws.tag.user.name.littlekbt.2017.08.07: 6,
# aws.tag.aws.created_by.littlekbt.2017.08.07: 2}
# def tag(pb_datas):
#     print(pb_datas)
# 
# # {aws.user.kubota.2017.08.07: 4}
# def user(pb_datas):
#     print(pb_datas)

# mapを渡してkeyを.で切ってvalueを登録する。
def insert(pb_data):
    print(pb_data)
