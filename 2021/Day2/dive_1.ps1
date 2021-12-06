$planned_course = Get-Content -Path 'input.txt'

function forward {
  param (
    $position,
    $amount
  )
  $position['horizontal'] += $amount
  return $position
}

function down {
  param (
    $position,
    $amount
  )
  $position['depth'] += $amount
  return $position
}

function up {
  param (
    $position,
    $amount
  )
  $position['depth'] -= $amount
  return $position
}

$position = @{
  horizontal =  0
  depth =  0
}
foreach ($movement in $planned_course) {
  $direction = $($movement -split ' ')[0]
  $amount = $($movement -split ' ')[1]

  $position = & (Get-ChildItem "Function:$direction") -position $position -amount $amount 
}

$result = $position['horizontal'] * $position['depth']
Write-Output $result