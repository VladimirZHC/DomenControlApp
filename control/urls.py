from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import (
    getgrouppolicyhistory, 
    getgrouppolicyhistoryid, 
    getgrouppolicyhistoryrollback, 
    getschemahistory, 
    getschemahistoryid, 
    getschemahistoryidrollback,
    getuseridpolicy,
    gethostidpolicy,
    )

orgunits_list = views.OrgUnitViewSet.as_view({
    'get': 'list',
}
)

orgunit_post_detail = views.OrgUnitViewSet.as_view({
    'post': 'create',
})


orgunit_detail = views.OrgUnitViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

group_policies_list = views.GroupPolicyViewSet.as_view({
    'get': 'list',
})

group_policy_post_detail = views.GroupPolicyViewSet.as_view({
    'post': 'create',
})

group_ploicy_detail = views.GroupPolicyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

users_list = views.DomainUserViewSet.as_view({
    'get': 'list',
})

user_post_detail = views.DomainUserViewSet.as_view({
    'post': 'create',
})

user_detail = views.DomainUserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

hosts_list = views.HostViewSet.as_view({
    'get': 'list',
})

host_post_detail = views.HostViewSet.as_view({
    'post': 'create',
})

host_detail = views.HostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

schemas_list = views.ParamsSchemaViewSet.as_view({
    'get': 'list',
})

schema_post_detail = views.ParamsSchemaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})




router = DefaultRouter()
router.register(r'orgunits', views.OrgUnitViewSet, basename='orgunit')
router.register(r'grouppolicies', views.GroupPolicyViewSet)
router.register(r'users', views.DomainUserViewSet)
router.register(r'hosts', views.HostViewSet)
router.register(r'schemas', views.ParamsSchemaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('orgunits/', orgunits_list, name='orgunits-list'),
    path('orgunit/', orgunit_post_detail, name='orgunit-post-detail'),
    path('orgunit/<int:pk>/', orgunit_detail, name='orgunit-detail'),
    path('grouppolicies/', group_policies_list, name='group-policies-list'),
    path('grouppolicy/', group_policy_post_detail, name='group-policy-post-detail'),
    path('grouppolicy/<int:pk>/', group_ploicy_detail, name='group-policy-detail'),
    path('users/', users_list, name='users-list'),
    path('user/', user_post_detail, name='user-post-detail'),
    path('user/<int:pk>/', user_detail, name='user-detail'),
    path('hosts/', hosts_list, name='hosts-list'),
    path('host/', host_post_detail, name='host-post-detail'),
    path('host/<int:pk>/', host_detail, name='host-detail'),
    path('schemas/', schemas_list, name='schemas-list'),
    path('schema/<str:type>/', schema_post_detail, name='computer-detail'),
    path('grouppolicy/<int:pk>/history/', getgrouppolicyhistory),
    path('grouppolicy/<int:pk>/history/<int:history_pk>/', getgrouppolicyhistoryid),
    path('grouppolicy/<int:pk>/history/<int:history_pk>/rollback/', getgrouppolicyhistoryrollback),
    path('schema/<str:type>/history/', getschemahistory),
    path('schema/<str:type>/history/<int:history_pk>/', getschemahistoryid),
    path('schema/<str:type>/history/<int:history_pk>/rollback/', getschemahistoryidrollback),
    path('user/<int:pk>/policy/', getuseridpolicy),
    path('host/<int:pk>/policy/', gethostidpolicy),
]


