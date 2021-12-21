SicsPy
========

SicsPy is Python package developed for algorithms for solving the Subgraph Isomorphism Constraint Satisfaction problem.

Simple example
--------------

.. code:: python

    >>> from sicspym import Graph, SicsAlgorithms, read_amalfi
    >>> m = Graph("adjacency_listmat", "undirected_tag", 3)
    >>> m.set_vertex_label(0, "red")
    >>> m.set_vertex_label(1, "blue")
    >>> m.set_vertex_label(2, "green")
    >>> m.add_edge(0, 1)
    >>> m.add_edge(1, 2)
    >>> m.add_edge(2, 0)
    >>> n = Graph("adjacency_listmat", "undirected_tag", 4)
    >>> n.set_vertex_label(0, "red")
    >>> n.set_vertex_label(1, "blue")
    >>> n.set_vertex_label(2, "gree>>> n.)
    >>> n.set_vertex_label(3, "gree>>> n.)
    >>> n.add_edge(0, 1)
    >>> n.add_edge(1, 2)
    >>> n.add_edge(2, 0)
    >>> n.add_edge(1, 3)
    >>> n.add_edge(3, 0)
    >>> c = SicsAlgorithms("adjacency_listmat", "undirected_tag")
    >>> c.backjumping_bitset_degreeprune_ind(m, n, "GCF", mapping=True)
    {0: 0, 1: 1, 2: 2}
    {0: 0, 1: 1, 2: 3}
    2
    >>> c.forwardchecking_bitset_mrv_degreeprune_ind(m, n, mapping=True)
    {0: 0, 1: 1, 2: 2}
    {0: 0, 1: 1, 2: 3}
    2
    >>> c.forwardchecking_bitset_mrv_degreeprune_ind(m, n)
    2
    >>> md = Graph("adjacency_degreesortedlistmat", "undirected_tag", graph=m)
    >>> nd = Graph("adjacency_degreesortedlistmat", "undirected_tag", graph=n)
    >>> cd = SicsAlgorithms("adjacency_degreesortedlistmat", "undirected_tag")
    >>> cd.backjumping_bitset_degreeprune_ind(md, nd, "GCF", mapping=True)
    {0: 0, 1: 1, 2: 2}
    {0: 0, 1: 1, 2: 3}
    2
    >>> head, tail = os.path.split(__file__)
    >>> file1 = os.path.join(head, "si2_b03_m200.A00")
    >>> file2 = os.path.join(head, "si2_b03_m200.B00")
    >>> g = read_amalfi("adjacency_listmat", "undirected_tag", repr(file1).strip("'"))
    >>> h = read_amalfi("adjacency_listmat", "undirected_tag", repr(file2).strip("'"))
    >>> s = SicsAlgorithms("adjacency_listmat", "undirected_tag")
    >>> s.backjumping_bitset_degreeprune_ind(g, h, "GCF", mapping=False)
    400

Test
-------

Run pytest command when you inside sicspy directory::
    
    $ pytest

Install
-------

Install the latest version of sicspy::

    $ pip install -i https://test.pypi.org/simple/ sicspy==0.0.1

License
-------

Released under the GNU General Public License v3.0 (see `LICENSE.txt`)::
