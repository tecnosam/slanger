const run_crawler = () => {
    if (!confirm("Are you sure you want to run the crawler. this process might take a while")) {
        return;
    }
    console.log("CRAWLER IS RUNNING");
    console.log( "Waiting for response..." );

    $('#run-crawler-btn').html( "CRAWLER IS RUNNING..." );

    // return;

    $('#comment-dump').html("");

    $.ajax({
        url: "/comments/0",
        timeout: 0,
        type: "POST",
        success: function( comments ) {

            console.log("Crawler has finished executing");

            console.log("Dumping comments in GUI...");

            for ( let comment of comments ) {

                try {

                    dumpComment ( comment );

                } catch (ReferenceError) {

                    console.log("Comments section is not yet mounted! skipping this process.");
                    break;

                }

            }

            console.log("Successfully executed script :>");

        },
        error: function( e ) {
            console.error( e );
            alert( e.responseText );
            $('#run-crawler-btn').html( "RUN CRAWLER" );
        }

    }).then( e => $('#run-crawler-btn').html( "RUN CRAWLER" ) );

}