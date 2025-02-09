# 3D扫描项目 - 成功扫描白色物体

## 项目概述
本项目记录了使用多种3D重建方法成功扫描白色物体的过程。主要挑战是重建一个表面特征很少的小型白色矩形物体。

## 设备配置
- 相机：Sony相机
- 图像分辨率：8640 x 5760
- 设置：黑色转盘配合参考图案
- 物体尺寸：约10厘米

## 成功要点

### 1. 参考图案
- 创建了自定义A4尺寸参考图案：
  - 不同大小的随机黑点
  - 三角形图案提供额外特征
  - 角落标记确保稳定性
  - 中心区域留空放置物体

### 2. 图像处理
- 将图像缩小到原始尺寸的25%（2160 x 1440）
  - 减少噪声
  - 提高处理速度
  - 改善特征检测

### 3. COLMAP重建

#### 特征提取参数
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

#### 特征匹配参数
```bash
colmap exhaustive_matcher \
    --database_path ~/Developer/3dscanner/turntable_scan/database.db \
    --ExhaustiveMatching.block_size 50
```

#### 稀疏重建参数
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

### 4. Apple Object Capture重建

使用苹果原生的Object Capture API进行3D重建，效果非常好：

#### 关键参数设置
```python
config = PhotogrammetrySession.Configuration()
config.featureSensitivity = .high  # 高特征敏感度，适合白色物体
config.sampleOrdering = .sequential  # 图片按顺序排列
config.isObjectMaskingEnabled = true  # 启用物体遮罩
```

#### 重建过程
1. 使用缩放后的图片作为输入
2. 设置最高质量重建
3. 输出USDZ格式模型
4. 可直接在Mac上预览和编辑

## 参数说明

### COLMAP参数
- `max_num_features 32768`: 增加特征点数量
- `edge_threshold 20`: 提高边缘检测灵敏度
- `peak_threshold 0.001`: 降低特征点检测阈值
- `upright 1`: 假设特征点垂直（适用于转台设置）

### Object Capture参数
- `featureSensitivity = .high`: 提高特征检测灵敏度
- `sampleOrdering = .sequential`: 优化相邻图片的匹配
- `isObjectMaskingEnabled = true`: 自动分离物体和背景

## 重建结果
成功重建白色物体的关键：
1. 使用参考图案提供稳定特征点
2. 缩小图片尺寸改善特征检测
3. 调整参数适应具有挑战性的表面
4. 使用苹果原生API获得更好的重建效果

## 未来扫描建议
1. 始终使用参考图案
2. 确保光照均匀，减少反射
3. 拍摄时使用更小的角度步进
4. 先用小图片处理，需要时再放大
5. 优先尝试Object Capture API，效果更好

## 创建日期：2025年2月10日
