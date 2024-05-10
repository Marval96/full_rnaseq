import pandas as pd
from networkx import Graph

def get_clusters_network(network_file, cluster_file):

    dataframe_network = pd.read_csv(network_file, sep='\t')
    dataframe_cluster = pd.read_csv(cluster_file)

    edges = []

    for node1, node2 in zip(dataframe_network['#node1'], dataframe_network['node2']):
        edges.append([node1, node2])

    clusters = {}
    for cluster, nodes in zip(dataframe_cluster['Cluster'], dataframe_cluster['Node IDs']):
        clusters[cluster]= nodes.split(', ')

    dict_aux_node_to_cluster={}
    for key, value in clusters.items():
        for node in value:
            dict_aux_node_to_cluster[node]=key

    new_edges = []
    for node1, node2 in edges:
        if (node1 in dict_aux_node_to_cluster) and (node2 in dict_aux_node_to_cluster): 
            cluster1 = dict_aux_node_to_cluster[node1]
            cluster2 = dict_aux_node_to_cluster[node2]
            if [cluster1, cluster2] not in new_edges:
                if cluster1!=cluster2:
                    new_edges.append([cluster1, cluster2])
    
    return Graph(new_edges)
