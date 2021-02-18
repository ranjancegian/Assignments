from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

from django.views.generic.edit import FormView

from .forms import ItemListForm
from .models import Item

import requests, time, json
from urllib.parse import urlencode


class GeeksFormView(FormView):
    form_class = ItemListForm
    template_name = 'home.html'
    success_url = ''

    def get(self, request, *args, **kwargs):
        if(request.GET.get('page','')==''):
            return super().get(request, args, kwargs)
        data = Item.objects.get(name='mydata').json_data
        page = int(request.GET.get('page',1))
        paginator = Paginator(data, 10)
        try:
            members = paginator.page(page)
        except PageNotAnInteger:
            members = paginator.page(1)
        except EmptyPage:
            members = paginator.page(paginator.num_pages)
        return render(request, 'base.html', {'members': members})

    @method_decorator(ratelimit(key='ip', rate='1/m', method='POST'), name='post')
    @method_decorator(ratelimit(key='ip', rate='1000/d', method='POST'), name='post')
    def post(self, request, *args, **kwargs):
        """was_limited = getattr(request, 'limited', False)
        if(was_limited):
            dump = json.dumps({'error':'you have reached the limit'})
            return HttpResponse(dump, content_type='application/json')"""
        request_data = dict(request.POST)
        params = []
        request_data = self.modify_data(request_data)
        for key, val in request_data.items():
            val = val[0]
            if(val!=''):
                params.append((key, val))
        params.append(('key', 'U4DMV*8nvpm3EOpvf69Rxw(('))
        params.append(('site', 'stackoverflow'))
        params = tuple(params)
        data = self.get_data(params)
        data = data.get('items',[])
        if len(Item.objects.filter(name='')):
            Item.objects.create(json_data=data)
        else:
            Item.objects.filter(name='mydata').update(json_data=data)
        page = 1
        paginator = Paginator(data, 10)
        try:
            members = paginator.page(page)
        except PageNotAnInteger:
            members = paginator.page(1)
        except EmptyPage:
            members = paginator.page(paginator.num_pages)
        return render(request, 'base.html', {"members":members})

    def get_data(self, params):
        url = 'https://api.stackexchange.com/2.2/search/advanced?'+urlencode(params)
        res = requests.get(url)
        return res.json()

    def epoc_time(self, date):
        if date=='':
            return ['']
        p = "%Y-%m-%d"
        epoch = int(time.mktime(time.strptime(date,p)))
        return [str(epoch)]

    def modify_data(self, request_data):
        token = request_data.pop('csrfmiddlewaretoken','')
        fromdata = self.epoc_time(request_data.pop('fromdate')[0])
        todate = self.epoc_time(request_data.pop('todate')[0])
        min = self.epoc_time(request_data.pop('min')[0])
        max = self.epoc_time(request_data.pop('max')[0])
        request_data.update({'fromdate':fromdata,'todate':todate,'max':max, 'min':min})
        return request_data



