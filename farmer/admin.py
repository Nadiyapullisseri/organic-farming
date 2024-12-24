from django.contrib import admin
from .models import Customer, Payment
from .models import Farmer
from .models import Product
from .models import Feedback
from .models import Query
from .models import Notice



# Register your models here.
admin.site.register(Customer)
admin.site.register(Farmer)
admin.site.register(Product)
admin.site.register(Feedback)
admin.site.register(Query)
admin.site.register(Notice)
admin.site.register(Payment)


