On Error Resume Next

Set objFSO = CreateObject("Scripting.FileSystemObject")
intAnswer = MsgBox("Are you sure you want to delete Just a Game?", vbYesNo + vbQuestion, "Confirmation")

If intAnswer = vbYes Then
    DeleteFolder "."
    MsgBox "Just a Game deleted successfully.", vbInformation, "Success"
Else
    MsgBox "Deletion canceled.", vbExclamation, "Canceled"
End If

Sub DeleteFolder(strFolder)
    Dim objFolder, objSubFolder, objFile
    Set objFolder = objFSO.GetFolder(strFolder)

    ' Delete all files in the folder
    For Each objFile in objFolder.Files
        objFile.Delete(True)
    Next

    ' Recursively delete all subfolders
    For Each objSubFolder in objFolder.Subfolders
        DeleteFolder objSubFolder.Path
    Next

    ' Delete the current folder
    objFSO.DeleteFolder strFolder, True
End Sub
