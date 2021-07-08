from locator import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from element import test_presence
from locator import WeldingTechniquesLocators
from locator import ProductsLocators
from locator import IndustriesLocators
from locator import RescourcesLocators
from locator import AboutUsLocators
import time


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        if self.driver.find_elements(*MainPageLocators.CookieButton):
            cookies_button = self.driver.find_element(*MainPageLocators.CookieButton)
            cookies_button.click()


class HomePage(BasePage):

    def text_match(self):
        text1 = self.driver.find_element(*MainPageLocators.MainText)
        text2 = self.driver.find_element(*MainPageLocators.Subtext1)
        return test_presence(text1, text2)

    def benefits(self):
        plus_button = self.driver.find_element(*MainPageLocators.PlusButton)
        plus_button.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(MainPageLocators.BenefitsOption2))
        option1 = self.driver.find_element(*MainPageLocators.BenefitsOption1)
        option2 = self.driver.find_element(*MainPageLocators.BenefitsOption2)
        option3 = self.driver.find_element(*MainPageLocators.BenefitsOption3)
        close_button = self.driver.find_element(*MainPageLocators.CloseButtonBenefits)
        search = self.driver.find_element(*MainPageLocators.ShowResults)
        option1.click()
        option2.click()
        option3.click()
        close_button.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.ShowResults))
        search.click()
        more_clad = self.driver.find_element(*MainPageLocators.MoreClads)
        if more_clad.text != "(0)":
            return True
        else:
            print('incorrect entry')
            return False

    def applications(self):
        plus = self.driver.find_element(*MainPageLocators.ApplicationsPlus)
        plus.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(MainPageLocators.ApplicationsOption2))
        option1 = self.driver.find_element(*MainPageLocators.ApplicationsOption1)
        option2 = self.driver.find_element(*MainPageLocators.ApplicationsOption2)
        close_button = self.driver.find_element(*MainPageLocators.CloseButtonApplications)
        search = self.driver.find_element(*MainPageLocators.ShowResults)
        option1.click()
        option2.click()
        close_button.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.ShowResults))
        search.click()
        more_pub = self.driver.find_element(*MainPageLocators.MorePublications)
        if more_pub.text != '(0)':
            return True
        else:
            print('no results')
            return False

    def metals(self):
        plus = self.driver.find_element(*MainPageLocators.MetalPlus)
        plus.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(MainPageLocators.MetalOption2))
        option1 = self.driver.find_element(*MainPageLocators.MetalOption1)
        option2 = self.driver.find_element(*MainPageLocators.MetalOption2)
        close_button = self.driver.find_element(*MainPageLocators.CloseButtonMetal)
        search = self.driver.find_element(*MainPageLocators.ShowResults)
        option1.click()
        option2.click()
        close_button.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.ShowResults))
        search.click()
        more_pub = self.driver.find_element(*MainPageLocators.MorePublications)
        if more_pub.text != '(0)':
            return True
        else:
            print('no results')
            return False

    def get_started(self):
        start_button = self.driver.find_element(*MainPageLocators.GetStarted)
        start_button.click()
        metal1 = self.driver.find_element(*MainPageLocators.Metal1)
        metal2 = self.driver.find_element(*MainPageLocators.Metal2)
        option1 = self.driver.find_element(*MainPageLocators.Option1)
        option2 = self.driver.find_element(*MainPageLocators.Option2)
        submit = self.driver.find_element(*MainPageLocators.Submit)
        metal1.click()
        option1.click()
        metal2.click()
        option2.click()
        submit.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(MainPageLocators.CladResult))
        results = self.driver.find_element(*MainPageLocators.CladResult)
        return test_presence(results)

    def link1(self):
        link1 = self.driver.find_element(*MainPageLocators.WatchVideo)
        link1.click()
        new_window = self.driver.window_handles[1]
        self.driver.switch_to_window(new_window)
        return 'Ultrasonic' in self.driver.title

    def link2(self):
        link2 = self.driver.find_element(*MainPageLocators.DetaClad)
        link2.click()
        return 'DetaClad' in self.driver.title

    def link3(self):
        link3 = self.driver.find_element(*MainPageLocators.LearnMore)
        link3.click()
        text1 = self.driver.find_element(*MainPageLocators.LMText1)
        text2 = self.driver.find_element(*MainPageLocators.LMText2)
        text3 = self.driver.find_element(*MainPageLocators.LMText3)
        return 'Zirconium' in self.driver.title and test_presence(text1, text2, text3)

    def link4(self):
        link4 = self.driver.find_element(*MainPageLocators.Explore)
        link4.click()
        return 'Tubesheets' in self.driver.title

    def lets_talk(self):
        link = self.driver.find_element(*MainPageLocators.LetsTalk)
        link.click()
        first_name = self.driver.find_element(*MainPageLocators.FirstName)
        text_field = self.driver.find_element(*MainPageLocators.TextArea)
        return test_presence(first_name, text_field)

    def search(self):
        search_button = self.driver.find_element(*MainPageLocators.SearchButton)
        search_area = self.driver.find_element(*MainPageLocators.SearchArea)
        search_button.click()
        search_area.send_keys('test')
        search_area.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(MainPageLocators.SearchResult))
        search_result = self.driver.find_element(*MainPageLocators.SearchResult)
        return test_presence(search_result)

    def email(self):
        email_field = self.driver.find_element(*MainPageLocators.EmailField)
        submit = self.driver.find_element(*MainPageLocators.SubmitEmail)
        email_field.click()
        email_field.send_keys('test@dmcglobal.com')
        submit.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(MainPageLocators.Confirmation))
        confirmation = self.driver.find_element(*MainPageLocators.Confirmation)
        return 'confirm' in confirmation.text


class WeldingTechniquesPage(BasePage):

    def text_match(self):
        text = self.driver.find_element(*WeldingTechniquesLocators.Intro)
        image1 = self.driver.find_element(*WeldingTechniquesLocators.Image1)
        image2 = self.driver.find_element(*WeldingTechniquesLocators.Image2)
        image3 = self.driver.find_element(*WeldingTechniquesLocators.Image3)
        image4 = self.driver.find_element(*WeldingTechniquesLocators.Image4)
        return test_presence(text, image1, image2, image3, image4)

    def link1(self):
        results = []
        link1 = self.driver.find_element(*WeldingTechniquesLocators.Link1)
        link1.click()
        link1_text1 = self.driver.find_element(*WeldingTechniquesLocators.Link1Text1)
        link1_text2 = self.driver.find_element(*WeldingTechniquesLocators.Link1Text2)
        link1_image1 = self.driver.find_element(*WeldingTechniquesLocators.Link1Image1)
        link1_image2 = self.driver.find_element(*WeldingTechniquesLocators.Link1Image2)
        link1_image3 = self.driver.find_element(*WeldingTechniquesLocators.Link1Image3)
        link1_image4 = self.driver.find_element(*WeldingTechniquesLocators.Link1Image4)
        results.append(test_presence(link1_text1, link1_text2))
        results.append(test_presence(link1_image1, link1_image2, link1_image3, link1_image4))
        return False not in results

    def link2(self):
        results = []
        link2 = self.driver.find_element(*WeldingTechniquesLocators.Link2)
        link2.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(WeldingTechniquesLocators.Link2Text5))
        text1 = self.driver.find_element(*WeldingTechniquesLocators.Link2Text1)
        text2 = self.driver.find_element(*WeldingTechniquesLocators.Link2Text2)
        text3 = self.driver.find_element(*WeldingTechniquesLocators.Link2Text3)
        text4 = self.driver.find_element(*WeldingTechniquesLocators.Link2Text4)
        text5 = self.driver.find_element(*WeldingTechniquesLocators.Link2Text5)
        text6 = self.driver.find_element(*WeldingTechniquesLocators.Link2Text6)
        results.append(test_presence(text1, text2, text3))
        results.append(test_presence(text4, text5, text6))
        return False not in results

    def link3(self):
        link3 = self.driver.find_element(*WeldingTechniquesLocators.Link3)
        link3.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(WeldingTechniquesLocators.Link3Text2))
        text1 = self.driver.find_element(*WeldingTechniquesLocators.Link3Text1)
        text2 = self.driver.find_element(*WeldingTechniquesLocators.Link3Text2)
        text3 = self.driver.find_element(*WeldingTechniquesLocators.Link3Text3)
        text4 = self.driver.find_element(*WeldingTechniquesLocators.Link3Text4)
        image1 = self.driver.find_element(*WeldingTechniquesLocators.Link3Image1)
        return test_presence(text1, text2, text3, text4, image1)


class ProductsPage(BasePage):

    def text_match(self):
        results = []
        text1 = self.driver.find_element(*ProductsLocators.Intro)
        text2 = self.driver.find_element(*ProductsLocators.Conclusion)
        image1 = self.driver.find_element(*ProductsLocators.Image1)
        image2 = self.driver.find_element(*ProductsLocators.Image2)
        image3 = self.driver.find_element(*ProductsLocators.Image3)
        image4 = self.driver.find_element(*ProductsLocators.Image4)
        results.append(test_presence(text1, text2))
        results.append(test_presence(image1, image2, image3, image4))
        return False not in results

    def link1(self):
        results = []
        link1 = self.driver.find_element(*ProductsLocators.Link1)
        link1.click()
        text1 = self.driver.find_element(*ProductsLocators.Link1Text1)
        text2 = self.driver.find_element(*ProductsLocators.Link1Text2)
        results.append(test_presence(text1, text2))
        image1 = self.driver.find_element(*ProductsLocators.Link1Image1)
        results.append(test_presence(image1))
        image2 = self.driver.find_element(*ProductsLocators.Link1Image2)
        results.append(test_presence(image2))
        image3 = self.driver.find_element(*ProductsLocators.Link1Image3)
        results.append(test_presence(image3))
        return False not in results

    def link2(self):
        results = []
        link2 = self.driver.find_element(*ProductsLocators.Link2)
        link2.click()
        text1 = self.driver.find_element(*ProductsLocators.Link2Text1)
        text2 = self.driver.find_element(*ProductsLocators.Link2Text2)
        image1 = self.driver.find_element(*ProductsLocators.Link2Image1)
        link = self.driver.find_element(*ProductsLocators.Link2Link1)
        results.append(test_presence(text1, text2, image1))
        link.click()
        results.append('Tubesheets' in self.driver.title)
        return False not in results

    def link3(self):
        results = []
        link3 = self.driver.find_element(*ProductsLocators.Link3)
        link3.click()
        text1 = self.driver.find_element(*ProductsLocators.Link3Text1)
        text2 = self.driver.find_element(*ProductsLocators.Link3Text2)
        image1 = self.driver.find_element(*ProductsLocators.Link3Image1)
        image2 = self.driver.find_element(*ProductsLocators.Link3Image2)
        results.append(test_presence(text1, text2, image1, image2))
        return False not in results

    def link4_ships(self):
        results = []
        link4 = self.driver.find_element(*ProductsLocators.Link4)
        link4.click()
        text1 = self.driver.find_element(*ProductsLocators.Link4Text1)
        text2 = self.driver.find_element(*ProductsLocators.Link4Text2)
        text3 = self.driver.find_element(*ProductsLocators.Link4Text3)
        text4 = self.driver.find_element(*ProductsLocators.Link4Text4)
        image1 = self.driver.find_element(*ProductsLocators.Link4Image1)
        image2 = self.driver.find_element(*ProductsLocators.Link4Image2)
        results.append(test_presence(text1, text2, text3, text4))
        results.append(test_presence(image1, image2))
        ship_building = self.driver.find_element(*ProductsLocators.ShipBuilding)
        ship_building.click()
        sb_text1 = self.driver.find_element(*ProductsLocators.ShipBuildingText1)
        sb_text2 = self.driver.find_element(*ProductsLocators.ShipBuildingText2)
        sb_text3 = self.driver.find_element(*ProductsLocators.ShipBuildingText3)
        sb_text4 = self.driver.find_element(*ProductsLocators.ShipBuildingText4)
        sb_text5 = self.driver.find_element(*ProductsLocators.ShipBuildingText5)
        sb_link = self.driver.find_element(*ProductsLocators.ShipBuildingLink)
        results.append(test_presence(sb_text1, sb_text2, sb_text3, sb_text4, sb_text5))
        sb_link.click()
        deta_couple = self.driver.find_element(*ProductsLocators.DetacoupleText)
        results.append(test_presence(deta_couple))
        return False not in results

    def link4_train(self):
        results = []
        link4 = self.driver.find_element(*ProductsLocators.Link4)
        link4.click()
        train = self.driver.find_element(*ProductsLocators.Train)
        train.click()
        t_text1 = self.driver.find_element(*ProductsLocators.ShipBuildingText1)
        t_text2 = self.driver.find_element(*ProductsLocators.ShipBuildingText2)
        t_text3 = self.driver.find_element(*ProductsLocators.ShipBuildingText3)
        t_image1 = self.driver.find_element(*ProductsLocators.TrainImage1)
        t_image2 = self.driver.find_element(*ProductsLocators.TrainImage2)
        t_link = self.driver.find_element(*ProductsLocators.TrainLink)
        results.append(test_presence(t_text1, t_text2, t_text3, t_image1, t_image2))
        t_link.click()
        sparks_text = self.driver.find_element(*ProductsLocators.SparksText)
        results.append(test_presence(sparks_text))
        return False not in results

    def link4_truck_trailer(self):
        results = []
        link4 = self.driver.find_element(*ProductsLocators.Link4)
        link4.click()
        truck_trailer = self.driver.find_element(*ProductsLocators.TruckTrailer)
        truck_trailer.click()
        tt_text1 = self.driver.find_element(*ProductsLocators.ShipBuildingText1)
        tt_text2 = self.driver.find_element(*ProductsLocators.ShipBuildingText2)
        tt_text3 = self.driver.find_element(*ProductsLocators.ShipBuildingText3)
        tt_text4 = self.driver.find_element(*ProductsLocators.ShipBuildingText4)
        tt_text5 = self.driver.find_element(*ProductsLocators.ShipBuildingText5)
        results.append(test_presence(tt_text1, tt_text2, tt_text3, tt_text4, tt_text5))
        tt_article = self.driver.find_element(*ProductsLocators.TTArticle)
        tt_article.click()
        new_window = self.driver.window_handles[1]
        old_window = self.driver.window_handles[0]
        self.driver.switch_to_window(new_window)
        results.append('aluminum' in self.driver.current_url)
        self.driver.switch_to_window(old_window)
        tt_learn_more = self.driver.find_element(*ProductsLocators.TTLearnMore)
        tt_learn_more.click()
        learn_more_text = self.driver.find_element(*ProductsLocators.LearnMoreText)
        results.append(test_presence(learn_more_text))
        return False not in results

    def link5(self):
        results = []
        link5 = self.driver.find_element(*ProductsLocators.Link5)
        link5.click()
        text1 = self.driver.find_element(*ProductsLocators.Link4Text1)
        text2 = self.driver.find_element(*ProductsLocators.ShipBuildingText2)
        text3 = self.driver.find_element(*ProductsLocators.ShipBuildingText3)
        image1 = self.driver.find_element(*ProductsLocators.Link3Image1)
        image2 = self.driver.find_element(*ProductsLocators.Link5Image2)
        results.append(test_presence(text1, text2, text3, image1, image2))
        return False not in results

    def link6(self):
        results = []
        link6 = self.driver.find_element(*ProductsLocators.Link6)
        link6.click()
        text1 = self.driver.find_element(*ProductsLocators.Link4Text1)
        text2 = self.driver.find_element(*ProductsLocators.ShipBuildingText2)
        text3 = self.driver.find_element(*ProductsLocators.ShipBuildingText3)
        image1 = self.driver.find_element(*ProductsLocators.Link3Image1)
        image2 = self.driver.find_element(*ProductsLocators.Link5Image2)
        results.append(test_presence(text1, text2, text3, image1, image2))
        return False not in results

    def link7(self):
        results = []
        link7 = self.driver.find_element(*ProductsLocators.Link7)
        link7.click()
        text1 = self.driver.find_element(*ProductsLocators.Link4Text1)
        text2 = self.driver.find_element(*ProductsLocators.ShipBuildingText2)
        image1 = self.driver.find_element(*ProductsLocators.Link3Image1)
        image2 = self.driver.find_element(*ProductsLocators.Link7Image2)
        results.append(test_presence(text1, text2, image1, image2))
        return False not in results


class IndustriesPage(BasePage):
    def text(self):
        text = self.driver.find_element(*IndustriesLocators.Intro)
        return test_presence(text)

    def link1(self):
        results = []
        link1 = self.driver.find_element(*IndustriesLocators.Link1)
        link1.click()
        text1 = self.driver.find_element(*IndustriesLocators.Text1)
        text2 = self.driver.find_element(*IndustriesLocators.Text2)
        image1 = self.driver.find_element(*IndustriesLocators.Image1)
        results.append(test_presence(text1, text2))
        results.append(test_presence(image1))
        old_window = self.driver.window_handles[0]
        image1.click()
        new_window1 = self.driver.window_handles[1]
        self.driver.switch_to_window(new_window1)
        results.append(test_presence(self.driver.find_element(*IndustriesLocators.Text1)))
        self.driver.switch_to_window(old_window)
        image2 = self.driver.find_element(*IndustriesLocators.Image2)
        image2.click()
        new_window2 = self.driver.window_handles[2]
        self.driver.switch_to_window(new_window2)
        results.append(test_presence(self.driver.find_element(*IndustriesLocators.Text1)))
        self.driver.switch_to_window(old_window)
        image4 = self.driver.find_element(*IndustriesLocators.Image4)
        image4.click()
        new_window3 = self.driver.window_handles[3]
        self.driver.switch_to_window(new_window3)
        results.append(test_presence(self.driver.find_element(*IndustriesLocators.Text1)))
        self.driver.switch_to_window(old_window)
        image3 = self.driver.find_element(*IndustriesLocators.Image3)
        image3.click()
        results.append(test_presence(self.driver.find_element(*IndustriesLocators.Text1)))
        return False not in results

    def link2(self):
        results = []
        link2 = self.driver.find_element(*IndustriesLocators.Link2)
        link2.click()
        text1 = self.driver.find_element(*IndustriesLocators.Text1)
        text2 = self.driver.find_element(*IndustriesLocators.Text2)
        image1 = self.driver.find_element(*IndustriesLocators.Image1)
        results.append(test_presence(text1, text2))
        results.append(test_presence(image1))
        old_window = self.driver.window_handles[0]
        image1.click()
        new_window1 = self.driver.window_handles[1]
        self.driver.switch_to_window(new_window1)
        results.append(test_presence(self.driver.find_element(*IndustriesLocators.Text1)))
        self.driver.switch_to_window(old_window)
        image2 = self.driver.find_element(*IndustriesLocators.Image2)
        image2.click()
        new_window2 = self.driver.window_handles[2]
        self.driver.switch_to_window(new_window2)
        results.append(test_presence(self.driver.find_element(*IndustriesLocators.Text1)))
        self.driver.switch_to_window(old_window)
        image4 = self.driver.find_element(*IndustriesLocators.Image4)
        image4.click()
        new_window3 = self.driver.window_handles[3]
        self.driver.switch_to_window(new_window3)
        results.append(test_presence(self.driver.find_element(*IndustriesLocators.Text1)))
        self.driver.switch_to_window(old_window)
        image3 = self.driver.find_element(*IndustriesLocators.Image3)
        image3.click()
        results.append(test_presence(self.driver.find_element(*IndustriesLocators.Text1)))
        return False not in results

    def link3(self):
        results = []
        link3 = self.driver.find_element(*IndustriesLocators.Link3)
        link3.click()
        text1 = self.driver.find_element(*IndustriesLocators.Text1)
        text2 = self.driver.find_element(*IndustriesLocators.Text2)
        image1 = self.driver.find_element(*IndustriesLocators.Image4)
        results.append(test_presence(text1, text2))
        results.append(test_presence(image1))
        old_window = self.driver.window_handles[0]
        image1.click()
        new_window1 = self.driver.window_handles[1]
        self.driver.switch_to_window(new_window1)
        results.append(test_presence(self.driver.find_element(*IndustriesLocators.Text1)))
        self.driver.switch_to_window(old_window)
        image2 = self.driver.find_element(*IndustriesLocators.Image5)
        image2.click()
        new_window2 = self.driver.window_handles[2]
        self.driver.switch_to_window(new_window2)
        results.append(test_presence(self.driver.find_element(*IndustriesLocators.Text1)))
        return False not in results

    def link4(self):
        results = []
        link4 = self.driver.find_element(*IndustriesLocators.Link4)
        link4.click()
        text1 = self.driver.find_element(*IndustriesLocators.Text1)
        text2 = self.driver.find_element(*IndustriesLocators.Text2)
        image1 = self.driver.find_element(*IndustriesLocators.Image1)
        results.append(test_presence(text1, text2))
        results.append(test_presence(image1))
        old_window = self.driver.window_handles[0]
        image1.click()
        new_window1 = self.driver.window_handles[1]
        self.driver.switch_to_window(new_window1)
        results.append(test_presence(self.driver.find_element(*IndustriesLocators.Text1)))
        self.driver.switch_to_window(old_window)
        image2 = self.driver.find_element(*IndustriesLocators.Image2)
        image2.click()
        new_window2 = self.driver.window_handles[2]
        self.driver.switch_to_window(new_window2)
        results.append(test_presence(self.driver.find_element(*IndustriesLocators.Text1)))
        self.driver.switch_to_window(old_window)
        image4 = self.driver.find_element(*IndustriesLocators.Image4)
        image4.click()
        new_window3 = self.driver.window_handles[3]
        self.driver.switch_to_window(new_window3)
        results.append(test_presence(self.driver.find_element(*IndustriesLocators.Text1)))
        self.driver.switch_to_window(old_window)
        image3 = self.driver.find_element(*IndustriesLocators.Image3)
        image3.click()
        results.append(test_presence(self.driver.find_element(*IndustriesLocators.Text1)))
        return False not in results

    def link5(self):
        results = []
        link5 = self.driver.find_element(*IndustriesLocators.Link5)
        link5.click()
        text1 = self.driver.find_element(*IndustriesLocators.Text1)
        text2 = self.driver.find_element(*IndustriesLocators.Text2)
        image1 = self.driver.find_element(*IndustriesLocators.Image2)
        results.append(test_presence(text1, text2))
        results.append(test_presence(image1))
        image1.click()
        new_window1 = self.driver.window_handles[1]
        self.driver.switch_to_window(new_window1)
        results.append(test_presence(self.driver.find_element(*IndustriesLocators.Text1)))
        return False not in results

    def link6(self):
        results = []
        link6 = self.driver.find_element(*IndustriesLocators.Link6)
        link6.click()
        text1 = self.driver.find_element(*IndustriesLocators.Text1)
        text2 = self.driver.find_element(*IndustriesLocators.Text2)
        image1 = self.driver.find_element(*IndustriesLocators.Image4)
        results.append(test_presence(text1, text2))
        results.append(test_presence(image1))
        old_window = self.driver.window_handles[0]
        image1.click()
        new_window1 = self.driver.window_handles[1]
        self.driver.switch_to_window(new_window1)
        results.append(test_presence(self.driver.find_element(*IndustriesLocators.Text1)))
        self.driver.switch_to_window(old_window)
        image2 = self.driver.find_element(*IndustriesLocators.Image6)
        image2.click()
        new_window2 = self.driver.window_handles[2]
        self.driver.switch_to_window(new_window2)
        results.append(test_presence(self.driver.find_element(*IndustriesLocators.Text1)))
        return False not in results

    def link7(self):
        results = []
        link7 = self.driver.find_element(*IndustriesLocators.Link7)
        link7.click()
        text1 = self.driver.find_element(*IndustriesLocators.Text1)
        text2 = self.driver.find_element(*IndustriesLocators.Text2)
        triclad = self.driver.find_element(*IndustriesLocators.TriClad)
        results.append(test_presence(text1, text2))
        triclad.click()
        new_window1 = self.driver.window_handles[1]
        old_window = self.driver.window_handles[0]
        self.driver.switch_to_window(new_window1)
        results.append('Transition' in self.driver.title)
        self.driver.switch_to_window(old_window)
        image1 = self.driver.find_element(*IndustriesLocators.Image5)
        results.append(test_presence(image1))
        image1.click()
        new_window2 = self.driver.window_handles[2]
        self.driver.switch_to_window(new_window2)
        results.append(test_presence(self.driver.find_element(*IndustriesLocators.Text1)))
        return False not in results

    def link8(self):
        link8 = self.driver.find_element(*IndustriesLocators.Link8)
        link8.click()
        text1 = self.driver.find_element(*IndustriesLocators.Text1)
        return test_presence(text1)


class ResourcesPage(BasePage):
    def publications(self):
        results = []
        pub1 = self.driver.find_element(*RescourcesLocators.Pub1)
        pub1.click()
        text1 = self.driver.find_element(*RescourcesLocators.Text1)
        results.append(test_presence(text1))
        self.driver.back()
        pub_results = self.driver.find_element(*RescourcesLocators.PubResults)
        pub_results.click()
        pub2 = self.driver.find_element(*RescourcesLocators.Pub2)
        pub2.click()
        text2 = self.driver.find_element(*RescourcesLocators.Text1)
        results.append(test_presence(text2))
        return False not in results

    def commmon_clads(self):
        results = []
        clad1 = self.driver.find_element(*RescourcesLocators.Clad1)
        clad1.click()
        pic1 = self.driver.find_element(*RescourcesLocators.Pic1)
        results.append(test_presence(pic1))
        self.driver.back()
        clad_results = self.driver.find_element(*RescourcesLocators.CladResults)
        clad_results.click()
        clad2 = self.driver.find_element(*RescourcesLocators.Clad2)
        clad2.click()
        pic2 = self.driver.find_element(*RescourcesLocators.Pic1)
        results.append(test_presence(pic2))
        return False not in results

    def products(self):
        results = []
        prod1 = self.driver.find_element(*RescourcesLocators.Prod1)
        prod1.click()
        text1 = self.driver.find_element(*RescourcesLocators.ProdText1)
        text2 = self.driver.find_element(*RescourcesLocators.ProdText2)
        text3 = self.driver.find_element(*RescourcesLocators.ProdText3)
        text4 = self.driver.find_element(*RescourcesLocators.ProdText4)
        results.append(test_presence(text1, text2, text3, text4))
        link1 = self.driver.find_element(*RescourcesLocators.Prod1Link1)
        link1.click()
        new_window1 = self.driver.window_handles[1]
        old_window = self.driver.window_handles[0]
        self.driver.switch_to_window(new_window1)
        results.append('Steel' in self.driver.title)
        self.driver.switch_to_window(old_window)
        link2 = self.driver.find_element(*RescourcesLocators.Prod1Link2)
        link2.click()
        text6 = self.driver.find_element(*RescourcesLocators.Text1)
        results.append(test_presence(text6))
        self.driver.back()
        self.driver.back()
        load_more = self.driver.find_element(*RescourcesLocators.ProductResults)
        load_more.click()
        prod2 = self.driver.find_element(*RescourcesLocators.Prod2)
        prod2.click()
        prod_text1 = self.driver.find_element(*RescourcesLocators.ProdText1)
        prod_text2 = self.driver.find_element(*RescourcesLocators.ProdText2)
        image1 = self.driver.find_element(*RescourcesLocators.Image1)
        results.append(test_presence(prod_text1, prod_text2, image1))
        return False not in results


class AboutUsPage(BasePage):
    def main_text(self):
        text1 = self.driver.find_element(*AboutUsLocators.MainText1)
        text2 = self.driver.find_element(*AboutUsLocators.MainText2)
        text3 = self.driver.find_element(*AboutUsLocators.MainText3)
        text4 = self.driver.find_element(*AboutUsLocators.MainText4)
        return test_presence(text1, text2, text3, text4)

    def link1(self):
        link1 = self.driver.find_element(*AboutUsLocators.Link1)
        link1.click()
        intro = self.driver.find_element(*AboutUsLocators.Intro)
        text1 = self.driver.find_element(*AboutUsLocators.Link1Text1)
        text2 = self.driver.find_element(*AboutUsLocators.Link1Text2)
        text3 = self.driver.find_element(*AboutUsLocators.Link1Text3)
        text4 = self.driver.find_element(*AboutUsLocators.Link1Text4)
        return test_presence(intro, text1, text2, text3, text4)

    def link2(self):
        link2 = self.driver.find_element(*AboutUsLocators.Link2)
        link2.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(AboutUsLocators.Link2Text1))
        text1 = self.driver.find_element(*AboutUsLocators.Link2Text1)
        text2 = self.driver.find_element(*AboutUsLocators.Link2Text2)
        return test_presence(text1, text2)

    def link3(self):
        link3 = self.driver.find_element(*AboutUsLocators.Link3)
        link3.click()
        intro = self.driver.find_element(*AboutUsLocators.Intro)
        text1 = self.driver.find_element(*AboutUsLocators.Link3Text1)
        text2 = self.driver.find_element(*AboutUsLocators.Link3Text2)
        text3 = self.driver.find_element(*AboutUsLocators.Link3Text3)
        return test_presence(intro, text1, text2, text3)

    def link4(self):
        link4 = self.driver.find_element(*AboutUsLocators.Link4)
        link4.click()
        return 'Events' in self.driver.title











