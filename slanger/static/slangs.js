$( document ).ready( function() {
    console.log("Fetching slangs from database...")
    $.ajax({
        url: "/slang/0",
        success: function( slangs ) {
            console.log("Loading slangs...");
            for (let slang of slangs) {
                dumpSlang( slang );
            }
            console.log("Loaded slangs");
        }
    });
})

const addSlang = () => {
    // var slang =  undefined;
    do {
        slang = prompt( "What slang would you like to add?" );
    } while ( slang.length == 0 );

    $.ajax( {
        url: "/slang/0",
        type: 'POST',
        data: { slang: slang },
        success: function( data ) {
            if ( data != null ) {
                dumpSlang( data );
            }
        }
    });

}

const removeSlang = ( id ) => {
    if ( confirm(`Delete slang with id ${id}?`) ) {
        $.ajax({
            'url': `/slang/${id}`,
            type: 'DELETE',
            success: function ( data ) {
                if ( data != null ) {
                    popSlang( id );
                }
            }
        })
    }
}