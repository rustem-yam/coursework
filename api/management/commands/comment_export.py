import os
import sys

api_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(api_path)

from api.resources import CommentResource
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Outputs Comments table export in CSV format"

    def handle(self, *args, **options):
        dataset = CommentResource().export()
        self.stdout.write(self.style.SUCCESS(dataset))
