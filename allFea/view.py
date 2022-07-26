from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def capital(request):
    getInpTextArea = request.GET.get('text', 'default')
    getInpCheckBox = request.GET.get('checkbox1', 'off')
    getInpCheckBox2 = request.GET.get('checkbox2', 'off')
    getInpCheckBox3 = request.GET.get('checkbox3', 'off')
    getInpCheckBox4 = request.GET.get('checkbox4', 'off')
    # print(getInpTextArea)
    # print(getInpCheckBox)
    # print(getInpCheckBox2)
    if  getInpCheckBox == 'on':
        capitalized = ''
        for char in getInpTextArea:
            capitalized = capitalized + char.upper()
        PM = {'capital':capitalized}
        return render(request, 'capital.html', PM)

    elif getInpCheckBox2 != 'off':
        punc = '''£¬!@#$%^&*)(_+-={]}[:;"'|\?/>.<,~`'''
        removeP = ""
        for char in getInpTextArea :
            if char not in punc:
                removeP = removeP + char
        RP = {'removepunt':removeP}
        # print(removeP)
        return render(request, 'capital.html', RP)

    elif getInpCheckBox3 == 'on':
        remNL = ''
        for char in getInpTextArea:
            if char not in '\n':
                remNL = remNL + char
        RNL = {'removenewline':remNL}
        return render(request, 'capital.html', RNL)
    elif getInpCheckBox4 == 'on':
        capti = ''
        capti = getInpTextArea.capitalize() 
        CP = {'firstCapital':capti}
        return render(request, 'capital.html', CP)
    
    else:
        return HttpResponse('Error')