# COLMAP 3D重建指南

本文档记录了使用COLMAP进行3D重建的详细过程和参数设置。

## COLMAP重建流程

### 1. 特征提取参数
```bash
colmap feature_extractor \
    --database_path ~/Developer/3dscanner/turntable_scan/database.db \
    --image_path "/Users/redwinam/Pictures/Sony Scan Resized" \
    --ImageReader.camera_model OPENCV \
    --SiftExtraction.max_num_features 32768 \
    --SiftExtraction.edge_threshold 20 \
    --SiftExtraction.peak_threshold 0.001 \
    --SiftExtraction.max_num_orientations 2 \
    --SiftExtraction.upright 1
```

### 2. 特征匹配参数
```bash
colmap exhaustive_matcher \
    --database_path ~/Developer/3dscanner/turntable_scan/database.db \
    --ExhaustiveMatching.block_size 50
```

### 3. 稀疏重建参数
```bash
colmap mapper \
    --database_path ~/Developer/3dscanner/turntable_scan/database.db \
    --image_path "/Users/redwinam/Pictures/Sony Scan Resized" \
    --output_path ~/Developer/3dscanner/turntable_scan/sparse \
    --Mapper.init_min_tri_angle 4 \
    --Mapper.multiple_models 1 \
    --Mapper.ba_refine_focal_length 1 \
    --Mapper.ba_refine_extra_params 1 \
    --Mapper.min_num_matches 15 \
    --Mapper.init_max_reg_trials 100
```

## 参数说明

### 特征提取
- `max_num_features 32768`: 增加特征点数量
- `edge_threshold 20`: 提高边缘检测灵敏度
- `peak_threshold 0.001`: 降低特征点检测阈值
- `upright 1`: 假设特征点垂直（适用于转台设置）

### 特征匹配
- 使用穷举匹配而不是顺序匹配
- 确保所有可能的图像对都被考虑
- 对于环形拍摄序列特别重要

### 稀疏重建
- `init_min_tri_angle 4`: 降低三角测量角度要求
- `multiple_models 1`: 允许多次重建尝试
- `min_num_matches 15`: 降低图像配准阈值
- `init_max_reg_trials 100`: 增加初始对查找尝试次数
