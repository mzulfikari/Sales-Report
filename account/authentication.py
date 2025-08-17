from django.contrib.auth.backends import BaseBackend
from Services.models import Services

class CustomerBackend(BaseBackend):
    
    def authenticate(self,phone=None):
        try:
            service = Services.objects.get(phone=phone)
            return service
        except Services.DoesNotExist:
            return None

    def get_user(self, service_id):
        try:
            return Services.objects.get(pk=service_id)
        except Services.DoesNotExist:
            return None