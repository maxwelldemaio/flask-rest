from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# Request parser object and arguments for video object
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, 
    help='Please pass a name for the video', required=True)
video_put_args.add_argument("views", type=str, 
    help='Please pass views of the video', required=True)
video_put_args.add_argument("likes", type=str,
    help='Please pass likes on the video', required=True)

videos = {}

class Video(Resource):
    # Request a video
    def get(self, video_id):
        return videos[video_id]
        
    # Create a new video
    def put(self, video_id):
        # Check if we have all valid args
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

# Make the Video resource available to endpoint
# Define arguments with <>
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
