from django.urls import path
from blog.views import Home, detail, search, Category
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',Home,name='home'),
    path('search/',search,name='search'),
    path('movie/<int:id>-<str:name>/',detail,name='detail'),
    # path('<int:pk>/',post,name='post'),

    # Categories
    # path('category/<str:cata>',Category,name='Category'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)