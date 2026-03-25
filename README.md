# apple-pmu

Dump Apple PMU counter definitions from `/usr/share/kpep` in macOS. Also in `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport/*/DeveloperDiskImage.dmg`

Also see [cyyself/m1-pmu-gen](https://github.com/cyyself/m1-pmu-gen) to see how to integrate the counters into perf.

See also: https://gist.github.com/ibireme/173517c208c7dc333ba962c1f0d67d12, https://github.com/Tencent/ncnn/blob/master/src/cpu.cpp https://github.com/Homebrew/brew/blob/master/Library/Homebrew/extend/os/mac/hardware/cpu.rb https://en.wikipedia.org/wiki/List_of_Apple_codenames https://github.com/xybp888/iOS-SDKs/blob/d7f1be9f5b79cffcfb547bbd930f92ec0fc35038/iPhoneOS17.5.sdk/usr/include/mach/machine.h#L365 /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/machine.h /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/mach/machine.h /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/Frameworks/Kernel.framework/Versions/A/Headers/arm/cpuid.h

Output of `sysctl -nx hw.cputype hw.cpusubtype hw.cpufamily`:

- A7 Cyclone: cpu_100000c_1_37a09642.md -> a7.md
- A8 Typhoon: cpu_100000c_1_2c91a47e.md -> a8.md
- A9 Twister: cpu_100000c_1_92fb37c8.md -> a9.md
- A10 Hurricane: cpu_100000c_1_67ceee93.md -> a10.md
- A11(H10) Monsoon+Mistral: cpu_100000c_1_e81e7ef6.md -> a11.md
- A12(H11) Vortex+Tempest: cpu_100000c_2_7d34b9f.md -> a12.md
- A13(H12) Lightning+Thunder: cpu_100000c_2_462504d2.md -> a13.md
- A14/M1(H13) Firestorm+Icestorm: cpu_100000c_2_1b588bb3.md -> a14.md
- A15/M2(H14) Avalanche+Blizzard: cpu_100000c_2_da33d83d.md -> a15.md
- A16(H15) Everest+Sawtooth: cpu_100000c_2_8765edea.md -> a16.md
- M3 (H15 Ibiza): cpu_100000c_2_fa33415e.md -> as1.md
- A17 Pro (H15 Coll): cpu_100000c_2_2876f5b5.md -> as2.md
- M3 Pro (H15 Lobos): cpu_100000c_2_5f4dea93.md -> as3.md
- M3 Max (H15 Palma): cpu_100000c_2_72015832.md -> as3.md
- M4 (H16G Donan): cpu_100000c_2_6f5129ac.md -> as4.md
- M4 Pro (H16S Brava Chop): cpu_100000c_2_17d5b93a.md -> as4-1.md
- M4 Max (H16C Brava): cpu_100000c_2_17d5b93a.md -> as4-1.md
- A18 (H17A Tupai): cpu_100000c_2_204526d0.md -> as4-2.md
- A18 Pro (H17P Tahiti): cpu_100000c_2_75d4acb9.md -> as4-2.md
- M5 (H17G Hidra): cpu_100000c_2_1d5a87e8.md -> as5.md
- cpu_100000c_2_da9d04c3.md -> as5-1.md
- Sotra: cpu_100000c_2_f76c5b1a.md -> as5-1.md
- A19 (H18A Tilos): cpu_100000c_2_1d7a72b.md -> as5-2.md
- A19 Pro (H18P Thera): cpu_100000c_2_ab345f09.md -> as5-2.md

From PMU:

a14 ~ a15 -> a16 = as1 = as2 = as3 -> as4 = as4-1 = as4-2 -> as5 = as5-1 = as5-2
