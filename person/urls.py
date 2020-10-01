from django.urls import path
from .views import (index, DepartmentListView, person_list,
                    GenralCreateView, GenralList, GenralUpdateView,GenralDetailView,GenralDeteleView,Genral_Uprav,
                    UpravList,UpravCreate,UpravUpdate,
                    OtdelList,
                    )
urlpatterns = [

    path('otdel/<int:id>/', OtdelList.as_view(),name='otdel_list'),
    path('update_uprav/', UpravUpdate.as_view(), name='uprav_update'),
    path('create_uprav/', UpravCreate.as_view(), name='uprav_create'),
    path('uprav/', UpravList.as_view(), name='uprav_list'),
    path('genral/', GenralList.as_view(), name='genral_list'),
    path('genral/<int:pk>/update', GenralUpdateView.as_view(), name='genral_update'),
    path('genral/<int:pk>/delete', GenralDeteleView.as_view(), name='genral_delete'),
    path('genral/<int:pk>/list', Genral_Uprav.as_view(), name='genral_uprav'),
    path('genral/<int:pk>/', GenralDetailView.as_view(), name='genral_detail'),
    path('genral/create', GenralCreateView.as_view(), name='genral_create'),
    # path('genral_update/', GenralUpdateView.as_view(), name='genral_update'),
    path('person/', person_list, name='perfilter'),
    path('list/', DepartmentListView.as_view(), name='department-list'),

    path('', index, name='index'),
]