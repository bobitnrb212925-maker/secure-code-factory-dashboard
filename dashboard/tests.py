from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import SITFPillar, SecurityFinding

User = get_user_model()


class SecureFactoryTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!",
        )
        self.pillar = SITFPillar.objects.create(
            name="Endpoint/IDE",
            description="Development environment security.",
        )

    def test_user_login(self):
        result = self.client.login(
            username="testuser",
            password="TestPassword123!",
        )
        self.assertTrue(result)

    def test_security_finding_creation(self):
        finding = SecurityFinding.objects.create(
            title="Weak Password Protection",
            description="User accounts lack strong password enforcement.",
            pillar=self.pillar,
            severity="High",
            status="Open",
        )
        self.assertEqual(SecurityFinding.objects.count(), 1)
        self.assertEqual(finding.severity, "High")
