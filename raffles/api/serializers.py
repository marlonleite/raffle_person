from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from ..models import Raffle, Person


class PersonSerializer(serializers.ModelSerializer):
    """
    Serializer to Person Model
    """

    class Meta:
        model = Person
        fields = ['id', 'name', 'birthday', 'phone']


class RaffleSerializer(serializers.ModelSerializer):
    """
    Serializer to Raffle Model
    """

    name = serializers.CharField(write_only=True)
    birthday = serializers.DateField(write_only=True, required=False)
    phone = serializers.CharField(write_only=True)

    class Meta:
        model = Raffle
        fields = ['number', 'name', 'phone', 'birthday']
        read_only_fields = ('number',)

    def validate_phone(self, attr):
        contains_letter = any(c.isalpha() for c in attr)

        if contains_letter:
            raise serializers.ValidationError(
                "Only numbers are allowed.")

        if len(attr) != 11:
            raise serializers.ValidationError(
                "Incorrect number. Make sure it contains 11 digits.")

        return attr

    def to_representation(self, instance):
        obj = super().to_representation(instance)
        obj['name'] = instance.person.name
        obj['birthday'] = instance.person.birthday
        obj['phone'] = instance.person.phone

        return obj

    def create(self, validated_data):
        person = PersonSerializer().create(validated_data=validated_data)
        return Raffle.objects.create(person=person)

    def update(self, instance, validated_data):
        PersonSerializer().update(
            instance=instance.person, validated_data=validated_data)
        return instance

    def get_numbers(self, obj):
        return obj.number
