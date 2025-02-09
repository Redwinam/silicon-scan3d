# SiliconScan3D

> 基于Apple Silicon优化的3D物体扫描重建工具集

## 项目概述

SiliconScan3D是一个利用Apple的Object Capture API将照片转化为高质量3D模型的工具集。项目特别优化了对于白色、低纹理物体的扫描过程，充分利用了Apple Silicon的神经引擎和Metal图形处理能力。

## 系统要求

- macOS 12或更高版本
- 搭载Apple Silicon芯片的Mac设备
- GPU内存至少4GB
- Python 3.8或更高版本

## 快速开始

### 1. 安装依赖

```bash
# 克隆项目
git clone https://github.com/yourusername/silicon-scan3d.git
cd silicon-scan3d

# 安装Python依赖
pip install -r requirements.txt
```

### 2. 生成参考图案

```bash
# 生成用于扫描的参考图案
python create_reference_pattern.py
```

### 3. 拍摄照片

1. 打印生成的参考图案
2. 将物体放置在参考图案中心
3. 使用转台或手动旋转物体，拍摄全方位照片
4. 建议图片分辨率不超过4K，可使用`select_images.py`进行批量缩放

### 4. 生成3D模型

```bash
# 使用Object Capture API生成模型
python object_capture.py
```

生成的USDZ模型将保存在桌面上，可直接在Mac上预览或使用Reality Composer编辑。

## 工具说明

### create_reference_pattern.py

生成用于3D扫描的参考图案，包含：
- 随机大小的黑点
- 三角形特征标记
- 角落定位点
- 预留的物体放置区域

```python
# 自定义参数
python create_reference_pattern.py --size A4 --dots 1000 --min_size 2 --max_size 10
```

### select_images.py

图片处理工具，支持：
- 批量缩放
- 图片筛选
- 重命名

```python
# 示例：每隔3张选择一张图片
python select_images.py --input "照片文件夹" --step 3
```

### object_capture.py

核心3D重建工具，特性：
- 使用Apple Object Capture API
- 支持高质量USDZ输出
- 优化的参数配置

```python
# 示例：使用最高质量设置
python object_capture.py --quality raw --sensitivity high
```

## 实际案例

### 设备配置
- 相机：Sony相机
- 图像分辨率：8640 x 5760（建议缩放至25%）
- 设置：黑色转盘配合参考图案
- 物体尺寸：约10厘米

### 最佳实践
1. 使用参考图案提供稳定特征点
2. 确保光照均匀，减少反射
3. 每次旋转角度建议在10-15度
4. 先用较小尺寸图片测试
5. 使用`select_images.py`控制图片数量（建议30-60张）

## 其他重建方法

除了Apple Object Capture API，本项目还支持使用COLMAP进行3D重建。详细信息请参考[COLMAP使用指南](./COLMAP_GUIDE.md)。

## 许可证

MIT

## 创建日期

2025年2月10日
