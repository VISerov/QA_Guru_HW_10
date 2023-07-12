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
    registration_page.fill_state('NCR')
    registration_page.fill_curent_address('Novgorod')
    registration_page.fill_city('Delhi')
    registration_page.submitting()
    time.sleep(5)
    registration_page.should_registered_user_with(
            'Vladimir Serov',
            'test@mail.ru',
            'Male',
            '8800555353',
            '21 May,1996',
            'English',
            'Sports, Reading, Music',
            'Lisa.bmp',
            'Novgorod',
            'NCR Delhi',
        )

