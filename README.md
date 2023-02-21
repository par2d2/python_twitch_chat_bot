Set up 

You will need to install python 3.7 on your machine for this to work. 
If your looking to change the code you will need an IDE pycharm is very good and free to use.

Request an oauth code. You'll need to login and give the app permissions to generate it for you. I used this URL https://twitchapps.com/tmi/

https://dev.twitch.tv/console/apps/create use this url to create an app and get a client ID once you created it you can go in and get the settings. 

Change the file named .env.example to .env and change the details 

run 
- pip install pipenv
- pipenv install
- pipenv run python bot.py <-- this command will start your chat bot 