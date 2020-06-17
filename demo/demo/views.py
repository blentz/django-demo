from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthView(APIView):
    """Provide the server status information."""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Return the server status."""
        return Response(True)
