from lxml import html
import requests
import csv

def modifyEntry(entry):
    if len(entry)==0:
        entry.append('')
def createTree(link):
    page = requests.get(link)
    tree = html.fromstring(page.text)
    return tree

def extractLinkWithTree(tree,xpath):
    temp = tree.xpath(xpath)
    #print temp
    return temp

def extractLink(link,xpath):
    return extractLinkWithTree(createTree(link),xpath)

def uniq(input):
    output = []
    for x in input:
        if x not in output:
            output.append(x)
    return output

with open('test.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                  quotechar='"', quoting=csv.QUOTE_MINIMAL)   
    
    newLink = []
    for x in xrange(0,32):

        a = "http://www.classverse.com/search-studios?df=&pid="+str(x)+"&latitude=&longitude=&view_type=list&seo_latitude=&seo_longitude=&seo_radius=&seo_page_type=&placeid=&placeid_text=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&cid=&searchName=Gym&searchID=12&searchType=Activity&exclude_premium=0"
        newLink.append(a)

    

    for LinkInPage in newLink:
        tree=createTree(LinkInPage)
        name=extractLinkWithTree(tree,"//*[@class='studio_name']/text()")
        address=extractLinkWithTree(tree,"//*[@class='address-col']/text()")
        modifyEntry(name)
        modifyEntry(address)
        
        for x in xrange(0,len(address)):
            row= [(name[x].strip()).encode('ascii','ignore')]+[address[x].strip().encode('ascii','ignore')]
            print row
            spamwriter.writerow(row) 
        
