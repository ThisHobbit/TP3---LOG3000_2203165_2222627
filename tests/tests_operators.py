import unittest
from utils.operators import add, subtract, multiply, divide

class TestOperators(unittest.TestCase):
    """
    Suite de tests pour les opérations arithmétiques de base
    définies dans utils/operators.py.
    """

    def test_add(self):
        """
        Teste la fonction `add` avec différents cas :
        - addition de nombres positifs
        - addition de nombres négatifs
        - addition avec zéro
        """
        self.assertEqual(add(10, 20), 30)          # Cas simple
        self.assertEqual(add(-2, 2), 0)            # Résultat nul
        self.assertEqual(add(0, 5), 5)             # Ajout de zéro

    def test_subtract(self):
        """
        Teste la fonction `subtract` avec divers scénarios :
        - soustraction de zéro
        - résultat négatif
        - soustraction de nombres négatifs
        """
        self.assertEqual(subtract(5, 0), 5)        # Soustraction de zéro
        self.assertEqual(subtract(2, 5), -3)       # Résultat négatif
        self.assertEqual(subtract(-3, -1), -2)     # Nombres négatifs

    def test_multiply(self):
        """
        Teste la fonction `multiply` avec plusieurs cas :
        - multiplication positive
        - mélange de signes positifs/négatifs
        - multiplication par zéro
        """
        self.assertEqual(multiply(3, 4), 12)       # Cas standard
        self.assertEqual(multiply(-2, 3), -6)      # Signe négatif
        self.assertEqual(multiply(-1, -1), 1)      # Deux négatifs
        self.assertEqual(multiply(0, 100), 0)      # Multiplication par zéro

    def test_divide(self):
        """
        Teste la fonction `divide` dans différents contextes :
        - division entière et flottante
        - résultat négatif
        - division par un
        - division par zéro (doit lever ZeroDivisionError)
        """
        self.assertEqual(divide(10, 2), 5)         # Division normale
        self.assertEqual(divide(-10, 2), -5)       # Résultat négatif
        self.assertEqual(divide(10, -2), -5)       # Diviseur négatif
        self.assertEqual(divide(10, 1), 10)        # Division par un
        with self.assertRaises(ZeroDivisionError): # Division par zéro
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
