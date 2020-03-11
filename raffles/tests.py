from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from raffles.api.serializers import PersonSerializer, RaffleSerializer
from .models import Raffle, Person


class CreateRaffleTest(APITestCase):
    """
    CreateRaffleTest APITestCase
    """

    def setUp(self):
        self.data = {
            "name": "Fulano de Tal",
            "phone": "01010101010",
            "birthday": "1990-05-12"
        }

        self.url = reverse('raffle-list')

    def test_create_raffle(self):
        """
        Ensure we can create a new raffle person object.
        """

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Raffle.objects.count(), 1)
        self.assertEqual(Raffle.objects.get().person.name, 'Fulano de Tal')

    def test_create_bad_data_raffle(self):
        """
        Ensure we can't create a new raffle object with bad fields.
        """

        data = {
            "name": "Fulano de Tal",
            "phone": "1A2B",
            "birthday": "10-10-1999",
        }

        data2 = {
            "name": "Fu",
            "phone": "88988888888",
            "birthday": "10-10-1999",
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response2 = self.client.post(self.url, data2, format='json')
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)


class ReadRaffleTest(APITestCase):
    """
        ReadRaffleTest APITestCase
    """

    def setUp(self):
        data = {
            "name": "Fulano de Tal",
            "phone": "01010101010",
            "birthday": "1990-05-12"
        }

        person = Person.objects.create(**data)
        self.raffle = Raffle.objects.create(person=person)

    def test_can_read_raffle_list(self):
        """
        Ensure we can read a list raffles.
        """
        response = self.client.get(reverse('raffle-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_raffle_detail(self):
        """
        Ensure we can read a raffle object.
        """
        response = self.client.get(reverse('raffle-detail', args=[self.raffle.number]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateRaffleTest(APITestCase):
    """
    Ensure we can update a obj raffle.
    """

    def setUp(self):
        data = {
            "name": "Fulano de Tal",
            "phone": "01010101010",
            "birthday": "1990-05-12"
        }

        person = Person.objects.create(**data)
        self.raffle = Raffle.objects.create(person=person)

    def test_can_update_raffle(self):
        data = {
            "name": "Sicrano Beltrano"
        }
        response = self.client.patch(
            reverse('raffle-detail', args=[self.raffle.number]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteRaffleTest(APITestCase):
    def setUp(self):
        self.data = {
            "name": "Fulano de Tal",
            "phone": "01010101010",
            "birthday": "1990-05-12"
        }

        person = Person.objects.create(**self.data)
        self.raffle = Raffle.objects.create(person=person)

    def test_can_delete_raffle(self):
        response = self.client.delete(reverse('raffle-detail', args=[self.raffle.number]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class RafflingTest(APITestCase):
    def setUp(self):
        data = [
            {
                "name": "Pedro José",
                "birthday": "1990-05-12",
                "phone": "01010101010"
            },
            {
                "name": "Marcos Joaquim",
                "birthday": "1990-05-12",
                "phone": "01010101010"
            },
            {
                "name": "Rafael José",
                "birthday": "1990-05-12",
                "phone": "01010101010"
            }
        ]

        for d in data:
            p = Person.objects.create(**d)

            Raffle.objects.create(person=p)

    def test_can_raffling(self):
        response = self.client.get(reverse('raffling'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
