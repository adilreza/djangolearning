
from django.contrib import admin
from django.conf import  settings
from django.conf.urls.static import static
from django.urls import path, include
from myapp.views import index_file
from myapp.views import adil_file, charlotte_file, newpage
from myapp.views import (about, contact, my_form, my_form2, manage_data, delete_post, edit_post, update_post,
manage_data2, delete_post2, edit_post2, update_post2
)
from myapp.views import response_test, blogpost, blog_details, image,ajax_request, charlotte_ajax
from myapp.views import FirstClassBasedView, manage_ajax, delete_ajax

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index_file),
    path('adil/', adil_file),
    path('newpage/', newpage),
    path('about/', about),
    path('contact/', contact),
    path('post/', my_form),
    path('', charlotte_file),
    path('form2/', my_form2),
    path('manage_data/', manage_data),
    path('delete_post/<int:id>', delete_post),
    path('edit_post/<int:id>', edit_post),
    path('update_post/', update_post),
    path('response_test/', response_test),
    path('manage_data2/', manage_data2),
    path('delete_post2/<int:id>', delete_post2),
    path('edit_post2/<int:id>', edit_post2),
    path('update_post2/', update_post2),

    path('response_test/', response_test),
    path('blogpost/', blogpost),
    path('image/', image),
    path('blog_details/<int:blog_id>', blog_details),
    path('request/ajax', ajax_request),

    path('custom/', include('myapp.our_custom_urls')),

    path('charlotteajax/', charlotte_ajax),
    path('class_based/', FirstClassBasedView.as_view()),
    path('manageajax/', manage_ajax),

    path('delete_ajax/<int:id>', delete_ajax),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
