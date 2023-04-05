#Kenny Barcena 009661626
Function ADstuff
{
    #Create AD OU
    $ADRoot = "DC=consultingfirm,DC=com"
    $OUname = "finance"
    New-ADOrganizationalUnit -Path $ADRoot -Name $OUname -ProtectedFromAccidentalDeletion $False

    #import csv into OU
    $NewADUsers = Import-Csv -Path $PSScriptRoot\financePersonnel.csv
    ForEach ($ADUser in $NewADUsers) {
        $First = $ADUser.First_Name
        $Last = $ADUser.Last_Name
        $DisplayName = $First + " " + $Last
        $PSCode = $ADUser.PostalCode
        $Office = $ADUser.OfficePhone
        $Mobile = $ADuser.MobilePhone

        New-ADUser -Name $DisplayName `
                   -GivenName $First `
                   -Surname $Last `
                   -DisplayName $DisplayName `
                   -PostalCode $PSCode `
                   -OfficePhone $Office `
                   -MobilePhone $Mobile `
                   -Path "OU=finance,DC=consultingfirm,DC=com"
    }
    

       
        
    }


Function SQLstuff
{
    #import SqlServer Module
    if (Get-Module -Name sqlps) {Remove-Module -Name sqlps}
    Import-Module -Name SqlServer

    #create database
    $dbname = "ClientDB"
    $instancename = "SRV19-PRIMARY\SQLEXPRESS"
    $objref = New-Object -TypeName Microsoft.SqlServer.Management.Smo.Server -ArgumentList $instancename
    $dbref = New-Object -TypeName Microsoft.SqlServer.Management.Smo.Database -ArgumentList $objref, $dbname
    $dbref.Create()

    #import CSV file into new table

    Invoke-Sqlcmd -ServerInstance $instancename -Database $dbname -InputFile $PSScriptRoot\Client_A_Contacts.sql 
    $Insert = "INSERT INTO [$dbname].[dbo].[Client_A_Contacts] ([first_name],[Last_Name],[City],[County],[Zip],[OfficePhone],[MobilePhone])"
    $Newleads = Import-Csv $PSScriptRoot\NewClientData.csv

    ForEach ($newlead in $Newleads)
    {
        $Values = "VALUES ( `
                          '$($newlead.first_name)', `
                          '$($newlead.last_name)', `
                          '$($newlead.city)', `
                          '$($newlead.county)', `
                          '$($newlead.zip)', `
                          '$($newlead.officePhone)', `
                          '$($newlead.mobilePhone)')"
                          
        $query = $Insert + $Values
        Invoke-Sqlcmd -Database $dbname -ServerInstance $instancename -Query $query
     }



}
try {
    ADstuff
    SQLstuff
}
catch [System.OutOfMemoryException] {
    Write_Host "System out of memory"
}