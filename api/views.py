from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SerialNumberSerializer
from .models import SerialNumber

class SerialNumberAPIView(APIView):
    def post(self, request):
        serializer = SerialNumberSerializer(data=request.data)

        if serializer.is_valid():
            serial_numbers = serializer.validated_data['serialNumber']
            results = []

            for sn in serial_numbers:
                if sn.startswith(('BN', 'MZ', 'AD')) and len(sn) <= 10:
                    # Проверка на уникальность
                    if not SerialNumber.objects.filter(serial_number=sn).exists():
                        # Сохранение валидного серийного номера в базу данных
                        SerialNumber.objects.create(serial_number=sn)

                    results.append({
                        "serialNumber": sn,
                        "success": True,
                        "message": "SUCCESS"
                    })
                else:
                    results.append({
                        "serialNumber": sn,
                        "success": False,
                        "message": f"Invalid serial number: {sn}"
                    })

            # Возвращаем результаты проверки
            return Response(results, status=status.HTTP_200_OK)

        # Если есть ошибки в формате входных данных
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # Получение всех серийных номеров из базы данных
        all_serial_numbers = SerialNumber.objects.all()
        serialized_data = [{"serial_number": sn.serial_number} for sn in all_serial_numbers]
        return Response(serialized_data, status=status.HTTP_200_OK)
