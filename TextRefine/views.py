from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newline = request.POST.get('newline', 'off')
    extraspace = request.POST.get('extraspace', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Changed To UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed

    if newline == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspace == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed += char
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == 'on':
        params = {'purpose': 'Characters Counted',
                  'analyzed_text': djtext, 'chars': f"Your text contains {len(djtext)} characters."}

    if(removepunc != 'on' and fullcaps != 'on' and newline != 'on' and extraspace != 'on' and charcount != 'on'):
        return HttpResponse("Please select atleast one operation!")

    return render(request, 'analyze.html', params)
