from django.conf import settings
from django.contrib import admin
from django.urls import path, include


from recipes.views import create_recipe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('blog/', include('blog.urls')),
    path('recipes/create/', create_recipe, name="create_recipe"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
