This is a basic implementation made from scratch that assumes that the 2 images were taken from the same distance, with same focal length.

With this assumption we can simplify space carving quite a bit and its biggest advantage is that this doesn't require the extrinsic matrix.

This has been generated using 2 100x100 pictures of guns (low resoltuion taken to speed up visualization, higher resolutions can be used as well). The output model obtained was satisfactory. The model has also been saved as a ply file.
The ply file was further converted to pcd file using MATLAB with the following MATLAB code:-

```
ptCloud = pcread("out.ply")

pcwrite(ptCloud,'out.pcd','Encoding','ascii');
```

Input images:-

![](E1.jpg)
![](E2.jpg)

Screenshots of model:-

![](Screenshot1.png)
![](Screenshot2.png)


