from django.test import TestCase
from forms.models import *

# Create your tests here.

class GamesModelTestCase(TestCase):
    def setUp(self):
        self.game = Games.objects.create(
            nombre="Juego de Prueba",
            descripcion="Descripción del juego de prueba",
            precio=50,
            stock=100,
            plataforma=1,
            imagen=None,
        )

    def test_nombre_max_length(self):
        max_length = self.game._meta.get_field('nombre').max_length
        self.assertEqual(max_length, 50)

    def test_precio_positive(self):
        self.assertGreaterEqual(self.game.precio, 0)

    def test_imagen_upload_to(self):
        if self.game.imagen:
            self.assertTrue(self.game.imagen.name.startswith('games/'))