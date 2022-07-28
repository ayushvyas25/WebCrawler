# WebCrawler
Web Crawler BFS of Ontario Tech University website using Python BeautifulSoup and Gephi to visualize all the nodes.

Analysis:![website direected](https://user-images.githubusercontent.com/40570777/181395664-7fa55011-ca50-40e6-9bd2-ae3f695576a7.png)

From this graph we can see that there are a lot of communities, 18 to be exact and the assorted color represent the different communities. I have used force atlas 2 layout to make the graph look more beautiful. The graph is directed as I had to crawl from one main node that is “ontariotechu.ca” and implement a BFS algorithm. After cleaning the data using check_link function I got around 4127 nodes and 62K edges. Wherein the highest number of degrees is 422 and policy page has the highest betweenness centrality around the network. The average path length is 2.42 which is the number required to move from one page to another page. The average clustering coefficient is 0.205. 

Nodes: 4127
Edges: 62021
Directed Graph
Average Degree: 15.028
Diameter: 3
Average Path length: 2.4249902310359985
Density: 0.004
Average Clustering Coefficient: 0.205
Number of Weakly Connected Components: 1
Number of Strongly Connected Components: 4127


Top 10 nodes having most Betweenness Centrality:![table 1](https://user-images.githubusercontent.com/40570777/181395109-07c5f0b7-7f54-405f-b1df-163ddfe75408.png)
Top 10 nodes having highest degree i.e., Degree Centrality:![table 2](https://user-images.githubusercontent.com/40570777/181395146-9333430d-68bc-4749-b9c8-6d987040dae3.png)
