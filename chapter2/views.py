from django.shortcuts import render

# Create your views here.

from . import chapter2_exe
from .froms import URLForm

def index(request):

    params ={'link_list' :['index', '_2_3']}
    return render(request, "chapter2/index.html", params)

def _2_3(request):
    params = {'section': 3}
    if request.method == 'POST':
        url = request.POST['url']
        data = chapter2_exe._2_3(url)
        params["data"] = data
        params["form"] = URLForm(request.POST)
    else:
        params["form"] = URLForm()
        params["text"] = "Please Input URL"
    return render(request, "chapter2/_2_3.html", params)

