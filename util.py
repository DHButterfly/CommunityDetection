#coding=utf-8
import networkx as nx

# 加载网络
def load_graph(path):
	G = nx.Graph()
	with open(path) as text:
		for line in text:
			vertices = line.strip().split(" ")
			source = int(vertices[0])
			target = int(vertices[1])
			G.add_edge(source, target)
	return G

# 克隆
def clone_graph(G):
	cloned_graph = nx.Graph()
	for edge in G.edges():
		cloned_graph.add_edge(edge[0], edge[1])
	return cloned_graph

# 计算Q值
def cal_Q(partition, G):
	m = len(list(G.edges()))
	a = []
	e = []

	# 计算每个社区的a值
	for community in partition:
		t = 0
		for node in community:
			t += len(list(G.neighbors(node)))
		a.append(t / float(2 * m))

	# 计算每个社区的e值
	for community in partition:
		t = 0
		for i in range(len(community)):
			for j in range(len(community)):
				if i != j:
					if G.has_edge(community[i], community[j]):
						t += 1
		e.append(t / float(2 * m))

	# 计算Q
	q = 0
	for ei, ai in zip(e, a):
		q += (ei - ai ** 2)
	return q