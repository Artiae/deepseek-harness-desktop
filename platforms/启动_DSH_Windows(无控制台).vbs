Set objShell = CreateObject("WScript.Shell")

' 先检查 DSH 服务是否运行
Dim httpReq, dshRunning
dshRunning = False
On Error Resume Next
Set httpReq = CreateObject("MSXML2.XMLHTTP")
httpReq.Open "GET", "http://127.0.0.1:3080/", False
httpReq.Send
If Err.Number = 0 And httpReq.Status = 200 Then
    dshRunning = True
End If
On Error GoTo 0

If Not dshRunning Then
    MsgBox "错误：DSH 服务未运行！" & vbCrLf & vbCrLf & _
           "请先在 CMD 中运行：" & vbCrLf & _
           "npx @deepseek-ai/dsh web", vbCritical, "DeepSeek Harness"
    WScript.Quit 1
End If

' 启动桌面应用（显示控制台以便看到错误）
objShell.Run """D:\Users\MI\Miniconda3\python.exe"" ""D:\DeepSeek Harness\dsh_desktop.py""", 1, True
