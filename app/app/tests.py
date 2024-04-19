"""
Sample tests
"""
from django.test import SimpleTestCase

from app  import cal
class CalTests(SimpleTestCase):
    """Test teh cal module. """
    def test_add_numbers(self):     # make sure that the function should start with ** test_ **
        """Test adding numbers togerther."""
        res = cal.add(5, 6)
        self.assertEqual(res, 11)
    
    def test_substract_number(self):
        """Test substract numbers."""
        res = cal.substract(10, 9)
        self.assertEqual(res, 1)