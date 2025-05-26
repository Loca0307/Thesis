# ERROR:
# 'becoz of `post`'
# @app.put('/posts/update/{id}')
# def update_post(id: int, post: Post):
#     for index, post in enumerate(my_posts):
#         if post['id'] == id:
#             my_posts[index]['title'] = post.title
#             return {'all-post': my_posts}
#     return {'message': 'post not found'}

# Works!! (Copilot):
# solved it via changing `post` -> `updated_post`