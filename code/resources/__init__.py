from .profiles import CRUDProfile
from .slangs import CRUDSlang
from .comments import CRUDComment
from .comments import CRUDComments

from .. import api


api.add_resource( CRUDProfile, '/profile/<int:id>' )
api.add_resource( CRUDSlang, '/slang/<int:id>' )

api.add_resource( CRUDComment, '/comment/<int:id>' )
api.add_resource( CRUDComments, '/comments/<int:pid>' )