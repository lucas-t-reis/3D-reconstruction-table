# 3D-reconstruction-table

## Requirements
 - Windows 10 (Instant-NGP)
 - Ubuntu 20.04 LTS (COLMAP)
 - Singularity 3.11.0
 - Python >= 3.9

## Installation

After cloning the repo, you can create a `workspace` directory to store the container images.
All commands below will assume you are in this directory and that you have an NVIDIA graphics card.

### COLMAP

To build the container:

```
$ sudo singularity build --sandbox COLMAP/ ../COLMAP.def
```

To run colmap gui:

```
$ singularity shell --nv -B /run COLMAP
Singularity> colmap gui
```

Alternatively, there is a script in src named `colmap-automatic-reconstruction.sh` that allows to run COLMAP via CLI.

### Instant-NGP
After choosing the appropriate version based on your graphics card, navigate to the scripts folder within the Instant-NGP repository and execute:

To extract pose data from the videos:

```
python C:/path/to/InstantNGP/scripts/colmap2nerf.py --video_in video.mp4 --video_fps 3 --run_colmap --aabb_scale 2
```


To understand more about the parameters, refer to the link below on tips for training NeRF models.


To begin the reconstruction, simply open Instant-NGP and drop the folder containing the generated data. The reconstruction should take no more than 2 minutes. If it doesn't converge until then, try enhancing the image quality, removing blurry pictures or following the data acquisition for the tool: [Tips for training NeRF models](https://github.com/NVlabs/instant-ngp/blob/master/docs/nerf_dataset_tips.md)



## Model
![turntable_model](https://github.com/lucas-t-reis/3D-reconstruction-table/assets/13222862/0d11b1c9-286b-46fe-b1fd-266036c12099)


In case you want to 3D-print the rotating table we've used in the experiment, there is a .obj file with the model in the `turntable` folder.
