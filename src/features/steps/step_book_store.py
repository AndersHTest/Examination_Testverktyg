from behave import given, when, then
from playwright.sync_api import expect
from src.features.pages.base_page import BasePage


# User Story 1
@given(u'Du är på Läslistans startsida')
def step_impl_start_page(context):
    base_page = BasePage(context.page)
    context.base_page = base_page
    context.base_page.navigate()


@then(u'Katalog-knappen är inaktiverad')
def step_impl_catalog_button_inactive(context):
    expect(context.base_page.catalog).to_be_disabled()


@then(u'De andra tre knapparna är aktiva')
def step_impl_three_buttons_active(context):
    expect(context.base_page.add_book).to_be_enabled()
    expect(context.base_page.my_books).to_be_enabled()
    expect(context.base_page.statistics).to_be_enabled()


@then(u'Det finns ett h2-element med texten "Välkommen!"')
def step_impl_welcome(context):
    expect(context.base_page.heading).to_be_visible()


@then(u'Det finns en paragraf med texten: "Sidan för dig som gillar att läsa. Välj dina favoriter."')
def step_impl_paragraph_1(context):
    expect(context.base_page.paragraph).to_be_visible()


# User Story 2
@when(u'Du klickar på hjärtknappen till vänster om boken du vill favoritmarkera')
def step_impl_click_fav(context):
    context.base_page.add_favorite_pw.click()


@when(u'Du klickar på knappen "Mina Böcker"')
def step_impl_my_books(context):
    context.base_page.my_books.click()


@then(u'Din favoritbok finns listad på sidan')
def step_impl_view_favorites(context):
    expect(context.base_page.list_object).to_be_attached()
    expect(context.base_page.list_object_pw).to_be_visible()


# User Story 3
@when(u'Du klickar på knappen "Lägg till bok"')
def step_impl_add_book(context):
    context.base_page.add_book.click()


@when(u'du fyller i titel och författare')
def step_impl_fill_title_author(context):
    context.base_page.fill_title.fill("Titanic")
    context.base_page.fill_author.fill("Astrid Lindgren")


@when(u'Du klickar på knappen "Lägg till ny bok"')
def step_impl_add_new_book(context):
    context.base_page.add_new_book.click()


@when(u'Du klickar på knappen "Katalog"')
def step_impl_press_catalog_button(context):
    context.base_page.catalog.click()


@then(u'Ska boken finnas listad i katalogen')
def step_impl_view_catalog(context):
    expect(context.base_page.catalog_titanic).to_be_visible()


# User Story 4
@when(u'Du klickar på knappen "Statistik"')
def step_impl_press_statistics_button(context):
    context.base_page.statistics.click()


@then(u'Verifiera att du kan se hur många böcker som är tillgängliga i katalogen')
def step_impl_verify_book_count(context):
    expect(context.base_page.book_count).to_be_visible()


@then(u'Verifiera att du kan se hur många böcker som har favoritmarkerats')
def step_impl_verify_favorite_count(context):
    expect(context.base_page.favorite_count).to_be_visible()
