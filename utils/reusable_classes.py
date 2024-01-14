from django.db import models
from django.core.cache import cache
from utils.reusable_methods import create_response, paginate_data
from utils.response_messages import *
from utils.reusable_methods import get_first_error_message


class TimeStamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class BaseAPIController:
    serializer_class = ""
    filterset_class = ""
    feature_name = ""
    cache_key = ""
    
    def post(self,request):
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid():
            instance = serialized_data.save()
            response_data = self.serializer_class(instance).data
            return create_response(response_data, SUCCESSFUL, 200)
        else:
            return create_response({},get_first_error_message(serialized_data.errors,UNSUCCESSFUL), 400)
        
    def get(self,request):
        if cache.get(self.cache_key):
            response = cache.get(self.cache_key)
            db= 'redis'
        else:
            response = self.serializer_class.Meta.model.objects.all().order_by('-created_at')
            cache.set(self.cache_key, response)
            db = 'ORM'
        serialized_data = self.serializer_class(response, many=True).data
        response_data = {
            'db': db,
            'count': response.count(),
            'data': serialized_data
        }
        return create_response(response_data, SUCCESSFUL, 200)

    def update(self,request):
        if not "id" in request.query_params:
            return create_response({}, ID_NOT_PROVIDED, 400)
        else:
            instance = self.serializer_class.Meta.model.objects.filter(id=request.query_params.get('id')).first()
            if not instance:
                return create_response({}, NOT_FOUND, 404)
            
            serialized_data = self.serializer_class(instance, data=request.data, partial=True)
            if serialized_data.is_valid():
                response_data = serialized_data.save()
                return create_response(self.serializer_class(response_data).data, SUCCESSFUL, 200)
            else:
                return create_response({},get_first_error_message(serialized_data.errors,UNSUCCESSFUL), 400)

    def delete(self,request):
        if not "id" in request.query_params:
            return create_response({}, ID_NOT_PROVIDED, 400)
        instance = self.serializer_class.Meta.model.objects.filter(id=request.query_params.get("id")).first()
        if not instance:
            return create_response({}, NOT_FOUND, 404)
        instance.delete()
        return create_response({}, SUCCESSFUL, 200)

