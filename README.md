# SiliconScan3D

> 基于 Apple Silicon 优化的 3D 物体扫描重建工具集

## 项目概述

SiliconScan3D 是一个利用 Apple 的 Object Capture API 将照片转化为高质量 3D 模型的工具集。项目特别优化了对于白色、低纹理物体的扫描过程，充分利用了 Apple Silicon 的神经引擎和 Metal 图形处理能力。

## 系统要求

- macOS 12 或更高版本
- 搭载 Apple Silicon 芯片的 Mac 设备
- GPU 内存至少 4GB
- Python 3.8 或更高版本

## 快速开始

### 1. 安装依赖

```bash
# 克隆项目
git clone https://github.com/redwinam/silicon-scan3d.git
cd silicon-scan3d

# 安装Python依赖
pip install -r requirements.txt

# 安装ImageMagick用于图片处理
brew install imagemagick
```

### 2. 生成参考图案

```bash
# 生成用于扫描的参考图案
python create_reference_pattern.py
```

参考图案的原理是通过在扫描场景中添加特征点，为 3D 重建算法提供稳定的参考信息。它包含：

- 不同大小的随机黑点：提供独特的特征点
- 三角形图案：提供方向性特征
- 角落标记：确保准确的相机位姿估计

生成的`reference_pattern.png`可以直接打印为 A4 纸张作为参考标记垫。将扫描物体放置在中心区域，周围的标记将帮助软件更准确地重建 3D 模型。

### 3. 拍摄照片

1. 打印生成的参考图案
2. 将物体放置在参考图案中心
3. 使用转台或手动旋转物体，拍摄全方位照片
4. 使用 ImageMagick 缩放图片（推荐）：
   ```bash
   # 批量缩放图片至25%
   mogrify -resize 25% "/path/to/images/*.jpg"
   ```

### 4. 生成 3D 模型

```bash
# 使用Object Capture API生成模型
python object_capture.py --input "/path/to/images" --output "./model.usdz"
```

生成的 USDZ 模型默认保存在当前目录，可直接在 Mac 上预览或使用 Reality Composer 编辑。

## 工具说明

### create_reference_pattern.py

生成用于 3D 扫描的参考图案，包含：

- 随机大小的黑点
- 三角形特征标记
- 角落定位点
- 预留的物体放置区域

```python
# 自定义参数
python create_reference_pattern.py --size A4 --dots 1000 --min_size 2 --max_size 10
```

### object_capture.py

核心 3D 重建工具，特性：

- 使用 Apple Object Capture API
- 支持高质量 USDZ 输出
- 优化的参数配置

```python
# 示例：使用最高质量设置
python object_capture.py --input "/path/to/images" --output "./model.usdz"
```

## 实际案例

### 设备配置

- 相机：Sony 相机
- 图像分辨率：8640 x 5760（建议缩放至 25%）
- 设置：黑色转盘配合参考图案
- 物体尺寸：约 10 厘米

### 最佳实践

1. 使用参考图案提供稳定特征点
2. 确保光照均匀，减少反射
3. 每次旋转角度建议在 10-15 度
4. 先用较小尺寸图片测试
5. 控制图片数量在 30-60 张之间

## 其他重建方法

除了 Apple Object Capture API，本项目曾尝试使用 COLMAP 进行 3D 重建。但由于 COLMAP 在 Apple Silicon 上不支持密集点云生成（dense point cloud generation），所以最终选择了 Object Capture API 作为主要方案。如果你对 COLMAP 的尝试过程感兴趣，可以参考[COLMAP 使用指南](./COLMAP_GUIDE.md)。

## 许可证

本作品采用 [知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](http://creativecommons.org/licenses/by-nc-sa/4.0/) 进行许可。

[![CC BY-NC-SA 4.0](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

## 创建日期

2025 年 2 月 10 日
