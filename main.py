import page
import unittest
from selenium import webdriver

path_dmc = "C:\\Users\\ashepston\\Downloads\\chromedriver_win32\\chromedriver.exe"
path_home = "C:\\Users\\aidan\\Documents\\chromedriver_win32\\chromedriver.exe"


class Home(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(path_dmc)
        self.driver.get("https://www.nobelclad.com/")

    def test_text(self):
        home_page = page.HomePage(self.driver)
        assert home_page.text_match()

    def test_benefits(self):
        home_page = page.HomePage(self.driver)
        assert home_page.benefits()

    def test_applications(self):
        home_page = page.HomePage(self.driver)
        assert home_page.applications()

    def test_metals(self):
        home_page = page.HomePage(self.driver)
        assert home_page.metals()

    def test_link1(self):
        home_page = page.HomePage(self.driver)
        assert home_page.link1()

    def test_link2(self):
        home_page = page.HomePage(self.driver)
        assert home_page.link2()

    def test_link3(self):
        home_page = page.HomePage(self.driver)
        assert home_page.link3()

    def test_link4(self):
        home_page = page.HomePage(self.driver)
        assert home_page.link4()

    def test_get_started(self):
        home_page = page.HomePage(self.driver)
        assert home_page.get_started()

    def test_lets_talk(self):
        home_page = page.HomePage(self.driver)
        assert home_page.lets_talk()

    def test_search(self):
        home_page = page.HomePage(self.driver)
        assert home_page.search()

    def test_email(self):
        home_page = page.HomePage(self.driver)
        assert home_page.email()

    def tearDown(self):
        self.driver.quit()


class WeldingTechniques(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(path_dmc)
        self.driver.get("https://www.nobelclad.com/process")

    def test_text(self):
        welding_page = page.WeldingTechniquesPage(self.driver)
        assert welding_page.text_match()

    def test_link1(self):
        welding_page = page.WeldingTechniquesPage(self.driver)
        assert welding_page.link1()

    def test_link2(self):
        welding_page = page.WeldingTechniquesPage(self.driver)
        assert welding_page.link2()

    def test_link3(self):
        welding_page = page.WeldingTechniquesPage(self.driver)
        assert welding_page.link3()

    def tearDown(self):
        self.driver.quit()


class Products(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(path_dmc)
        self.driver.get("https://www.nobelclad.com/products")

    def test_text(self):
        product_page = page.ProductsPage(self.driver)
        assert product_page.text_match()

    def test_link1(self):
        product_page = page.ProductsPage(self.driver)
        assert product_page.link1()

    def test_link2(self):
        product_page = page.ProductsPage(self.driver)
        assert product_page.link2()

    def test_link3(self):
        product_page = page.ProductsPage(self.driver)
        assert product_page.link3()

    def test_link4_ships(self):
        product_page = page.ProductsPage(self.driver)
        assert product_page.link4_ships()

    def test_link4_train(self):
        product_page = page.ProductsPage(self.driver)
        assert product_page.link4_train()

    def test_link4_truck_trailer(self):
        product_page = page.ProductsPage(self.driver)
        assert product_page.link4_truck_trailer()

    def test_link5(self):
        product_page = page.ProductsPage(self.driver)
        assert product_page.link5()

    def test_link6(self):
        product_page = page.ProductsPage(self.driver)
        assert product_page.link6()

    def test_link7(self):
        product_page = page.ProductsPage(self.driver)
        assert product_page.link7()

    def tearDown(self):
        self.driver.quit()


class Industries(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(path_dmc)
        self.driver.get("https://www.nobelclad.com/industries")

    def test_text(self):
        industries_page = page.IndustriesPage(self.driver)
        assert industries_page.text()

    def test_link1(self):
        industries_page = page.IndustriesPage(self.driver)
        assert industries_page.link1()

    def test_link2(self):
        industries_page = page.IndustriesPage(self.driver)
        assert industries_page.link2()

    def test_link3(self):
        industries_page = page.IndustriesPage(self.driver)
        assert industries_page.link3()

    def test_link4(self):
        industries_page = page.IndustriesPage(self.driver)
        assert industries_page.link4()

    def test_link5(self):
        industries_page = page.IndustriesPage(self.driver)
        assert industries_page.link5()

    def test_link6(self):
        industries_page = page.IndustriesPage(self.driver)
        assert industries_page.link6()

    def test_link7(self):
        industries_page = page.IndustriesPage(self.driver)
        assert industries_page.link7()

    def test_link8(self):
        industries_page = page.IndustriesPage(self.driver)
        assert industries_page.link8()

    def tearDown(self):
        self.driver.quit()


class Resources(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(path_dmc)
        self.driver.get("https://www.nobelclad.com/resources")

    def test_publications(self):
        resources_page = page.ResourcesPage(self.driver)
        assert resources_page.publications()

    def test_clads(self):
        resources_page = page.ResourcesPage(self.driver)
        assert resources_page.commmon_clads()

    def test_products(self):
        resources_page = page.ResourcesPage(self.driver)
        assert resources_page.products()

    def tearDown(self):
        self.driver.quit()


class AboutUs(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(path_dmc)
        self.driver.get("https://www.nobelclad.com/about")

    def test_main_text(self):
        about_us_page = page.AboutUsPage(self.driver)
        assert about_us_page.main_text()

    def test_link1(self):
        about_us_page = page.AboutUsPage(self.driver)
        assert about_us_page.link1()

    def test_link2(self):
        about_us_page = page.AboutUsPage(self.driver)
        assert about_us_page.link2()

    def test_link3(self):
        about_us_page = page.AboutUsPage(self.driver)
        assert about_us_page.link3()

    def test_link4(self):
        about_us_page = page.AboutUsPage(self.driver)
        assert about_us_page.link4()

    def tearDown(self):
        self.driver.quit()

