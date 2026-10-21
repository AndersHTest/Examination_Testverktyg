from behave import given as givet, when as när, then as så
from playwright.sync_api import expect
from src.features.pages.base_page import BasePage


# User Story: Startsida
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


# User Story: Klicka på hjärtknappen flera gånger
@när(u'du klickar på hjärtknappen 1 gång(er)')
def step_impl_klicka_1(context):
    context.base_page.book_wyt.click()


@så(u'ser du att det läggs till ett hjärta')
def step_impl_hjärta(context):
    expect(context.base_page.book_wyt).to_have_class("star selected")


@när(u'du klickar på hjärtknappen 2 gång(er)')
def step_impl_klicka_2(context):
    context.base_page.book_wyt.click()
    context.base_page.book_wyt.click()


@så(u'ser du att hjärtat tas bort')
def step_impl_hjärta_bort(context):
    expect(context.base_page.book_wyt).to_have_class("star")


@när(u'du klickar på hjärtknappen 3 gång(er)')
def step_impl_hjärta_1(context):
    context.base_page.book_wyt.click()
    context.base_page.book_wyt.click()
    context.base_page.book_wyt.click()
