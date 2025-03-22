def create_item(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        Item.objects.create(name=name, description=description, price=price)
        return redirect('item_list')
    return render(request, 'create.html')


@csrf_exempt
def create_item(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        item = Item.objects.create(name=name, description=description, price=price)
        return JsonResponse({'id': item.id, 'name': item.name, 'description': item.description, 'price': item.price})

    return render(request, 'create.html')