#plugin_checker2.py
#The goal of this script is to display all of the versions listed of all of the plugins that are on the plugin check page and the blocklist page
##############################################################
### block list # version # date ##  plugin # version # date###
#              #         #      ##         #         #     ###
#              #         #      ##         #         #     ###
#              #         #      ##         #         #     ###
#              #         #      ##         #         #     ###
#              #         #      ##         #         #     ###
##############################################################

from urllib2 import * 
import sys

blocklisturl = "https://addons.mozilla.org/en-US/firefox/blocked/"
#list of only plugins in here
pluginlist=["Adobe Flash Player", 
			"Adobe Reader", 
			"Cisco Web Communicator", 
			"Java Runtime Environment",
			"QuickTime Plug-in",
			"RealPlayer",
			"Silverlight Plug-In",
			"VLC Multimedia Plug-in"]
blocklistKeyword =["Java", "Reader", "Cisco Web Communicator", "RealPlayer", "Silverlight", "VLC", "Quicktime"]
class Plugins(object):

    def __init__(self, name_string,date_string):
        self.Date = date_string
        self.name = name_string

    def apple(self):
        print "I AM CLASSY APPLES!"


def find_between_r( s, first, last ):
	try:
		start = s.rindex( first ) + len( first )
		end = s.rindex( last, start )
		return s[start:end]
	except ValueError:
		return ""

def find_plugin(string, sub):
	start = 0
	while True:
		start = string.find(sub, start)
		if start == -1: return
		yield start
		start += len(sub) # use start += 1 to find overlapping matches
def returnDats(dex1, dex2):
	x = dex1
	while(x <= dex2): 
		Dates = List[x]
		if x == dex2: 
			return
		x+=1 

           

def main():

        # or later add for plugins.mozilla: 
    #HTTPBasicAuthHandler.http_error_401(req, fp, code, msg, hdrs)
    #   Retry the request with authentication information, if available.#
    #this is the request html for blocklist page            
    # try this instead: http://stackoverflow.com/questions/23278879/using-urlopen-to-open-list-of-urls
    stuff = urlopen(blocklisturl)
    html  = stuff.read()
    #print html
    index = html.find('blocked-items')
    print index

    print "everything after blocked-items: ", html[index]

    """<span class="dt new_style">"""
    index1 = list(find_plugin(html, '<span class="dt">')) 
    print "where first index is: ", index1
    #add length of string to index
    index2 =list(find_plugin(html, ':</span>'))
    print "index2: ",index2
    

    # store strings
    for i in index1:
    	for j in index2:
    		print "this is the string"
    		print html[(i + len('<span class="dt">')):j]
    		Dates = html[(i + len('<span class="dt">')):(i+len('<span class="dt">')+len('April 16, 2008'))]

    print "**********"
    print Dates
    print ">*********"

    index3 = list(find_plugin(html, '<a href="/en-US/firefox/blocked/i'))
    #print list(find_plugin(html, '<a href="/en-US/firefox/blocked/i'))
    #add legth to the index and add 5
    index4 =list(find_plugin(html, '</a>   </li>'))
    names = []
    for i in index3:
    	print "this is the string"
    	print html[(i + len('<a href="/en-US/firefox/blocked/i')+4):(i+len('<a href="/en-US/firefox/blocked/i')+(10))]
    	names = html[(i + len('<a href="/en-US/firefox/blocked/i')+4):(i+len('<a href="/en-US/firefox/blocked/i')+(10))]
    print "**********"
    print names
    print ">*********"

    #print list(find_plugin(html, '</a>   </li>'))	
    #compare
    #start with plugin entry and search in blocklist for each to match keyword

    #funtions: 
    #what is the input
    # > test case input
    # what is the outpit

    #starts dates <span class="dt">
    #ends :</span>
    #startname <a href="/en-US/firefox/blocked/i
    #endname /a>
    #  </li>i9u8uhk

    # show recent versions for each plugin and side by side with version 

#boiler plate main
if __name__ == '__main__':
	main()