def test_schema():
    column1 = ColumnSchema("device", TSDataType.STRING, ColumnCategory.TAG)
    column2 = ColumnSchema("sensor", TSDataType.STRING, ColumnCategory.TAG)
    # Default by FIELD.
    column3 = ColumnSchema("value1", TSDataType.DOUBLE)
    column4 = ColumnSchema("value2", TSDataType.INT32, ColumnCategory.FIELD)
    table = TableSchema("test_table", [column1, column2, column3, column4])

    assert column3.get_category() == ColumnCategory.FIELD
    assert column4.__str__() == "ColumnSchema(value2, INT32, FIELD)"

    with pytest.raises(ValueError):
        tablet = TableSchema("", [column1, column2, column3, column4])

    with pytest.raises(ValueError):
        tablet = TableSchema("test_table", [])

    with pytest.raises(ValueError):
        column = ColumnSchema("test_column",None, ColumnCategory.TAG)

    with pytest.raises(ValueError):
        tablet = TableSchema("test_table", [ColumnSchema("", TSDataType.DOUBLE)])
