class TestCheckDictCase(unittest.TestCase):
    def setUp(self):
        # If check_dict_case is in another module, replace with the proper import.
        from __main__ import check_dict_case  # noqa: E402
        self.func: Callable = check_dict_case

    # --- Positive cases ------------------------------------------------------
    def test_all_lowercase_keys(self):
        self.assertTrue(
            self.func({"a": "apple", "b": "banana", "c": "cherry"}),
            "Should return True when every key is lower-case.",
        )

    def test_all_uppercase_keys(self):
        self.assertTrue(
            self.func({"ZIP": "27514", "STATE": "NC"}),
            "Should return True when every key is upper-case.",
        )

    # --- Negative cases ------------------------------------------------------
    def test_empty_dict_returns_false(self):
        self.assertFalse(self.func({}), "Empty dictionary must return False.")

    def test_mixed_case_keys_returns_false(self):
        self.assertFalse(
            self.func({"a": "apple", "B": "banana"}),
            "Mixed lower- and upper-case keys must return False.",
        )

    def test_non_string_key_returns_false(self):
        self.assertFalse(
            self.func({"a": 1, 3: "three"}),
            "Presence of non-string keys must return False.",
        )