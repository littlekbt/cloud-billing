# -*- coding: utf-8 -*-

from __future__ import print_function
import boto3
import csv
import time
import pandas as pd

s3 = boto3.client('s3')

def handler(event, context):
  with open('tmp.csv', 'w') as data:
    s3.download_fileobj("littlekbt-billing-report", "603023411334-aws-billing-csv-2017-08.csv", data)
  pd_datas = pd.read_csv('tmp.csv')
  total(pd_datas)
    # insert(resource(pb_datas))
    # insert(resource_usage_type(pb_datas))


# {aws.total.2017.08.07: 10}
def total(pb_datas):
    print(pb_datas['TotalCost'].max) 

# {aws.s3.2017.08.07: 8,
# aws.lambda.2017.08.07: 7}
def resource(pb_datas):
    print(pb_datas)

# {aws.lambda.Request.2017.08.07: 6,
# aws.s3.USW1-TimedStorage-ByteHrs.2017.08.07: 2}
def resource_usage_type(pb_datas):
    print(pb_datas)

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
