# from selenium import webdriver

from facebook_scraper import get_posts

import re, time

def perform_regex( regexp, comment ):
    if 'comment_text' in comment:
        if comment['comment_text'] is None:
            return (False, set())

    slangs = re.findall(re.compile( regexp ), comment['comment_text'].lower())

    return ( len(slangs) > 0, set(slangs) )


def post_comments(posts, matching = None):
    i = 0
    for post in posts:
        print( "post ", i )
        comments = post['comments_full']
        if (comments is None):
            return
        for comment in comments:
            if (matching is not None): # if we want all comments
                searched = perform_regex( matching, comment ) 
                if ( searched[0] ):
                    _comment = dict()

                    _comment['user'] = comment[ 'commenter_name' ]
                    _comment['post_url'] = post[ 'post_url' ]
                    _comment['comment_id'] = comment[ 'comment_id' ]
                    _comment['comment'] = comment[ 'comment_text' ]
                    _comment['slangs'] = ', '.join( searched[1] )

                    # comment['slangs'] = ', '.join( searched[1] )
                    yield _comment
                else:
                    continue
            else:
                yield comment

            time.sleep( 2 )
        
        i += 1

        # slow it down to prevent banning

def scrape( page, regexp = "mother" ):
    regexp = regexp.lower()
    posts = get_posts( page, options = {'comments': True} )

    comments = ( comment for comment in post_comments(posts, regexp) )

    return comments


# driver = webdriver.Firefox( executable_path="geckodriver/linux/geckodriver" )

# driver.get( "https://www.facebook.com/chrisbrown" )

