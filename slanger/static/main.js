const run_crawler = () => {

    if (!confirm("Are you sure you want to run the crawler. this process might take a while")) {
        return;
    }

    // do {
    //     secret_key = prompt(  "Your facebook api secret key. Dont worry. we wont store it", "not-set" );
    // } while ( secret_key == "not-set" );

    // if ( secret_key == "not-set" ) {
    //     return;
    // }

    console.log("CRAWLER IS RUNNING");
    console.log( "Waiting for response..." );

    $('#run-crawler-btn').html( "CRAWLER IS RUNNING..." );

    // return;


    $.ajax({
        url: "/comments/0",
        timeout: 0,
        type: "POST",
        success: function( comments ) {



            if (comments == -1) {
                alert( "Crawler has been executed 3 times and cannot run till tommorow" )
                console.log( "Maximum run time reached" )
                return;
            }

            console.log("Crawler has finished executing");

            console.log("Dumping comments in GUI...");
            $('#comment-dump').html("");

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