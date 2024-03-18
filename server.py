import os
from livekit import api
from flask import Flask, request

app = Flask(__name__)

@app.route('/token')
def getToken():
    participant_identity = request.headers.get('identity', 'default_identity')
    participant_name = request.headers.get('name', 'default_name')
    room_name = request.headers.get('room', 'default_room')

    token = api.AccessToken(os.getenv('LIVEKIT_API_KEY'), os.getenv('LIVEKIT_API_SECRET')) \
    .with_identity(participant_identity) \
    .with_name(participant_name) \
    .with_grants(api.VideoGrants(
        room_join=True,
        room=room_name,
    ))

    return token.to_jwt()

if __name__ == "__main__":
    app.run(host='0.0.0.0')