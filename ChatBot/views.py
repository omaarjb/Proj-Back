from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Message
from .serializers import MessageSerializer
import google.generativeai as genai

@api_view(['POST'])
def chat_view(request):
    if request.method == 'POST':
        user_message = request.data.get('message')

        if not user_message:
            return Response({'error': 'Message is required'}, status=400)

        # Generate response using Gemini API
        response = generate_gemini_response(user_message)
        bot_response = response

        # Save user message
        serializer = MessageSerializer(data={'text': user_message, 'sender': 'user'})
        if serializer.is_valid():
            serializer.save()

        # Save bot response
        Message.objects.create(text=bot_response, sender='bot')

        return Response({'message': bot_response})

def generate_gemini_response(prompt):
    GOOGLE_API_KEY = 'AIzaSyDNSYp3CCxHm9CQ8OsfnvYpHb_qiq6-jlk'
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    result = ''.join([p.text for p in response.candidates[0].content.parts])
    return result
