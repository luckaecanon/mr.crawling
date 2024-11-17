from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound

posts = [
    {
        "id": 1,
        "title": "django - eto veb freimwork",
        "content": "kgj khgg hk,hgk k ghk g",
    },
    {
        "id": 2,
        "title": "qwertyuio",
        "content": "dfghjk",
    },

]

def aaaaa(request):
    return HttpResponse("Hello World!")

# def home(request):
#     html = ""
#     for post in posts:
#         html += f"""
#                <div>
#                <a href=""></a>
#                   <h1>{post["id"]} - {post["title"]}</h1>
#                   </a>
#                   <p>{post["contentet"]}</p>
#               </div>
#                """
#     return HttpResponse(html)

def home(request):
#     html = ""
#     for post in posts:
#         html += f"""
#                 <div>
#                     <a href="">
#                         <h1>{post["id"]} - {post["title"]}</h1>
#                     </a>
#                     <p>{post["content"]}</p>
#                 </div>
#                 """
# #
    return render(request, "posts/home.html", {"posts": posts})
#
#
def post(request, id):  # id=5
    valid_id = False
    for post in posts:
        if post["id"] == id:  # posts/1
            post_dict = post
            valid_id = True
            break
    if valid_id:
        # html = f"""
        #         <div>
        #             <h1>{post_dict["id"]}</h1>
        #             <p>{post_dict["main"]}</p>
        #         </div>
        #         """
        return render(request, "posts/posts.html",{"post_dict":post_dict})
    else:
        return HttpResponseNotFound("Пост не найден 💀")
