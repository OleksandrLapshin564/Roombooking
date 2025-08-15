$baseUrl = "http://localhost:8001/api"
$endpoints = @("rooms", "categories", "bookings")

foreach ($endpoint in $endpoints) {
    $url = "$baseUrl/$endpoint/"
    Write-Host "`n===== Testing endpoint: $url =====`n"
    try {
        $response = Invoke-RestMethod -Uri $url -Headers @{ "Accept" = "application/json" }
        $response | ConvertTo-Json -Depth 5
    } catch {
        Write-Host "Cannot fetch $endpoint endpoint. It may require authentication or the server did not respond." -ForegroundColor Yellow
    }
}
