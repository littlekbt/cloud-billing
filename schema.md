データ構造メモ

User - Provider - Unit - Resource - Data

kubota - AWS - CloudBilling - S3      - 20170801
                                      - 20170802
                            - Dynamo  - 20170801
                                      - 20170802
                            - EC2     - 20170801
                                      - 20170802

             - SlackLambda  - S3      - 20170801
                                      - 20170802
                            - EC2     - 20170801
                                      - 20170802

        - GCP - Todo        - cloudFunction - 20170801
                                            - 20170802


データをDynamoとS3から読んで、同じインターフェイスでAPIを提供するサーバーが必要

Unitまでがwebで持つ
Resourceからはdynamo, s3が持つ(UnitのIDが必要)


/api/v1/billing-datas/:unit_id
{
	"unitId": 1,
	"resources": [{
			"resource": "S3",
			"datas": [{
					"date": "20170801",
					"value": "4.0"
				},
				{
					"date": "20170802",
					"value": "4.4"
				}
			]
		},
		{
			"resource": "Dynamo",
			"datas": [{
					"date": "20170801",
					"value": "10.0"
				},
				{
					"date": "20170802",
					"value": "12.8"
				}
			]
		}
	]
}
