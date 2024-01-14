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
    cache_key = "make_cache"

class VechileController(BaseAPIController):
    serializer_class = VechileSerializer
    filterset_class = VechileFilter
    cache_key = "vechile_cache"

