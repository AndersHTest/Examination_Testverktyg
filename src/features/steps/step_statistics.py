from behave import when as när, then as så
from playwright.sync_api import expect


# User Story 4
@när(u'du klickar på knappen "Statistik"')
def step_impl_press_statistics_button(context):
    context.base_page.statistics.click()


@så(u'verifierar du att du kan se hur många böcker som är tillgängliga i katalogen')
def step_impl_verify_book_count(context):
    expect(context.base_page.book_count).to_be_visible()


@så(u'verifierar du att du kan se hur många böcker som har favoritmarkerats')
def step_impl_verify_favorite_count(context):
    expect(context.base_page.favorite_count).to_be_visible()
