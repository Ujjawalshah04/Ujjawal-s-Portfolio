
import pyglet 
from pyglet.window import key

# Create a window
window = pyglet.window.Window(width=800, height=600)

# Load the car image
car_image = pyglet.image.load("car.png")
car_image.anchor_x = car_image.width // 2
car_image.anchor_y = car_image.height // 2

# Create a sprite for the car
car = pyglet.sprite.Sprite(car_image, x=400, y=300)

# Set the car's speed
car_speed = 5

# Set the track boundaries
track_boundaries = [(0, 0), (800, 0), (800, 600), (0, 600)]

# Set the lap counter
lap_counter = 0

@window.event
def on_draw():
    window.clear()
    car.draw()

def update(dt):
    global lap_counter

    # Update the car's position
    if key.RIGHT in keys:
        car.x += car_speed
    if key.LEFT in keys:
        car.x -= car_speed
    if key.UP in keys:
        car.y += car_speed
    if key.DOWN in keys:
        car.y -= car_speed

    # Check for collisions with the track boundaries
    for boundary in track_boundaries:
        if car.x < boundary[0] or car.x > boundary[0] or car.y < boundary[1] or car.y > boundary[1]:
            print("Crash! Game over.")
            pyglet.app.exit()

    # Check for lap completion
    if car.x > 400 and car.y > 300:
        lap_counter += 1
        print(f"Lap {lap_counter} completed!")

keys = key.KeyStateHandler()
window.push_handlers(keys)

pyglet.clock.schedule_interval(update, 1/60.0)

pyglet.app.run()

