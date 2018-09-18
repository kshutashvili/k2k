from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from info.forms import QuestionForm
from info.models import (
    Question, LandingTabTransfer, MainBlock, FooterMenuBlock1Transfer,
    FooterMenuBlock2Transfer, FooterMenuBlock3Transfer, Privileges
)
from users.views import VerifiedPhoneRequiredMixin


class TransferView(LoginRequiredMixin,
                   VerifiedPhoneRequiredMixin,
                   TemplateView):

    template_name = 'finance/transfers.html'

    def get_context_data(self, **kwargs):
        context = super(TransferView, self).get_context_data(**kwargs)

        context['tabs'] = LandingTabTransfer.objects\
                                            .actual()\
                                            .select_related('content')
        context['questions'] = Question.objects.answered()\
                                               .filter(theme='transfers')
        context['main_block'] = MainBlock.objects.filter(page='transfers')
        context['footer_menu1'] = FooterMenuBlock1Transfer.objects\
                                                          .actual()\
                                                          .select_related(
                                                              'content')
        context['footer_menu2'] = FooterMenuBlock2Transfer.objects\
                                                          .actual()\
                                                          .select_related(
                                                              'content')
        context['footer_menu3'] = FooterMenuBlock3Transfer.objects\
                                                          .actual()\
                                                          .select_related(
                                                              'content')
        context['privileges'] = Privileges.objects\
                                          .filter(
                                              page='transfers',
                                              draft=False)
        context['question_form'] = QuestionForm()

        return context


class TransferViewPage(LoginRequiredMixin,
                       VerifiedPhoneRequiredMixin,
                       TemplateView):

    template_name = 'finance/transfer_page.html'

    def get_context_data(self, **kwargs):
        context = super(TransferViewPage, self).get_context_data(**kwargs)

        context['tabs'] = LandingTabTransfer.objects\
                                            .actual()\
                                            .select_related(
                                                'content')
        context['footer_menu1'] = FooterMenuBlock1Transfer.objects\
                                                          .actual()\
                                                          .select_related(
                                                              'content')
        context['footer_menu2'] = FooterMenuBlock2Transfer.objects\
                                                          .actual()\
                                                          .select_related(
                                                              'content')
        context['footer_menu3'] = FooterMenuBlock3Transfer.objects\
                                                          .actual()\
                                                          .select_related(
                                                              'content')

        return context
