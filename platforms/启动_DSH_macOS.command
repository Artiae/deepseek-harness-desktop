#!/bin/bash
# DeepSeek Harness macOS 启动脚本
# 双击 .command 文件即可运行

cd "$(dirname "$0")/.."

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "错误：未找到 Python3，请先安装 Python"
    read -p "按回车键退出..."
    exit 1
fi

# 检查 pywebview
python3 -c "import webview" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "正在安装 pywebview..."
    pip3 install pywebview
fi

echo "正在启动 DeepSeek Harness..."
python3 dsh_desktop.py
