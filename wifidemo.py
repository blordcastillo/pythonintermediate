import requests
url = "https://raw.githubusercontent.com/marigolds6/pythonintermediate/master/wifisample.js"
r = requests.get(url)
# We should ask forgiveness instead of permission
if r.status_code == 200:
    nodes = r.json()
    for node in nodes:
        node['building'] = node['building'].strip()
        node['wifitype'] = node['type']
        del node['type']
        #print node
        fields = tuple(node)
        values = tuple([node[x] for x in fields])
        print fields
        print values
        print "A wifi node of type {wifitype} is located in {building} at {lat}, {long}".format(**node)
else:
    print "Unable to connect. Error code {}".format(r.status_code)