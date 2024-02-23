from django.http import HttpResponse
from django.shortcuts import redirect,render
from .forms import OrderForm, Order

# Create your views here.
def addOrder_view(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_urls')
    template_name = 'CRUD_APP/add.html'
    context = {'form':form}
    return render(request,template_name,context)

def show_view(request):
    obj = Order.objects.all()
    template_name = 'CRUD_APP/show.html'
    context = {'data':obj}
    return render(request,template_name,context)


def delete_view(request, pk):
    obj = Order.objects.filter(eid=pk)
    if request.method == 'POST':
        for i in obj:
            i.delete()
        return redirect('show_urls')
    template_name = 'CRUD_APP/del_confirm.html'
    context = {'data': obj }
    return render(request, template_name, context)



def update_view(request, upk):
    print(upk)
    obj = Order.objects.get(eid=upk)
    form = OrderForm(instance = obj)
    if request.method == 'POST':
        form = OrderForm(data=request.POST , instance = obj)
        if form.is_valid():
            form.save()
            return redirect('show_urls')
    template_name = 'CRUD_APP/add.html'
    context = {'form': form}
    return render(request,template_name,context)