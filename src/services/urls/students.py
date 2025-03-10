from django.urls import path
from services.views import students

app_name = 'students'


urlpatterns = [
     path('<str:registration_code>/', students.ValidateStudentFormView.as_view(), name='validate_student'),
     path('<str:registration_code>/rules-and-regulations/', students.RulesAndRegulationsView.as_view(), name='rules_and_regulations'),
     path('<str:registration_code>/select-stop/', students.StopSelectFormView.as_view(), name='stop_select'),
     path('<str:registration_code>/select-schedule/', students.SelectScheduleGroupView.as_view(), name='schedule_group_select'),
     
     path('<str:registration_code>/select-pickup-stop/', students.PickupStopSelectFormView.as_view(), name='pickup_stop_select'),
     path('<str:registration_code>/select-pickup-bus/', students.PickupBusSearchResultsView.as_view(), name='pickup_bus_select'),
     path('<str:registration_code>/select-drop-stop/', students.DropStopSelectFormView.as_view(), name='drop_stop_select'),
     path('<str:registration_code>/select-drop-bus/', students.DropBusSearchResultsView.as_view(), name='drop_bus_select'),
     
     path('bus-results/<str:registration_code>/', students.BusSearchResultsView.as_view(), name='bus_search_results'),
     path('bus-results/<str:registration_code>/not-found/', students.BusNotFoundView.as_view(), name='bus_not_found'),
     path('bus-results/<str:registration_code>/request/', students.BusRequestFormView.as_view(), name='bus_request'),
     path('bus-results/<str:registration_code>/request/success/', students.BusRequestSuccessView.as_view(), name='bus_request_success'),
     path('book/<str:registration_code>/', students.BusBookingView.as_view(), name='book_bus'),
     path('book/<str:registration_code>/success/', students.BusBookingSuccessView.as_view(), name='book_success'),

]