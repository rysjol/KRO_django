from django.conf import settings
from django.urls import path, include

from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cat/<int:id>', views.category, name='category'),
    path('cat/', views.categories, name='categories')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)), ]
