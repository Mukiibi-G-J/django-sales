

import uuid, base64
from .models import Customer
from .models import Profile
from io import BytesIO
import matplotlib.pyplot as plt

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

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.closed
    return graph
    
    pass

def get_chart():
    chart = get_graph()
    pass