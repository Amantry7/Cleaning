from django.shortcuts import render
from .models import Settings,Subject,Client,Partners
from apps.secondary.models import About, Team
from apps.contact.models import Contact
from apps.telegram.views import get_text


# Create your views here.
def index(request):
    settings = Settings.objects.latest("id")
    subject = Subject.objects.all()
    client = Client.objects.all()
    partners = Partners.objects.all()
    return render(request, "base/index.html", locals() )

def about(request):
    settings = Settings.objects.latest("id")
    about = About.objects.latest('id')
    team = Team.objects.all()
    partners = Partners.objects.all()

    return render(request, "about.html", locals())

def servise(request):
    settings = Settings.objects.latest("id")
    subject = Subject.objects.all()
    partners = Partners.objects.all()
    return render(request, "services.html", locals())

def contact(request):
    settings = Settings.objects.latest("id")

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        salary = request.POST.get('salary')
        number = request.POST.get('number')
        message = request.POST.get("message")
        
        contact = Contact.objects.create(name=name, email=email, phone=number, sabject=salary, message=message)

        # Получаем ID заказа и отправляем сообщение с инлайн-кнопками
        order_id = contact.id
        get_text(f"""
            Оставлен запрос о клининге
            Имя: {name}
            Почта: {email} 
            Услуга: {salary}
            Номер телефона: {number}
            Сообщение: {message}
        """, order_id)


    return render(request, "contact.html", locals())