from selene import browser, have, command

from tests.conftest import path


class RegistrationPage:
    def __init__(self):
        self.state = browser.element('#state')

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('[id="firstName"]').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('[id="lastName"]').type(value)
        return self

    def fill_email(self, value):
        browser.element('[id="userEmail"]').type(value)
        return self

    def fill_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()
        return self

    def fill_mobile(self, value):
        browser.element('[id="userNumber"]').type(value)
        return self

    def fill_date_of_birth(self, year, day, month):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self


    def fill_subjects(self, value):
        browser.element('[id="subjectsInput"]').type(value).press_enter()
        return self

    def choose_hobbies(self, *args):
        browser.element('label[for="hobbies-checkbox-1"]').click()
        browser.element('label[for="hobbies-checkbox-2"]').click()
        browser.element('label[for="hobbies-checkbox-3"]').click()
        return self

    def upload_image(self, file_name):
        browser.element('#uploadPicture').send_keys(path(file_name))
        return self
    #
    def fill_curent_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def fill_state(self, state):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.all("[id^=react-select][id*=option]").element_by(have.exact_text(state)).click()
        return self

    def fill_city(self, city):
        browser.element('#city').perform(command.js.scroll_into_view).click()
        browser.all("[id^=react-select][id*=option]").element_by(have.exact_text(city)).click()
        return self

    def submitting(self):
        browser.element('#submit').click()

    def should_registered_user_with(self, full_name, email, gender, number, date_of_birth, subjects,
                                    hobbies, image, curent_address, state_city
                                    ):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                number,
                date_of_birth,
                subjects,
                hobbies,
                image,
                curent_address,
                state_city,
            )
        )
        return self
