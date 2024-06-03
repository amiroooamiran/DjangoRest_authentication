from django.core.management.base import BaseCommand
class Command(BaseCommand):
    # python3 manage.py help welcome
    help = 'Just saying Welcome to django users'  
    
    def handle(self, *args, **kwargs):
        self.stdout.write("Welcome to django commands")