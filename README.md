This is drunkdroid. He gets a little annoying sometimes. His favourite pastime is watching pidits suffer.

**List of available commands:**

**_.ddhelp_** (display list of available commands)<br>
**_.ddping_** (display latency)<br>
**_.ping @username_** (ping specified user 5 times every 3 seconds)<br>
**_.ultraping @username_** (ping specified user 10 times every second)<br>
**_.dogfact_** (display random dog facts)<br>
**_.dogpic_** (display random dog pictures)

drunkdroid also likes to interrupt users with random facts while they are typing. 

drunkdroid is currently hosted in heroku. Heroku's GitHub integration is messed up currently hence immediate automatic deployment after commit in this repo is not supported. 

So, open up a terminal. Clone the repo using **git clone https://github.com/w1ndro1d/DrunkDroid_bot.git**. Change directory to the directory where you cloned using cd. Install Heroku CLI. Login using **heroku login**. A remote called drunkdroid has already been created. In case another needs to be created, use **heroku git:remote -a drunkdroid**. Check status of various available remotes using **git remote -v**. Perform modifications to the code locally and when ready to push, use **git commit -am "comment"** to commit. Finally, use **git push heroku** to push onto Heroku Git.
