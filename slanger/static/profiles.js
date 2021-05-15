$( document ).ready( function() {
    console.log("Fetching profiles from database...")
    $.ajax({
        url: "/profile/0",
        success: function( profiles ) {
            console.log("Loading profiles...");
            for (let profile of profiles) {
                dumpProfile( profile );
            }
            console.log("Loaded profiles");
        }
    });
});

const addProfile = () => {
    do {
        profile_url = prompt( "profile or page url" );
    } while ( profile_url.length == 0 );

    do {
        tag = prompt( "A tag to identify this page", "New page" );
    } while ( tag.length == 0 );

    console.log( profile_url );
    $.ajax( {
        url: "/profile/0",
        type: 'POST',
        data: { profile_url: profile_url, tag: tag },
        success: function( data ) {
            if ( data != null ) {
                dumpProfile( data );
            }
        }
    });

}

const removeProfile = ( id ) => {
    if ( confirm(`Delete profile with id ${id}?`) ) {
        $.ajax({
            'url': `/profile/${id}`,
            type: 'DELETE',
            success: function ( data ) {
                if ( data != null ) {
                    popProfile( id );
                }
            }
        })
    }
}