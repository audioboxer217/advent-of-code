$planned_course = Get-Content -Path 'input.txt'

function forward {
  param (
    $position,
    $amount
  )
  $position['horizontal'] += $amount
  $depth_movement = $amount * $position['aim']
  $position['depth'] += $depth_movement
  return $position
}

function down {
  param (
    $position,
    $amount
  )
  $position['aim'] += $amount
  return $position
}

function up {
  param (
    $position,
    $amount
  )
  $position['aim'] -= $amount
  return $position
}


$position = @{
  horizontal =  [int]0
  depth =  [int]0
  aim = [int]0
}
foreach ($movement in $planned_course) {
  $direction = $($movement -split ' ')[0]
  $amount = [int]$($movement -split ' ')[1]

  $position = & (Get-ChildItem "Function:$direction") -position $position -amount $amount 
}

$result = $position['horizontal'] * $position['depth']
Write-Output $result