import lxml.html, urllib2, urllib, urlparse

base_url = 'http://www.math.uh.edu/~rohop/fall_06/'

#this fetches the page
res = urllib2.urlopen(base_url)

#parse the response into an xml tree
tree = lxml.html.fromstring(res.read())

# construct a namespace dictionary to pass to the xpath() call
# this lets us use regular expressions in the xpath
ns = {'re': 'http://exslt.org/regular-expressions'}
# iterate over all <a> tags whose href ends in ".pdf" (case-insensitive)

urlist = []
i=0
for node in tree.xpath('//a[re:test(@href, "\.pdf$", "i")]', namespaces=ns):
    #creates a vector with all the urls that contain .pdf as an ending string
    urlist.append(urlparse.urljoin(base_url, node.attrib['href']))

#fetches all the pdfs and puts them in the directory defined in the filename variable
#changes in the directory and filename are both done in the filename
for i,e in enumerate(urlist):
	urllib.urlretrieve(e,filename='/Users/gongui/Dropbox/sci/neuro/optimization_theory/hoppe_opt_theory'+str(i)+'.pdf')
	print (i/float(len(urlist)))*100
