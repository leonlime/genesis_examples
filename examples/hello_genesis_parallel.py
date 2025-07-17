import genesis as gs
import torch

gs.init(backend=gs.gpu)

scene = gs.Scene(
    show_viewer = True,
    viewer_options = gs.options.ViewerOptions(
        camera_pos = (3.5, -1.0, 2.5),
        camera_lookat = (0.0, 0.0, 0.5),
        camera_fov = 40,
        max_FPS = 60,
    ),
    sim_options = gs.options.SimOptions(
        dt = 0.01,
    ),
)

plane = scene.add_entity(
    gs.morphs.Plane(),
)
franka = scene.add_entity(
    gs.morphs.MJCF(file='xml/franka_emika_panda/panda.xml'),
)

# create 12 parallel env
B = 12
scene.build(n_envs=B, env_spacing=(1.0, 1.0))

# control all the robots
for i in range(1500):
    if i < 500:
        franka.control_dofs_position(
            torch.tile(
                torch.tensor([1, 1, 0, 0, 0, 0, 0, 0.04, 0.04], device=gs.device),
                (B, 1)
            )
        )
    elif i < 1000:
        franka.control_dofs_position(
            torch.tile(
                torch.tensor([-1, 0.8, 1, -2, 1, 0.5, -0.5, 0.04, 0.04], device=gs.device),
                (B, 1)
            )
        )
    else:
        franka.control_dofs_position(
            torch.tile(
                torch.tensor([0, 0, 0, 0, 0, 0, 0, 0, 0], device=gs.device),
                (B, 1)
            )
        )
    scene.step()
