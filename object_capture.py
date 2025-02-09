import subprocess
import os
from pathlib import Path

def create_3d_model(input_folder: str, output_file: str):
    """
    Create a 3D model using Apple's Object Capture API.
    
    Args:
        input_folder: Path to folder containing input images
        output_file: Path for the output USDZ file
    """
    # Create the Swift script
    script = f'''
import RealityKit
import Foundation

guard PhotogrammetrySession.isSupported else {{
    print("Object Capture is not supported on this device")
    exit(1)
}}

let inputFolder = URL(fileURLWithPath: "{input_folder}")
let outputFile = URL(fileURLWithPath: "{output_file}")

// 使用高级配置
var config = PhotogrammetrySession.Configuration()
config.featureSensitivity = .high  // 高特征敏感度，适合白色物体
config.sampleOrdering = .unordered  // 让算法自己决定最佳顺序
config.isObjectMaskingEnabled = true  // 启用物体遮罩

guard let session = try? PhotogrammetrySession(input: inputFolder, configuration: config) else {{
    print("Failed to create photogrammetry session")
    exit(1)
}}

// Create the request
// 创建请求
// 使用最高质量设置
let request = PhotogrammetrySession.Request.modelFile(url: outputFile, detail: .raw)

// Process and wait for completion
let waiter = Task {{
    do {{
        for try await output in session.outputs {{
            switch output {{
                case .processingComplete:
                    print("Processing complete!")
                    exit(0)
                case .requestProgress(_, let fractionComplete):
                    print("Progress: \\(fractionComplete * 100)%")
                case .requestError(_, let error):
                    print("Error: \\(error)")
                    exit(1)
                case .inputComplete:
                    print("Input processing complete, beginning reconstruction...")
                case .invalidSample(let id, let reason):
                    print("Invalid sample \\(id): \\(reason)")
                case .skippedSample(let id):
                    print("Skipped sample: \\(id)")
                case .automaticDownsampling:
                    print("Notice: Images were automatically downsampled")
                default:
                    break
            }}
        }}
    }} catch {{
        print("Error: \\(error)")
        exit(1)
    }}
}}

// Start processing
try! session.process(requests: [request])

// Run until completion
RunLoop.main.run()
'''
    
    # Save the Swift script
    script_path = Path('reconstruct.swift')
    script_path.write_text(script)
    
    # Compile and run the Swift script
    try:
        subprocess.run(['swiftc', 'reconstruct.swift'], check=True)
        subprocess.run(['./reconstruct'], check=True)
    finally:
        # Cleanup
        if script_path.exists():
            script_path.unlink()
        if Path('reconstruct').exists():
            Path('reconstruct').unlink()

if __name__ == '__main__':
    input_folder = os.path.expanduser("~/Pictures/Sony Scan Resized")
    output_file = os.path.expanduser("~/Desktop/model_v4.usdz")
    
    print(f"Starting 3D reconstruction...")
    print(f"Input folder: {input_folder}")
    print(f"Output file: {output_file}")
    
    create_3d_model(input_folder, output_file)
