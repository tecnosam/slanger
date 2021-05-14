from flask_restful import Resource, marshal, reqparse, fields, marshal_with
from flask import abort, Response
from ..models.models import Comment, Profile, Slang
from ..crawler import scrape

import os, time

comment_fields = {
    'id': fields.Integer,
    'user': fields.String,
    'post_url': fields.String,
    'comment_id': fields.String,
    'comment': fields.String,
    'slangs': fields.String,
    'profile_id': fields.String
}

comment_parser = reqparse.RequestParser(  )

comment_parser.add_argument( 'user', required = True, 
        type=str, help = "The user that made the comment" )

comment_parser.add_argument( 'post_url', required = True, 
        type=str, help = "The url of the post that the comment was made on" )

# comment_parser.add_argument( 'profile_id', required = True, 
#         type=int, help = "The profile id (id in our database) of the page or profile that owns the post" )

comment_parser.add_argument( 'comment_id', required = True, 
        type=int, help = "The id of the comment" )

comment_parser.add_argument( 'comment', required = True, 
        type=str, help = "The comment that was made" )

comment_parser.add_argument( 'slangs', required = True, 
        type=str, help = "The slang(s) that where matched" )


class CRUDComment( Resource ):

    @marshal_with( comment_fields )
    def get( self, id ):
        if (id != 0):
            _comment = Comment.query.get( id )
            if ( _comment is None ):
                abort( Response( "Error: (404) COmment not found", 404 ) )
            return _comment

        return Comment.query.all()

    def delete( self, id ):
        
        _comment = Comment.delete_comment( id )

        if _comment is None:
            abort( Response( f"Error: (404) Comment with id {id} not found", 404 ) )

        return _comment

class CRUDComments(Resource):
    @marshal_with( comment_fields )
    def get( self, pid ):

        if pid == 0:
            return Comment.query.all()

        return Comment.query.join( Profile, Profile.id == Comment.profile_id )\
            .filter( Profile.id == pid ).all()

    @marshal_with( comment_fields )
    def post( self, pid ):
        res = list()
        
        print("> Fetching profiles...")
        if pid != 0:
            profiles = (Profile.query.get( pid ))
            if profiles[0] is None:
                abort( Response( f"Error: (404) profile with id {pid} not found", 404 ) )
        else:
            profiles = Profile.query.all()

        print( "> Fetched profiles" )
        print( "> Executing crawler..." )

        old = marshal( Comment.empty_comments(), comment_fields )

        try:
            for profile in profiles:

                page = profile.profile_url.split("/")[-1]

                slangs = Slang.query.all()

                regexp = f"({'|'.join( [ slang.slang for slang in slangs ] )})"

                # comment = comment_parser.parse_args()
                # comment['profile_id'] = pid

                for comment in scrape( page, regexp ):

                    comment['profile_id'] = pid

                    res.append( Comment.add_comment( **comment ) )
            print("> All done")

        except Exception as e:
            log = f"{time.time()}:\t{str(e)}\n"

            with open( "logs/crawler.txt", "a" ) as f:
                f.write( log )

            f.close()
            res = list()

            for comment in old:
                comment.pop("id")

                res.append( Comment.add_comment( **comment ) )
            
            abort( Response( 
                "Error: (500) Sorry about that, there seems to be an error on the server. you can contact the developer", 500 
            ))

        return res
