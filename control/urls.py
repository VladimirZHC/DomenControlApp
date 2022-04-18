from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


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

result_policy_user = views.DomainUserViewSet.as_view({
    'get': 'policy',
})

result_policy_host = views.HostViewSet.as_view({
    'get': 'policy',
})

schema_id_history =  views.HistoryParamsSchemaViewSet.as_view({
    'get': 'list',
})


schema_id_history_id =  views.HistoryParamsSchemaViewSet.as_view({
    'get': 'retrieve',
})


group_policy_id_history = views.HistoryGroupPolicyViewSet.as_view({
    'get': 'list',
})

group_policy_id_history_id = views.HistoryGroupPolicyViewSet.as_view({
    'get': 'retrieve',
})

group_policy_id_history_id_rollback = views.HistoryGroupPolicyViewSet.as_view({
    'put': 'update',
})


schema_id_history_id_rollback = views.HistoryParamsSchemaViewSet.as_view({
    'put': 'update',
})


# router = DefaultRouter()
# router.register(r'orgunits', views.OrgUnitViewSet, basename='orgunit')
# router.register(r'grouppolicies', views.GroupPolicyViewSet)
# router.register(r'users', views.DomainUserViewSet)
# router.register(r'hosts', views.HostViewSet)
# router.register(r'schemas', views.ParamsSchemaViewSet)


urlpatterns = [
    # path('', include(router.urls)),
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
    path('grouppolicy/<int:history_of>/history/', group_policy_id_history, name='group-policy-id-history'),
    path('grouppolicy/<int:history_of>/history/<int:pk>/', group_policy_id_history_id, name='group-policy-id-history-id'),
    path('grouppolicy/<int:history_of>/history/<int:pk>/rollback/', group_policy_id_history_id_rollback, name='group-policy-id-history-id-rollback'),
    path('schema/<str:type>/history/<int:pk>/rollback/', schema_id_history_id_rollback, name='schema-id-history-id-rollback'),
    path('user/<int:pk>/policy/', result_policy_user, name='result-policy-user'),
    path('host/<int:pk>/policy/', result_policy_host, name='result-policy-host'),
    path('schema/<str:type>/history/', schema_id_history, name='schema-id-history'),
    path('schema/<str:type>/history/<int:pk>/', schema_id_history_id, name='schema-id-history-id')
]


