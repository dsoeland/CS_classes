from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.

@csrf_exempt
def index(request):
    output = ""
    if request.method == "POST":
        user_submission = Post()
        user_submission.post_title = request.POST.__getitem__("posttitle")
        user_submission.post_text = request.POST.__getitem__("posttextbox")
        user_submission.pub_date = datetime.datetime.now()
        user_submission.save()
        output = "<p>Thank you for post, everyone will be uplifted by your thoughts!</p>"
        output = output + '<div class="homey"><form action="/blog/" method="dirty">'
        output = output + '<input type="submit" value="My Posts"/></form></div>'
        return HttpResponse(output)
    else:
        '''Post list is needed'''
        
        post_list = Post.objects.order_by('-pub_date')
        
        '''CSS stuff to make the page look a bit better without a CSS file'''
        
        output = '<head><title>Blog Page</title>'
        output = output + '<style>'
        output = output + 'h1{ text-align: center; }'
        output = output + 'h2{ text-align: center; }'
        output = output + 'h3{ margin-top: 10px; margin-bottom: 10px; }'
        output = output + '.butt{ margin-top: 5px; }'
        output = output + '.box{ width: 180px; margin: auto; border: 3px solid green; padding: 10px;}'
        output = output + '.homey{ width: 125px; margin: auto; padding: 10px;}'
        output = output + 'b{ padding-left: 20px; }'
        output = output + '</style></head>'
        
        '''Needed so that you know what page your on and to provided the useful information'''
        
        output = output + '<header><h1>My Blog</h1>'
        output = output + '<h2>What do my addoring fans have to say?!</h2></header>'
        
        for p in post_list:
            output = output + '<h3>' + p.post_title + '</h3>'
            output = output + '<b>' + "Date and time: " + '</b>' + str(p.pub_date)
            output = output + '<b>' + "    Post information: " + '</b>' + p.post_text + '<br>'
        
        output = output + '<div class="homey">'    
        output = output + '<a class="button" href="/blog/submission/">Submit Blog Post</a><p></div>'
    return HttpResponse(output)
    
    
@csrf_exempt    
def submission(request):
    output = ''
    output = '<head><title>Submission Page</title>'
    output = output + '<style>'
    output = output + 'h1{ text-align: center; }'
    output = output + 'h2{ text-align: center; }'
    output = output + 'h3{ margin-top: 10px; margin-bottom: 10px; }'
    output = output + '.butt{ margin-top: 5px; }'
    output = output + '.box{ width: 180px; margin: auto; border: 3px solid green; padding: 10px;}'
    output = output + '.homey{ width: 60px; margin: auto; padding: 10px;}'
    output = output + '</style></head>'
    output = output + '<h1>What do you have to say?</h1>'
    output = output + '<h2>Fill in the boxes down below to leave me your username and a short message.</h2>'
    output = output + '<div class="box">'
    output = output + '<form action="/blog/" method="post">'
    output = output + '<h3>Post Title</h3> <input type="textarea" name="posttitle" id="posttitle"/>'
    output = output + '<h3>Post Content</h3> <input type="textarea" name="posttextbox" id="posttextbox"/>'
    output = output + '<input class="butt" type="submit" value="Submit Post"/>'
    output = output + '</form></div>'
    output = output + '<div class="homey"><form action="/blog/" method="dirty">'
    output = output + '<input type="submit" value="My Posts"/></form></div>'
    return HttpResponse(output)