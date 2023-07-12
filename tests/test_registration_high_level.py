import datetime


from pages.high_level_registration_form import RegistrationPage
from models.users import User


def test_filling_form():
    registration_page = RegistrationPage()

    vova = User(
        first_name='Vladimir',
        last_name='Serov',
        email='test@mail.ru',
        gender='Male',
        phone_number='8800555353',
        date_of_birth=datetime.date(1996, 21, 5),
        hobbies='English',
        subjects='Computer Science',
        image='Lisa.bmp',
        current_address='Novgorod',
        state='NCR',
        city='Delhi'

    )
    registration_page.open()
    registration_page.register(vova)
    registration_page.should_have_registered(vova)