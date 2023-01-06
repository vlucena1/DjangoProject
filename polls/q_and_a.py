import csv
from django.core.management import BaseCommand
from app.models import Question

class Command(BaseCommand):
    help = 'carregar arquivos de um Arquivo csv para uma database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                Question.objects.create(
                    attr1=row[0],
                    attr2=row[1],
                )