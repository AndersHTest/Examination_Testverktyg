from behave import when as när, then as så
from playwright.sync_api import expect


# User Story: Lägg till favoritbok
@när(u'du klickar på hjärtknappen till vänster om boken du vill favoritmarkera')
def step_impl_click_fav(context):
    context.base_page.book_pwc.click()


@när(u'du klickar på knappen "Mina Böcker"')
def step_impl_my_books(context):
    context.base_page.my_books.click()


@så(u'är din favoritbok listad på sidan')
def step_impl_view_favorites(context):
    expect(context.base_page.list_object).to_be_attached()
    expect(context.base_page.list_object_pwc).to_be_visible()
