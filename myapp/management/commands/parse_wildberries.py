from django.core.management.base import BaseCommand
from myapp.task import parse_wildberries

class Command(BaseCommand):
    help = 'Parse Wildberries products'
    
    def add_arguments(self, parser):
        parser.add_argument('query', type=str, help='Search query')
    
    def handle(self, *args, **options):
        query = options['query']
        parse_wildberries(query)
        self.stdout.write(self.style.SUCCESS(f'Successfully parsed products for query: {query}'))