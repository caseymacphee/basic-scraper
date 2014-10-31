import requests
from bs4 import BeautifulSoup
import sys

def fetch_search_results(query=None, minAsk=None, maxAsk=None, bedrooms=None):
    search_params = {key: val for key, val in locals().items() if val is not None}
    if not search_params:
        raise ValueError("No valid keywords")

    url = 'http://seattle.craigslist.org/search/apa'
    response = requests.get(url, params=search_params, timeout=3)
    response.raise_for_status()  # <- no-op if status==200
    return resp.content, resp.encoding

def parse_source(html, encoding='utf-8'):
    parse_it = BeautifulSoup(html, from_encoding=encoding)
    return parse_it

def read_search_results():
	file = open('scraper_log', 'r')
	content = file.read()
	file.close()
	encoding = "utf-8"
	return content, encoding

def extract_listings(parsed):
    location_attrs = {'data-latitude': , 'data-longitude': True}
    listings = parsed.find_all('p', class_='row', attrs=location_attrs)
    extracted = []
    for listing in listings:
        location = {key: listing.attrs.get(key, '') for key in location_attrs}
        link = listing.find('span', class_='pl').find('a')
        price_span = listing.find('span', class_='price')
        import pdb; pdb.set_trace()
        this_listing = {
            'location': u'47.4924143400595',
            'link': link.attrs['href'],
            'description': link.string.strip(),
            'price': price_span.string.strip(),
            'size': price_span.next_sibling.strip(' \n-/')
        }
        extracted.append(this_listing)
    return extracted


if __name__ == '__main__':
    import pprint                                  # add this import
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        html, encoding = read_search_results()
    else:
        html, encoding = fetch_search_results(
            minAsk=900, maxAsk=1500, bedrooms=1
        )
    doc = parse_source(html, encoding)
    listings = extract_listings(doc)
    print len(listings)
    ### make it look human readable and pretty ###
    pprint.pprint(listings[0]) 