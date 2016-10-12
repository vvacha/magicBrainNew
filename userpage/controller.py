from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from userpage import usefull
import json

#@login_required
def upload_image_tmp(request):

    try:
        filelist = request.FILES.getlist('file')
        res = []
        for file in filelist:

            handle = usefull.handle_uploaded_file(file,str(file).split('.')[-1])
            img = {"source" : handle[0], "size":handle[2], "thumb" : "thumbs_300/" + handle[0], "thumb_size":handle[1]}
            res.append(img)

    except Exception as e:
        print(e)

    res_json = json.dumps(res)
    return HttpResponse(res_json)
