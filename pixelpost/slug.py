def slugify(title):
    """Turn a post title into a URL slug.

    "Hello world becomes "hello-world".
    """
    return title.lower().replace(" ","-")
