from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ojfreshmachinedb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls))
)


# Text to put at the end of each page's <title>.
admin.site.site_title = 'OJ Fresh Admin'

# Text to put in each page's <h1>.
admin.site.site_header = 'OJ Fresh Database'

# Text to put at the top of the admin index page.
admin.site.index_title = 'Admin'