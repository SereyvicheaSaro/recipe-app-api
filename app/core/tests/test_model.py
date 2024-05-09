"""
Test for model
"""

from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def create_user(email='test@example.com', password='testpass123'):
    """Create and return a new user"""
    return get_user_model().objects.create_user(email, password)

class ModelTests(TestCase):
    """Test models."""
    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['test2@Example.com', 'test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'smaple123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Thes that creating a user without an email raises a ValuesError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Test creating a new superuser."""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    # test recipe model
    def test_create_recipe(self):
        """Test creating a recipe is successful."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )
        recipe = models.Recipe.objects.create(
            user = user,
            title = 'Sample',
            time_minutes = 5,
            price = Decimal('5.50'),
            description = 'Sample description.',
        )
        self.assertEqual(str(recipe), recipe.title)

    # test for tags
    def test_create_tag(self):
        """test creating a tag is successful."""
        user = create_user()
        tag = models.Tag.objects.create(user=user, name='Tage1')
        self.assertEqual(str(tag), tag.name)

    # test for ingredient
    def test_create_ingredient(self):
        """Test creating ingredient successful."""
        user = create_user()
        ingredient = models.Ingredient.objects.create(
            user= user,
            name = 'Ingredient1'
        )
        self.assertEqual(str(ingredient), ingredient.name)