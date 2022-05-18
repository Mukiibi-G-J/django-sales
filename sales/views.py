 

from cProfile import label
from django.shortcuts import render
from django.views.generic import DetailView,ListView
# Create your views here.
from django.shortcuts import render
from .models import Sale
from .form import SalesSearchForm
import pandas as pd
from .utils import get_salesman_from_id,get_chart, get_customer_from_id


def home_view(request):
    form= SalesSearchForm(request.POST or None)
    sales_df=None
    postions_df=None
    merge_df=None
    df=None
    chart = None
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to= request.POST.get('date_to')
        chart_type= request.POST.get('chart_type')
        print(date_from, date_to, chart_type)
        sale_qs = Sale.objects.filter(created__date__lte =date_to, created__date__gte=date_from )
        if len(sale_qs)> 0:
            sales_df=pd.DataFrame(sale_qs.values())
            sales_df['customer_id']= sales_df['customer_id'].apply(get_customer_from_id)
            sales_df['salesman_id']= sales_df['salesman_id'].apply(get_salesman_from_id)
            # sales_df=sales_df.rename({'customer_id': 'customer', 'salesman_id': 'salesman'}, axis=1 )
            sales_df.rename({'customer_id': 'customer', 'salesman_id': 'salesman', 'id':'sales_id'}, axis=1, inplace=True)
            sales_df['created']= sales_df['created'].apply(lambda x: x.strftime('%Y-%m-%d'))
            sales_df['updated']= sales_df['updated'].apply(lambda x: x.strftime('%Y-%m-%d'))
            positions_data=[]
            for sale in sale_qs:
                for pos in sale.get_positions():
                    obj={ 
                         "postion_id":pos.id,
                         'product':pos.product.name,
                         'quantity':pos.quantity,
                         'price':pos.price,
                         'sales_id':pos.get_sales_id()
                    }
                    positions_data.append(obj)

            postions_df =pd.DataFrame(positions_data)
            merge_df = pd.merge(sales_df, postions_df, on='sales_id')
             #?merging basing on the sales id
            merge_df = pd.merge(sales_df, postions_df, on='sales_id')
            postions_df = postions_df.to_html()
            sales_df = sales_df.to_html()
            
            df = merge_df.groupby('transaction_id', as_index=False )['price'].agg('sum')
            chart = get_chart(chart_type, df, labels=df['transaction_id'].values)
            df = df.to_html()
             
            merge_df = merge_df.to_html()
            # print(postions_df)
    context ={
        "form":form,
        "sales_df":sales_df,
        "postions_df":postions_df,
        "merge_df":merge_df,
        "df":df,
        'chart':chart
        
    }        
        # # ?lsit of dictionaries
        # print(qs.values())
        # #? returns list tuples
        # print(qs.values_list())
        # #? this  give u the titles
        
        
        # #? this does not give u the titles
        # df1=pd.DateFrame(qs.values_list())
        # print(df1) 
        
        
    
    return  render(request, 'sales/home.html', context)



class SalesListView(ListView):
    model = Sale
    template_name ='sales/main.html'

class SalesDetailView(DetailView):
    model = Sale
    template_name ='sales/detail.html'
 
    