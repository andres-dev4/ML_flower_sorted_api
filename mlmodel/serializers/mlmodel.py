from rest_framework import serializers

class FlowerSerializer(serializers.Serializer):
    """
    serializer definition
    """
    save_data=serializers.BooleanField()
    name=serializers.CharField(allow_null=False)
    inputs_values = serializers.ListField(
        child=serializers.ListField(
            child=serializers.FloatField()
        ),
        min_length=1
    )
