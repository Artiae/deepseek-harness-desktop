"""
DeepSeek Harness 桌面应用
基于 pywebview 将 DSH 网页封装为桌面应用（支持 Windows / macOS / Linux）
"""
import webview
import sys
import os
import platform
import urllib.request

DSH_URL = "http://127.0.0.1:3080/"


def check_dsh_running():
    """检查 DSH 服务是否在运行"""
    try:
        urllib.request.urlopen(DSH_URL, timeout=3)
        return True
    except Exception:
        return False


def main():
    if not check_dsh_running():
        print("=" * 50)
        print("错误：DeepSeek Harness 服务未运行！")
        print(f"请先启动 DSH 服务（{DSH_URL}）")
        print("然后再运行本程序。")
        print("=" * 50)
        if platform.system() == "Windows":
            input("按回车键退出...")
        sys.exit(1)

    # 获取图标路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(base_dir, "assets", "icon.ico")

    window = webview.create_window(
        title="DeepSeek Harness",
        url=DSH_URL,
        width=1400,
        height=900,
        min_size=(800, 600),
        resizable=True,
        text_select=True,
        icon=icon_path if os.path.exists(icon_path) else None,
    )

    # macOS 用 cocoa，Windows 用 edgechromium，Linux 用 gtk
    gui = None
    system = platform.system()
    if system == "Darwin":
        gui = "cocoa"
    elif system == "Windows":
        gui = "edgechromium"

    webview.start(gui=gui, debug=False)


if __name__ == "__main__":
    main()
