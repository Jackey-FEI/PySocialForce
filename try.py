from pathlib import Path
import numpy as np
import pysocialforce as psf
from PIL import Image
import numpy as np
import yaml
import itertools


if __name__ == "__main__":
    # initial states, each entry is the position, velocity and goal of a pedestrian in the form of (px, py, vx, vy, gx, gy)
    initial_state = np.array(
        [
            [200, 150,-1.0, 0.5, 100, 200],
            [300, 100, 0.0, -3.0, 400, 150],
            [400, 150, 0.0, 3.0, 300, 100],
            [100, 30, -3, 0.0, 50, 100],
            # [1.0, 1.0, 0.0, 0.5, -6.0, 1.0],
            # [2.0, 0.0, 0.0, 0.5, 3.0, 10.0],
            # [0.0, 6.0, 0.5, 0.5, 5.0, 6.0],
            # [5.0, 6.0, -0.5, 0.5, 0.0, 6.0],
        ]
    )
    # social groups informoation is represented as lists of indices of the state array
    groups = [[1], [0], [2],[3]]
    obs = []
    # list of linear obstacles given in the form of (x_min, x_max, y_min, y_max)
    for i in np.arange(0,10,0.1):
        obs.append([390,150-i])
    # for i in np.arange(0,10,0.1):
    #     obs.append([3+i,i])
    # obs.append([385,142])
    # obs.append([384,142])
    # obs.append([384.143])
    # obs.append([385,143])
    #obs = [[-1, -1, -1, 11], [3, 3, -1, 11]]
    img = Image.open("sample_map.pgm").convert('L')
    img_np = np.array(img)  # ndarray
    white=0
    wall=0
    space=0
    # obs = []
    for i in np.arange(img_np.shape[0]):
        for j in np.arange(img_np.shape[1]):
            if img_np[i][j]== 255:  # my-map 254 ->space, 0 -> wall, 205-> nonspace
                white=white+1
                # obs.append([j,i])
            if img_np[i][j]== 0:    # sample-map 128 -> space, 0 -> wall, 255-> nonspace
                wall=wall+1
                obs.append([j,i])
            if img_np[i][j]== 128:
                space=space+1 
    
    # for i in np.arange(img_np.shape[0]):
    #     for j in np.arange(img_np.shape[1]):
    #         if img_np[i][j] != 255 and img_np[i][j] != 0:
    #            print(img_np[i][j])
    print(white)
    print(space)
    print(wall)
    print(img_np[160:170,320:330])
    print(img_np.shape)
    #obs = [[1, 2, 7, 8]]
    # obs = img_np[0:4,0:10]
    # initiate the simulator,
    s = psf.Simulator(
        initial_state,
        groups=groups,
        obstacles=obs,
        config_file=Path(__file__).resolve().parent.joinpath("examples/example.toml"),
    )
    # update 80 steps
    s.step(200)

    with psf.plot.SceneVisualizer(s, "images/result") as sv:
        sv.animate()
        # sv.plot()
