from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
import sqlite3
from sqlite3 import Error

from .models import Management, Department, Employee, Order
from django.views.decorators.http import require_GET
from .forms import OrderForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UsernameField
from django.forms import PasswordInput, CharField, TextInput
from .tasks import send_message

from .forms import SignUpForm

@require_GET
def index(request: HttpRequest):
    management = Management.objects.all().order_by('name')
    department = Department.objects.all().order_by('name')
    employee = Employee.objects.all().order_by('name_ru')
    return render(request, 'dostup2app/index.html', {'management': management, 'department': department, 'employee': employee}, status=200)


class ClientApiView(View):

    def get(self, request: HttpRequest, client_id=None):
        if not client_id:
            clients = Employee.objects.all()
            data = {}
            for client in clients:
                data[str(client.id)] = {

                    'department': client.department.name,
                    'name_ru': client.name_ru
                }
            return JsonResponse(data=data)
        else:
            client = Employee.objects.filter(pk=client_id)
            if client:
                client = client[0]
                client = {
                    'id': client.id,
                    'department': client.department.name,
                    'name_ru': client.name_ru
                }
                return JsonResponse(data=client)
            else:
                return JsonResponse(data={'status': 404, 'detail': f'client {client_id} is not exist'})



class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'dostup2app/signup.html'
    success_url = reverse_lazy('signin')


class SignInView(LoginView):
    template_name = 'dostup2app/signin.html'
    username = CharField(
        widget=TextInput(
            attrs={
                'name': 'your_name',
                'id': 'your_name',
                'placeholder': 'Username'
            }
        )

    )

# def index1(request):
#     return HttpResponse('email')

# @require_http_methods(['GET'])
def index1(request: HttpRequest, year: int):
    return HttpResponse('<b>Hello</b>')


def index2(request: HttpRequest):
    management = Management.objects.all().order_by('name')
    department = Department.objects.all().order_by('name')
    employee = Employee.objects.all().order_by('name_ru')
    return render(request, 'dostup2app/index1.html', {'employee': employee, 'management': management,
                                                      'department': department}, status=200)


def index3(request: HttpRequest):
    order = Order.objects.all().order_by('date_created')

    # image = Order.objects.all().order_by('image')
    return render(request, 'dostup2app/index3.html', {'order': order}, status=200)


def index5(id):
    path = 'D:\Python\pythonProject\pythonProject9\dostup2\db.sqlite3'

    try:
        conn = sqlite3.connect(path)
        print("connect to DB ")
    except Error as e:
        print("Could not connect to DB using given credentials")

    cur = conn.cursor()
    sql1 = """SELECT 'ФИО', e.name_ru FROM orders as o 
    join employee as e on o.employee_id=e.id
    WHERE o.id=%(id)s
    union all
    select 'Отдел', d.name from orders as o 
    join department as d on o.employee_id=d.id
    WHERE o.id=%(id)s
    union ALL
    select 'Телефонная связь', case WHEN o.Телефонная_связь='1' then 'V' else 'X' end
    FROM orders as o
    WHERE o.id=%(id)s
     """ % {'id': id}
    cur.execute(sql1)
    rows = cur.fetchall()

    with open("1.xls", 'w') as file:
        for x in rows:
            print(x)
            file.write(str(x) + '\n')

    conn.close()
    return 1


def index4(request):
    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            # убрать комментарий, если хотим проверить celery
            # send_message.delay(request.POST.get('employee'))
            return redirect('home')
        else:
            error = 'Неверно заполнена форма'

    form = OrderForm()
    department = Department.objects.all().order_by('name')
    employee = Employee.objects.all().order_by('name_ru')
    return render(request, 'dostup2app/index4.html',
                  {'department': department, 'employee': employee, 'form': form, 'error': error}, status=200)


def email(request):
    return HttpResponse('email')

# Create your views here.
from django.shortcuts import render

# Create your views here.
