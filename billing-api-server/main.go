package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	testStr := `{
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
}`

	w.Header().Set("Content-Type", "application/json")
	fmt.Fprint(w, testStr)
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil)
}
