from django.http.response import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Mutant
import numpy as np
import json as js


class MutantView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    
    # Metodo get
    def get(self, request):
        # Se obtiene la lista de mutantes
        mutants = list(Mutant.objects.all())
        data = []
        for mutant in mutants:
            data.append({
                'dna': mutant.dna
            })
        return JsonResponse(data, safe=False)


    # Metodo post
    def post(self, request):
        # Se obtiene el body de la peticion
        jd = js.loads(request.body)
        dna = jd['dna']
        dna = np.array([list(i) for i in dna])
        try:
            status, mutandDna = self.isMutant(dna)
            if status:
                # Se crea el objeto mutant
                mutant = Mutant(dna=mutandDna)
                mutant.save()
                return HttpResponse(status=200)
        except:
            return HttpResponse(status=403)




    def isMutant(self, dna):
        mutantList = ['AAAA', 'TTTT', 'CCCC', 'GGGG']
        mutant = ''

        #buqueda horizontal
        for y in range(len(dna)):
            for i in range(len(dna[y])):
                mutant += dna[y][i]
            #print('mutant: ', mutant)
            for i in mutantList:
                if mutant.find(i) != -1:
                    #print('mutant hor: ', mutant)
                    return True, mutant
            mutant = ''


        #buqueda vertical
        for x in range(len(dna[0])):
            for i in range(len(dna)):
                mutant += dna[i][x]
            #print('mutant: ', mutant)
            for i in mutantList:
                if mutant.find(i) != -1:
                    #print('mutant ver: ', mutant)
                    return True, mutant
            mutant = ''

        #buqueda cada diagonal
        diags = [dna[::-1,:].diagonal(i) for i in range(dna.shape[0]+1,dna.shape[1])]
        diags2= [dna[::-1,:].diagonal(-i) for i in range(-dna.shape[0]+1,dna.shape[1])]

        diags.extend(dna.diagonal(i) for i in range(dna.shape[1]-1,-dna.shape[0],-1))
        diags2.extend(dna.diagonal(i) for i in range(dna.shape[1]-1,dna.shape[0],-1))
        arr = ([n.tolist() for n in diags])
        arrInv = ([n.tolist() for n in diags2])

        ltr = [str(arr).replace(",","").replace(" ", "").replace("'","").replace("[","").replace("]","|")]
        rtl = [str(arrInv).replace(",","").replace(" ", "").replace("'","").replace("[","").replace("]","|")]

        for i in range(len(arr)):
            for letter in arr[i]:
                mutant += letter
            #print('mutant: ', mutant)
            for i in mutantList:
                if mutant.find(i) != -1:
                    #print('mutant diag: ', mutant)
                    return True
            mutant = ''
        for i in range(len(arrInv)):
            for letter in arrInv[i]:
                mutant += letter
            #print('mutant: ', mutant)
            for i in mutantList:
                if mutant.find(i) != -1:
                    #print('mutant diag: ', mutant)
                    return True, mutant
            mutant = ''
        
        return False