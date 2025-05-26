

def test_function_with_namespace():
    res = query("RETURN string.join(null, ',') AS result")
    assert res.result_set == [[None]]

    res = query("RETURN string.join([], 'foo') AS result")
    assert res.result_set == [[""]]

    res = query("RETURN string.join(['a', 'b'], ', ') AS result")
    assert res.result_set == [['a, b']]

    res = query("RETURN string.join(['a', 'b']) AS result")
    assert res.result_set == [['ab']]

    try:
        query(f"RETURN string.join(['a', 'b'], ', ', ', ') AS result")
        assert False, "Expected an error"
    except ResponseError as e:
        assert "Received 3 arguments to function 'string.join', expected at most 2" in str(e)

    try:
        query(f"RETURN string.join(1, 2) AS result")
        assert False, "Expected an error"
    except ResponseError as e:
        assert "Type mismatch: expected List or Null but was Integer" in str(e)

    for value, name in [(1.0, 'Float'), (True, 'Boolean'), ({}, 'Map'), ([], 'List'), ("null", 'Null')]:
        try:
            query(f"RETURN string.join(['a', {value}], ',') AS result")
            assert False, "Expected an error"
        except ResponseError as e:
            assert f"Type mismatch: expected String but was {name}" in str(e)