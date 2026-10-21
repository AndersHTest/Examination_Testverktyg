from behave import when as när, then as så
from playwright.sync_api import expect


@när(u'jag klickar på "Katalog"')
def step_impl_navigera(context):
    # context.base_page.catalog.click()
    expect(context.base_page.catalog).to_be_disabled()
    # Eftersom man landar på katalog-sidan när man går in på hemsidan
    # så verifierar jag bara att knappen är inaktiverad istället för att klicka på den


@så(u'ser jag elementen_a')
def step_impl_verifiera_element_1(context):
    expect(context.page).to_have_title("Läslistan")
    expect(context.base_page.bild).to_be_visible()
    expect(context.base_page.add_book).to_be_enabled()
    expect(context.base_page.my_books).to_be_enabled()
    expect(context.base_page.statistics).to_be_enabled()
    expect(context.base_page.heading).to_be_visible()
    expect(context.base_page.paragraph).to_be_visible()


@när(u'jag klickar på "Lägg till bok"')
def step_impl_navigera_2(context):
    context.base_page.add_book.click()


@så(u'ser jag elementen_b')
def step_impl_verifiera_element_2(context):
    expect(context.page).to_have_title("Läslistan")
    expect(context.base_page.bild).to_be_visible()
    expect(context.base_page.catalog).to_be_enabled()
    expect(context.base_page.add_book).to_be_disabled()
    expect(context.base_page.my_books).to_be_enabled()
    expect(context.base_page.statistics).to_be_enabled()
    expect(context.base_page.heading).to_be_visible()
    expect(context.base_page.fill_title).to_be_visible()
    expect(context.base_page.fill_author).to_be_visible()
    expect(context.base_page.add_new_book).to_be_disabled()
    expect(context.base_page.title_label).to_be_visible()
    expect(context.base_page.author_label).to_be_visible()


@när(u'jag klickar på "Mina Böcker"')
def step_impl_navigera_3(context):
    context.base_page.my_books.click()


@så(u'ser jag elementen_c')
def step_impl_verifiera_element_3(context):
    expect(context.page).to_have_title("Läslistan")
    expect(context.base_page.bild).to_be_visible()
    expect(context.base_page.catalog).to_be_enabled()
    expect(context.base_page.add_book).to_be_enabled()
    expect(context.base_page.my_books).to_be_disabled()
    expect(context.base_page.statistics).to_be_enabled()
    expect(context.base_page.heading).to_be_visible()
    expect(context.base_page.book_list).to_be_attached()
    expect(context.base_page.paragraph_1).to_be_visible()


@när(u'jag klickar på "Statistik"')
def step_impl_navigera_4(context):
    expect(context.page).to_have_title("Läslistan")
    context.base_page.statistics.click()


@så(u'ser jag elementen_d')
def step_impl_verifiera_element_4(context):
    expect(context.page).to_have_title("Läslistan")
    expect(context.base_page.bild).to_be_visible()
    expect(context.base_page.catalog).to_be_enabled()
    expect(context.base_page.add_book).to_be_enabled()
    expect(context.base_page.my_books).to_be_enabled()
    expect(context.base_page.statistics).to_be_disabled()
    expect(context.base_page.heading).to_be_visible()
    expect(context.base_page.book_count).to_be_visible()
    expect(context.base_page.favorite_count).to_be_visible()
