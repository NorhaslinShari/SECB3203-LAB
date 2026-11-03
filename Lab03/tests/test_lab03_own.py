from qc import classify_read, qc_summary, trim_low_quality

def test_classify_read_boundary1():
    assert classify_read(500, 11, 55.0) == "review"

def test_classify_read_boundary2():
    assert classify_read(499, 10, 50.0) == "reject"
   
def test_trim_low_quality():
    assert trim_low_quality([30, 32, 35, 12, 10]) == 3 
    