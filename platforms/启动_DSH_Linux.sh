#!/bin/bash
# DeepSeek Harness Linux 启动脚本

cd "$(dirname "$0")/.."

# 检查依赖
if ! command -v python3 &> /dev/null; then
    echo "错误：未找到 Python3"
    exit 1
fi

# Linux 需要安装 webkit2gtk
if ! python3 -c "import webview" 2>/dev/null; then
    echo "正在安装依赖..."
    pip3 install pywebview[gtk]
    # Ubuntu/Debian: sudo apt install python3-gi gir1.2-webkit2-4.1
    # Fedora: sudo dnf install python3-gobject webkit2gtk4.1
fi

python3 dsh_desktop.py
