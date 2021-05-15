from ..models.models import Profile
from flask_restful import Resource, fields, marshal_with, reqparse
from flask import abort, Response

profile_field = {
    'id': fields.Integer,
    'profile_url': fields.String,
    'tag': fields.String
}

profile_parser = reqparse.RequestParser()

profile_parser.add_argument( 'profile_url', required = True, type = str, help = "You forgot the profile url" )
profile_parser.add_argument( 'tag', type = str, help = "Add a tag to help you identify this" )

class CRUDProfile( Resource ):

    @marshal_with( profile_field )
    def post( self, id = 0 ):
        profile = profile_parser.parse_args()

        return Profile.add_profile( **profile )

    @marshal_with( profile_field )
    def get( self, id = 0 ):
        if id != 0:
            _profile = Profile.query.get( id )

            if _profile is None:
                return abort( 
                    Response( "Error: (404) Profile %d not found\n" % id, 404 )
                )

            return _profile
        
        return Profile.query.all()

    @marshal_with( profile_field )
    def put( self, id ):
        profile = profile_parser.parse_args()

        _profile = Profile.edit_profile( id, **profile )
        
        if _profile is None:
            return abort( 
                Response( "Error: (404) Profile %d not found\n" % id, 404 )
            )
        
        return _profile

    @marshal_with( profile_field )
    def delete( self, id ):
        _profile = Profile.delete_profile( id )

        if _profile is None:
            return abort( 
                Response( "Error: (404) Profile %d not found\n" % id, 404 )
            )

        return _profile