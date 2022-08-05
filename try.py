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
            # [950, 850, 1.0, -0.5, 1000, 850],
            # [950, 900, 2.0, -0.5, 1000, 900],
            # [1000, 890, -1.0, -0.5, 975, 850],
            [1.0, 0.0, 0.0, 0.5, 2.0, 10.0],
            [2.0, 0.0, 0.0, 0.5, 3.0, 10.0],
            [3.0, 0.0, 0.0, 0.5, 4.0, 10.0],
        ]
    )
    # social groups informoation is represented as lists of indices of the state array
    groups = [[1], [0], [2]]
    obs = []
    # list of linear obstacles given in the form of (x_min, x_max, y_min, y_max)
    for i in np.arange(0,10,0.1):
        obs.append([-1,i])
    for i in np.arange(0,10,0.1):
        obs.append([3+i,i])
    #obs = [[-1, -1, -1, 11], [3, 3, -1, 11]]
    img = Image.open("my_map.pgm").convert('L')
    img_np = np.array(img)  # ndarray
    white=0
    wall=0
    space=0
    # obs = []
    # for i in np.arange(img_np.shape[0]):
    #     for j in np.arange(img_np.shape[1]):
    #         if img_np[i][j]== 205:
    #             white=white+1
    #         if img_np[i][j]== 0:
    #             wall=wall+1
    #             obs.append([j,i])
    #         if img_np[i][j]== 254:
    #             space=space+1 
    # print(white)
    # print(space)
    # print(wall)
    # for i in np.arange(img_np.shape[0]):
    #     for j in np.arange(img_np.shape[1]):
    #         if img_np[i][j] != 205 and img_np[i][j] != 0:
    #            print(img_np[i][j])
    print(img_np[0:100,0:100])
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
    s.step(100)

    with psf.plot.SceneVisualizer(s, "images/result") as sv:
        sv.animate()
        # sv.plot()
