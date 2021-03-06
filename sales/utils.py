

import uuid, base64
from .models import Customer
from .models import Profile
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns

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
    buffer.close()
    return graph
    
  

def get_chart(chart_type, data ,**kwargs):
    plt.switch_backend('AGG')
    fig =plt.figure(figsize=(10, 4))
    if chart_type == '#1':
        # plt.bar(data['transaction_id'], data['price'])
        sns.barplot(x='transaction_id', y='price', data=data)
        print('bar chart')
    elif chart_type == '#2':
        labels = kwargs.get('labels') 
        plt.pie(data=data, x='price', labels=labels)
        print('pie chart')
    elif chart_type == '#3':
        plt.plot(data['transaction_id'] ,data['price'], color='green', marker='o', linestyle='dashed')
        print('line chart')
    else:
        print('unkwon chart')
    
    plt.tight_layout()
    chart = get_graph()
    return chart