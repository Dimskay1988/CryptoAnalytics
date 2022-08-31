from django.urls import path, include


routes = [
    path('employees/', include('apps.Employees.urls')),
    path('crypt/', include('apps.Coin.urls')),
]
