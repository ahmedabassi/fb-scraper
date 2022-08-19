from facebook_scraper import get_posts

def scraper(page_name,nb_pages,email,password):

    l=[]
    for post in get_posts(page_name, pages=nb_pages , credentials=(email ,password)):
        l.append({
            'post_url' : post['post_url'],
            'text' : post['text'],
            'time' : str(post['time']),
            'image' : post['image'],
            'likes' : post['likes'],
            'comments' : post['comments'],
            'shares' : post['shares'],
            })

    return l

