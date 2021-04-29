import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testsite.settings")
import django
django.setup()

from django.conf import settings
import cms.api
from cms.api import add_plugin, create_page, publish_page, constants
from cms.models import Placeholder
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

def create_a_page(site, parent, title, slug):
        
    template = settings.CMS_TEMPLATES[0][0]
    lang = settings.LANGUAGES[0][0]
    
    page = create_page(title, template, lang,
                       in_navigation=True,
                       site=site,
                       parent=parent,
                       slug=slug)
    placeholder = page.placeholders.get(slot="content")
    add_plugin(placeholder, "TextPlugin", lang, body='<h1>This is ' + title + ' on '+ site.name + '</h1>')

    # In order to publish the page there needs to be at least one user
    if User.objects.count() > 0:
        publish_page(page, User.objects.all()[0], lang)

    return page
        

def create_pages(site1, site2):
    h1 = create_a_page(site1, None, 'Lab Home', 'home')
    h1.set_as_homepage()
    h11 = create_a_page(site1, h1, 'Lab Page 1', 'p1')
    h12 = create_a_page(site1, h1, 'Lab Page 2', 'p2')
    h111 = create_a_page(site1, h11, 'Lab Subpage 1', 's1')
    h2 = create_a_page(site2, None, 'Team Home', 'home')
    h2.set_as_homepage()
    h21 = create_a_page(site2, h2, 'Team Page 1', 'p1')
    h22 = create_a_page(site2, h2, 'Team Page 2', 'p2')
    h211 = create_a_page(site2, h21, 'Team Subpage 1', 's1')

def create_site():
    admin = User(username='admin', password=make_password('admin'),
                 is_superuser=True, is_staff = True)
    admin.save()
    site1 = Site(id=1, name='site1', domain='localhost:8001')
    site2 = Site(id=2, name='site2', domain='localhost:8002')
    site1.save()
    site2.save()
    create_pages(site1, site2)
    
if __name__ == "__main__":
    import django
    
    create_site()
