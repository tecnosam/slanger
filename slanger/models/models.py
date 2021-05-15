from .. import db

import datetime

class Slang(db.Model):
    # slangs we're looking for

    id = db.Column( db.Integer, primary_key = True, auto_increment = True )

    slang = db.Column( db.String(40), unique = True, nullable = False )

    date = db.Column( db.DateTime(40), default=datetime.datetime.utcnow, nullable = False )

    def __repr__( self ):
        return "<Slang %r>" % self.slang

    # def getreqexp( self ):
    #     return re.compile(f"{slang}")

    @staticmethod
    def add_slang( slang ):
        _slang = Slang( slang = slang )
        db.session.add( _slang )

        db.session.commit()

        return _slang
    
    @staticmethod
    def edit_slang( id, slang ):
        _slang = Slang.query.get(id)
        if _slang is None:
            print( "Slang %d not found" % id )
            return None
        
        _slang.slang = slang

        db.session.commit()

        return _slang
    
    @staticmethod
    def delete_slang( id ):
        _slang = Slang.query.get( id )

        if _slang is None:
            print( "Slang %d not found" % id )
            return None
        
        db.session.delete( _slang )

        db.session.commit()

        return _slang

class Profile( db.Model ):
    # facebook profile or page in which we would be crawling

    id = db.Column( db.Integer, primary_key = True, auto_increment = True )

    profile_url = db.Column( db.String(200 ) , unique = True )

    tag = db.Column( db.String(30), default = "Another user to watch", nullable = True )

    comments = db.relationship('Comment', backref='profile', lazy=True)

    @staticmethod
    def add_profile( profile_url, tag ):

        _profile = Profile( profile_url = profile_url, tag = tag )

        db.session.add( _profile )

        db.session.commit()

        return _profile
    
    @staticmethod
    def edit_profile( id, profile_url, tag = None ):
        _profile = Profile.query.get(id)

        if _profile is None:
            print( "Profile %d not found" % id )
            return None

        _profile.profile_url = profile_url

        if 'tag' is not None:
            _profile.tag = tag

        db.session.commit()

        return _profile

    @staticmethod
    def delete_profile( id ):
        _profile = Profile.query.get( id )

        if _profile is None:
            print( "Profile %d not found" % id )
            return None

        db.session.delete( _profile )

        db.session.commit()

        return _profile

class Comment( db.Model ):
    # comment found containing slang

    id = db.Column( db.Integer, primary_key = True, auto_increment = True )

    user = db.Column( db.String(100), nullable = False )

    post_url = db.Column( db.String(1000), nullable = False )

    comment_id = db.Column( db.String( 200 ), default = "#", nullable = False )
    profile_id = db.Column( db.Integer, db.ForeignKey('profile.id'), nullable = False )

    comment = db.Column( db.String(1000), nullable = False )

    slangs = db.Column( db.String(1000), nullable = False )


    @staticmethod
    def add_comment( user, post_url, comment_id, profile_id, comment, slangs ):

        _comment = Comment( user = user, post_url = post_url, 
            comment_id = comment_id, profile_id = profile_id, comment = comment, slangs = slangs )

        db.session.add( _comment )

        db.session.commit()

        return _comment

    @staticmethod
    def delete_comment( id ):

        _comment = Comment.query.get( id )

        if _comment is None:
            print( "Comment %d not found" % id )
            return None

        db.session.delete( _comment )

        db.session.commit()

        return _comment
    
    @staticmethod
    def empty_comments():

        _comments = Comment.query.all()

        for _comment in _comments:
            db.session.delete( _comment )

        db.session.commit()

        return _comments

    def __repr__( self ):
        return "%r" % self.comment

