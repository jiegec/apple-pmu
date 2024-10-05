# apple-pmu

Dump Apple PMU counter definitions from `/usr/share/kpep` in macOS. Also in `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport/*/DeveloperDiskImage.dmg`

Also see [cyyself/m1-pmu-gen](https://github.com/cyyself/m1-pmu-gen) to see how to integrate the counters into perf.

See also: https://gist.github.com/ibireme/173517c208c7dc333ba962c1f0d67d12, https://github.com/Tencent/ncnn/blob/master/src/cpu.cpp https://github.com/Homebrew/brew/blob/master/Library/Homebrew/extend/os/mac/hardware/cpu.rb https://en.wikipedia.org/wiki/List_of_Apple_codenames https://github.com/xybp888/iOS-SDKs/blob/d7f1be9f5b79cffcfb547bbd930f92ec0fc35038/iPhoneOS17.5.sdk/usr/include/mach/machine.h#L365 /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/machine.h /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/mach/machine.h /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/Frameworks/Kernel.framework/Versions/A/Headers/arm/cpuid.h

Output of `sysctl -nx hw.cputype hw.cpusubtype hw.cpufamily`:

- A7 Cyclone: cpu_100000c_1_37a09642.md -> a7.md
- A8 Typhoon: cpu_100000c_1_2c91a47e.md -> a8.md
- A9 Twister: cpu_100000c_1_92fb37c8.md -> a9.md
- A10 Hurricane: cpu_100000c_1_67ceee93.md -> a10.md
- A11(H10) Monsoon+Mistral: 100000c_1_e81e7ef6.md -> a11.md
- A12(H11) Vortex+Tempest: cpu_100000c_2_7d34b9f -> a12.md
- A13(H12) Lightning+Thunder: 100000c_2_462504d2 -> a13.md
- A14/M1(H13) Firestorm+Icestorm: 100000c_2_1b588bb3 -> a14.md
- A15/M2(H14) Avalanche+Blizzard: 100000c_2_da33d83d -> a15.md
- A16(H15) Everest+Sawtooth: 100000c_2_8765edea -> a16.md
- M3 (H15 Ibiza): 100000c_2_fa33415e -> as1.md
- A17 Pro (H15 Coll): 100000c_2_2876f5b5 -> as2.md
- M3 Pro (H15 Lobos): 100000c_2_5f4dea93 -> as3.md
- M3 Max (H15 Palma): 100000c_2_72015832 -> as3.md
- M4 (H16G Donan): 100000c_2_6f5129ac -> as4.md
- A18 (H17A Tupai): 100000c_2_204526d0
- A18 Pro (H17P Tahiti): 100000c_2_75d4acb9

From PMU:

a14 ~ a15 -> a16 = as1 = as2 = as3 -> as4
