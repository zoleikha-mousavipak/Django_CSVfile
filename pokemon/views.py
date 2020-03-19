from django.shortcuts import render, HttpResponse
import csv, io
from django.contrib.auth.decorators import permission_required
from .models import Pokemon
from django.db.models import Q
from .serializers import PokemonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@permission_required('admin.can_add_log_entry')
# Define a function for upload the CSV file:
def pokemon_upload(request):
    template = "pokemon_upload.html"

    prompt = {
        'order' : 'Order of CSV file should be Name, Type1, Type2, ... '
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        return render(request, "This is not a CSV file")

    # importing uploaded CSV file to database:

    decoded_file = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(decoded_file)
    next(io_string)
    reader = csv.reader(io_string, delimiter=',', quotechar="|")

    for column in reader:
        _, created = Pokemon.objects.update_or_create(
            Name=column[1],
            Type1=column[2],
            Type2=column[3],
            Total=column[4],
            HP=column[5],
            Attack=column[6],
            Defense=column[7],
            SpAtk=column[8],
            SpDef=column[9],
            Speed=column[10],
            Generation=column[11],
            Legendary=column[12],
        )
    context={}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def pokemon_download(request):
    items = Pokemon.objects.filter(~Q(Type1='Ghost') | ~Q(Type2='Ghost') | Q(Name__startswith='G'))
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="new_pokemon.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['Name', 'Type1', 'Type2', 'Total', 'HP', 'Attack', 'Defense', 'SpAtk', 'SpDef', 'Speed', 'Generation'])

    for obj in items:
        writer.writerow([obj.Name, obj.Type1, obj.Type2, obj.Total, obj.HP, obj.Attack, obj.Defense, obj.SpAtk, obj.SpDef, obj.Speed, obj.Generation])
    return response


# api endpoint
@api_view(['GET'])
def api_pokemon(request, format=None):
    if request.method == 'GET':
        items = Pokemon.objects.filter(~Q(Type1='Ghost') | ~Q(Type2='Ghost') | Q(Name__startswith='G'))
        serializer = PokemonSerializer(items, many=True)
        return Response(serializer.data)


