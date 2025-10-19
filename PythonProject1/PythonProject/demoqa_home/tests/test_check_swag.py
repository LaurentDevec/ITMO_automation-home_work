from pages.swag_labs import SwagLabs


class TestSwagLabs:

    def test_check_icon(self, browser):
        swag_labs = SwagLabs(browser)
        swag_labs.visit()
        assert swag_labs.exist_icon()

    def test_check_username_field(self, browser):
        swag_labs = SwagLabs(browser)
        swag_labs.visit()
        assert swag_labs.exist_username_field()

    def test_check_password_field(self, browser):
        swag_labs = SwagLabs(browser)
        swag_labs.visit()
        assert swag_labs.exist_password_field()
