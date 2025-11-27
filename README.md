
# Project Title: 2D to 3D Mesh Reconstruction (3D Reconstruction from 2D Images for Peripheral Edema Analysis)

## Description
- This project aims to reconstruct 3D meshes from 2D images. 
- Each steps are performed individually in each notebook, from data analysis to postprocessing.
- The project is done as a collaboration with Eli Lilly (LCCP), NUHS, and CADENCE.


<<<<<<< HEAD

=======
>>>>>>> e4d416dfebbc4937a2d332377cdf80639a343e36
## Notebooks

**1. EDA of input data**
- main_0_data_analysis.ipynb
    - Performs data analysis on the input dataset.
<br>

**2. Plot data for visualizations**
- main_1_data_plot.ipynb
    - Generates various plots to visualize the data.
<br>

**3. Convert videos into multi-frame images**
- main_2_video_to_image.ipynb
    - Extracts frames from a video and converts them into images.
<br>

**4. Remove backgrounds from images**
- main_3_remove_bg.ipynb
    - Removes the background from the images using deep learning models.
<br>

**5. Improve image resolution via debluring**
- main_4_deblur.ipynb
    - Deblurs the images to enhance their quality.
<br>

**6. Performs SFM and MVG on images**
- main_5_2D_to_3D.ipynb
    - Reconstructs 3D meshes from the 2D images via various CV libraries.
- Models used:
    - OpenMVG [Link OpenMVG](https://github.com/openMVG/openMVG)
    - OpenMVS [Link OpenMVS](https://github.com/cdcseacave/openMVS)
    - COLMAP [Link COLMAP](https://github.com/colmap/colmap)
    - VGGSFM [Link VGGSFM](https://github.com/facebookresearch/vggsfm)
    - MVE [Link MVE](https://github.com/simonfuhrmann/mve)
<br>

**7. Compute volume and success rates of SFM and MVG**
- main_6_volume_calculation.ipynb
    - Calculates the volume of the reconstructed 3D meshes.
<br>

**8.  Postprocess 3D cloud and meshes**
- main_7_postprocessing.ipynb
    - Performs postprocessing on the 3D meshes to refine them.
<br>

## Getting Started
To get started with this project, clone the repository and open the Jupyter notebooks in the order listed above.

## Prerequisites
- Python 3.8
- Jupyter Notebook
- Required libraries (listed in each notebook)

## Installation
1. Clone the repo:
   
```bash
git clone https://github.com/WeiYanPeh/2D-to-3D-mesh-reconstruction.git
cd 2D-to-3D-mesh-reconstruction
```
<br>

2. Download and install various libraries:
- Directly required:
    - OpenMVG [Link OpenMVG](https://github.com/openMVG/openMVG)
    - OpenMVS [Link OpenMVS](https://github.com/cdcseacave/openMVS)
    - COLMAP [Link COLMAP](https://github.com/colmap/colmap)
    - VGGSFM [Link VGGSFM](https://github.com/facebookresearch/vggsfm)
    - MVE [Link MVE](https://github.com/simonfuhrmann/mve)
- Indirectly required: 
    - ceres-bin: [Link ceres-bin](http://ceres-solver.org/installation.html)
    - eigen: [Link eigen](https://github.com/eigen-mirror/eigen)
    - glog: [Link glog](https://github.com/google/glog)
    - LightGLue (VGGSFM): [Link LightGLue](https://github.com/cvg/LightGlue)
    - minieigen: [Link minieigen](https://github.com/eudoxos/minieigen)
    - openexr: [Link openexr](https://github.com/AcademySoftwareFoundation/openexr)
    - rapidjson: [Link rapidjson](https://rapidjson.org/)
    - sphinx: [Link sphinx](https://github.com/sphinx-doc/sphinx)
    - vcglib: [Link vcglib](https://github.com/cnr-isti-vclab/vcglib)
    - viser: [Link viser](https://github.com/nerfstudio-project/viser)