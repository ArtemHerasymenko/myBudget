from django.shortcuts import render
from .forms import PurchaseForm

# Create your views here.

def newPurchase(request):
	form = PurchaseForm(request.POST or None)

	context = {
		"hint" : "Add new purchase",
		"form" : form,
	}

	if form.is_valid():
		form.save()
		context = {
			"hint" : "You purchase was saved successfully"
		}

	print(form)

	
	
	return render(request, "newPurchase.html", context)
