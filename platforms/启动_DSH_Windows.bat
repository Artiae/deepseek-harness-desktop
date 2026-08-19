@echo off
chcp 65001 >nul 2>&1
title DeepSeek Harness
echo ========================================
echo   DeepSeek Harness 桌面版启动器
echo ========================================
echo.

echo [1/2] 检查 DSH 服务...
curl -s -o nul -w "%%{http_code}" http://127.0.0.1:3080/ >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] DSH 服务未运行！
    echo.
    echo 请先在 CMD 中运行：npx @deepseek-ai/dsh web
    echo.
    pause
    exit /b 1
)
echo [OK] DSH 服务正在运行

echo.
echo [2/2] 启动桌面应用...
echo.
"D:\Users\MI\Miniconda3\python.exe" "%~dp0..\dsh_desktop.py"

echo.
echo 程序已退出。
pause
