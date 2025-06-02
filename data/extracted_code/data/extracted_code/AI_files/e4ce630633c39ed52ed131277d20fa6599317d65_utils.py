

class UtilityTests(TestCase):
    def test_get_age_edge_cases(self):
        "Ensure that get_age() handles edge cases correctly."
        player = PlayerFactory.create(date_of_birth=date(2014, 2, 8))
        for census_date, expected_age in [
            (date(2022, 2, 7), 7),
            (date(2022, 2, 8), 8),
            (date(2022, 2, 9), 8),
        ]:
            with self.subTest(census_date=census_date):
                self.assertEqual(get_age(player, census_date), expected_age)