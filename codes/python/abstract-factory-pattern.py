from abc import ABC
from abc import abstractmethod


class Browser(ABC):
    @abstractmethod
    def create_toolbar(self):
        pass

    @abstractmethod
    def create_window(self):
        pass

    def __str__(self):
        return str(self.__class__.__name__)


class Site(ABC):
    @abstractmethod
    def open(self, browser):
        pass

    def __str__(self):
        return str(self.__class__.__name__)


class AbstractFactory(ABC):
    @abstractmethod
    def create_browser(self):
        pass

    @abstractmethod
    def create_site(self):
        pass

    def __str__(self):
        return str(self.__class__.__name__)


class ChromeBrowser(Browser):
    def create_toolbar(self):
        return

    def create_window(self):
        return


class FirefoxBrowser(Browser):
    def create_toolbar(self):
        return

    def create_window(self):
        return


class Website(Site):
    def open(self, browser):
        print("Opened website on {}".format(browser))


class ChromeBrowserFactory(AbstractFactory):
    def create_browser(self):
        return ChromeBrowser()

    def create_site(self):
        return Website()


class FirefoxBrowserFactory(AbstractFactory):
    def create_browser(self):
        return FirefoxBrowser()

    def create_site(self):
        return Website()


def main():
    for factory in [ChromeBrowserFactory(), FirefoxBrowserFactory()]:
        browser = factory.create_browser()
        website = factory.create_site()

        browser.create_window()
        browser.create_toolbar()
        website.open(browser)


if __name__ == '__main__':
    main()
