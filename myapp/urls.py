from django.urls import path
from rest_framework_nested import routers
from .views import FileDataViewSet, FileScoreListView

router = routers.DefaultRouter()
router.register(r'files', FileDataViewSet, basename='files')

urlpatterns = [
    path('score/<str:score_field>/', FileScoreListView.as_view(), name='file-score-list'),
]

urlpatterns += router.urls