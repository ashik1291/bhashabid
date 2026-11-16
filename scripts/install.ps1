# Bhashabid (ভাষাবিদ) — Zero-Dependency Universal Skill & IDE Installer (Windows PowerShell)
# Works 100% out of the box with or without Python installed!
[CmdletBinding()]
param(
    [string]$Target = "all",
    [string]$Workspace = ""
)

$ErrorActionPreference = "Stop"

Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "BHASHABID (ভাষাবিদ) — UNIVERSAL SKILL & IDE INSTALLER" -ForegroundColor Cyan
Write-Host "=================================================================" -ForegroundColor Cyan

$HomeDir = if ($env:USERPROFILE) { $env:USERPROFILE } else { [Environment]::GetFolderPath("UserProfile") }
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path -ErrorAction SilentlyContinue
$RepoRoot = if ($ScriptDir) { Split-Path -Parent $ScriptDir } else { $null }

$GithubRawBase = "https://raw.githubusercontent.com/ashik1291/bhashabid/main"

# 1. Determine Source of Skill and References
$IsLocal = ($RepoRoot -and (Test-Path "$RepoRoot/skills/bangla-expert/SKILL.md"))

$TempDir = $null
if (-not $IsLocal) {
    Write-Host "→ Fetching latest Bhashabid skill files from GitHub..." -ForegroundColor Yellow
    $TempDir = Join-Path ([System.IO.Path]::GetTempPath()) "bhashabid_install_$([Guid]::NewGuid().ToString('N'))"
    New-Item -ItemType Directory -Path "$TempDir/references" -Force | Out-Null

    # Download core skill
    Invoke-WebRequest -Uri "$GithubRawBase/skills/bangla-expert/SKILL.md" -OutFile "$TempDir/SKILL.md" -UseBasicParsing
    
    # Download cursor rule
    Invoke-WebRequest -Uri "$GithubRawBase/adapters/cursor/.cursorrules" -OutFile "$TempDir/.cursorrules" -UseBasicParsing

    # Reference guides
    $References = @(
        "academic_legal_medical.md",
        "constitutional_writs.md",
        "creative_writing.md",
        "ecommerce_fintech_civic.md",
        "grammar_registers.md",
        "journalism_domains.md",
        "numerals.md",
        "official_letters.md",
        "orthography.md"
    )
    foreach ($ref in $References) {
        Invoke-WebRequest -Uri "$GithubRawBase/skills/bangla-expert/references/$ref" -OutFile "$TempDir/references/$ref" -UseBasicParsing
    }
    $SourceSkillDir = $TempDir
    $SourceCursorRule = "$TempDir/.cursorrules"
} else {
    Write-Host "→ Using local Bhashabid repository source..." -ForegroundColor Green
    $SourceSkillDir = "$RepoRoot/skills/bangla-expert"
    $SourceCursorRule = "$RepoRoot/adapters/cursor/.cursorrules"
}

# 2. Install to Cursor
if ($Target -in @("cursor", "all")) {
    $CursorRulesDir = "$HomeDir/.cursor/rules"
    $CursorRefsDir = "$HomeDir/.cursor/bangla-references"
    New-Item -ItemType Directory -Path $CursorRulesDir -Force | Out-Null
    New-Item -ItemType Directory -Path $CursorRefsDir -Force | Out-Null

    Copy-Item -Path $SourceCursorRule -Destination "$CursorRulesDir/bangla-expert.mdc" -Force
    Copy-Item -Path "$SourceSkillDir/references/*" -Destination $CursorRefsDir -Recurse -Force
    Write-Host "[✓] Cursor IDE:" -ForegroundColor Green
    Write-Host "    • Global Rule: $CursorRulesDir/bangla-expert.mdc"
    Write-Host "    • References:  $CursorRefsDir (9 domain guides)"
}

# 3. Install to Antigravity
if ($Target -in @("antigravity", "all")) {
    $AgDest1 = "$HomeDir/.gemini/config/skills/bhashabid"
    $AgDest2 = "$HomeDir/.gemini/antigravity/skills/bangla-expert"
    
    New-Item -ItemType Directory -Path "$AgDest1/references" -Force | Out-Null
    New-Item -ItemType Directory -Path "$AgDest2/references" -Force | Out-Null

    Copy-Item -Path "$SourceSkillDir/SKILL.md" -Destination "$AgDest1/SKILL.md" -Force
    Copy-Item -Path "$SourceSkillDir/references/*" -Destination "$AgDest1/references" -Recurse -Force

    Copy-Item -Path "$SourceSkillDir/SKILL.md" -Destination "$AgDest2/SKILL.md" -Force
    Copy-Item -Path "$SourceSkillDir/references/*" -Destination "$AgDest2/references" -Recurse -Force

    Write-Host "[✓] Google Antigravity:" -ForegroundColor Green
    Write-Host "    • Global Skill: $AgDest1"
    Write-Host "    • Legacy Path:  $AgDest2"
}

# 4. Install to Claude
if ($Target -in @("claude", "all")) {
    $ClaudeDest = "$HomeDir/.claude/skills/bangla-expert"
    New-Item -ItemType Directory -Path "$ClaudeDest/references" -Force | Out-Null

    Copy-Item -Path "$SourceSkillDir/SKILL.md" -Destination "$ClaudeDest/SKILL.md" -Force
    Copy-Item -Path "$SourceSkillDir/references/*" -Destination "$ClaudeDest/references" -Recurse -Force
    Write-Host "[✓] Claude Desktop / Code:" -ForegroundColor Green
    Write-Host "    • Global Skill: $ClaudeDest"
}

# 5. Optional Workspace Directory
if ($Workspace) {
    $WsRulesDir = "$Workspace/.cursor/rules"
    $WsRefsDir = "$Workspace/.cursor/bangla-references"
    New-Item -ItemType Directory -Path $WsRulesDir -Force | Out-Null
    New-Item -ItemType Directory -Path $WsRefsDir -Force | Out-Null

    Copy-Item -Path $SourceCursorRule -Destination "$Workspace/.cursorrules" -Force
    Copy-Item -Path $SourceCursorRule -Destination "$WsRulesDir/bangla-expert.mdc" -Force
    Copy-Item -Path "$SourceSkillDir/references/*" -Destination $WsRefsDir -Recurse -Force
    Write-Host "[✓] Workspace Target ($Workspace):" -ForegroundColor Green
    Write-Host "    • Local Rule: $Workspace/.cursorrules"
}

# 6. Python & MCP Environment Check
Write-Host ""
Write-Host "--- Environment & Tool Capability Status ---" -ForegroundColor Cyan
$PythonCmd = Get-Command python -ErrorAction SilentlyContinue
if ($PythonCmd) {
    $PythonExe = $PythonCmd.Source
    Write-Host "[✓] Python Detected: $PythonExe" -ForegroundColor Green
    
    # Configure MCP if possible
    try {
        $McpEntry = @{
            command = $PythonExe.Replace("\", "/")
            args = @("-m", "bhashabid.mcp")
        }

        # Helper for UTF-8 without BOM
        $utf8NoBom = New-Object System.Text.UTF8Encoding($false)

        # Cursor MCP
        $CursorMcp = "$HomeDir/.cursor/mcp.json"
        $CursorJson = if (Test-Path $CursorMcp) { Get-Content $CursorMcp -Raw | ConvertFrom-Json } else { [PSCustomObject]@{ mcpServers = [PSCustomObject]@{} } }
        if (-not $CursorJson.mcpServers) { $CursorJson | Add-Member -MemberType NoteProperty -Name "mcpServers" -Value ([PSCustomObject]@{}) }
        $CursorJson.mcpServers | Add-Member -MemberType NoteProperty -Name "bhashabid" -Value $McpEntry -Force
        $cursorJsonStr = $CursorJson | ConvertTo-Json -Depth 5
        [System.IO.File]::WriteAllText($CursorMcp, $cursorJsonStr, $utf8NoBom)
        Write-Host "    • Cursor MCP Server configured: $CursorMcp" -ForegroundColor DarkGray

        # Antigravity MCP
        foreach ($agMcpPath in @("$HomeDir/.gemini/config/mcp_config.json", "$HomeDir/.gemini/antigravity/mcp_servers.json")) {
            New-Item -ItemType Directory -Path (Split-Path -Parent $agMcpPath) -Force | Out-Null
            $AgJson = if (Test-Path $agMcpPath) { 
                $content = Get-Content $agMcpPath -Raw
                if ($content.Trim()) { $content | ConvertFrom-Json } else { [PSCustomObject]@{ mcpServers = [PSCustomObject]@{} } }
            } else { 
                [PSCustomObject]@{ mcpServers = [PSCustomObject]@{} } 
            }
            if (-not $AgJson.mcpServers) { $AgJson | Add-Member -MemberType NoteProperty -Name "mcpServers" -Value ([PSCustomObject]@{}) }
            $AgJson.mcpServers | Add-Member -MemberType NoteProperty -Name "bhashabid" -Value $McpEntry -Force
            $agJsonStr = $AgJson | ConvertTo-Json -Depth 5
            [System.IO.File]::WriteAllText($agMcpPath, $agJsonStr, $utf8NoBom)
            Write-Host "    • Antigravity MCP configured: $agMcpPath" -ForegroundColor DarkGray
        }
    } catch {
        Write-Host "    Notice: MCP configuration skipped: $($_.Exception.Message)" -ForegroundColor DarkGray
    }
} else {
    Write-Host "[!] Python Not Detected on this machine." -ForegroundColor Yellow
    Write-Host "    • Skill Mode: FULLY ACTIVE ✓ (AI directly applies Bangla Academy standards," -ForegroundColor Green
    Write-Host "      active voice, numeral words, and legal/deed templates inside your IDE)." -ForegroundColor Green
    Write-Host "    • If you later want zero-token local CLI tools (e.g. bhashabid number), simply" -ForegroundColor DarkGray
    Write-Host "      install Python 3.10+ and run: pip install bhashabid" -ForegroundColor DarkGray
}

# Cleanup temp files if created
if ($TempDir -and (Test-Path $TempDir)) {
    Remove-Item -Path $TempDir -Recurse -Force -ErrorAction SilentlyContinue
}

Write-Host ""
Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "✓ BHASHABID INSTALLATION COMPLETE! READY TO USE." -ForegroundColor Green
Write-Host "=================================================================" -ForegroundColor Cyan
