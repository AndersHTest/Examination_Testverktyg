from behave import given as givet, when as när, then as så
from playwright.sync_api import expect
import re


# User Story: Statistik
@när(u'du klickar på knappen "Statistik"')
def step_impl_press_statistics_button(context):
    context.base_page.statistics.click()


@så(u'verifierar du att du kan se hur många böcker som är tillgängliga i katalogen')
def step_impl_verify_book_count(context):
    expect(context.base_page.book_count).to_be_visible()


@så(u'verifierar du att du kan se hur många böcker som har favoritmarkerats')
def step_impl_verify_favorite_count(context):
    expect(context.base_page.favorite_count).to_be_visible()


# User Story: Statistik antal hjärtmarkerade böcker
@när(u'du hjärtmarkerar 2 böcker')
def step_impl_check_2_books(context):
    context.base_page.book_opep.click()
    context.base_page.book_tpp.click()


@när(u'klickar på statistik')
def step_impl_click_statistics_button(context):
    context.base_page.statistics.click()


@så(u'stämmer 2 hjärtmarkerade böcker')
def step_impl_verify_2_books(context):
    expect(context.base_page.text_2).to_be_visible()


@när(u'du hjärtmarkerar 4 böcker')
def step_impl_check_4_books(context):
    context.base_page.book_opep.click()
    context.base_page.book_tpp.click()
    context.base_page.book_pff.click()
    context.base_page.book_wyt.click()


@så(u'stämmer 4 hjärtmarkerade böcker')
def step_impl_verify_4_books(context):
    expect(context.base_page.text_4).to_be_visible()


@när(u'du hjärtmarkerar 6 böcker')
def step_impl_check_6_books(context):
    context.base_page.book_opep.click()
    context.base_page.book_tpp.click()
    context.base_page.book_pff.click()
    context.base_page.book_wyt.click()
    context.base_page.book_pwc.click()
    context.base_page.book_gbo.click()


@så(u'stämmer 6 hjärtmarkerade böcker')
def step_impl_verify_6_books(context):
    expect(context.base_page.text_6).to_be_visible()


# User Story: Statistik antal böcker i katalogen
@givet(u'att det från början finns 13 böcker i katalogen')
def step_impl_count_books(context):
    expect(context.base_page.book_general).to_have_count(13)


@givet(u'att det finns två nya böcker tillagda')
def step_impl_add_2_new_books(context):
    context.base_page.add_book.click()
    context.base_page.fill_title.fill("Titanic 2")
    context.base_page.fill_author.fill("Céline Dion")
    context.base_page.add_new_book.click()
    context.base_page.fill_title.fill("Pepparkråkan")
    context.base_page.fill_author.fill("Astrid Pettersson")
    context.base_page.add_new_book.click()


@när(u'jag klickar på statistik')
def step_impl_press_statistics_button_2(context):
    context.base_page.statistics.click()


@så(u'visar statistiken lika många böcker som det finns i katalogen')
def step_impl_verify_statistics(context):
    expect(context.base_page.book_count.get_by_text(re.compile("Listan har 15.+"))).to_be_visible()
