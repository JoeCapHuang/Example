import time
import pytest
from pages.google_pages import *
from hamcrest import *


@pytest.mark.parametrize('animal_in, animal_out', [('котики', 'Кошка'), ('собачки', 'Собака')])
def test_first(animal_in, animal_out):
    google_main = GooglePages().open()

    google_main.search_field().enter_text(animal_in)
    time.sleep(1)
    google_main.search_button().click()

    assert_that(google_main.checked_object().get_text(), equal_to(animal_out))
