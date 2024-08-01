# apple-pmu

Dump Apple PMU counter definitions from `/usr/share/kpep` in macOS. Also in `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport/*/DeveloperDiskImage.dmg`

Also see [cyyself/m1-pmu-gen](https://github.com/cyyself/m1-pmu-gen) to see how to integrate the counters into perf.

See also: https://gist.github.com/ibireme/173517c208c7dc333ba962c1f0d67d12, https://github.com/Tencent/ncnn/blob/master/src/cpu.cpp https://github.com/Homebrew/brew/blob/master/Library/Homebrew/extend/os/mac/hardware/cpu.rb https://en.wikipedia.org/wiki/List_of_Apple_codenames https://github.com/xybp888/iOS-SDKs/blob/d7f1be9f5b79cffcfb547bbd930f92ec0fc35038/iPhoneOS17.5.sdk/usr/include/mach/machine.h#L365 /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/mach/machine.h

Output of `sysctl -nx hw.cputype hw.cpusubtype hw.cpufamily`:

1. A14/M1 Firestorm+Icestorm: 100000c_2_1b588bb3 -> a14.md
2. A15/M2 Avalanche+Blizzard: 100000c_2_da33d83d -> a15.md
3. A16 Everest+Sawtooth: 100000c_2_8765edea -> a16.md
4. A17 (Coll): 100000c_2_2876f5b5 -> as2.md
5. M3 (Ibiza): 100000c_2_fa33415e -> as1.md
6. M3 Pro (Lobos): 100000c_2_5f4dea93 -> as3.md
7. M3 Max (Palma): 100000c_2_72015832 -> as3.md
8. M4 (Donan): 100000c_2_6f5129ac -> as4.md
