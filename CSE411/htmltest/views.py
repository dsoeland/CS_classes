from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("""<h1>Title #1</h1><p>I need to have an activity about HTML before starting this unit as it will help 
    people better understand the value of what they are doing. So far, we just mindlessly copy and paste 
    everything from the acitivity into the code without being forced to understand or truly use the code. 
    I fear most students are not even understanding what they are doing.</p><p>Wacka Wacka</p>
    <h2>Title #2</h2>
    <h3>Title #3</h3>
    <a href="http://www.w3schools.com">The best place for HTML help</a>
    
    <form><input type="text"><br><input type="text"><br><input type="submit"></form>
    """)