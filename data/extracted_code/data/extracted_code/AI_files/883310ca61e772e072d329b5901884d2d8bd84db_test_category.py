import unittest
import unittest
from wooODM.products.category import Category
from wooODM.core import WooCommerce

class TestCategoryModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize WooCommerce API with dummy credentials for testing
        WooCommerce.init(
            url="",
            consumer_key="",
            consumer_secret=""
        )
    @classmethod
    def create_test_category(cls, name="Test Category", slug="test-category", description="A category for testing"):
        category = Category(
            name=name,
            slug=slug,
            description=description
        )
        return category.save()

    @classmethod
    def delete_test_category(cls, category: Category):
        return category.delete()

    def test_create_category(self):
        category = Category(
            name="Test Category",
            slug="test-category",
            description="A category for testing"
        )
        saved_category = category.save()
        self.assertIsNotNone(saved_category.id)
        self.assertEqual(saved_category.name, "Test Category")

    def test_get_category(self):
        test_category = TestCategoryModel.create_test_category(name="Get Test Category", slug="get-test-category")
        category = Category.get(test_category.id)
        self.assertEqual(category.id, test_category.id)
        self.assertEqual(category, test_category)

        test_category.delete()
        with self.assertRaises(Exception):
            Category.get(test_category.id)

    def test_get_all_categories(self):
        categories = Category.all(per_page=5, page=1)
        self.assertIsInstance(categories, list)
        self.assertGreaterEqual(len(categories), 1)
        self.assertIsInstance(categories[0], Category)

    def test_create_incomplete_category(self):
        with self.assertRaises(ValueError):
            Category(
                slug="incomplete-category"
            ).save()

    def test_create_category_without_slug(self):
        with self.assertRaises(ValueError):
            Category(
                name="Category without Slug"
            ).save()

    def test_create_category_with_invalid_data(self):
        with self.assertRaises(ValueError):
            Category(
                name="Invalid Category",
                slug="invalid-category",
                description=123  # Invalid type for description
            ).save()

    def test_update_category_with_invalid_data(self):
        category_id = 1  # Update with a valid category ID
        category = Category.get(category_id)
        category.description = 123  # Invalid type for description
        with self.assertRaises(ValueError):
            category.save()

    def test_smoke(self):
        # Create a category
        category = TestCategoryModel.create_test_category(
            name="Smoke Test Category",
            slug="smoke-test-category",
            description="A category for smoke testing"
        )
        self.assertIsNotNone(category.id)
        self.assertEqual(category.name, "Smoke Test Category")
        self.assertEqual(category.description, "A category for smoke testing")

        # Update the category
        category.name = "Updated Smoke Test Category"
        updated_category = category.save()
        self.assertEqual(updated_category.name, "Updated Smoke Test Category")

        # Delete the category
        delete_response = updated_category.delete()
        self.assertEqual(delete_response, updated_category)

if __name__ == '__main__':
    unittest.main()