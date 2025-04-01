from rest_framework import serializers
from .models import KayakReservation, KayakRoute, KayakRentalSettings, CabinReservation, Cabin, CampingReservation, BlogPost

class KayakRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = KayakRoute
        fields = '__all__'

class KayakRentalSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = KayakRentalSettings
        fields = '__all__'


class KayakReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = KayakReservation
        fields = '__all__'

        def validate(self, data):
            if data['kayak_extra_child_quantity'] > data['kayak_double_quantity']:
                raise serializers.ValidationError("Liczba dostawek nie może być większa niż liczba kajaków 2-osobowych.")
            return data

    def validate(self, data):
        reservation = KayakReservation(**data)
        reservation.clean()  # Sprawdzenie dostępności kajaków
        return data

class CabinReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CabinReservation
        fields = '__all__'
        read_only_fields = ['total_price']

class CabinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabin
        fields = '__all__'

class CampingReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampingReservation
        fields = '__all__'
        read_only_fields = ['total_price']  # Cena obliczana automatycznie

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'image', 'link']