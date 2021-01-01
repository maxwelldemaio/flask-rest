from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


# DB Models
class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video (name={name}, views={views}, likes={likes}"


# Request parser object and arguments for video object
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, 
    help='Please pass a name for the video', required=True)
video_put_args.add_argument("views", type=str, 
    help='Please pass views of the video', required=True)
video_put_args.add_argument("likes", type=str,
    help='Please pass likes on the video', required=True)

# Define how DB object should be serialized
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

class Video(Resource):
    # Request a video from DB
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        # Check if not in DB
        if not result:
            abort(404, message="Could not find video with specified ID")
        return result

    # Create a new video in DB
    @marshal_with(resource_fields)
    def put(self, video_id):
        # Check if already in DB
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video ID already exists in the database")

        args = video_put_args.parse_args()
        video = VideoModel(id=video_id, name=args['name'],
            views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    # Delete video
    def delete(self, video_id):
        # Check if not in DB
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video ID does not exist in the database")
        db.session.delete(result)
        db.session.commit()
        return '', 204


# Make the Video resource available to endpoint
# Define arguments with <>
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
