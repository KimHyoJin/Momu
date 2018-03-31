from .models import Test, LANGUAGE_CHOICES
from rest_framework import serializers

"""
class TestSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    boolean = serializers.BooleanField(default=False)
    char = serializers.CharField(allow_null=False, allow_blank=True, default="char", max_length=256)
    email = serializers.EmailField(allow_null=False)
    text = serializers.CharField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default="KR")

    def create(self, validated_data):
        return Test.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.boolean = validate_data.get('boolean', instance.boolean)
        instance.char = validate_data.get('char', instance.char)
        instance.email = validate_data.get('email', instance.email)
        instance.text = validate_data.get('text', instance.text)
        instance.language = validate_data.get('language', instance.language)
        instance.save()

        return instance
"""

# 자동으로 serializers.Serializer에서 설정한 field들과 create, update 함수를 생성
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'boolean', 'char', 'text', 'email', 'language')