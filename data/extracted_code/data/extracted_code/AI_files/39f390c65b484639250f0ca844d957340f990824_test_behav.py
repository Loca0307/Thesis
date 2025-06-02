    expected_insertions = 4
    assert len(after) - len(before) == expected_insertions, (
        f"PositionIntervalMap failed to insert the expected number of entries. "
        f"Expected {expected_insertions}, but got {len(after) - len(before)}."
    )