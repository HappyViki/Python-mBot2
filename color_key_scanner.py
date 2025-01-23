import cyberpi, mbuild

# CONSTANTS

w = "white"
r = "red"
y = "yellow"
c = "cyan"

l2_x = 9*2*3
l1_x = 9*2*4
r1_x = 9*2*5
r2_x = 9*2*6

# KEYS

key1 = w+y+y+w
key2 = w+c+c+w

key_void = w+r+r+w

# SETUP BOT

show_color_names = True

cyberpi.led.off(id='all')
cyberpi.display.show_label("Insert Key", 0, 0, 0, index = 1)

while True:

    # GET COLORS FROM SENSOR
    l2_color = mbuild.quad_rgb_sensor.get_color_sta("L2")
    l1_color = mbuild.quad_rgb_sensor.get_color_sta("L1")
    r1_color = mbuild.quad_rgb_sensor.get_color_sta("R1")
    r2_color = mbuild.quad_rgb_sensor.get_color_sta("R2")
        
    # TROUBLESHOOT COLORS
    if show_color_names:
      cyberpi.display.show_label("L2: " + l2_color, 16, 0, l2_x, index = 3)
      cyberpi.display.show_label("L1: " + l1_color, 16, 0, l1_x, index = 4)
      cyberpi.display.show_label("R1: " + r1_color, 16, 0, r1_x, index = 5)
      cyberpi.display.show_label("R2: " + r2_color, 16, 0, r2_x, index = 6)
    
    # KEY LOGIC
    
    current_key = l2_color+l1_color+r1_color+r2_color
    
    if current_key in [key1, key2]:
        cyberpi.display.show_label("PASS", 0, 0, 0, index = 1)
        cyberpi.led.play(name = "rainbow")
    
    if key_void == current_key:
        cyberpi.display.show_label("VOID", 0, 0, 0, index = 1)
        cyberpi.led.play(name = "flash_red")
