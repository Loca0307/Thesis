                'body': post['body']
            })
        
        with open('posts.csv', 'w', newline='') as cf:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(cf, fieldnames=fieldnames)
            