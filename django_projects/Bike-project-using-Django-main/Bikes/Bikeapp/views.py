# from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout
# from Bikeapp.models import Useradd,Contact
# from django.contrib.auth.decorators import login_required

url="https://www.bikewale.com/bajaj-bikes/"
resp=requests.get(url).content
print(resp)
# soup=BeautifulSoup(resp,'html.parser')
# # print(soup)
# links=soup.find_all("a",class_="o-cpnuEd o-SoIQT o-eZTujG o-fzpilz")
# # print(links)
# bajlink=[]
# for i in links:
#     d="https://www.bikewale.com/"+i["href"]
#     bajlink.append(d)
#     # print(bajlink)
# pricess=soup.find_all("span",class_="o-eZTujG o-byFsZJ o-bkmzIL o-bVSleT")
# # print(pricess)
# price=[]
# for j in pricess:
#     d=j.get_text()
#     price.append(d)
# # print(price)
# titles=soup.find_all("h3",class_="o-jjpuv o-cVMLxW o-mHabQ o-fzpibK")
# # print(titles)
# title=[]
# for i in titles:
#     d=i.get_text()
#     title.append(d)
# # print(title)
    

# images=soup.find_all("img",class_="o-bXKmQE o-cgkaRG o-cQfblS o-bNxxEB o-pGqQl o-wBtSi o-bwUciP o-btTZkL o-bfyaNx o-eAZqQI")
# # print(images)
# image=[]
# for i in images:
#     d=i["src"]
#     image.append(d)
# # print(image)

# mylist=zip(bajlink,
#            price,
#            title,
#            image
#            )
# # print(mylist)
# def bajaj(request):
#     return render(request,"bajaj.html",{'mylist':mylist})




# url1="https://www.zigwheels.com/upcoming-bikes"
# resp1=requests.get(url1).content
# # print(resp1)
# soup1=BeautifulSoup(resp1,'html.parser')
# # print(soup1)


# links1=soup1.find_all("a",class_="")
# # print(links1)
# link1=[]
# for w in links1:
#     e="https://www.zigwheels.com/"+w["href"]
#     link1.append(e)
# # print(link1)






# images1=soup1.find_all("img",class_="lazy_image i-b c-p")
# # print(images1)
# image1=[]
# for i in images1:
#     j=i['src']
#     image1.append(j)
# # print(image1)

# titles1=soup1.find_all("strong",class_="lnk-hvr block of-hid h-height")
# # print(titles1)
# title1=[]
# for i in titles1:
#     s=i.get_text()
#     title1.append(s)
# # print(title1)
# prices1=soup1.find_all("div",class_="b fnt-15")
# # print(prices1)
# price1=[]
# for l in prices1:
#     d=l.get_text()
#     price1.append(d)
# # print(price1)

# mylist1=zip(image1,
#             title1,
#             price1,
#             link1
#             )
# # print(mylist1)


# @login_required(login_url='login')
# def bike(request):
#     return render(request,"base.html",{'mylist1':mylist1})

# def contact(request):
#     return render(request,"contact.html")


# url2="https://www.autocarindia.com/new-bikes"
# resp2=requests.get(url2).content
# # print(resp2)

# soup2=BeautifulSoup(resp2,'html.parser')

# # print(soup2)

# links2=soup2.find_all("a",class_="")
# # print(links2)
# link2=[]
# for i in links2:
#     a="https://www.autocarindia.com/"+i['href']
#     link2.append(a)
# # print(link2)

# titles2=soup2.find_all("h3",class_="heading-h4")

# # print(titles2)
# title2=[]
# for i in titles2:
#     e=i.get_text()
#     title2.append(e)
# # print(title2)


# prices2=soup2.find_all("h4",class_="price-model")
# # print(prices2)
# price2=[]
# for g in prices2:
#     h=g.get_text()
#     price2.append(h)
# # print(price2)



# images2=soup2.find_all("img",class_="img-fluid listing-img-car")
# # print(images2)
# image2=[]
# for i in images2:
#     s=i['src']
#     image2.append(s)
# # print(image2)

# mylist2=zip(image2,price2,title2,link2)
# # print(mylist2)

# def hero(request):
#     return render(request,"hero.html",{'mylist2':mylist2})


# url3="https://www.zigwheels.com/honda-bikes"
# resp3=requests.get(url3)
# # print(resp3)
# soup3=BeautifulSoup(resp3.content,'html.parser')
# # print(soup3)
# images3=soup3.find_all("img",class_="i-b c-p")
# # print(images3)
# image3=[]
# for i in images3:
#     j=i['src']
#     image3.append(j)
# # print(image3)

# links3=soup3.find_all("a",class_="")
# # print(links3)
# link3=[]
# for i in links3:
#     k="https://www.zigwheels.com/"+i['href']
#     link3.append(k)
# # print(link3)

# titles3=soup3.find_all("h3",class_="lnk-hvr fnt-16 b block of-hid h-height ml-0 mb-0-imp")
# # print(titles3)
# title3=[]
# for h in titles3:
#     i=h.get_text()
#     title3.append(i)
# # print(title3)


# prices3=soup3.find_all("div",class_="clr-bl")
# # print(prices3)
# price3=[]
# for y in prices3:
#     z=y.get_text()
#     price3.append(z)
# # print(price3)
# mylist3=zip(
#     image3,
#     link3,
#     title3,
#     price3
# )
# print(mylist3)

# def honda(request):
#     return render(request,"honda.html",{'mylist3':mylist3})


# def login_user(request):
#     if request.method=="POST":
#         username=request.POST.get("username")
#         password=request.POST.get("password")
#         user=authenticate(username=username,password=password)
#         if user is not None:
#             login(request,user)
#         return redirect("home")
#     return render(request,"login.html")
# def register(request):
#     if request.method=="POST":
#         username=request.POST.get("username")
#         password=request.POST.get("password")
#         email=request.POST.get("email")
#         c=User.objects.create_user(username=username,email=email,password=password)
#         c.save()
#         return redirect("login")
#     return render(request,"register.html")

# def logout_user(request):
#     logout(request)
#     return redirect("login")


# def contact(request):
#     if request.method=="POST":
#        name=request.POST['name']
#        email=request.POST['email']
#        message=request.POST['message']
       
       
       
#        c=Contact(name=name,email=email,message=message)
#        c.save()
#        return redirect("home")
#     return render(request,"contact.html")
