[app]

title = ChemLab Calculator
package.name = chemlabcalculator
package.domain = org.chemlab

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0
head -2 .github/workflows/build.yml
head -1 buildozer.spec

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 23
android.archs = arm64-v8a
android.accept_sdk_license = True
android.build_tools_version = 33.0.2
android.allow_backup = False

[buildozer]

log_level = 2
warn_on_root = 1
