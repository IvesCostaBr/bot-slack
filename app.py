from typing import Text
import slack
from pathlib import Path
import requests
import os
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter



env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


app = Flask(__name__)

# slack_event_adapter = SlackEventAdapter(
#     os.environ['SIGINING_SECRET'],'/slack/events',app)

# client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
# BOT_ID = client.api_call("auth.test")['user_id']


@app.route("/")
def home_view():
    return "<h1>Welcome do Painel Bot Slack</h1>"

# #BOT ACTIONSpip install PyGithub
#         client.chat_postMessage(channel=channel_id , text=text_event)
    

@app.route("/github")
def github_api():
    resp = requests.get("https://github.com/d3estudio/d3-site-environment/pulls?state=all",
                 headers={
                    "Authorization":"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",
                    "Accept":"application/vnd.github.v3+json"
                })
    print(resp)
    return "<h1>Test API</h1>"



if __name__ == "__main__":
    app.run(debug=os.environ['DEBUG'], port="8000")