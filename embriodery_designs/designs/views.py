from django.shortcuts import redirect, render 
from .models import Design

# Create your views here.
def design_list(request):
    designs = Design.objects.all()
    return render(request, "index.html", {"alldesigns":designs})

def add_design(request):
    if request.method == "POST":
        image = request.FILES.get('image')
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        dimensions = request.POST.get('dimensions')
        stitch_details = request.POST.get('stitch_details')
        price = request.POST.get('price')

        design = Design(
            image = image if image else None,
            product_name = product_name,
            description = description,
            dimensions = dimensions,
            stitch_details = stitch_details,
            price = price
        )
        design.save()
        return redirect("all-designs")
    return render(request, "index.html")

def update_design(request, id):
    design = Design.objects.get(id=id)   # Load existing row

    if request.method == "POST":
        image = request.FILES.get('image')
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        dimensions = request.POST.get('dimensions')
        stitch_details = request.POST.get('stitch_details')
        price = request.POST.get('price')

        # Update fields
        design.product_name = product_name
        design.description = description
        design.dimensions = dimensions
        design.stitch_details = stitch_details
        design.price = price

        # 👉 Correctly handle image update
        if image:
            design.image = image  

        design.save()
        return redirect("all-designs")

    # GET request → return form with existing details
    return render(request, "index.html", {"design": design})


def delete_design(request, id):
    design = Design.objects.filter(id=id)
    design.delete()

    return redirect("all-designs")