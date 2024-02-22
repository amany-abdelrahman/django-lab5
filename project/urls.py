"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path

from company.views import EmpView, EmpView2, TeamView
from myapi.views import EmpFunBaseView, TeamClassViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TeamClassViewSet, basename='team')
urlpatterns = router.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", EmpView,name="employee"),
    path("emp/", EmpView2,name="employee2"),
    # path('team/', TeamView, name='team-create'),
    path('api-auth/', include('rest_framework.urls')),
    # path('emp-all/', EmpFunBaseView, name='emp-all'),
    path('emp-all/', EmpFunBaseView.as_view(), name='emp-all'),
    path('team/', include(router.urls)),
    path('emp-all/<int:pk>/', EmpFunBaseView.as_view(), name='delete'),
    path('emp-all/<int:pk>/', EmpFunBaseView.as_view(), name='update'),
    
]
