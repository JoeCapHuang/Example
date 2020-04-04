import pytest
from infr.decorators import (
    mobile,
    android,
)
from pages.google_pages_mobile import *
from hamcrest import *


@pytest.mark.parametrize('animal_in, animal_out', [('котики', 'Кошка'), ('собачки', 'Собака')])
@mobile()
@android()
def test_one(animal_in, animal_out):
    google_main = GooglePagesMobile().open()

    google_main.search_field().enter_text(animal_in)
    google_main.search_button().click()

    assert_that(google_main.checked_object().get_text(), equal_to(animal_out))
