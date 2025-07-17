# initialization:
import genesis as gs
gs.init(
    seed                = None,
    precision           = '32',
    debug               = False,
    eps                 = 1e-12,
    logging_level       = None,
    backend             = gs.gpu,
    theme               = 'dark',
    logger_verbose_time = False
)

# create scene:
scene = gs.Scene(
    show_viewer    = True,
    viewer_options = gs.options.ViewerOptions(
        res           = (1280, 960),
        camera_pos    = (3.5, 0.0, 2.5),
        camera_lookat = (0.0, 0.0, 0.5),
        camera_fov    = 40,
        max_FPS       = 60,
    ),
    vis_options = gs.options.VisOptions(
        show_world_frame = True,            # visualize the coordinate frame of `world` at its origin
        world_frame_size = 1.0,             # length of the world frame in meter
        show_link_frame  = False,           # do not visualize coordinate frames of entity links
        show_cameras     = False,           # do not visualize mesh and frustum of the cameras added
        plane_reflection = True,            # turn on plane reflection
        ambient_light    = (0.1, 0.1, 0.1), # ambient light setting
    ),
    renderer = gs.renderers.Rasterizer(),   # using rasterizer for camera rendering
)

# add objects:
plane = scene.add_entity(gs.morphs.Plane())
franka = scene.add_entity(
    gs.morphs.MJCF(
        file  = 'xml/franka_emika_panda/panda.xml',
        pos   = (0, 0, 0),
        euler = (0, 0, 90), # we follow scipy's extrinsic x-y-z rotation convention, in degrees,
        # quat  = (1.0, 0.0, 0.0, 0.0), # we use w-x-y-z convention for quaternions,
        scale = 1.0,
    ),
)

# build:
scene.build()
for i in range(1000):
    scene.step()
