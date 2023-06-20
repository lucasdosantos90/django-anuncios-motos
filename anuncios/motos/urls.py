from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('moto_detalhe/<int:id>/',views.moto_detalhe,name='moto_detalhe'),
    path('sobre/',views.sobre,name='sobre'),
    path('contato/',views.contato,name='contato'),
    path('moto_detalhe_pesq/<int:opc>/',views.moto_detalhe_pesq,name='moto_detalhe_pesq'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
