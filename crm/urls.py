from leads.views import landingPageview, signupView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),  # admin
    path('', landingPageview.as_view(), name="landing-page"),  # landing page
    path('leads/', include('leads.urls', namespace='leads')),  # leads urls
    path('agents/', include('agents.urls', namespace='agents')),  # agents path
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signupView.as_view(), name='signup')
    # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
