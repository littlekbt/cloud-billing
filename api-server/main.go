package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	testStr := `
[{
	"unitId": 1,
  "startDate": "20170801",
  "endDate": "20170805",
	"resources": [
    {
			"resource": "S3",
			"datas": [4.0, 4.3, 4.7, 5.8, 6.9] 
		},
		{
			"resource": "Dynamo",
			"datas": [4.0, 4.3, 14.7, 15.8, 19.0] 
		},
		{
			"resource": "lambda",
			"datas": [4.0, 4.3, 4.7, 5.8 ,5.9] 
		},
		{
			"resource": "EC2",
			"datas": [4.0, 4.3, 4.7, 5.8, 7.8] 
		}
	]
},{
	"unitId": 2,
  "startDate": "20170801",
  "endDate": "20170805",
	"resources": [
    {
			"resource": "cloudFunction",
			"datas": [4.0, 4.3, 4.7, 5.8, 6.9] 
		},
		{
			"resource": "AppEngine",
			"datas": [1.0, 2.3, 3.7, 3.8, 5.0] 
		}
	]
}]
`
	v := r.URL.Query()
	fmt.Println(v)
	// Get Data
	// EncodeJson

	w.Header().Set("Content-Type", "application/json")
	fmt.Fprint(w, testStr)
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil)
}
