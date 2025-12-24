from django.urls import path
from .views import generate, save, mine, remove

urlpatterns = [
    path('generate/', generate),        # POST
    path('mine/', mine),                # GET
    path('', save),                     # POST 저장
    path('<int:package_id>/', remove),  # DELETE
]
