# apple-pmu

Dump Apple PMU counter definitions from `/usr/share/kpep` in macOS. Also in `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport/*/DeveloperDiskImage.dmg`

Also see [cyyself/m1-pmu-gen](https://github.com/cyyself/m1-pmu-gen) to see how to integrate the counters into perf.

Output of `sysctl -nx hw.cputype hw.cpusubtype hw.cpufamily`. The `cpu_<cputype>_<cpusubtype>_<cpufamily>.md` name comes from this tuple (`2` = `CPU_SUBTYPE_ARM64E`, `c` = `CPU_SUBTYPE_ARM64E_X1`).

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
- Unknown: cpu_100000c_2_8d264dca.md, cpu_100000c_c_8d264dca.md

Identical files (same counter set, different `hw.cpufamily`):

- M3 = M3 Pro = M3 Max = A16 = A17 Pro: cpu_100000c_2_8765edea.md = cpu_100000c_2_fa33415e.md = cpu_100000c_2_2876f5b5.md = cpu_100000c_2_5f4dea93.md = cpu_100000c_2_72015832.md
- M4 = M4 Pro = A18 = A18 Pro: cpu_100000c_2_6f5129ac.md = cpu_100000c_2_17d5b93a.md = cpu_100000c_2_204526d0.md = cpu_100000c_2_75d4acb9.md
- M5 = M5 Pro = A19 = A19 Pro: cpu_100000c_2_1d5a87e8.md = cpu_100000c_2_f76c5b1a.md = cpu_100000c_2_1d7a72b.md = cpu_100000c_2_ab345f09.md
- M12 = M6 = A20: cpu_100000c_2_37652b0c.md = cpu_100000c_2_6d0ccb0c.md = cpu_100000c_2_7db56df1.md = cpu_100000c_2_8d264dca.md = cpu_100000c_c_37652b0c.md = cpu_100000c_c_6d0ccb0c.md = cpu_100000c_c_7db56df1.md = cpu_100000c_c_8d264dca.md

PMU evolution across generations:

- **A12**: Add exclusive/atomic success/fail, barrier, demand L1I cache miss, non-temporal load/store, dispatch bubble/stall, retire and scheduler-empty events
- **A13**: Add `INTERRUPT_PENDING`, drop `INST_BRANCH_COND`
- **A14/M1**: Add TLB fill and table walk events (`L1D_TLB_FILL`, `L1I_TLB_FILL`, `LDST_XPG_UOP`, `MMU_TABLE_WALK_*`)
- **A15/M2**: Add `INST_SIMD_ALU_VEC`, drop `SCHEDULE_UOP`
- **A16/A17/M3**: Add decode/map/schedule events (`DECODE_UOP`, `MAP_UOP`, `MAP_DISPATCH_BUBBLE_IC/ITLB`, `SCHEDULE_UOP_ANY`, `LDST_UNIT_*_OLD_L1D_CACHE_MISS`), re-add `INST_BRANCH_COND`
- **A18/M4**: Add ARM architectural events (`ARM_BR_MIS_PRED`, `ARM_BR_PRED`, `ARM_L1D_CACHE*`, `ARM_STALL*`, etc.), SME engine counters (`INST_SME_ENGINE_*`, `LD_SME_*`, `ST_SME_*`, `LDST_SME_*`, `SME_ENGINE_*`, `MAP_*_SME_*`)
- **A19/M5**: Add `ARM_L1I_CACHE` / `ARM_MEM_ACCESS*` (including checked accesses), load data source tracking (`LD_SRC_*`), PL2 cache events (`PL2_CACHE_*`), MTE events (`LDST_MEM_ACCESS_CHECKED_X2K`, `LDST_OLDEST_MTE_TAG_CHECK_CYCLE`), more branch events (`INST_BRANCH_CALL_INDIR`, `BRANCH_BR_INDIR_MISPRED_NONSPEC`), `INST_MICROCODED` and more SME wait events
- **A20/M6**: Drop `LD_BLOCKED_BY_SME_LDST` / `ST_BARRIER_BLOCKED_BY_SME_LDST`, add `LD_SME_MEM_ORDER_VIOL_LD_NONSPEC` / `ST_SME_MEM_ORDER_VIOL_LD_NONSPEC`

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
