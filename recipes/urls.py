from recipes.views import create_recipe
from django.urls import path
from . import views


urlpatterns = [

    path("create/", views.create_recipe, name="create_recipe"),
    # path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.recipes_detail, name="recipes_detail"),
    path("<category>/", views.recipes_category, name="recipes_category"),
]
#     path('admin/', admin.site.urls),
#     path('recipes/create/', create_recipe, name="create_recipe"),
# ]

# , create_recipe, name="create_recipe")