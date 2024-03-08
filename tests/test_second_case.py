from driver_with_settings import start_driver
from pages.sbis_contacts_page import SbisContactsPage
import re
import pytest
from time import sleep

class TestSecondCase:
    @pytest.mark.parametrize(
        "region, city, expectation",
        [
            ("Ярославская обл.", "Ярославль", True),
            ("Камчатский край", "Петропавловск-Камчатский", False)    
        ]
    )
    def test_sbis_contacts_region(self, region, city, expectation):
        SCP_test = SbisContactsPage(start_driver())
        SCP_test.open()
        
        equals_check = region == str(SCP_test.check_region())
        list_of_partners_city = city == re.compile(r'\w+').findall(SCP_test.check_list_of_partners())[0]
        
        assert equals_check == expectation
        assert list_of_partners_city == expectation
        
        SCP_test.close()
        
    @pytest.mark.parametrize(
        "region, url, title",
        [
            ("Камчатский край", "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients", "СБИС Контакты — Камчатский край")
        ]
    )
    def test_sbis_contacts_change_region(self, region, url, title):
        SCP_test = SbisContactsPage(start_driver())
        SCP_test.open()
        
        first_city = re.compile(r'\w+').findall(SCP_test.check_list_of_partners())[0]
        SCP_test.change_region(region)
        
        sleep(1)
        
        assert first_city != re.compile(r'\w+').findall(SCP_test.check_list_of_partners())[0]
        assert url == SCP_test.current_url()
        assert title == SCP_test.title()
        
        SCP_test.close()