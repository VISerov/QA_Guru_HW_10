from selene import browser, have, be
import os
import time


# Filling the form
class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('[id="firstName"]').type(value)

    def fill_first_name(self, value):
        browser.element('[id="lastName"]').type('Serov')

    def fill_first_name(self, value):
        browser.element('[id="userEmail"]').type('hello@gmail.com')

    def fill_first_name(self, value):
        browser.element('//*[@id="genterWrapper"]/div[2]/div[1]').click()

    def fill_first_name(self, value):
        browser.element('[id="userNumber"]').type('8800555353')

    def fill_first_name(self, value):
        browser.element('[id="dateOfBirthInput"]').click()

    def fill_first_name(self, value):
        browser.element('[value="1996"]').click()
        browser.element('[value="0"]').click()
        browser.element('[aria-label="Choose Friday, January 5th, 1996"]').click()
        browser.element('[id="subjectsInput"]').type('Computer').press_enter()
        browser.element('[for="hobbies-checkbox-1"]').click()
        input_field = browser.element('#uploadPicture')
        input_field.send_keys(os.getcwd() + '\img\Mona_Lisa1.jpg')
        browser.element('#currentAddress').type('Novgorod')
        browser.element('#state').click()
        browser.all("#state div").element_by(have.exact_text("NCR")).click()
        browser.element('#city').click()
        browser.all("#city div").element_by(have.exact_text("Delhi")).click()
        browser.element('#submit').click()