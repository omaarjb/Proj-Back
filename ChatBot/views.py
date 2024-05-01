from django.shortcuts import render
from rest_framework import status
# Create your views here.
from rest_framework.response import Response 
from rest_framework.decorators import api_view 
from .models import Message
from .serializers import MessageSerializer
import google.generativeai as genai
from Produits.models import Produit
from Categorie.models import Categorie




@api_view(['POST'])
def chat_view(request):
    if request.method == 'POST':
        user_message = request.data.get('message')

        if not user_message:
            return Response({'error': 'Message is required'}, status=400)

        # Generate response using Gemini API
        prompt = firstChatBotPrompt()
        prompt_message = f"""
            {prompt}\n
            now answer this message: {user_message}\n

        """
        response = generate_gemini_response(prompt_message)
        bot_response = response

        # Save user message
        serializer = MessageSerializer(data={'text': user_message, 'sender': 'user'})
        if serializer.is_valid():
            serializer.save()

        # Save bot response
        Message.objects.create(text=bot_response, sender='bot')

        return Response({'message': bot_response})
    
@api_view(['DELETE'])
def delete_all(request):
    if request.method == 'DELETE':
        Message.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def startChatBot(request):
    response = firstChatBotPrompt()
    if response:
        return Response(status=status.HTTP_200_OK)

def generate_gemini_response(prompt):
    GOOGLE_API_KEY = 'AIzaSyDNSYp3CCxHm9CQ8OsfnvYpHb_qiq6-jlk'
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    result = ''.join([p.text for p in response.candidates[0].content.parts])
    return result


def firstChatBotPrompt():
    electronics_category = Categorie.objects.get(Id_categorie=1)
    jewelery_category = Categorie.objects.get(Id_categorie=2)
    men_category = Categorie.objects.get(Id_categorie=3)
    women_category = Categorie.objects.get(Id_categorie=4)

    electronics = Produit.objects.filter(category=electronics_category)
    jeweleries = Produit.objects.filter(category=jewelery_category)
    men_clothing = Produit.objects.filter(category=men_category)
    women_clothing = Produit.objects.filter(category=women_category)

    electronics_info = ""
    for product in electronics:
        electronics_info += f"{product.title}: {product.description}\n"

    jeweleries_info = ""
    for product in jeweleries:
        jeweleries_info += f"{product.title}: {product.description}\n"

    men_clothing_info = ""
    for product in men_clothing:
        men_clothing_info += f"{product.title}: {product.description}\n"

    women_clothing_info = ""
    for product in women_clothing:
        women_clothing_info += f"{product.title}: {product.description}\n"
    

    prompt = f"""
        You are a chatbot in an e-commerce website named Bi3smart we sell men clothing, women clothing, jewelleries and Electronics, the upcoming prompts are from the user visiting the website.
        I.	the user might ask about our products:
            1)	Men's clothing:
                {men_clothing_info}
            2)	Women's clothing:
                {women_clothing_info}
            3)	Jewelleries:
                {jeweleries_info}
            4)	Electronics: 
                {electronics_info}

        II.	The user might Ask where we deliver our Product:
            We ship our products all across Morocco
        III.	Payement methods?
            Visa, MasterCard and paypal
    """
    # print(prompt)
    return prompt
