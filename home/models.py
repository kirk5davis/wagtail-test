from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    def get_context(self, request):
        
        context = super().get_context(request)
        menu_items= self.get_children().live().in_menu()
        context["menu_items"] = menu_items
        return context
