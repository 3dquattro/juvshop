from my.services import send_message, get_messages, dialogues_list_context
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render


# Заглушка под представление диалога по заказу
@login_required
def messages_for_order(request, id: int):
    if request.method == "POST":
        # Отправим сообщение, если мы его отправляем
        send_message(request.user, request.POST["dialogue"], request.POST["text"])
    # ...а потом отрисуем шаблон, вне зависимости отправляли что-либо или нет
    context = get_messages(id, request.user)
    return render(request, "my/messaging.html", context)


# Представление под список диалогов
@login_required
def dialogues_list(request):
    context = dialogues_list_context(request.user)
    return render(request, "my/dialogues.html", context)
