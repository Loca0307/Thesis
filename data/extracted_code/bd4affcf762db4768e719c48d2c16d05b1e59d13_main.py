        return []

def save_posts_to_db(posts):
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as session:
        for post_data in posts:
            post = Post(id=post_data['id'], title=post_data['title'], body=post_data['body'])
            session.merge(post)  # merge to avoid duplicates on re-run
        session.commit()
    print("Posts saved to database.")