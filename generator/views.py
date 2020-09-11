from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
import json

# Create your views here.


def index(request):
    return render(request, 'generator/index.html')


def password_generator(request):
    character = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    specialCharacters = list("!@#$%^&*()_+?><=-")
    upercaseChar = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    nums = [str(i) for i in range(0, 10)]


    if request.method =='POST':
        email = request.POST.get('email')
        length = int(request.POST.get('lengthSelect', '10'))

        uppercase = request.POST.get('uppercase', 'OFF')
        specialChar = request.POST.get('specialCharacter', 'OFF')
        numbers = request.POST.get('numbers', 'OFF')

        # print(email,length,uppercase, specialChar, numbers)

        if uppercase == 'ON':
            character.extend(upercaseChar)
            uppercaseCounter = 0

        if numbers == 'ON':
            character.extend(nums)
            numberCounter = 0

        if specialChar == 'ON':
            character.extend(specialCharacters)
            specialCounter = 0

        generatedPassword = ''
        for i in range(0, length):
            if (uppercase == 'ON' and uppercaseCounter == 0):
                generatedPassword += random.choice(upercaseChar)
                uppercaseCounter = 1

            elif (numbers == 'ON' and numberCounter == 0):
                generatedPassword += random.choice(nums)
                numberCounter = 1

            elif (specialChar == 'ON' and specialCounter == 0):
                generatedPassword += random.choice(specialCharacters)
                specialCounter = 1

            else:
                generatedPassword += random.choice(character)

        print(character)
        print('new password is ', generatedPassword)

        data = {'email': email, 'generated_password': generatedPassword}

        return JsonResponse(data)