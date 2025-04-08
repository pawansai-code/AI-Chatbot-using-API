from django.shortcuts import render
from django.http import JsonResponse
from groq import Groq
import json
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'home.html')


@csrf_exempt
def get_response(request):
    if (
        request.method == 'POST' and
        request.headers.get('Content-Type') ==
        'application/json'
    ):
        data = json.loads(request.body)
        user_input = data.get('message', '')  # The text user sent
        api_key = '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'
        client = Groq(api_key=api_key)
        prompt = user_input
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.5,
        )
        result = response.choices[0].message.content
        return JsonResponse({'response': result}, status=500)
