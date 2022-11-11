from django.urls import path, register_converter, re_path

from .views import index, index1, index2, index3, index4, index5
from .views import SignUpView, SignInView, ClientApiView


class YearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)

register_converter(YearConverter, 'yyyy')

urlpatterns = [
    path('', index, name='home'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('department', index1, name='department'),
    path('api/client/', ClientApiView.as_view(), name='api'),
    path('api/client/<int:client_id>/', ClientApiView.as_view(), name='api_id'),
    path('emp', index2, name='employee'),
    path('order', index3, name='order'),
    path('formorder', index4, name='formorder'),
    path('script', index5, name='script')
    # path('<yyyy:year>', index1)
    # path('category/<int:category_id>', index)
    # re_path('[^@]+@[^\.]+\..+', email)
]