import time
from pages.registration_form import RegistrationPage

registration_page = RegistrationPage()


def test_form_registration_page():
    registration_page.open()
    registration_page.fill_first_name('Vladimir')
    registration_page.fill_last_name('Serov')
    registration_page.fill_email('test@mail.ru')
    registration_page.fill_gender('Male')
    registration_page.fill_mobile('8800555353')
    registration_page.fill_date_of_birth('1996', '21', 'May')
    registration_page.fill_subjects('English')
    registration_page.choose_hobbies()
    registration_page.upload_image('Lisa.bmp')
    time.sleep(5)
