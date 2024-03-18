import os
from livekit import api
from flask import Flask

app = Flask(__name__)

@app.route('/token')
def getToken():
  token = api.AccessToken(os.getenv('LIVEKIT_API_KEY'), os.getenv('LIVEKIT_API_SECRET')) \
    .with_identity("raspberry") \
    .with_name("Raspberry") \
    .with_grants(api.VideoGrants(
        room_join=True,
        room="rccar",
    ))
  return token.to_jwt()

if __name__ == "__main__":
    app.run(host='0.0.0.0')