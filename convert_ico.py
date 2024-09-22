from PIL import Image

# 打开原始 ICO 文件
input_file = 'D:\\MyCode\\weibu.ico'
output_file = 'D:\\MyCode\\weibu_converted.ico'

# 打开并保存为 ICO 格式
with Image.open(input_file) as img:
    img.save(output_file, format='ICO')

print(f"转换完成: {output_file}")
