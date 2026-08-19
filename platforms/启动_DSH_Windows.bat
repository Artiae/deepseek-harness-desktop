@echo off
chcp 65001 >nul 2>&1
title DeepSeek Harness
echo 正在启动 DeepSeek Harness 桌面版...
"D:\Users\MI\Miniconda3\python.exe" "%~dp0..\dsh_desktop.py"
pause
