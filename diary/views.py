from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayCreateForm
from .models import Day

class IndexView(generic.ListView):
    model = Day
    paginate_by = 3

class AddView(LoginRequiredMixin, generic.CreateView):
    model = Day
    form_class = DayCreateForm #カスタマイズしたクラスformを使用
    #fields = '__all__'で汎用ビューで単純なモデルの場合はこれで作成できる。→forms.pyを省ける。
    success_url = reverse_lazy('diary:index')

class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')
        
class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Day
    success_url = reverse_lazy('diary:index')

class DetailView(generic.DetailView):
    model = Day
    