from rest_framework import exceptions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from mainapp.models import(
    Worker, TradePoint, Visit
)
from mainapp.serializers import(
    WorkerSerializer, TradePointSerializer,
    TradePointReadSerializer, PhoneSerializer,
    VisitSerializer
)

class WorkerCreateAPIView(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    
    @action(methods=['get', 'post'], detail=False, serializer_class=PhoneSerializer)
    def get_trade_points(self, request, *args, **kwargs):
        if request.method == "POST":
            serializer = PhoneSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            phone = serializer.validated_data['phone_number']
            data = TradePoint.objects.filter(worker__phone_number=phone)
            serializer = TradePointReadSerializer(instance=data, many=True) 
            return Response(serializer.data)
        return Response({"message": 'Введите ваш номер телефона'})
    
class TradePointCreateAPIView(CreateAPIView):
    queryset = TradePoint.objects.all()
    serializer_class = TradePointSerializer
        
        
class VisitModelViewSet(ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer