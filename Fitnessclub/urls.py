from django.urls import path, include
from .views import ( hall_list, card_list, card_detail, signup,
                    create_card, delete_card, update_card, create_service, service_list,
                    about_us, service_detail, hall_add, employee_list, privacy_policy,
                     NewsView, NewsReadView, current_date_view, employees_info, faq_view,
                     WorkView, feedback_add_view, feedback_view, promocode_view, mediaview, plot_view,
                        news_read1, news_read2,
                     plot_clients_view)
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('about_us', about_us, name='about_us'),
    path('Work/', WorkView, name = 'Work'),
    path('calendar/', current_date_view, name = 'calendar'),
    path('halls/', hall_list, name='halls_list'),
    path('Promocodes/', promocode_view, name='Promocodes'),
    path('halls/create/', hall_add, name='halls_add'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
    path('news/', NewsView, name='news'),
    path('feedback/', feedback_view, name='feedback'),
    path('feedback/feedback_add', feedback_add_view, name='feedback_add'),
    path('FAQ/', faq_view, name='faq'),
    path('news_read', NewsReadView, name='news_read'),
    path('news_read/news1', news_read1, name='news1'),
    path('news_read/news2', news_read2, name='news2'),
    path('cards/', card_list, name='card_list'),
    path('services/', service_list, name='service_list'),
    path('employees/', employee_list, name = 'employee_list'),
    path('employees/<int:employee_id>/', employees_info, name = 'employees_info'),
    path('services/<int:service_id>/', service_detail, name='service_detail'),
    path('cards/card/<int:card_id>/', card_detail, name='card_detail'),
    path('registation/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', signup, name='signup'),
    path('media/', mediaview, name = 'media'),
    path('plot/', plot_view, name = 'plot'),
    path('plot/', plot_clients_view, name = 'plot_clients_view'),
    path('cards/create/', create_card, name='create_card'),
    path('cards/delete/<int:card_id>/', delete_card, name='delete_card'),
    path('cards/update/<int:card_id>/', update_card, name='update_card'),
    path('cards/<int:card_id>/create_service/', create_service, name='create_service')
]