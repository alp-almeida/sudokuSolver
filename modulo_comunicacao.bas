Attribute VB_Name = "modulo_comunicacao"
'comunicação: email
'
' Algoritmo principal de geração de e-mail
' --------------------------------------------
Sub envio_email_de_saldo()
    Dim var_path_folder As String
    var_path_folder = "C:\Users\513130\Desktop\saldos"
    
    Set fs = CreateObject("Scripting.FileSystemObject")
    Dim var_folder_object
    Set var_folder_object = fs.getfolder(var_path_folder)
    
    Set var_files_in_folder = var_folder_object.Files
    
    s = Empty
    
    '
    ' Varre os arquivos da pasta, prepara o email
    ' -----------------------------------------------
    Dim var_email_destinatario As String
    Dim var_email_assunto As String
    For Each file In var_files_in_folder
        If (file.DateLastModified >= Date) Then
            If (file.Name = "barretos.pdf") Then var_email_destinatario = "transportes@agrodinardi.com.br"
            If (file.Name = "cab.pdf") Then var_email_destinatario = "vendascpp@grupowgsbrasil.com.br; jorgekassis@terra.com.br"
            If (file.Name = "germinare.pdf") Then var_email_destinatario = "assessoriacomercial@germinareagro.com.br; assessoriacomercial2@germinareagro.com.br; consultoria1@germinareagro.com.br"
            If (file.Name = "global.pdf") Then var_email_destinatario = "fabiana_perdoes@yahoo.com.br"
            If (file.Name = "jpa.pdf") Then var_email_destinatario = "maick@grupojpa.com.br"
            If (file.Name = "hs.pdf") Then var_email_destinatario = "paulo@hsassessorias.com.br"
            If (file.Name = "casa do campo.pdf") Then var_email_destinatario = "casadocampo@msn.com"
            If (file.Name = "sr agro.pdf") Then var_email_destinatario = "ricardo@sragronegocio.com.br; comercial@sragronegocio.com.br;"
            
            var_email_assunto = Format(Date, "yyyy-mm-dd") & " Saldo " & file.Name
            
            Set objeto_outlook = CreateObject("Outlook.Application")
            Set Email = objeto_outlook.createitem(0)
            
            Email.display
            Email.to = var_email_destinatario
            Email.Subject = var_email_assunto
            Email.Attachments.Add (var_path_folder & "\" & file.Name)
            ' Ajustar para não salvar o e-mail
            'Email.send
            'GoTo saida_de_emergencia
        End If
    Next

saida_de_emergencia:
End Sub


Private Sub enviar_email()
    Set objeto_outlook = CreateObject("Outlook.Application")
    Set Email = objeto_outlook.createitem(0)
    
    Email.display
    Email.to = ""
    Email.Subject = "Relatório de Vendas"
    Email.Attachments.Add ("")
    'Email.send
End Sub

Private Function ListaArquivos(ByVal Caminho As String) As String()
    'Atenção: Faça referência à biblioteca Micrsoft Scripting Runtime
    Dim FSO As New FileSystemObject
    Dim result() As String
    Dim Pasta As folder
    Dim Arquivo As file
    Dim Indice As Long


    ReDim result(0) As String
    If FSO.FolderExists(Caminho) Then
        Set Pasta = FSO.getfolder(Caminho)

        For Each Arquivo In Pasta.Files
            Indice = IIf(result(0) = "", 0, Indice + 1)
            ReDim Preserve result(Indice) As String
            result(Indice) = Arquivo.Name
        Next
    End If

    ListaArquivos = result
ErrHandler:
    Set FSO = Nothing
    Set Pasta = Nothing
    Set Arquivo = Nothing
End Function

Private Sub ListaArquvos()
    Dim arquivos() As String
    Dim lCtr As Long
    arquivos = ListaArquivos("C:\Users\513130\Desktop\saldos")
    For lCtr = 0 To UBound(arquivos)
      Debug.Print arquivos(lCtr)
    Next
End Sub




Private Sub original_enviar_email()
'https://www.hashtagtreinamentos.com/como-enviar-e-mail-pelo-excel
    Set objeto_outlook = CreateObject("Outlook.Application")
    Set Email = objeto_outlook.createitem(0)
    Email.display
    Email.to = Cells(2, 1).Value
    Email.cc = Cells(3, 1).Value
    Email.bcc = "diego@gmail.com"
    Email.Subject = "Relatório de Vendas"
    texto1 = "Fala " & Cells(2, 2).Value & "!<br><br>Dá uma olhada nessa imagem e nessa tabela que separei para você!<br><br>"
    Email.htmlbody = texto1 & "<img src='C:UsersdamorOneDriveHashtag (1)OnlineConteúdosPlanilhas2020VBA11-14 - Enviar E-mail pelo VBATabela.png'>" _
    & "<br><br>" _
    & RangetoHTML(Range("A5:C11")) _
    & Email.htmlbody
    Email.Attachments.Add ("C:UsersdamorOneDriveHashtag (1)OnlineConteúdosPlanilhas2020VBA11-14 - Enviar E-mail pelo VBATabela.png")
    Email.send
End Sub














'script em powershell |------------------------------------------------------

'So our finished script creates a COM object to communicate with Outlook, creates a MailItem Outlook object, sends a mail message, and quits. (Remember, '#' is a comment and is ignored by Powershell.)

'create COM object named Outlook
'$Outlook = New-Object -ComObject Outlook.Application

'create Outlook MailItem named Mail using CreateItem() method
'$Mail = $Outlook.CreateItem(0)

'add properties as desired
'$Mail.To = recipient@test.com
'$Mail.Subject = subject
'$Mail.Body = testing

'send Message
'$Mail.Send()

'quit and cleanup
'$Outlook.Quit() [System.Runtime.Interopservices.Marshal]::ReleaseComObject($Outlook) | Out-Null

'Powershell lets us send mail via Outlook with a few lines of code.
'The same methods and properties are valid for a language such as VBA, so you can also write a short script to (for example) send mail from Excel using Outlook.

'Pasta onde ficarão os arquivos
' C:\Users\513130\Desktop\saldos

'barretos - transportes@agrodinardi.com.br
'cab - vendascpp@grupowgsbrasil.com.br; jorgekassis@terra.com.br
'germinare - assessoriacomercial@germinareagro.com.br; assessoriacomercial2@germinareagro.com.br; consultoria1@germinareagro.com.br
'global - fabiana_perdoes@yahoo.com.br
'jpa - maick@grupojpa.com.br
'hs - paulo@hsassessorias.com.br
'
'
