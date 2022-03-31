from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


divisions_list = views.DivisionViewSet.as_view({
    'get': 'list',
}
)

division_post_detail = views.DivisionViewSet.as_view({
    'post': 'create',
})


division_detail = views.DivisionViewSet.as_view({
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

users_list = views.DomenUserViewSet.as_view({
    'get': 'list',
})

user_post_detail = views.DomenUserViewSet.as_view({
    'post': 'create',
})

user_detail = views.DomenUserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

computers_list = views.ComputersViewSet.as_view({
    'get': 'list',
})

computer_post_detail = views.ComputersViewSet.as_view({
    'post': 'create',
})

computer_detail = views.ComputersViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

schemas_list = views.SchemaParamsViewSet.as_view({
    'get': 'list',
})

schema_post_detail = views.SchemaParamsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})




router = DefaultRouter()
router.register(r'divisions', views.DivisionViewSet)
router.register(r'grouppolicies', views.GroupPolicyViewSet)
router.register(r'users', views.DomenUserViewSet)
router.register(r'computers', views.ComputersViewSet)
router.register(r'schemas', views.SchemaParamsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('divisions/', divisions_list, name='division-list'),
    path('division/', division_post_detail, name='divison-post-detail'),
    path('division/<int:pk>', division_detail, name='divison-id'),
    path('grouppolicies/', group_policies_list, name='group-policies-list'),
    path('grouppolicy/', group_policy_post_detail, name='group-policy-post-detail'),
    path('grouppolicy/<int:pk>', group_ploicy_detail, name='group-policy-detail'),
    path('users/', users_list, name='users-list'),
    path('user/', user_post_detail, name='user-post-detail'),
    path('user/<int:pk>', user_detail, name='user-detail'),
    path('computers/', computers_list, name='computers-list'),
    path('computer/', computer_post_detail, name='computer-post-detail'),
    path('computer/<int:pk>', computer_detail, name='computer-detail'),
    path('schemas/', schemas_list, name='schemas-list'),
    path('schema/<int:pk>', schema_post_detail, name='computer-detail'),
]


