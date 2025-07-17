# initialization:
import genesis as gs
gs.init(backend=gs.cpu)

# create scene:
scene = gs.Scene(show_viewer=True)

# add objects:
plane = scene.add_entity(gs.morphs.Plane())
franka = scene.add_entity(
    gs.morphs.MJCF(file='xml/franka_emika_panda/panda.xml'),
)

# build:
scene.build()
for i in range(1000):
    scene.step()
