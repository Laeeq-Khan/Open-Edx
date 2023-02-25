"""
Serializers for learner recommendations APIs.
"""
from rest_framework import serializers


class ActiveCourseRunSerializer(serializers.Serializer):
    """Serializer for active course run for course about page recommendations API"""
    key = serializers.CharField()
    marketingUrl = serializers.URLField(source="marketing_url")


class CourseOwnersSerializer(serializers.Serializer):
    """Serializer for course owners for course about page recommendations API"""
    key = serializers.CharField()
    name = serializers.CharField()
    logoImageUrl = serializers.URLField(source="logo_image_url")


class CourseImageSerializer(serializers.Serializer):
    """Serializer for course image for course about page recommendations API"""
    src = serializers.URLField()


class RecommendedCourseSerializer(serializers.Serializer):
    """Serializer for a recommended course from the recommendation engine"""
    key = serializers.CharField()
    uuid = serializers.UUIDField()
    title = serializers.CharField()
    image = CourseImageSerializer()
    prospectusPath = serializers.SerializerMethodField()
    owners = serializers.ListField(
        child=CourseOwnersSerializer(), allow_empty=True
    )
    activeCourseRun = ActiveCourseRunSerializer(source="active_course_run")

    def get_prospectusPath(self, instance):
        url_slug = instance.get("url_slug")
        return f"course/{url_slug}"


class RecommendationsSerializer(serializers.Serializer):
    """Recommended courses for course about page"""

    courses = serializers.ListField(
        child=RecommendedCourseSerializer(), allow_empty=True
    )
    isControl = serializers.BooleanField(
        source="is_control",
        default=None
    )
