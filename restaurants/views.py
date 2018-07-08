from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"my_list": [
            {
                "restaurant_name":"Burgers",
                "Food_type":"American",
            },
            {
                "restaurant_name":"Pizza",
                "Food_type":"Italian",
            },
            {
                "restaurant_name":"Taccos",
                "Food_type":"Mexican",
            },
        ],

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {'restaurant_name' : 'Lorenzo'

    }
    return render(request, 'detail.html', context)
