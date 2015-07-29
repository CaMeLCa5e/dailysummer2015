from rest_framework.test import APIRequestFactory 
from django.test.client import encode_multipart, RwquestFactory 

# factory = APIRequestFactory()
# request = factory.post('/notes/', {'title': 'new idea'})

# request = factory.put('/notes/547/', {'title': 'remember to email'})

factory = RequestFactory()
data = {'title': 'subject'}
content = encode_multipart('bountryString', data)
content_type = 'multipart/form-data; boundry=bountryString'
request = factory.put('/notes/547/', content, content_type=content_type)

