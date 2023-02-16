from page_objects.LoginPage import LoginPage
class Test_001_login:
    base_url="https://admin-demo.nopcommerce.com/"
    username="admin@yourstore.com"
    password="admin"

    def test_homepagetitile(self,setup):
        self.driver=setup
        self.driver.get(self.base_url)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
        else:
            self.driver.save_screenshot("test_homepagetitle.png")
            assert False
        self.driver.close()


    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.base_url)
        self.lp =LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title=self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            print("title is samme")
        else:
            self.driver.save_screenshot(r"C:\Users\PRAMOD R\Desktop\pyth\report\screenshots\test_login.png")
            assert False
            print("title is different")
        self.driver.close()