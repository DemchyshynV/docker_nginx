import uuid
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.generics import CreateAPIView

from .models import InviteModel
from .serializers import InviteSerializer


class CustomInvalidToken(InvalidToken):
    status_code = status.HTTP_403_FORBIDDEN


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise CustomInvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class CreateInviteView(CreateAPIView):
    queryset = InviteModel.objects.all()
    serializer_class = InviteSerializer

    def perform_create(self, serializer):
        serializer.save(uuid=uuid.uuid1())
        super().perform_create(serializer)

