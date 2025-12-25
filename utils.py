from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def get_params(url):
    parsed = urlparse(url)
    return parse_qs(parsed.query)

def inject_payload(url, param, payload):
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    params[param] = payload
    new_query = urlencode(params, doseq=True)
    return urlunparse(parsed._replace(query=new_query))
