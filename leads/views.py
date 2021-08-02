from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lead
from .forms import LeadModelForm, CustomUserCreationForm

# class based views


class signupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class landingPageview(generic.TemplateView):
    template_name = "landing.html"


class leadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class leadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class leadCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        # TODO send email
        send_mail(
            subject="A Lead has been created",
            message="Get to site to see the new Lead.",
            from_email="email@email.com",
            recipient_list=["email2@email.com"]
        )
        return super(leadCreateView, self).form_valid(form)


class leadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


class leadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")

# function based views


# def landing_page(request):
#     return render(request, "landing.html")


# # Create your views here.


# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         "leads": leads
#     }
#     #parameters: request and template
#     return render(request, "leads/lead_list.html", context)


# def lead_detail(request, pk):

#     lead = Lead.objects.get(id=pk)
#     context = {
#         "lead": lead
#     }
#     print(lead)
#     return render(request, "leads/lead_detail.html", context)


# def lead_create(request):
#     form = LeadModelForm()
#     if request.POST:
#         print('Post request receival...')
#         # passing data to be created as parameter
#         form = LeadModelForm(request.POST)
#         # form validity
#         if form.is_valid():
#             form.save()

#             return redirect("/leads")

#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)

#     # form
#     if request.method == "POST":
#         print('Post request on Update . . .')

#         form = LeadModelForm(request.POST, instance=lead)

#         if form.is_valid():
#             form.save()
#             return redirect('/leads')

#     context = {
#         "form": form,
#         "lead": lead
#     }
#     return render(request, 'leads/lead_update.html', context)


# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect("/leads")
