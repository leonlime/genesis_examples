import numpy as np
import genesis as gs


gs.init(seed=0, precision='32', logging_level='debug')
dt= 3e-3

scene = gs.Scene(
    sim_options=gs.options.SimOptions(
        substeps=10,
    ),
    viewer_options= gs.options.ViewerOptions(
        camera_pos=(1.5, 1.3, 0.5),
        camera_lookat=(0.0, 0.0, 0.0),
        camera_fov=40,
    ),
    rigid_options=gs.options.RigidOptions(
        dt=dt,
        gravity=(0, 0, -9.8),
        enable_collision=True,
        enable_self_collision=False,
    ),
    mpm_options=gs.options.MPMOptions(
        dt=dt,
        lower_bound=( 0.0,  0.0, -0.2),
        upper_bound=( 1.0,  1.0,  1.0),
        gravity=(0, 0, 0), # mimic gravity compensation
        enable_CPIC=True,
    ),
    vis_options=gs.options.VisOptions(
        show_world_frame=True,
        visualize_mpm_boundary=False,
    ),
)

scene.add_entity(
    morph=gs.morphs.Plane()
)

robot = scene.add_entity(
    morph=gs.morphs.URDF(
        file="urdf/simple/two_link_arm.urdf",
        pos=(0.5, 0.5, 0.3),
        euler=(0.0, 0.0, 0.0),
        scale=0.2,
        fixed=True,
    ),
    material=gs.materials.Hybrid(
        mat_rigid=gs.materials.Rigid(
            gravity_compensation=1.,
        ),
        mat_soft=gs.materials.MPM.Muscle(
            E=1e4,
            nu=0.45,
            rho=1000.,
            model='neohooken',
        ),
        thickness=0.05,
        damping=1000.,
        func_instantiate_rigid_from_soft=None,
        func_instantiate_soft_from_rigid=None,
        func_instantiate_rigid_soft_association=None,
    ),
)

scene.build()

for i in range(1000):
    scene.step()
