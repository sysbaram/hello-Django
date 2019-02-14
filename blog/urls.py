

from django.urls import path, re_path	
from blog.views import index, hello_times
from blog.views import articles_by_year
from blog.views import naver_realtime_keywords
from django.urls import register_converter
from blog.converters import FourDigitYearConverter, SlugUnicodeConverter

register_converter(FourDigitYearConverter, 'year')
register_converter(SlugUnicodeConverter, 'slug_unicode')


app_name = 'blog'

urlpatterns = [
    path('articles/<year:year>/', articles_by_year),

    # re_path('^blog/1/$', post_detail),
    # re_path('^blog/1/edit/$', post_edit),

    path('hello_times/<int:times>/', hello_times),
     # re_path(r'blog/hello_times/(?P<times>\d+)/$', hello_times),

    path('', index),
    # re_path(r'^$', index),

    path('naver/실시간검색어/', naver_realtime_keywords),
]