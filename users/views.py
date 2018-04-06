from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from users.forms import RegForm, ContactVerificationForm
from users.models import ContactVerification, User


class VerifiedPhoneRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        verifications = request.user.contact_verifications.verified(
            type=ContactVerification.TYPE.PHONE
        )
        if verifications.count() == 0:
            return render(request, 'users/verification_required.html')
        return super(VerifiedPhoneRequiredMixin, self)\
            .dispatch(request, *args, **kwargs)


class RegView(FormView):
    template_name = 'users/reg.html'
    form_class = RegForm
    success_url = '/'

    def form_valid(self, reg_form):
        user = reg_form.save()
        user = authenticate(username=user.phone,
                            password=reg_form.cleaned_data['password1'])
        if user is None:
            pass # TODO: show login error
        else:
            login(self.request, user)
        return super(RegView, self).form_valid(reg_form)

    def form_invalid(self, reg_form):
        return JsonResponse({'errors': reg_form.errors})
        # return self.render_to_response(self.get_context_data(reg_form=reg_form),
        #                                status=400)


class VerifyContactView(LoginRequiredMixin, View):
    form_class = ContactVerificationForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(VerifyContactView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            params = {'user': request.user,
                      'type': self.kwargs['ctype']}
            code = ContactVerification.objects.filter(**params)\
                .order_by('actual_till').last()
            if code is None or (not code.is_verified() and not code.is_actual()):
                code = ContactVerification.objects.create(**params)
            elif code.is_verified():
                return render(self.request, 'users/verify_contact/result.html')
        return render(self.request,
                      'main/_verify_form.html',
                      {'code': code, 'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        try:
            code = ContactVerification.objects.verifiable().get(
                user=request.user,
                type=self.kwargs['ctype']
            )
        except ContactVerification.DoesNotExist:
            context = {'title': _('Contact validation'),
                       'msg': _('There is no any codes for this contact.')}
            return render(self.request, 'main/message.html', context,
                          status=400)
        
        form = self.form_class(data=self.request.POST)
        if form.is_valid():
            if self.request.is_ajax():
                if code.code == form.cleaned_data['code']:
                    code.set_verified()
                    code.save()
                    return render(self.request, 'users/verify_contact/result.html')
                code.errors += 1
                code.save()
                form.add_error('code', _('Unknown code'))
        return render(self.request, 'main/_verify_form.html',
                      {'form': form, 'code': code}, status=400)


def user_login(request):
    login_form = AuthenticationForm()
    if request.method == 'POST':
        request.session.set_test_cookie()
        login_form = AuthenticationForm(request, request.POST)
        response_data = {}
        if login_form.is_valid():
            if request.is_ajax():
                user = login(request, login_form.get_user())
              
        else:
            return JsonResponse({'errors': login_form.errors})
            
    login_form = AuthenticationForm()

    context = {
        'next': request.GET.get('next', '/'),
        'login_form': login_form,
        'request': request
    }

    return render(request, 'users/login.html', context)

# @login_required
# def user_detail(request):

#     def get_user():
#         if hasattr(request, 'user'):
#             return request.user
#         else:
#             from django.contrib.auth.models import AnonymousUser
#             return AnonymousUser()

#     return render(request, 'main/private.html', {
#         'user': SimpleLazyObject(get_user),
#         'perms':  lazy(lambda: PermWrapper(get_user()), PermWrapper)(),
#     })

# @login_required
# def user_edit(request):
#     return render(request, 'main/data_change.html', {})


class CurrentUserMixin(object):
    model = User

    def get_object(self, *args, **kwargs):
        try:
            obj = super(CurrentUserMixin, self).get_object(*args, **kwargs)
        except AttributeError:
            obj = self.request.user

        return obj

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CurrentUserMixin, self).dispatch(*args, **kwargs)


class UserDetailView(CurrentUserMixin, DetailView):
    template_name = 'main/private.html'


class UserUpdateView(CurrentUserMixin, UpdateView):
    template_name = 'main/data_change.html'
    fields = '__all__'