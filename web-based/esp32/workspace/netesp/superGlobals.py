IP = {"entities": []}

def parse_query_string(query):
    """Parses a URL-encoded query string into a dictionary."""
    params = {}
    for pair in query.split('&'):
        if '=' in pair:
            key, value = pair.split('=', 1)
            params[key] = value
    return params