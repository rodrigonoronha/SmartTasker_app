from rest_framework.views import APIView
from ai.models import AIResult
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from rest_framework import response, status


class AICommentAPIView(APIView):
    queryset = AIResult.objects.all()
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)

    def get(self, request):
        last_ia_comment = self.queryset.values('result').first()

        return response.Response(
            data={'result': last_ia_comment}['result'],
            status=status.HTTP_200_OK,
        )
