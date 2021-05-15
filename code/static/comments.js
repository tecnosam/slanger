$( document ).ready( function() {
    console.log("Fetching comments from database...")
    $.ajax({
        url: "/comments/0",
        success: function( comments ) {
            console.log("Loading comments...");
            for (let comment of comments) {
                dumpComment( comment );
            }
            console.log("Loaded comments");
        }
    });
});
