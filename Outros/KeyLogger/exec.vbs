Set WshShell = CreateObject("WScript.Shell")

WshShell.Run chr(34) & "RQ.bat" & chr(34), 0, True
Set WshShell = Nothing
