from ursina import *

app = Ursina()

from models import *
 
sky = Sky(texture='sky_sunset')

map = Map()
try:
    map.load()
except:
    map.new_map(size=30)
    


window.fullscreen = True
app.run()