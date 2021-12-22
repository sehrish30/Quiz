from django.shortcuts import render, get_object_or_404

from questions.forms import UserRegisteration
from .models import Question

# Create your views here.
def question_list(request):
    question_list = Question.objects.all().order_by("-created_at")
    return render(request, "QList.html", {"question_list": question_list})


def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    return render(request, "QDetails.html", {"question": question})


def register(request):
    if request.method == "POST":
        user_form = UserRegisteration(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])

            new_user.save()
            return render(request, "register_done.html", {"user_form": user_form})
    else:
        user_form = UserRegisteration()

    return render(request, "register.html", {"user_form": user_form})
