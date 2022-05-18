

import uuid
from .models import Customer
from .models import Profile


def generate_code():
    code =uuid.uuid4()
    code_mod = str(code).replace('-',"")[:12].upper()
    print(code_mod)
    
    return code_mod

def get_salesman_from_id(val):
    salesman = Profile.objects.get(id=val)
    return salesman.user.username
    
def get_customer_from_id(val):
    customer = Customer.objects.get(id=val)
    return customer