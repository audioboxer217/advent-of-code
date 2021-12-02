$depth_readings = Get-Content -Path 'input.txt'

$increases = 0
for ($i = 0; $i -lt $depth_readings.length; $i++) {
  $curr_window = [int]$depth_readings[$i] + [int]$depth_readings[$i-1] + [int]$depth_readings[$i-2]
  $prev_window = [int]$depth_readings[$i-1] + [int]$depth_readings[$i-2] + [int]$depth_readings[$i-3]
  if ($curr_window -gt $prev_window) {
    $increases += 1
  }
}

Write-Output $increases