"""
DeepSeek Harness 移动端 PWA 代理服务器
在 DSH 服务基础上注入 PWA 支持，手机访问即可添加到主屏幕
"""
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

app = FastAPI(title="DSH Mobile PWA")

DSH_URL = "http://127.0.0.1:3080"

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 挂载静态文件（图标等）
if os.path.exists(os.path.join(current_dir, "icons")):
    app.mount("/icons", StaticFiles(directory=os.path.join(current_dir, "icons")), name="icons")


@app.get("/manifest.json")
async def manifest():
    """PWA 清单文件"""
    return JSONResponse({
        "name": "DeepSeek Harness",
        "short_name": "DSH",
        "description": "DeepSeek Harness AI 助手",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#000000",
        "theme_color": "#4F46E5",
        "orientation": "portrait-primary",
        "icons": [
            {"src": "/icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/icons/icon-512.png", "sizes": "512x512", "type": "image/png"}
        ]
    })


@app.get("/sw.js")
async def service_worker():
    """Service Worker"""
    sw_code = """
    const CACHE_NAME = 'dsh-v1';
    self.addEventListener('install', event => {
        self.skipWaiting();
    });
    self.addEventListener('activate', event => {
        event.waitUntil(clients.claim());
    });
    self.addEventListener('fetch', event => {
        event.respondWith(
            fetch(event.request).catch(() => caches.match(event.request))
        );
    });
    """
    return HTMLResponse(sw_code, media_type="application/javascript")


@app.get("/{full_path:path}")
async def proxy(full_path: str):
    """代理 DSH 页面并注入 PWA 支持"""
    import urllib.request

    target_url = f"{DSH_URL}/{full_path}" if full_path else DSH_URL

    try:
        req = urllib.request.Request(target_url)
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode("utf-8")

        # 注入 PWA meta 标签
        pwa_inject = """
    <link rel="manifest" href="/manifest.json">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="DSH">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="theme-color" content="#4F46E5">
    <link rel="apple-touch-icon" href="/icons/icon-192.png">
    <script>
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('/sw.js');
        }
    </script>
"""
        # 在 </head> 前注入
        content = content.replace("</head>", pwa_inject + "</head>")

        return HTMLResponse(content)

    except Exception as e:
        return HTMLResponse(f"<h1>无法连接 DSH 服务</h1><p>{DSH_URL}</p><p>{e}</p>", status_code=502)


if __name__ == "__main__":
    print("=" * 50)
    print("DSH 移动端 PWA 服务启动中...")
    print(f"手机访问: http://<你的IP>:8080")
    print(f"本机访问: http://localhost:8080")
    print("=" * 50)
    uvicorn.run(app, host="0.0.0.0", port=8080)
