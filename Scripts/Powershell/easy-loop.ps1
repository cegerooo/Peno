$count = 0;
while ($count -lt 5)
{

if ($count -eq 1)
 {
 Write-Output "Skip $count";
 $count++;
 continue;
 }

 $count;
 $count++;

}


$words = "powershell","offensive","security","hacker","scripting","forensics","pentest"
foreach ($word in $words)
{
  if ($word -eq "hacker")
  {
    break
  }
  Write-Output $word
}
