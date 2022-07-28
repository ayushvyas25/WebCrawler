# importing  libraries
from urllib.request import urljoin
from bs4 import BeautifulSoup
import requests
from urllib.request import urlparse
import networkx as nx
import matplotlib.pyplot as plt


# initializing variables
links = set()
url_UOIT = "https://ontariotechu.ca/"
depth = 2 #to get the urls in depth
url_linking = []


def check_link(url):
    url_domain = urlparse(url_UOIT).netloc
    filetype = urlparse(url).path.split('/')[-1].split('.')[-1]                                             #collecting  only the links that is necessary
    if  (url_domain == 'ontariotechu.ca' and filetype != 'pdf' and filetype != 'jpg' and filetype != 'png'): #removing all the links with png,pdf or jpg
        return True                                                                                          #making the nodes or links more clean
    else:
        return False

# function for crawling a url
def crawl(url_UOIT):
    url_domain = urlparse(url_UOIT).netloc

	# Creating bs4 object to get html tag
    bs4obj = BeautifulSoup(
		requests.get(url_UOIT).content, "lxml")

	# finding all anchor tags from uoit website
        href = anchor.attrs.get("href")
        if(href != "" or href != None):
            href = urljoin(url_UOIT, href)
            href_parsed = urlparse(href)
            href = href_parsed.scheme
            href += "://"
            href += href_parsed.netloc
            href += href_parsed.path
            final_parsed_href = urlparse(href)

            is_valid = bool(final_parsed_href.scheme) and bool(final_parsed_href.netloc)
            if is_valid and url_domain in href  and check_link(href):
                url_linking.append((url_UOIT,href))
            if is_valid and url_domain in href  and check_link(href) and href not in links:
                links.add(href)
    return links

queue = []
queue.append(url_UOIT)
counter = 0
for j in range(depth):
    for count in range(len(queue)):
        url = queue.pop(0) #in bfs pop 0 to pop to the top one out when visited
        urls = crawl(url)
        for i in urls:
            queue.append(i)
            counter += 1
            if(counter >= 1000000):  #using counter to stop nodes if it goes more than 100000 links
                break
        if(counter >= 1000000):      #used this to stop my loop going in infinite loop
            break
    if(counter >= 1000000):
        break


G=nx.Graph() #used for plotting the graph
G.add_edges_from(url_linking)
nx.write_gexf(G, "Gephi.gexf") #storing the nodes in the gexf file to visualize and analyze it better in gephi
print(nx.info(G)) 

'''   
print("\n\n density::",nx.density(G))  
print("\n\n diameter::",nx.diameter(G)) 
print("\n\n average_pathlength::",nx.average_shortest_path_length(G))  #prints the avg path length
print("\n\n\n\n avg_clustering::",nx.average_clustering(G)) #prints the avg clustering
print("\ndegree_centrality :") #prints the degree centrality
for i in sorted(nx.degree_centrality(G), key=nx.degree_centrality(G).get, reverse= False):
    print(i,nx.degree_centrality(G)[i])
print("\nbetweenness_centrality")
for j in sorted(nx.betweenness_centrality(G), key=nx.betweenness_centrality(G).get, reverse= False):
    print(j,nx.betweenness_centrality(G)[j])
print("\ncloseness_centrality")
for k in sorted(nx.closeness_centrality(G), key=nx.closeness_centrality(G).get, reverse= False):
    print(k,nx.closeness_centrality(G)[k])
print("\npagerank")
for l in sorted(nx.pagerank(G), key=nx.pagerank(G).get, reverse= False):
    print(l,nx.pagerank(G)[l])
#for visualization
nx.draw_spring(G)
plt.show()

degrees = [G.degree(n) for n in G.nodes()]
plt.hist(degrees)
plt.show()   
'''
