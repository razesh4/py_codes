from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        userid = request.POST.get('name_url')
    
    beg, sep, end = userid.partition('.com/')
    a = end.strip('/')
    context = {
        'var' : a
    }

    import instaloader
    L = instaloader.Instaloader()
    # L.login("")
    # profileID = input('Enter the userid of the profile: ')
    profileID = a # you can uncomment the above line and input the value to search
    profile = instaloader.Profile.from_username(L.context, profileID)
    def getBasicInfo():
        print('Username: ',profile.username)
        print('UserID: ',profile.userid)
        print('No. of Posts: ',profile.mediacount)
        print('No. of Followers: ',profile.followers)
        print('No. of Followings: ',profile.followees)
        print('Bio :',profile.biography)
        print('Other URLs: ',profile.external_url)
        return [profile.username,profile.userid,profile.mediacount,profile.followers,profile.followees,profile.biography]

    context['var2'] = getBasicInfo()
    # if getBasicInfo():
    #     context['one'] = profile.username
    #     context['two'] = profile.userid
    #     context['three'] = profile.mediacount
    #     context['four'] = profile.followers
    #     context['five'] = profile.followees
    #     context['six'] = profile.biography
    #     context['seven'] = profile.external_url

    return render(request,'index.html',context)
    # return HttpResponse('This is homepage')