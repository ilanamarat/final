from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from core.views import BooksViewSet, JournalDetailsViewSet, JournalsViewSet
urlpatterns = [
    path('auth/login', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('books/', BooksViewSet.as_view({'get':'list'})),
    path('journals/', JournalDetailsViewSet.as_view({'get':'list'})),
    path('journals/<int:id>/delete/', JournalsViewSet.as_view({'delete':'destroy'}) ),
    path('journals/<int:id>/', JournalDetailsViewSet.as_view({'get':'get_item'}) ),
    path('journals/create/', JournalsViewSet.as_view({'put':'create'}) ),
    path('journals/<int:id>/update/', JournalsViewSet.as_view({'post':'update'}) ),
]
