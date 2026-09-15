# apple-pmu

Dump Apple PMU counter definitions from `/usr/share/kpep` in macOS. Also in `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport/*/DeveloperDiskImage.dmg`

Also see [cyyself/m1-pmu-gen](https://github.com/cyyself/m1-pmu-gen) to see how to integrate the counters into perf.

Output of `sysctl -nx hw.cputype hw.cpusubtype hw.cpufamily`:

- A8 Typhoon: cpu_100000c_1_2c91a47e.md
- A12(H11) Vortex+Tempest: cpu_100000c_2_7d34b9f.md
- A13(H12) Lightning+Thunder: cpu_100000c_2_462504d2.md
- A14/M1(H13) Firestorm+Icestorm: cpu_100000c_2_1b588bb3.md
- A15/M2(H14) Avalanche+Blizzard: cpu_100000c_2_da33d83d.md
- A16(H15) Everest+Sawtooth: cpu_100000c_2_8765edea.md
- M3 (H15 Ibiza): cpu_100000c_2_fa33415e.md
- A17 Pro (H15 Coll): cpu_100000c_2_2876f5b5.md
- M3 Pro (H15 Lobos): cpu_100000c_2_5f4dea93.md
- M3 Max (H15 Palma): cpu_100000c_2_72015832.md
- M4 (H16G Donan): cpu_100000c_2_6f5129ac.md
- M4 Pro (H16S Brava Chop) / M4 Max (H16C Brava): cpu_100000c_2_17d5b93a.md
- A18 (H17A Tupai): cpu_100000c_2_204526d0.md
- A18 Pro (H17P Tahiti): cpu_100000c_2_75d4acb9.md
- M5 (H17G Hidra): cpu_100000c_2_1d5a87e8.md
- M5 Pro (H17S Sotra S) / M5 Max: cpu_100000c_2_f76c5b1a.md
- A19 (H18A Tilos): cpu_100000c_2_1d7a72b.md
- A19 Pro (H18P Thera): cpu_100000c_2_ab345f09.md
- M6 (H18G Komodo): cpu_100000c_2_6d0ccb0c.md, cpu_100000c_c_6d0ccb0c.md
- A20 (H19P Borneo): cpu_100000c_2_7db56df1.md, cpu_100000c_c_7db56df1.md
- M12 Nevis: cpu_100000c_2_37652b0c.md, cpu_100000c_c_37652b0c.md
- cpu_100000c_2_8d264dca.md, cpu_100000c_c_8d264dca.md

From PMU:

a14 ~ a15 -> a16 = as1 = as2 = as3 -> as4 = as4-1 = as4-2 -> as5 = as5-1 = as5-2

PMU evolution across generations:

- **as4**: Add ARM architectural events (`ARM_BR_MIS_PRED`, `ARM_L1D_CACHE`, `ARM_STALL`, etc.), SME engine counters (`INST_SME_ENGINE_*`)
- **as5**: Add load data source tracking (`LD_SRC_*`), PL2 cache events, additional ARM arch events

See also: 

- https://gist.github.com/ibireme/173517c208c7dc333ba962c1f0d67d12
- https://github.com/Tencent/ncnn/blob/master/src/cpu.cpp
- https://github.com/Homebrew/brew/blob/master/Library/Homebrew/extend/os/mac/hardware/cpu.rb
- https://en.wikipedia.org/wiki/List_of_Apple_codenames
- https://github.com/xybp888/iOS-SDKs/blob/d7f1be9f5b79cffcfb547bbd930f92ec0fc35038/iPhoneOS17.5.sdk/usr/include/mach/machine.h#L365
- https://theapplewiki.com/wiki/User:Ilikeiphone123/Playground/Codenames
- https://github.com/Homebrew/brew/blob/main/Library/Homebrew/extend/os/mac/hardware/cpu/hardware.rb
- https://asahilinux.org/docs/hw/soc/soc-codenames/
- /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/machine.h
- /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/Frameworks/Kernel.framework/Versions/A/Headers/arm/cpuid.h
- /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/mach/machine.h
- /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/System/Library/Frameworks/Kernel.framework/Versions/A/Headers/arm/cpuid.h

