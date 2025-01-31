# ML Model API using Django

## Setup

- install required frameworks
	```
	pip install django djangorestframework
	```

- starting the server
	```
	python manage.py runserver
	```

## API calls

- get_recommendations
  
  Send the user_id to recieve a JSON object containing list of recommended item_ids
  Example:
    ```
	http://127.0.0.1:8000/get_recommendations/?user_id=3917
	```
  Result:
  	```
  	{"recommends": [10486, 10820, 9350, 1082, 548, 7781, 2155, 10963, 11748, 11901]}
  	```
- get_recommendations 
	Send the user_id, currently accessed itemids and current actions.
	- 1 for view
	- 2 for addtocart
	- 3 for purchased

	Example:
	http://127.0.0.1:8000/get_recommendations/?user_id=3917&itemids=[9350, 1082, 548, 7781]&events=[1,2,1,1]
