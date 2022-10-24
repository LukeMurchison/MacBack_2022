from django.test import TestCase
from app import models


class TestContact(TestCase):
    def test_can_create_product(self):
        contact = models.create_product(
            "Banana",
            "Yellow",
            661723,
            True,
        )

        self.assertEqual(contact.id, 1)
        self.assertEqual(contact.name, "Banana")
        self.assertEqual(contact.decs, "Yellow")
        self.assertTrue(contact.in_stock)

    def test_can_view_all_products_at_once(self):
        products_data = [
            {
                "name": "Apples",
                "decs": "keeps the doctor away",
                "batch_number": 8760876,
                "in_stock": True,
            },
            {
                "name": "Limes",
                "decs": "lemon but green",
                "batch_number": 6548546845,
                "in_stock": False,
            },
            {
                "name": "Almonds",
                "decs": "wooden tears",
                "batch_number": 6757959765,
                "in_stock": True,
            },
        ]

        for product_data in products_data:
            models.create_product(
                product_data["name"],
                product_data["decs"],
                product_data["batch_number"],
                product_data["in_stock"],
            )

        products = models.all_products()
        self.assertEqual(len(products), len(products_data))

        products_data = sorted(products_data, key=lambda c: c["name"])
        products = sorted(products, key=lambda c: c.name)

        for data, products in zip(products_data, products):
            self.assertEqual(data["name"], products.name)
            self.assertEqual(data["decs"], products.decs)
            self.assertEqual(data["batch_number"], products.batch_number)
            self.assertEqual(data["in_stock"], products.in_stock)

    def test_can_search_by_name(self):
        products_data = [
            {
                "name": "Apples",
                "decs": "keeps the doctor away",
                "batch_number": 8760876,
                "in_stock": True,
            },
            {
                "name": "Limes",
                "decs": "lemon but green",
                "batch_number": 6548546845,
                "in_stock": False,
            },
            {
                "name": "Almonds",
                "decs": "wooden tears",
                "batch_number": 6757959765,
                "in_stock": True,
            },
        ]

        for product_data in products_data:
            models.create_product(
                product_data["name"],
                product_data["decs"],
                product_data["batch_number"],
                product_data["in_stock"],
            )

        self.assertIsNone(models.find_product_by_name("ibihbi"))

        product = models.find_product_by_name("Apples")

        self.assertIsNotNone(product)
        self.assertEqual(product.decs, "keeps the doctor away")

    def test_can_view_stock(self):
        products_data = [
            {
                "name": "Apples",
                "decs": "keeps the doctor away",
                "batch_number": 8760876,
                "in_stock": True,
            },
            {
                "name": "Limes",
                "decs": "lemon but green",
                "batch_number": 6548546845,
                "in_stock": False,
            },
            {
                "name": "Almonds",
                "decs": "wooden tears",
                "batch_number": 6757959765,
                "in_stock": True,
            },
        ]

        for product_data in products_data:
            models.create_product(
                product_data["name"],
                product_data["decs"],
                product_data["batch_number"],
                product_data["in_stock"],
            )

        self.assertEqual(len(models.stock_products()), 2)

    def test_can_update_product_decs(self):
        products_data = [
            {
                "name": "Apples",
                "decs": "keeps the doctor away",
                "batch_number": 8760876,
                "in_stock": True,
            },
            {
                "name": "Limes",
                "decs": "lemon but green",
                "batch_number": 6548546845,
                "in_stock": False,
            },
            {
                "name": "Almonds",
                "decs": "wooden tears",
                "batch_number": 6757959765,
                "in_stock": True,
            },
        ]

        for product_data in products_data:
            models.create_product(
                product_data["name"],
                product_data["decs"],
                product_data["batch_number"],
                product_data["in_stock"],
            )

        models.update_product_decs("Almonds", "wooden tears that could kill you if you ate a ton.")

        self.assertEqual(
            models.find_product_by_name("Almonds").decs, "wooden tears that could kill you if you ate a ton."
        )

    def test_can_delete_contact(self):
        products_data = [
            {
                "name": "Apples",
                "decs": "keeps the doctor away",
                "batch_number": 8760876,
                "in_stock": True,
            },
            {
                "name": "Limes",
                "decs": "lemon but green",
                "batch_number": 6548546845,
                "in_stock": False,
            },
            {
                "name": "Almonds",
                "decs": "wooden tears",
                "batch_number": 6757959765,
                "in_stock": True,
            },
        ]

        for product_data in products_data:
            models.create_product(
                product_data["name"],
                product_data["decs"],
                product_data["batch_number"],
                product_data["in_stock"],
            )

        models.delete_product("Apples")

        self.assertEqual(len(models.all_products()), 2)