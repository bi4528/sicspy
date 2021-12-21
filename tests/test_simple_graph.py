from sicspy import Graph, SicsAlgorithms

def test_simple_graph_result(capsys):

    m = Graph("adjacency_list", "undirected_tag", 3)
    m.set_vertex_label(0, "red")
    m.set_vertex_label(1, "blue")
    m.set_vertex_label(2, "green")
    m.add_edge(0, 1)
    m.add_edge(1, 2)
    m.add_edge(2, 0)
    
    n = Graph("adjacency_list", "undirected_tag", 4)
    n.set_vertex_label(0, "red")
    n.set_vertex_label(1, "blue")
    n.set_vertex_label(2, "green")
    n.set_vertex_label(3, "green")
    n.add_edge(0, 1)
    n.add_edge(1, 2)
    n.add_edge(2, 0)
    n.add_edge(1, 3)
    n.add_edge(3, 0)

    c = SicsAlgorithms("adjacency_list", "undirected_tag")
    
    c.backjumping_bitset_degreeprune_ind(m, n, "GCF", mapping=False)

    captured = capsys.readouterr()
    assert captured.out == "2\n"

def test_simple_graph_mapping(capsys):

    m = Graph("adjacency_list", "undirected_tag", 3)
    m.set_vertex_label(0, "red")
    m.set_vertex_label(1, "blue")
    m.set_vertex_label(2, "green")
    m.add_edge(0, 1)
    m.add_edge(1, 2)
    m.add_edge(2, 0)
    
    n = Graph("adjacency_list", "undirected_tag", 4)
    n.set_vertex_label(0, "red")
    n.set_vertex_label(1, "blue")
    n.set_vertex_label(2, "green")
    n.set_vertex_label(3, "green")
    n.add_edge(0, 1)
    n.add_edge(1, 2)
    n.add_edge(2, 0)
    n.add_edge(1, 3)
    n.add_edge(3, 0)

    c = SicsAlgorithms("adjacency_list", "undirected_tag")
    
    c.backjumping_bitset_degreeprune_ind(m, n, "GCF", mapping=True)

    captured = capsys.readouterr()
    assert captured.out == "{0: 0, 1: 1, 2: 2}\n{0: 0, 1: 1, 2: 3}\n2\n"
