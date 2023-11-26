from reddit_functions import *
from system_functions import *

## open reddit 
swipe_up()
open_reddit()

names = [

]

for i in names:

    ## search for the user and start chat
    top_search_bar()
    type_text(f'{i}')
    first_user_search()
    start_chat()

    ## type the message
    message_box()
    type_text("hi")
    message_send()

    ## exit back to the start menu
    time.sleep(5)
    exit_chat()
