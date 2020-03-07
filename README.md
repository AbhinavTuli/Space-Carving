This is a basic implementation made from scartch that assumes that the 2 images were taken from the same distance, with same focal length.

With this assumption we can simplify space carving quite a bit and its biggest advantage is that this doesn't require the extrinsic matrix.

We have tested this using 2 100x100 pictures of guns (low resoltuion taken to speed up visualization, higher resolutions can be used as well). The output model obtained was satisfactory.

To do:-

Save the model to a .pcd file
