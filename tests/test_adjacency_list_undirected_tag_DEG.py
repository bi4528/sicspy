import os
from sicspy import Graph, SicsAlgorithms, read_amalfi

head, tail = os.path.split(__file__)
g = read_amalfi("adjacency_list", "undirected_tag", repr(os.path.join(head, "si2_b03_m200.A00")).strip("'"))
h = read_amalfi("adjacency_list", "undirected_tag", repr(os.path.join(head, "si2_b03_m200.B00")).strip("'"))
s = SicsAlgorithms("adjacency_list", "undirected_tag")

def test_backjumping_bitset_degreeprune_ind(capsys):
    s.backjumping_bitset_degreeprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backjumping_bitset_degreesequenceprune_ind(capsys):
    s.backjumping_bitset_degreesequenceprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backjumping_degreeprune_ind(capsys):
    s.backjumping_degreeprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backjumping_degreesequenceprune_ind(capsys):
    s.backjumping_degreesequenceprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backjumping_ind(capsys):
    s.backjumping_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_adjacentconsistency_forwardcount_ind(capsys):
    s.backtracking_adjacentconsistency_forwardcount_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_adjacentconsistency_ind(capsys):
    s.backtracking_adjacentconsistency_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_adjacentconsistency_precount_ind(capsys):
    s.backtracking_adjacentconsistency_precount_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_bitset_degreeprune_ind(capsys):
    s.backtracking_bitset_degreeprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_bitset_degreesequenceprune_ind(capsys):
    s.backtracking_bitset_degreesequenceprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_degreeprune_adjacentconsistency_forwardcount_ind(capsys):
    s.backtracking_degreeprune_adjacentconsistency_forwardcount_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_degreeprune_adjacentconsistency_ind(capsys):
    s.backtracking_degreeprune_adjacentconsistency_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_degreeprune_adjacentconsistency_precount_ind(capsys):
    s.backtracking_degreeprune_adjacentconsistency_precount_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_degreeprune_ind(capsys):
    s.backtracking_degreeprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_degreesequenceprune_ind(capsys):
    s.backtracking_degreesequenceprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_forwardcount_ind(capsys):
    s.backtracking_forwardcount_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_ind(capsys):
    s.backtracking_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_parent_adjacentconsistency_forwardcount_ind(capsys):
    s.backtracking_parent_adjacentconsistency_forwardcount_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_parent_adjacentconsistency_ind(capsys):
    s.backtracking_parent_adjacentconsistency_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_parent_adjacentconsistency_precount_ind(capsys):
    s.backtracking_parent_adjacentconsistency_precount_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_parent_degreeprune_adjacentconsistency_forwardcount_ind(capsys):
    s.backtracking_parent_degreeprune_adjacentconsistency_forwardcount_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_parent_degreeprune_adjacentconsistency_ind(capsys):
    s.backtracking_parent_degreeprune_adjacentconsistency_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_parent_degreeprune_adjacentconsistency_precount_ind(capsys):
    s.backtracking_parent_degreeprune_adjacentconsistency_precount_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_parent_degreeprune_ind(capsys):
    s.backtracking_parent_degreeprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_parent_forwardcount_ind(capsys):
    s.backtracking_parent_forwardcount_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_backtracking_parent_ind(capsys):
    s.backtracking_parent_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_conflictbackjumping_degreeprune_ind(capsys):
    s.conflictbackjumping_degreeprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_conflictbackjumping_degreesequenceprune_ind(capsys):
    s.conflictbackjumping_degreesequenceprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_conflictbackjumping_ind(capsys):
    s.conflictbackjumping_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_forwardchecking_bitset_degreeprune_ac1_ind(capsys):
    s.forwardchecking_bitset_degreeprune_ac1_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_forwardchecking_bitset_degreeprune_countingalldifferent_ind(capsys):
    s.forwardchecking_bitset_degreeprune_countingalldifferent_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_forwardchecking_bitset_degreeprune_ind(capsys):
    s.forwardchecking_bitset_degreeprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_forwardchecking_bitset_degreesequenceprune_ac1_ind(capsys):
    s.forwardchecking_bitset_degreesequenceprune_ac1_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_forwardchecking_bitset_degreesequenceprune_countingalldifferent_ind(capsys):
    s.forwardchecking_bitset_degreesequenceprune_countingalldifferent_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_forwardchecking_bitset_degreesequenceprune_ind(capsys):
    s.forwardchecking_bitset_degreesequenceprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_forwardchecking_bitset_mrv_degreeprune_ac1_ind(capsys):
    s.forwardchecking_bitset_mrv_degreeprune_ac1_ind(g, h, mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_forwardchecking_bitset_mrv_degreeprune_countingalldifferent_ind(capsys):
    s.forwardchecking_bitset_mrv_degreeprune_countingalldifferent_ind(g, h, mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_forwardchecking_bitset_mrv_degreeprune_ind(capsys):
    s.forwardchecking_bitset_mrv_degreeprune_ind(g, h, mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_forwardchecking_bitset_mrv_degreesequenceprune_ac1_ind(capsys):
    s.forwardchecking_bitset_mrv_degreesequenceprune_ac1_ind(g, h, mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_forwardchecking_bitset_mrv_degreesequenceprune_countingalldifferent_ind(capsys):
    s.forwardchecking_bitset_mrv_degreesequenceprune_countingalldifferent_ind(g, h, mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_forwardchecking_bitset_mrv_degreesequenceprune_ind(capsys):
    s.forwardchecking_bitset_mrv_degreesequenceprune_ind(g, h, mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_forwardchecking_degreeprune_ind(capsys):
    s.forwardchecking_degreeprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_forwardchecking_degreesequenceprune_ind(capsys):
    s.forwardchecking_degreesequenceprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_forwardchecking_ind(capsys):
    s.forwardchecking_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_forwardchecking_mrv_degreeprune_ind(capsys):
    s.forwardchecking_mrv_degreeprune_ind(g, h, mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_lazyforwardchecking_degreeprune_ind(capsys):
    s.lazyforwardchecking_degreeprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_lazyforwardchecking_degreesequenceprune_ind(capsys):
    s.lazyforwardchecking_degreesequenceprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_lazyforwardchecking_ind(capsys):
    s.lazyforwardchecking_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_lazyforwardchecking_low_bitset_degreeprune_ind(capsys):
    s.lazyforwardchecking_low_bitset_degreeprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_lazyforwardchecking_low_bitset_degreesequenceprune_ind(capsys):
    s.lazyforwardchecking_low_bitset_degreesequenceprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_lazyforwardchecking_low_degreeprune_ind(capsys):
    s.lazyforwardchecking_low_degreeprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_lazyforwardchecking_low_degreesequenceprune_ind(capsys):
    s.lazyforwardchecking_low_degreesequenceprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_lazyforwardchecking_low_ind(capsys):
    s.lazyforwardchecking_low_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_lazyforwardchecking_low_parent_degreeprune_ind(capsys):
    s.lazyforwardchecking_low_parent_degreeprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_lazyforwardchecking_low_parent_ind(capsys):
    s.lazyforwardchecking_low_parent_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_lazyforwardchecking_parent_degreeprune_ind(capsys):
    s.lazyforwardchecking_parent_degreeprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_lazyforwardchecking_parent_degreesequenceprune_ind(capsys):
    s.lazyforwardchecking_parent_degreesequenceprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_lazyforwardchecking_parent_ind(capsys):
    s.lazyforwardchecking_parent_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_lazyforwardcheckingbackjumping_low_bitset_degreeprune_ind(capsys):
    s.lazyforwardcheckingbackjumping_low_bitset_degreeprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

def test_lazyforwardcheckingbackjumping_low_bitset_degreesequenceprune_ind(capsys):
    s.lazyforwardcheckingbackjumping_low_bitset_degreesequenceprune_ind(g, h, "DEG", mapping=False)
    captured = capsys.readouterr()
    assert captured.out == '400\n'

