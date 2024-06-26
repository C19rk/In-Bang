from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('InBang.urls')),
    # re_path(r'^.*$', TemplateView.as_view(template_name=str(settings.BASE_DIR / 'static_my_project' / 'index.html')), name='home'),
    # path('api/products/', include('base.urls.product_urls')),
    # path('api/users/', include('base.urls.user_urls')),
    # path('api/orders/', include('base.urls.order_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)