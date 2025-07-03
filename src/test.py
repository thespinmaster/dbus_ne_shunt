import time
import sys
import os
from gi.repository import GLib

sys.path.append(os.path.join(os.path.dirname(__file__), 'ext'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'ne_shunt_dbus'))

from ne_shunt_dbus.dbus_connection import dbusconnection
from ne_shunt_dbus.dbus_constants import dbus_constants
from ext.settingsdevice import SettingsDevice  # available in the velib_python repository

def main2():
    print("hello world")

def main():

    # unique path used to generate unique ClassAndVrmInstance value 
    # see https://github.com/victronenergy/localsettings#using-addsetting-to-allocate-a-vrm-device-instance
    settingsPath = "/Settings/Devices/ne_shunt_ttyAMC0"

    settings = SettingsDevice(
        bus = dbusconnection(),
        supportedSettings = {
            'ShowFreshWaterTank': [f'{settingsPath}/ShowFreshWaterTank', 1, 0, 1],
            'ShowGreyWasteTank': [f'{settingsPath}/ShowGreyWasteTank', 1, 0, 1],  # When empty, default path will be used.
            'ShowGreyWasteTank2': [f'{settingsPath}/ShowGreyWasteTank2', 1, 0, 1],
            'ShowInternalLightSwitch': [f'{settingsPath}/ShowInternalLightSwitch', 1, 0, 1],
            'ShowExternalLightSwitch': [f'{settingsPath}/ShowExternalLightSwitch', 1, 0, 1],
            'ShowWaterPumpSwitch': [f'{settingsPath}/ShowWaterPumpSwitch', 1, 0, 1],
            'ShowAuxSwitch': [f'{settingsPath}/ShowAuxSwitch', 1, 0, 1],
            'FreshWaterTank_ClassAndVrmInstance' : [f'{settingsPath}_fresh_water_tank/ClassAndVrmInstance', 
                                        f'{dbus_constants.SERVICE_TYPE_TANK}:{dbus_constants.DEFAULT_DEVICE_INSTANCE}', 0, 0],
            'GreyWasteTank_ClassAndVrmInstance' : [f'{settingsPath}_grey_waste_tank/ClassAndVrmInstance', 
                                        f'{dbus_constants.SERVICE_TYPE_TANK}:{dbus_constants.DEFAULT_DEVICE_INSTANCE}', 0, 0],
            'GreyWasteTank2_ClassAndVrmInstance' : [f'{settingsPath}_grey_waste_tank_2/ClassAndVrmInstance', 
                                        f'{dbus_constants.SERVICE_TYPE_TANK}:{dbus_constants.DEFAULT_DEVICE_INSTANCE}', 0, 0],
            'CabBattery_ClassAndVrmInstance' : [f'{settingsPath}_cab_battery/ClassAndVrmInstance', 
                                        f'{dbus_constants.SERVICE_TYPE_BATTERY}:{dbus_constants.DEFAULT_DEVICE_INSTANCE}', 0, 0],
            'Switches_ClassAndVrmInstance' : [f'{settingsPath}_switches/ClassAndVrmInstance', 
                                        f'{dbus_constants.SERVICE_TYPE_SWITCH}:{dbus_constants.DEFAULT_DEVICE_INSTANCE}', 0, 0]
            },
        eventCallback = _handle_changed_setting)

    print(f'FreshWaterTank_ClassAndVrmInstance = {settings['FreshWaterTank_ClassAndVrmInstance']}')
    print(f'GreyWasteTank_ClassAndVrmInstance = {settings['GreyWasteTank_ClassAndVrmInstance']}')
    print(f'GreyWasteTank2_ClassAndVrmInstance = {settings['GreyWasteTank2_ClassAndVrmInstance']}')
    print(f'CabBattery_ClassAndVrmInstance = {settings['CabBattery_ClassAndVrmInstance']}')
    print(f'Switches_ClassAndVrmInstance = {settings['Switches_ClassAndVrmInstance']}')

def _handle_changed_setting(setting, oldvalue, newvalue):
    return True

def _update():
    print("doing stuff")
    return True

if __name__ == "__main__":
    from dbus.mainloop.glib import DBusGMainLoop
    # Have a mainloop, so we can send/receive asynchronous calls to and from dbus
    DBusGMainLoop(set_as_default=True)
  
    time.sleep(1)
    GLib.timeout_add(1000, _update)
    
    main()

    mainloop = GLib.MainLoop()
    mainloop.run()
    