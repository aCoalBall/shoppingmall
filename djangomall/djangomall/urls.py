"""djangomall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from django.contrib.auth import views, forms as auth_forms
from django import forms

from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import JavaScriptCatalog

def validate_email_domain(value):
    if '@' not in value:
        raise ValidationError(
            _('Enter a valid email address.')
        )
        
class AuthenticationFormExample(auth_forms.AuthenticationForm):
    username = forms.EmailField(
        min_length=6,
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        ),
        validators=[validate_email_domain]
          
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )



class NewLoginView(views.LoginView):
    template_name = 'accounts/login.html'
    # 表单改成 AuthenticationFormExample
    form_class = AuthenticationFormExample


urlpatterns = i18n_patterns(
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('admin/', admin.site.urls),
    
    path('accounts/', include('accounts.urls')),
    # 把 auth.urls 读取到 accounts/
    path('accounts/', include('django.contrib.auth.urls')),

    path('products/', include(('products.urls', 'products'), namespace='products')),
    path('carts/', __import__('carts').views.index),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),


    prefix_default_language=False)

'''
urlpatterns = i18n_patterns(

    
    path('admin/', admin.site.urls),
    # /accounts/login/ 转给 NewLoginView 处理
    path('accounts/login/', NewLoginView.as_view()),
    # 把 auth.urls 读取到 accounts/
    path('accounts/', include('django.contrib.auth.urls')),

    path('products/', include('products.urls')),
    path('api/', include('api.urls')),
    path('carts/', __import__('carts').views.index),
    
    path('orders/', include('orders.urls')),
    prefix_default_language=False
)
'''

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

