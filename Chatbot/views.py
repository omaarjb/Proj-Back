import openai
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Message
from .serializers import MessageSerializer

@api_view(['POST'])
def chat_view(request):
    if request.method == 'POST':
        user_message = request.data.get('message')

        if not user_message:
            return Response({'error': 'Message is required'}, status=400)

        # Send user message to OpenAI API for generating bot response
        openai.api_key = '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'
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-0125", 
            prompt=user_message, 
            max_tokens=50
        )
        bot_response = response.choices[0].text.strip()

        # Save user message
        serializer = MessageSerializer(data={'text': user_message, 'sender': 'user'})
        if serializer.is_valid():
            serializer.save()

        # Save bot response
        Message.objects.create(text=bot_response, sender='bot')

        return Response({'message': bot_response})
