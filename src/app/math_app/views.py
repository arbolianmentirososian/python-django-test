from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def add(request, num1, num2):
    """Calculates the sum of two integer numbers passed into the function.

    Parameters
    ----------
        num1: int
            The first number.
        num2: int
            The second number.
    
    Returns
    -------
        JSON
            JSON containing values of passed in numbers and their sum.
    """
    response = {
        "num1": num1,
        "num2": num2,
        "num1 + num2": num1 + num2
    }

    return Response(response, status=status.HTTP_200_OK)