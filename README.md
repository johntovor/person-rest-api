# person-rest-api
Person REST API developed using Python, Django, and the Django REST Framework.
It supports all HTTP CRUD operations.

To fetch all Persons::
Use the "GET" method with the below URL
http://localhost:8000/persons/

To create a new Person::
Use the "POST" method with the below URL
http://localhost:8000/persons/

To fetch a single person::
Use the "GET" method with the below URL
http://localhost:8000/persons/{id}
NB: Replace {id} with the id of the Person instance you want to fetch.

To update a Person instance::
Use the "PUT" method with the below URL
http://localhost:8000/persons/{id}

To update some fields in the Person instance::
Use the "PATCH" method with the below URL
http://localhost:8000/persons/{id}

To delete Person instance::
Use the "DELETE" method with the below URL
http://localhost:8000/persons/{id}
