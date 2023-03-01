import os, random, json, requests, sched
from InstagramAPI import InstagramAPI
from time import sleep, time
from requests_toolbelt import MultipartEncoder

def readConfig():
    filename = "config.json"
    if filename:
        with open(filename, 'r') as f:
            cfg = json.load(f)
    return cfg  

def loginIG(username, password):
    ig = InstagramAPI(username, password)

    if (ig.login()):
        print("Logged into Instagram")
    else:
        print("Failed to log into Instagram")
    
    return ig

def postPhoto(interval, caption, ig_api):
    rndPhoto = random.choice(os.listdir("photos"))
    rndPath = 'photos/' + rndPhoto

    post = ig_api.uploadPhoto(rndPath, caption)
    
    if post:
        print("posted photo")
    else:
        print("post failed")
   
    

def main():
    igUsername = readConfig()['username']
    igPassword = readConfig()['password']
    igCaption = readConfig()['caption']
    postInterval = readConfig()['interval']

    api = loginIG(igUsername, igPassword) # Log into Instagram
    s = sched.scheduler(time, sleep) # Create scheduler for schedueled posts
    s.enter(60, 1, postPhoto(postInterval, igCaption, api), (s,))  # (delay, priority, action, argument)

if __name__ == "__main__":
    main()
