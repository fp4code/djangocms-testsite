import os
from django.conf import settings

blabla = "<h1>Welcome to django CMS!</h1><p>The easy-to-use and developer-friendly CMS</p>"

def create_pages():
    from cms.api import add_plugin, create_page, publish_page
    from cms.models import Placeholder
    from django.contrib.auth.models import User
    from django.utils.translation import ugettext_lazy as _
    
    placeholder = {}

    try:
        # try to get a feature template with fallback
        template = settings.CMS_TEMPLATES[1][0]
        if template != "feature.html":
            template = settings.CMS_TEMPLATES[0][0]
    except IndexError:
        template = settings.CMS_TEMPLATES[0][0]

    lang = settings.LANGUAGES[0][0]
    page = create_page(_("Home"), template, lang)
    placeholder["main"] = page.placeholders.get(slot="content")

    try:
        # try to get a feature placeholder
        placeholder_feature = page.placeholders.get(slot="feature")
        add_plugin(placeholder_feature, "TextPlugin", lang, body=blabla)
    except Placeholder.DoesNotExist:
        # fallback, add it to the
        add_plugin(placeholder["main"], "TextPlugin", lang, body=blabla)

    # In order to publish the page there needs to be at least one user
    if User.objects.count() > 0:
        publish_page(page, User.objects.all()[0], lang)


if __name__ == "__main__":
    import django
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testsite.settings")
    django.setup()
    # setting.configure()
    create_pages()
