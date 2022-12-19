from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, FormView, DetailView, ListView
from django.urls import reverse_lazy
from customerprofile.forms import CustomerLoginForm
from django.contrib.auth import authenticate, login
from .models import Manager
from order.models import Order, ORDER_STATUS_CHOICES


class ManagerLoginView(FormView):
    template_name = 'managerlogin.html'
    form_class = CustomerLoginForm
    success_url = reverse_lazy('manager:home')

    def form_valid(self, form):
        uname = form.cleaned_data.get('username')
        pword = form.cleaned_data.get('password')
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Manager.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name,
                          {'form': self.form_class, 'error': 'Логін або пароль не співпадають!'})
        return super().form_valid(form)


class ManagerRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Manager.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect('/manager/login/')
        return super().dispatch(request, *args, **kwargs)


class ManagerHomeView(ManagerRequiredMixin, TemplateView):
    template_name = 'managerhome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['created_orders'] = Order.objects.filter(status='created')
        return context


class ManagerOrderDetailView(ManagerRequiredMixin, DetailView):
    template_name = 'manager-order-detail.html'
    model = Order
    context_object_name = 'ord_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allstatus'] = ORDER_STATUS_CHOICES

        return context


class ManagerOrderListView(ManagerRequiredMixin, ListView):
    template_name = 'manager-order-list.html'
    queryset = Order.objects.all()
    context_object_name = 'allorders'


class ManagerOdrerStatusChangeView(ManagerRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        order_id = self.kwargs['pk']
        order_obj = Order.objects.get(id=order_id)
        new_status = request.POST.get('status')
        order_obj.status = new_status
        order_obj.save()

        return redirect(reverse_lazy('manager:orderdetail', kwargs={'pk': order_id}))
