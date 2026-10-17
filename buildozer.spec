[app]

title = ChemLab Calculator
package.name = chemlabcalculator
package.domain = org.chemlab

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

requirements = python3==3.11.5,hostpython3==3.11.5,kivy==2.3.0

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 24
android.ndk_api = 24
android.archs = arm64-v8a
android.accept_sdk_license = True
android.build_tools_version = 33.0.2
android.allow_backup = False

[buildozer]

log_level = 2
warn_on_root = 1
