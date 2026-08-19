"""生成 PWA 图标"""
import os

# 创建简单的 SVG 图标（不需要 Pillow 依赖）
icons_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons")
os.makedirs(icons_dir, exist_ok=True)

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="80" fill="#4F46E5"/>
  <text x="256" y="320" font-family="Arial, sans-serif" font-size="240" font-weight="bold" fill="white" text-anchor="middle">DSH</text>
</svg>"""

# 保存 SVG
with open(os.path.join(icons_dir, "icon.svg"), "w") as f:
    f.write(svg_content)

# 创建简单的 HTML 图标页面（可用于在线生成 PNG）
html_content = """<!DOCTYPE html>
<html><body style="margin:0;display:flex;justify-content:center;align-items:center;height:100vh;background:#4F46E5">
<h1 style="color:white;font-size:200px;font-family:Arial">DSH</h1>
<p style="color:white">右键保存为 PNG 图标</p>
</body></html>"""

with open(os.path.join(icons_dir, "icon-generator.html"), "w") as f:
    f.write(html_content)

print(f"图标文件已生成到: {icons_dir}")
print("请打开 icon-generator.html，右键另存为 PNG 图标（192x192 和 512x512）")
