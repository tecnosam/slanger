from ..models.models import Slang
from flask_restful import Resource, fields, marshal_with, reqparse
from flask import abort, Response

slang_field = {
    'id': fields.Integer,
    'slang': fields.String,
    'date': fields.DateTime
}

slang_parser = reqparse.RequestParser()
slang_parser.add_argument( 'slang', type = str, required = True, help = "You forgot the slang" )

class CRUDSlang( Resource ):

    @marshal_with( slang_field )
    def post( self, id = 0 ):
        slang = slang_parser.parse_args()['slang']
        print( slang )

        return Slang.add_slang( slang )

    @marshal_with( slang_field )
    def get( self, id = 0 ):
        if id != 0:
            # print(id == 0)
            _slang = Slang.query.get( id )
            if _slang is None:
                return abort(
                    Response( 'Error: (404) Slang %d not found\n' % id, 404 )
                )
            return _slang

        return Slang.query.all()

    @marshal_with( slang_field )
    def put( self, id ):
        slang = slang_parser.parse_args()['slang']

        _slang = Slang.edit_slang( id, slang )
        
        if _slang is None:
            return abort(
                Response( 'Error: (404) Slang %d not found\n' % id, 404 )
            )
        
        return _slang

    @marshal_with( slang_field )
    def delete( self, id ):
        _slang = Slang.delete_slang( id )

        if _slang is None:
            return abort(
                Response( 'Error: (404) Slang %d not found\n' % id, 404 )
            )
        
        return _slang