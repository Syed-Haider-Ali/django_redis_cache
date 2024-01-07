from utils.reusable_classes import BaseAPIController
from .serializer import *
from .filters import *
from utils.response_messages import *
from utils.reusable_methods import *
from .models import *
from django.core.cache import cache



class MakeController(BaseAPIController):
    serializer_class = MakeSerializer
    filterset_class = MakeFilter


class VechileController(BaseAPIController):
    serializer_class = VechileSerializer
    filterset_class = VechileFilter

    def get(self,request):
        response = []

        if cache.get('response_key'):
            response = cache.get('response_key')
            db= 'redis'
        else:
            instances = self.serializer_class.Meta.model.objects.select_related('make').all()
            for i in instances:
                response.append(i.name)
            cache.set('response_key', response)
            db = 'ORM'

        response_data = {
            'db': db,
            'data': response
        }
        return create_response(response_data, SUCCESSFUL, 200)
