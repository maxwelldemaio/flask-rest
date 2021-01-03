# flask-rest
REST API built with the Flask framework

**Overall**

In this project I created a REST API with Flask, Flask-SQLAlchemy, and Flask-RESTful. With this REST API we can create, read, update and delete resources from our database, which in our case are YouTube videos.

Resource)
```py
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

    # Update video in DB
    @marshal_with(resource_fields)
    def patch(self, video_id):
        # Check if not in DB
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video ID does not exist in the database")
        args = video_patch_args.parse_args()
        # Update DB row with arguments
        if 'name' in args and args['name'] != None:
            result.name = args['name']
        if 'likes' in args and args['likes'] != None:
            result.likes = args['likes']
        if 'views' in args and args['views'] != None:
            result.views = args['views']
        db.session.commit()
        return result
```

Note for my YouTube video resource, we have properties such as likes, video name, and views. These represent columns in our database and each row will be a new resource. Each method in our resource allows us to create, read, update and delete YouTube videos from our database. Earlier in `app.py` I define required arguments for put/patch operations and I define how the resource should be returned using the `@marshal_with` decorator.
