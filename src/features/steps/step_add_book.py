from behave import when as när, then as så
from playwright.sync_api import expect


# User Story: Lägg till ny bok
@när(u'du klickar på knappen "Lägg till bok"')
def step_impl_add_book(context):
    context.base_page.add_book.click()


@när(u'du fyller i titel och författare')
def step_impl_fill_title_author(context):
    context.base_page.fill_title.fill("Titanic")
    context.base_page.fill_author.fill("Astrid Lindgren")


@när(u'du klickar på knappen "Lägg till ny bok"')
def step_impl_add_new_book(context):
    context.base_page.add_new_book.click()


@när(u'du klickar på knappen "Katalog"')
def step_impl_press_catalog_button(context):
    context.base_page.catalog.click()


@så(u'ska boken finnas listad i katalogen')
def step_impl_view_catalog(context):
    expect(context.base_page.book_titanic).to_be_visible()
