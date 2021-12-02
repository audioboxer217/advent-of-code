$depth_readings = Get-Content -Path 'input.txt'

$increases = 0
for ($i = 0; $i -lt $depth_readings.length; $i++) {
  if ($depth_readings[$i] -gt $depth_readings[$i-1]) {
    $increases += 1
  }
}

Write-Output $increases