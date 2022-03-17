from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import variables


class SayHello(App):
    variables.init_variables()

    def build(self):
        # returns a window object with all it's widgets
        self.window = GridLayout()

        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # image widget
        self.window.add_widget(Image(source="logo_white.png"))

        # label widget
        self.greeting = Label(
            text="Vivaro Smart Interface",
            font_size=30,
            color='#00B8A5',
            bold=True
        )
        self.window.add_widget(self.greeting)

        # button widget
        self.light = Button(
            text="Lights on",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00587F',
        )
        self.light.bind(on_press=self.light_callback)
        self.window.add_widget(self.light)
        
        # button widget
        self.fridge = Button(
            text="Fridge on",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00587F',
        )
        self.fridge.bind(on_press=self.fridge_callback)
        self.window.add_widget(self.fridge)
        
        # button widget
        self.heater = Button(
            text="Heater on",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00587F',
        )
        self.heater.bind(on_press=self.heater_callback)
        self.window.add_widget(self.heater)
        
        # button widget
        self.water = Button(
            text="Waterpump on",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00587F',
        )
        self.water.bind(on_press=self.water_callback)
        self.window.add_widget(self.water)

        # button widget
        self.relay = Button(
            text="Relay on",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00587F',
        )
        self.relay.bind(on_press=self.relay_callback)
        self.window.add_widget(self.relay)


        self.monitoring = Label(
            text="Monitoring",
            font_size=30,
            color='#00B8A5',
            bold=True
        )

        self.window.add_widget(self.monitoring)

        self.bottomsection = GridLayout()
        self.bottomsection.cols = 2
        self.bottomsection.size_hint = (0.6, 0.7)
        self.bottomsection.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # label widget
        self.state_of_charge_label = Label(
            text="State of charge",
            font_size=25,
            color='white',
            bold=True,
            halign="left", valign="middle"
        )
        # label widget
        self.state_of_charge = Label(
            text="89%",
            font_size=25,
            color='white',
            bold=True,
            halign="left", valign="middle",
            size_hint=(1.0, 1.0),
        )

        # label widget
        self.voltage_label = Label(
            text='Voltage',
            font_size=25,
            color='white',
            bold=True,
            halign="left", valign="middle",
            size_hint=(1.0, 1.0),
        )
        # label widget
        self.voltage = Label(
            text="13.1V",
            font_size=25,
            color='white',
            bold=True,
            halign="left", valign="middle",
            size_hint=(1.0, 1.0),
        )

        # label widget
        self.solar_energy_label = Label(
            text="Solar-energy",
            font_size=25,
            color='white',
            bold=True,
            halign="left", valign="middle",
            size_hint=(1.0, 1.0),
        )
        # label widget
        self.solar_energy = Label(
            text="49W",
            font_size=25,
            color='white',
            bold=True,
            halign="left", valign="middle",
            size_hint=(1.0, 1.0),
        )

        self.bottomsection.add_widget(self.state_of_charge_label)
        self.bottomsection.add_widget(self.state_of_charge)
        self.bottomsection.add_widget(self.voltage_label)
        self.bottomsection.add_widget(self.voltage)
        self.bottomsection.add_widget(self.solar_energy_label)
        self.bottomsection.add_widget(self.solar_energy)

        self.window.add_widget(self.bottomsection)






        return self.window

    def light_callback(self, instance):
        if variables.light_on == False:
            self.light.background_color = "#00B8A5"
            self.light.text = "Lights off"
            variables.light_on = True
        elif variables.light_on == True:
            self.light.background_color = "##00587F"
            self.light.text = "Lights on"
            variables.light_on = False
            
    def fridge_callback(self, instance):
        if variables.fridge_on == False:
            self.fridge.background_color = "#00B8A5"
            self.fridge.text = "Fridge off"
            variables.fridge_on = True
        elif variables.fridge_on == True:
            self.fridge.background_color = "##00587F"
            self.fridge.text = "Fridge on"
            variables.fridge_on = False
            
    def heater_callback(self, instance):
        if variables.heater_on == False:
            self.heater.background_color = "#00B8A5"
            self.heater.text = "Heater off"
            variables.heater_on = True
        elif variables.heater_on == True:
            self.heater.background_color = "##00587F"
            self.heater.text = "Heater on"
            variables.heater_on = False
            
    def water_callback(self, instance):
        if variables.water_on == False:
            self.water.background_color = "#00B8A5"
            self.water.text = "Waterpump off"
            variables.water_on = True
        elif variables.water_on == True:
            self.water.background_color = "##00587F"
            self.water.text = "Waterpump on"
            variables.water_on = False

    def relay_callback(self, instance):
        if variables.relay_on == False:
            self.relay.background_color = "#00B8A5"
            self.relay.text = "Relay off"
            variables.relay_on = True
        elif variables.relay_on == True:
            self.relay.background_color = "#00587F"
            self.relay.text = "Relay on"
            variables.relay_on = False



# run Say Hello App Calss
if __name__ == "__main__":
    SayHello().run()
