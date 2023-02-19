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
    
#  extracting vidos files and storing in videos folder
files = os.listdir('./{}/'.format(profileid))
files = [file for file in files if file.endswith(".mp4")]
if 'videos' in os.listdir('./{}/'.format(profileid)):
    print('Dir is already present')
else:
    os.mkdir('./{}/videos/'.format(profileid))
    print('Video folder created.')
    
print("Moving Files to videos dir")
for file in files:
    if not file in os.listdir('./{}/videos/'.format(profileid)):
        os.replace('./{}/'.format(profileid) + file,'./{}/videos/'.format(profileid) + file)
print('Completed')


# extracting text files and storing in textx folder
files = os.listdir('./{}/'.format(profileid))
files = [file for file in files if file.endswith(".txt")]
if 'texts' in os.listdir('./{}/'.format(profileid)):
    print('Dir is already present')
else:
    os.mkdir('./{}/texts/'.format(profileid))
    print('texts folder created.')
    
print("Moving Files to texts dir")
for file in files:
    if not file in os.listdir('./{}/texts/'.format(profileid)):
        os.replace('./{}/'.format(profileid) + file,'./{}/texts/'.format(profileid) + file)
print('Completed')
