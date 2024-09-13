from django.shortcuts import render
from .models import CarDescription

# Create your views here.

def index(request):

    '''
    desc1 = CarDescription()
    desc1.name = "BMW 6-series gran coupe"
    desc1.img = "fc1.png"
    desc1.price = "$69,100"
    desc1.description = "Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non."
    desc1.model = 2017
    desc1.miles = 3100
    desc1.horsepower = 240
    desc1.auto = True

    desc2 = CarDescription()
    desc2.name = "chevrolet camaro wmv20"
    desc2.img = "fc2.png"
    desc2.price = "$66,575"
    desc2.description = "Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non."
    desc2.model = 2017
    desc2.miles = 3100
    desc2.horsepower = 240
    desc2.auto = False

    desc3 = CarDescription()
    desc3.name = "lamborghini v520"
    desc3.img = "fc3.png"
    desc3.price = "$125,250"
    desc3.description = "Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non."
    desc3.model = 2017
    desc3.miles = 3100
    desc3.horsepower = 240
    desc3.auto = False

    desc4 = CarDescription()
    desc4.name = "audi a3 sedan"
    desc4.img = "fc4.png"
    desc4.price = "$95,500"
    desc4.description = "Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non."
    desc4.model = 2017
    desc4.miles = 3100
    desc4.horsepower = 240
    desc4.auto = True

    desc5 = CarDescription()
    desc5.name = "infiniti z5"
    desc5.img = "fc5.png"
    desc5.price = "$36,850"
    desc5.description = "Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non."
    desc5.model = 2017
    desc5.miles = 3100
    desc5.horsepower = 240
    desc5.auto = False

    desc6 = CarDescription()
    desc6.name = "porsche 718 cayman"
    desc6.img = "fc6.png"
    desc6.price = "$48,500"
    desc6.description = "Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non."
    desc6.model = 2017
    desc6.miles = 3100
    desc6.horsepower = 240
    desc6.auto = False

    desc7 = CarDescription()
    desc7.name = "bmw 8-series coupe"
    desc7.img = "fc7.png"
    desc7.price = "$56,000"
    desc7.description = "Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non."
    desc7.model = 2017
    desc7.miles = 3100
    desc7.horsepower = 240
    desc7.auto = True

    desc8 = CarDescription()
    desc8.name = "BMW x series-6"
    desc8.img = "fc8.png"   
    desc8.price = "$75,800"
    desc8.description = "Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non."
    desc8.model = 2017
    desc8.miles = 3100
    desc8.horsepower = 240
    desc8.auto = False

    descs = [desc1, desc2, desc3, desc4, desc5, desc6, desc7, desc8]
    '''

    descs = CarDescription.objects.all()

    return render(request, 'index.html', {
    'descs': descs,
})