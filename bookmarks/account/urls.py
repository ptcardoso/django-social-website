from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, logout_then_login
from django.urls import reverse_lazy

from . import views

app_name = 'account'
urlpatterns = [
    # url(r'^login/$', views.user_login, name='login')
    url(r'^password-reset/$', PasswordResetView.as_view(success_url=reverse_lazy('account:password_reset_done')),
        name='password_reset'),
    url(r'^password-reset/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        PasswordResetConfirmView.as_view(success_url=reverse_lazy('account:password_reset_complete')),
        name='password_reset_confirm'),
    url(r'^password-reset/complete/^$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url(r'^password-change/$', PasswordChangeView.as_view(), name='password_change'),
    url(r'^password-change/done/$', PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard')
]
