Sub StockData()

Dim Ticker As String
Dim Volume As Double


lr = Cells(Rows.Count, 1).End(xlUp).Row

Dim i As Long
Dim change As Single
Dim j As Integer
Dim start As Long
Dim rowNo As Integer
Dim perchange As Single
Dim days As Integer
Dim dailychange As Single
Dim avgchange As Single

Dim SummaryTableRow As Integer
SummaryTableRow = 2
change = 0
perchange = 0
avgchange = 0
strt = 2
dailychange = 0
Volume = 0

For i = 2 To lr

    If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
        Ticker = Cells(i, 1).Value
        Volume = Volume + Cells(i, 7).Value
        
        change = (Cells(i, 6) - Cells(strt, 3))
       
        If Cells(strt, 3) = 0 Then
            Cells(strt, 3).Value = Null
        Else
            perchange = Round((change / Cells(strt, 3) * 100), 2)
        End If
        
        dailychange = dailychange + (Cells(i, 4) - Cells(i, 5))
        
        days = (i - strt) + 1
        
        If days = 0 Then
            avgchange = 0
        
        Else
            avgchange = dailychange / days
        End If
        
        Sheets("output").Range("A1").Value = "Ticker"
        Sheets("output").Range("A" & SummaryTableRow).Value = Ticker
        
        Sheets("output").Range("B1").Value = "Total Change"
        Sheets("output").Range("B" & SummaryTableRow).Value = change
        
        Sheets("output").Range("C1").Value = "% of Change"
        Sheets("output").Range("C" & SummaryTableRow).Value = perchange
        
        Sheets("output").Range("D1").Value = "Avg.Daily Change"
        Sheets("output").Range("D" & SummaryTableRow).Value = avgchange
               
        Sheets("output").Range("E1").Value = "Total Volume"
        Sheets("output").Range("E" & SummaryTableRow).Value = Volume
    
      strt = i + 1
      SummaryTableRow = SummaryTableRow + 1
      
      Volume = 0
      
         
    Else
        
        Volume = Volume + Cells(i, 7).Value
                        
    End If
      
         
Next i
        
End Sub



Sub Greatest()

Dim PIncrease As Long
Dim PDecrease As Long

glr = Cells(Rows.Count, 1).End(xlUp).Row

Sheets("output").Range("J1").Value = "Ticker"
Sheets("output").Range("I1").Value = "Value"
Sheets("output").Range("H2").Value = "Greatest % Increase"
Sheets("output").Range("H3").Value = "Greatest % Decrease"
Sheets("output").Range("H4").Value = "Greatest Total Volume"

PIncrease = WorksheetFunction.Max(Range("C2:C4000"))
Sheets("output").Cells(2, 9).Value = PIncrease

PDecrease = WorksheetFunction.Min(Range("C2:C4000"))
Sheets("output").Cells(3, 9).Value = PDecrease

Volume = WorksheetFunction.Max(Range("E2:E4000"))
Sheets("output").Cells(4, 9).Value = Volume


For k = 2 To glr

If Volume = Cells(k, 5) Then
    Sheets("output").Range("J4").Value = Sheets("output").Cells(k, 1)
End If

Next k

End Sub

Sub PIcrease()

Dim PIncrease As Long

PIncrease = WorksheetFunction.Max(Range("C2:C4000"))
Cells(2, 9).Value = PIncrease

pclr = Cells(Rows.Count, 1).End(xlUp).Row

For m = 2 To pclr

If PIncrease = Cells(m, 3) Then
    Sheets("output").Range("J2").Value = Cells(m, 1)
End If

Next m

End Sub

Sub PDcrease()

Dim PDecrease As Long

PDecrease = WorksheetFunction.Min(Range("C2:C4000"))
Cells(3, 9).Value = PDecrease

pdlr = Cells(Rows.Count, 1).End(xlUp).Row

For n = 2 To pdlr

If PDecrease = Cells(n, 3) Then
    Sheets("output").Range("J3").Value = Cells(n, 1)
    Sheets("output").Range("I3").NumberFormat = "0.00%"
End If

Next n
End Sub

Sub Formatting()

flr = Cells(Rows.Count, 1).End(xlUp).Row

  For j = 2 To flr
         If Sheets("output").Cells(j, 3).Value >= 0 Then
        '4 = Green, 3 = Red
            Sheets("output").Cells(j, 3).Interior.ColorIndex = 4
          Else
            Sheets("output").Cells(j, 3).Interior.ColorIndex = 3
         End If
         
         Sheets("output").Range("B2:B4000").NumberFormat = "0.00"
         Sheets("output").Range("C2:C4000").NumberFormat = "0.00%"
         Sheets("output").Range("D2:D4000").NumberFormat = "0.00"
         Sheets("output").Range("E2:E4000").NumberFormat = "000,000"
        

      
 Next j

 
End Sub



