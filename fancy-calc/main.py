from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.spinner import Spinner


Builder.load_file('front.kv')


class HomeScreen(Screen):
    def solwent(self):
        self.manager.current = 'solwent_screen'

    def cyfra(self):
        self.manager.current = 'cyfra_screen'


class SolwentScreen(Screen):
    def roll_up(self):
        self.manager.current = 'roll_up_screen'

    def banner(self):
        self.manager.current = 'banner_screen'

    def foil(self):
        self.manager.current = 'foil_screen'

    def owv(self):
        self.manager.current = 'owv_screen'

    def paper(self):
        self.manager.current = 'paper_screen'

    def return_home(self):
        self.manager.current = 'home_screen'


class CyfraScreen(Screen):
    def business_card(self):
        self.manager.current = 'business_card_screen'

    def posters(self):
        self.manager.current = 'posters_screen'

    def flyers(self):
        self.manager.current = 'flyer_screen'

    def folded_flyers(self):
        self.manager.current = 'folded_flyer_screen'

    def custom_flyers(self):
        self.manager.current = 'custom_flyer_screen'

    def return_home(self):
        self.manager.current = 'home_screen'


class BusinessCardsScreen(Screen):
    def return_home(self):
        self.manager.current = 'home_screen'

    def cyfra(self):
        self.manager.current = 'cyfra_screen'


class PostersScreen(Screen):
    def return_home(self):
        self.manager.current = 'home_screen'

    def cyfra(self):
        self.manager.current = 'cyfra_screen'


class FlyerScreen(Screen):
    def return_home(self):
        self.manager.current = 'home_screen'

    def cyfra(self):
        self.manager.current = 'cyfra_screen'


class FoldedFlyerScreen(Screen):
    def return_home(self):
        self.manager.current = 'home_screen'

    def cyfra(self):
        self.manager.current = 'cyfra_screen'


class CustomFlyerScreen(Screen):
    def return_home(self):
        self.manager.current = 'home_screen'

    def cyfra(self):
        self.manager.current = 'cyfra_screen'


class RollUpScreen(Screen):
    def return_home(self):
        self.manager.current = 'home_screen'

    def cyfra(self):
        self.manager.current = 'solwent_screen'


class BannerScreen(Screen):
    def return_home(self):
        self.manager.current = 'home_screen'

    def cyfra(self):
        self.manager.current = 'solwent_screen'


class FoilScreen(Screen):
    def return_home(self):
        self.manager.current = 'home_screen'

    def cyfra(self):
        self.manager.current = 'solwent_screen'


class OwvScreen(Screen):
    def return_home(self):
        self.manager.current = 'home_screen'

    def cyfra(self):
        self.manager.current = 'solwent_screen'


class PaperScreen(Screen):
    def return_home(self):
        self.manager.current = 'home_screen'

    def cyfra(self):
        self.manager.current = 'solwent_screen'


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()