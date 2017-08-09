# メモ
cloudを横断した料金分析をできるように。

AWS上に構築。フロント以外はサーバーレスで

## データ構造

- クラウドごと
  aws.total.2017.08.07
- クラウドのリソースごと
  aws.s3.2017.08.07
  aws.lambda.2017.08.07
  aws.datatransfar.2017.08.07
- クラウドのリソースのusage-typeごと(aws)
  aws.lambda.Request.2017.08.07
  aws.s3.USW1-TimedStorage-ByteHrs.2017.08.07
- クラウドのタグごと(aws)
  aws.tag.user.name.littlekbt.2017.08.07
  aws.tag.aws.created_by.littlekbt.2017.08.07
- クラウドのユーザーごと(aws)
  aws.user.kubota.2017.08.07

タグがついてると同じリソースのusage-typeに重なってレコードがある
ので、usage-typeとリソースのトートルはタグなしを使う。

Currencyはどこに保存しよう。。

```
aws
  - total
    - 2017
      - 08
        - 07
          - 10
  - s3
    - 2017
      - 08
        - 07
          - 3
    - USW-1TimedStorage-ByteHrs
      - 2017
        - 08
          - 07
            - 2
  - tag
    - user
      - name
        - littlekbt
          - 2017
            - 08
              - 07
                - 8
  - account
    - kubota
      - 2017
        - 08
          - 07
            - 10
```

## データの収集(batch)
各Cloudから料金情報を取ってきて保存する。

* 多角的に分析できるようなデータの保存を。
    - 時間
    - リソースごと
    - タグごと(aws)
    - ユーザーごと(aws)

概要
    step functionでlambdaを動かし、Dynamoに保存

TODO 
    - lambda作成
        - from aws
        - from gcp
    - step function
    - 3ヶ月以上のデータはs3へ

## APIの作成(api)
API Gatewayとlambdaでdynamo, s3からのデータを統一的なインターフェイスで提供

TODO
    - api作成
    - lambda作成

## 画面(front)
RailsでGUIの作成
