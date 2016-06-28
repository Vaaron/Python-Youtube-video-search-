import urllib
import re

c = raw_input()
query_string = urllib.urlencode({"search_query" : c})
html_content = urllib.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode('utf-8'))
for n in search_results:
    print "http://www.youtube.com/watch?v=" + n

