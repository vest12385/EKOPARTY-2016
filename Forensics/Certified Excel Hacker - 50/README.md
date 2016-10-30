# Certified Excel Hacker

**Points : 50**
**Solves : 169**

##Description:

	Can you wait for the answer?

	Hint
		Do not wait for it, it is already there :)

[Attachment](for50_ed4b8625b6be1bd0.zip)

## Write-up
Method 1
using [CALCULATOR.xlsm](CALCULATOR.xlsm), [crack.xlsm](crack.xlsm), [CALCULATOR.xls](CALCULATOR.xls) and [CALCULATOR_modify.xls](CALCULATOR_modify.xls)

Method 2
using [CALCULATOR.xlsm](CALCULATOR.xlsm), [CALCULATOR_modify.xlsm](CALCULATOR_modify.xlsm), [test.xlsm](test.xlsm), [CALCULATOR](CALCULATOR), and [test](test)
First need to crack the password, I refet [this](http://stackoverflow.com/questions/22663809/excel-vba-password-via-hex-editor) can bypass execl protect, then found the program source code, then covert VB code to [python script](calculate.py), I try many possible to generate flag using python script, but it didn't work.
![](http://i.imgur.com/jbwTEUp.jpg)
Finally, I found this execl have two sheet, but sheet2 is hidden, so change sheet2 Visible attribute to -1, then you can see the sheet, the flag is in sheet2.
![](http://i.imgur.com/VnPitPM.jpg)
The flag is `EKO{HIDDEN_SHEET_123}`