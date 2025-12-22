from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate(request):
    return Response({'message': 'generate ok'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save(request):
    return Response({'message': 'save ok'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mine(request):
    return Response([])

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove(request, package_id):
    return Response(status=status.HTTP_204_NO_CONTENT)
