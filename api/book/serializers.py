from book.models import (
    Instructor, 
    FitnessClass,
    BookingSlot
    )
from account.models import CustomUser
from rest_framework import serializers

class CustomUserReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "key",
            "email",
            "user_type",
            "first_name",
            "last_name",
            "is_active"
        )

class InstructerSerializers(serializers.ModelSerializer):
    user_instructor = CustomUserReadSerializers(read_only=True)
    user_instructor_id = serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.filter(user_type='instructor'),
                                                            write_only=True,
                                                            source='user_instructor'
                                                            )
    class Meta:
        model = Instructor
        fields = '__all__'
        
        
        read_only_fields = ("user_instructor", )
        # extra_kwargs = {
        #     'user_instructor': {'read_only': True},

        # }
    
    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['experience'] = str(result.get("experience")) + " month"
        return result

class FitnessClassSerializers(serializers.ModelSerializer):
    instructor_email = serializers.SerializerMethodField()
    def get_instructor_email(self, obj):
        return [i.user_instructor.email for i in obj.instructer.all()]
        
    

    class Meta:
        model = FitnessClass
        fields = '__all__'
        
        read_only_fields = ("instructor_email",  )
        extra_kwargs = {
                'instructer': {'write_only': True}
            }


class BookingSlotSerialisers(serializers.ModelSerializer):
    client_email = serializers.SerializerMethodField()
    client_name = serializers.SerializerMethodField()

    # instructor_email = serializers.SerializerMethodField()
    
    
    # def get_instructor_email(self, obj):
    #     return [j.user_instructor.email for i in obj.fitness_class.all() for j in i.instructer.all() ]

    
    def get_client_name(self, object):
        return object.client.first_name + " " + object.client.last_name
    
    def get_client_email(self, object):
        return object.client.email
    
    class Meta:
        model = BookingSlot
        fields = '__all__'

        # read_only_fields = ("client_email", 'instructor_email')
        read_only_fields = ("client_email", )

        extra_kwargs = {
                'client': {'write_only': True},
                # 'fitness': {'write_only': True},
            }
    
    def validate(self, attrs):
        for classes in attrs.get('fitness_class'):
            booking_slot = BookingSlot.objects.filter(fitness_class=classes)
            if booking_slot.filter(client=attrs.get('client')).exists():
                raise serializers.ValidationError(f"Fitness class id {classes.id} allready exist with user {attrs.get('client').id} ids")
            if classes.available_slot == booking_slot.count():
                raise serializers.ValidationError(f"Available slot are not available in fitness class {classes.id}")
        return super().validate(attrs)