from driver_with_settings import start_driver
from pages.sbis_main_page import SbisMainPage
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_main_page import TensorMainPage
from pages.tensor_about_page import TensorAboutPage

class TestFirstCase:
    def test_sbis_main_to_sbis_contacts(self):
        SMP_test = SbisMainPage(start_driver())
        SMP_test.open()
        SMP_test.go_to_contacts()
        
        SCP_test = SbisContactsPage(start_driver())
        SCP_test.open()
        
        assert SCP_test.current_url() == SMP_test.current_url()
        SMP_test.close()
        SCP_test.close()
    
    def test_sbis_contact_to_tenzor_main_from_banner(self):
        SCP_test = SbisContactsPage(start_driver())
        SCP_test.open()
        SCP_test.go_to_banner_tensor()
        
        TMP_test = TensorMainPage(start_driver())
        TMP_test.open()
        
        assert TMP_test.current_url() == SCP_test.current_url()
        SCP_test.close()
        TMP_test.close()
        
    def test_check_power_is_in_people(self):
        TMP_test = TensorMainPage(start_driver())
        TMP_test.open()
        
        assert TMP_test.find_power_is_in_people() == "Сила в людях"
        TMP_test.close()
        
    def test_tenzor_main_to_tenzor_about(self):
        TMP_test = TensorMainPage(start_driver())
        TMP_test.open()
        TMP_test.go_to_about()
        
        TAP_test = TensorAboutPage(start_driver())
        TAP_test.open()
        
        assert TMP_test.current_url() == TAP_test.current_url()
        TMP_test.close()
        TAP_test.close()
    
    def test_check_size_images_in_working(self):
        TAP_test = TensorAboutPage(start_driver())
        TAP_test.open()
        images = TAP_test.check_size_images_in_working()
        
        for image in images:
            assert image.size == images[0].size
        
        
        
        