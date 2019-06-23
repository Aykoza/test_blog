from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Message
from blog.forms.message import MessageForm


class MessageList(generic.ListView):
    model = Message
    template_name = 'main.html'
    form = MessageForm

    def get_context_data(self, **kwargs):
        context = super(MessageList, self).get_context_data(**kwargs)
        context['messages'] = Message.objects.all()
        context['form'] = self.form
        return context

    def add_message(request):
        if request.method == 'POST':
            new_message = Message(text=request.POST['text'])
            new_message.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            Http404('Post request ERROR!')

