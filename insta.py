import instaloader
import os


L = instaloader.Instaloader()
# L.login("")
# profileID = input('Enter the userid of the profile: ')
profileID = "abdul_______110" # you can uncomment the above line and input the value to search
profile = instaloader.Profile.from_username(L.context, profileID)
def getBasicInfo():
    print('Username: ',profile.username)
    print('UserID: ',profile.userid)
    print('No. of Posts: ',profile.mediacount)
    print('No. of Followers: ',profile.followers)
    print('No. of Followings: ',profile.followees)
    print('Bio :',profile.biography)
    print('Other URLs: ',profile.external_url)

getBasicInfo()

L.download_profile(profileID)

# for txt files
files_txt = [x for x in os.listdir('./{}'.format(profileID)) if x.endswith(".txt")]
for file in files_txt:
    print(file)

# for video files
files_txt = [x for x in os.listdir('./{}'.format(profileID)) if x.endswith(".mp4")]
for file in files_txt:
    print(file)
