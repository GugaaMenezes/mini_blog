from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def insert_article(request):
    return render(request, 'insert_article.html')


@csrf_exempt
def generate_token(request):
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            access_token = data.get('accessToken')
                        
            response_data = {
                'access_token': access_token,
                'message': 'Token gerado com sucesso',
            }
            
            return JsonResponse(response_data, status=200)

        except Exception as e:
            error_message = str(e)
            return JsonResponse({'error': error_message}, status=401)

    return render(request, 'generate_token.html')
