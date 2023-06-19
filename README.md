# 3D-reconstruction-table

## Requirements
 - Ubuntu 20.04 LTS
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


## Model
![turntable_model](https://github.com/lucas-t-reis/3D-reconstruction-table/assets/13222862/0d11b1c9-286b-46fe-b1fd-266036c12099)


In case you want to 3D-print the rotating table we've used in the experiment, there is a .obj file with the model in the `turntable` folder.
