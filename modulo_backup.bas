Attribute VB_Name = "modulo_backup"

'modulo de backup

Sub backupDestaPlanilha()
    myLocal = "\\Brwsaqafs\wrk\Exportacao\CUSTOMER SERVICE\CPP\"
    myFullPath = myLocal & ThisWorkbook.Name
    ThisWorkbook.Save
    ThisWorkbook.SaveAs myFullPath
    checarArquivo (myFullPath)
End Sub

Private Sub checarArquivo(ByVal myFullPath As String)
    If (Round(FileSystem.FileDateTime(myFullPath), 0) = Date) Then
        MsgBox "Backup realizado."
    End If
End Sub




'----------------- VERSAO ANTIGA DO ALGORITIMO DE CRIACAO DE MENU
'
'
Sub bkp_criarMenu()
    
    Dim myR As Range
    Set myR = menu.Cells(1, 2) 'inicio em B3
    
    Dim csoLinks As Range
    Set csoLinks = p01.Cells(2, 4) 'inicio em D4
    
    Dim corPasta As String
    Dim corArquivo As String
    corPasta = RGB(32, 255, 204) '"#FFE699"
    corArquivo = RGB(0, 5, 231) '"#E7E6E6"
    
    Dim bAltura As Double
    Dim bLargura As Double
    Dim bDivisao As Double
    
    bAltura = 20
    bLargura = bAltura * 8
    bDivisao = 5
    
    Dim nBotao As Integer
    nBotao = 0
    
    Dim myButton1 As OLEObject
    Dim appNomeBotao As String
    Dim appTituloBotao As String
    Dim appPosicaoTopBotao As Double
    
    
    '------------------------ processo de criação dinamica
    While (csoLinks <> Empty)
        Set myButton1 = ActiveSheet.OLEObjects.Add(ClassType:="Forms.CommandButton.1", Link:=False, DisplayAsIcon:=False)
        
        'durante a criação dinamica o calculo de top será posicaoInicial + nElemento * (bAltura + bEspaco)
        
        appNomeBotao = "bto_" & csoLinks.Text
        appTituloBotao = csoLinks.Offset(0, -1).Text
        appPosicaoTopBotao = myR.Top + nBotao * (bAltura + bDivisao)

        'set main button properties
        With myButton1
            .Name = appNomeBotao
            .Object.Caption = appTituloBotao
            .Top = appPosicaoTopBotao
            .Left = myR.Left
            .Height = bAltura
            .Width = bLargura
            .Placement = xlMoveAndSize
            .PrintObject = True            'or false as per your taste
        End With

        nBotao = nBotao + 1
        Set csoLinks = csoLinks.Offset(1, 0)
    Wend
    'MsgBox "Altura: " & myR.Height & Chr(13) & "Largura: " & myR.Width
End Sub
