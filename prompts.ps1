#Kenny Barcena 009661626

#try catch exception handling
try {
    #set up while loop, executes until user inputs 5
    while ($userinput -ne 5) {
        #prompt user input
        $userinput = Read-Host "Provide input 1-5"
        #switch statement to run code for input provided
        switch ($userinput) {
            #retrieves .log files and stores it in a new txt file named "DailyLog.txt"
            1 {Write-Host "Retrieving files and creating Daily logs..."
               "TIMESTAMP: " + (Get-Date) | Out-File -FilePath $PSScriptRoot\DailyLog.txt -Append
               Get-ChildItem -Path $PSScriptRoot -Filter *.log | Out-File -FilePath DailyLog.txt -Append
            }

            #retrieves all files and stores it alphabetically in a new file named "C916contents.txt"
            2 {Write-Host "Retrieving files and creating txt file..."
               Get-ChildItem -Path $PSScriptRoot | Sort-Object Name | Format-Table -AutoSize -Wrap | Out-File -FilePath C916contents.txt
            }

            #displays CPU and Memory usage, 4 times, 5 seconds apart
            3 {Write-Host "Calculating CPU and Memory usage..."
               $myStringArray = "\Processor(_Total)\% Processor Time", "\Memory\Committed Bytes"
               Get-Counter -Counter $myStringArray
            }

            #retrieves running processes, sorts them by size, then outputs the list in grid view
            4 {Write-Host "Retrieving running processes..."
               Get-Process | Select-Object ID, Name, VM | Sort-Object VM | Out-Gridview
            }
    }
}
}
catch [System.OutOfMemoryException] {
    {Write-Host "System out of memory"}
}