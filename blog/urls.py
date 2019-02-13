

from django.urls import path, re_path	
from views import index, hello_times
from views import articles_by_year

from django.urls import register_converter
from converters import FourDigitYearConverter
from converters import SlugUnicodeConverter

register_converter(FourDigitYearConverter, 'year')
register_converter(SlugUnicodeConverter, 'slug_unicode')


app_name = 'blog'

urlpatterns = [
    path('articles/<year:year>/', articles_by_year),

    # re_path('^blog/1/$', post_detail),
    # re_path('^blog/1/edit/$', post_edit),

    path('admin/', admin.site.urls),	    
    path('blog/hello_times/<int:times>/', hello_times),
     # re_path(r'blog/hello_times/(?P<times>\d+)/$', hello_times),

    path('', index),
    # re_path(r'^$', index),
]