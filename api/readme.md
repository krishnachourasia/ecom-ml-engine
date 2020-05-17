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

