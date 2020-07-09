from html.parser import HTMLParser

class HTMLParser(HTMLParser):
    
    def handle_starttag(self, tags, attrs):
        print(tags)
        
        if len(attrs) > 0:
            for i in attrs:
                print('->', i[0], '>', i[1])

html = ''

for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = HTMLParser()
parser.feed(html)
parser.close()

