# 🖥️ DeepSeek Harness Desktop

将 [DeepSeek Harness](http://127.0.0.1:3080/) 网页版封装为桌面应用和移动端 PWA。

## ✨ 功能特性

- 🖥️ **Windows / macOS / Linux** 桌面独立窗口
- 📱 **手机 PWA** — 添加到主屏幕，像原生 App 一样使用
- 🔍 自动检测 DSH 服务是否运行
- 🎯 无浏览器地址栏，沉浸式体验
- 📐 支持窗口缩放、文字选择

## 🚀 快速开始

### 前置条件

确保 DeepSeek Harness 服务正在运行：
```
http://127.0.0.1:3080/
```

### 安装依赖

```bash
pip install -r requirements.txt
```

### Windows

```bash
# 方式1：直接运行
python dsh_desktop.py

# 方式2：双击 bat 文件
platforms/启动_DSH_Windows.bat

# 方式3：无控制台窗口
双击 platforms/启动_DSH_Windows(无控制台).vbs
```

### macOS

```bash
# 方式1：直接运行
python3 dsh_desktop.py

# 方式2：双击 command 文件
双击 platforms/启动_DSH_macOS.command

# 方式3：首次需要赋予执行权限
chmod +x platforms/启动_DSH_macOS.command
双击运行
```

### Linux

```bash
# 安装系统依赖（Ubuntu/Debian）
sudo apt install python3-gi gir1.2-webkit2-4.1

# 运行
python3 dsh_desktop.py
```

### 📱 手机端（PWA）

```bash
# 1. 生成图标
python mobile/generate_icons.py

# 2. 启动 PWA 代理服务
python mobile/pwa_server.py

# 3. 手机浏览器访问
http://<你的电脑IP>:8080

# 4. 浏览器菜单 → "添加到主屏幕"
```

## 📁 项目结构

```
DeepSeek Harness/
├── dsh_desktop.py              # 桌面应用主程序（跨平台）
├── requirements.txt            # Python 依赖
├── README.md                   # 项目说明
├── .gitignore
├── platforms/                  # 各平台启动脚本
│   ├── 启动_DSH_Windows.bat
│   ├── 启动_DSH_Windows(无控制台).vbs
│   ├── 启动_DSH_macOS.command
│   └── 启动_DSH_Linux.sh
└── mobile/                     # 手机端 PWA
    ├── pwa_server.py           # PWA 代理服务器
    ├── generate_icons.py       # 图标生成器
    └── icons/                  # PWA 图标
```

## 🛠️ 技术栈

| 平台 | 技术 |
|------|------|
| 桌面端 | Python + pywebview (WebView2/Cocoa/WebKitGTK) |
| 移动端 | PWA (Progressive Web App) + FastAPI 代理 |

## 📝 注意事项

- 桌面版需要先启动 DSH 服务（`http://127.0.0.1:3080/`）
- 手机 PWA 需要手机和电脑在同一局域网
- macOS 首次运行 `.command` 文件需要在"系统设置 → 隐私与安全性"中允许
- Windows 需要 Edge WebView2 运行时（Win10/11 自带）

## 📄 License

MIT License
