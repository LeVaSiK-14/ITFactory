from django.urls import path
from rest_framework.routers import SimpleRouter
from mainapp.views import(
    WorkerCreateAPIView, TradePointCreateAPIView,
    VisitModelViewSet
)

router = SimpleRouter()
router.register('workers', WorkerCreateAPIView)
router.register('visits', VisitModelViewSet)

urlpatterns = [
    path('trade_points/', TradePointCreateAPIView.as_view(), name='trade_point'),
]

urlpatterns += router.urls