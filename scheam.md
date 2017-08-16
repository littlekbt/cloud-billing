dynamodbのdb設計
アカウントにひもづく一つのcloudアカウントをunitとする。


id
unit_id
resource
timestamp
value
{
    id int # primary key
    unit_id int # index
    resource string # index
    timestamp
    value
}
