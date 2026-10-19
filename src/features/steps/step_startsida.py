from behave import given as givet, when as när, then as så
from playwright.sync_api import expect
from src.features.pages.base_page import BasePage


# User Story 1
@givet(u'att du är på Läslistans startsida')
def step_impl_start_page(context):
    base_page = BasePage(context.page)
    context.base_page = base_page
    context.base_page.navigate()


@så(u'är katalog-knappen inaktiverad')
def step_impl_catalog_button_inactive(context):
    expect(context.base_page.catalog).to_be_disabled()


@så(u'de andra tre knapparna är aktiva')
def step_impl_three_buttons_active(context):
    expect(context.base_page.add_book).to_be_enabled()
    expect(context.base_page.my_books).to_be_enabled()
    expect(context.base_page.statistics).to_be_enabled()


@så(u'det finns ett h2-element med texten "Välkommen!"')
def step_impl_welcome(context):
    expect(context.base_page.heading).to_be_visible()


@så(u'det finns en paragraf med texten: "Sidan för dig som gillar att läsa. Välj dina favoriter."')
def step_impl_paragraph_1(context):
    expect(context.base_page.paragraph).to_be_visible()


# User Story 2
@när(u'du klickar på hjärtknappen till vänster om boken du vill favoritmarkera')
def step_impl_click_fav(context):
    context.base_page.add_favorite_pw.click()


@när(u'du klickar på knappen "Mina Böcker"')
def step_impl_my_books(context):
    context.base_page.my_books.click()


@så(u'är din favoritbok listad på sidan')
def step_impl_view_favorites(context):
    expect(context.base_page.list_object).to_be_attached()
    expect(context.base_page.list_object_pw).to_be_visible()
