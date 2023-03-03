from django.urls import path
from. import views
urlpatterns = [
    path('',views.analysis,name='analysis'),
    path('<int:subanalysis_id>', views.subanalysis, name='subanalysis')
]
