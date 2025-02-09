import os
import shutil
from pathlib import Path

def select_images(input_folder, output_folder, step=3):
    """
    从输入文件夹中每隔step张选择一张图片复制到输出文件夹
    """
    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)
    
    # 获取所有JPG文件并排序
    images = sorted([f for f in os.listdir(input_folder) if f.endswith('.JPG')])
    
    # 每隔step张选择一张
    selected_images = images[::step]
    
    print(f"从{len(images)}张图片中选择了{len(selected_images)}张")
    
    # 复制选中的图片
    for img in selected_images:
        src = os.path.join(input_folder, img)
        dst = os.path.join(output_folder, img)
        shutil.copy2(src, dst)
        print(f"复制: {img}")

if __name__ == '__main__':
    input_folder = "/Users/redwinam/Developer/3dscanner/turntable_scan/resized_images"
    output_folder = "/Users/redwinam/Developer/3dscanner/turntable_scan/selected_images"
    
    # 每隔6张选一张，确保覆盖完整的360度
    select_images(input_folder, output_folder, step=6)
    
    # 确保输出文件夹中的图片数量不超过30张
    images = sorted([f for f in os.listdir(output_folder) if f.endswith('.JPG')])
    if len(images) > 30:
        # 删除多余的图片
        for img in images[30:]:
            os.remove(os.path.join(output_folder, img))
        print(f"限制图片数量到30张")
