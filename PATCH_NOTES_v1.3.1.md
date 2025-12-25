# Arikuri Mod - Patch Notes v1.3.1
**Release Date:** December 25, 2025  
**CK3 Compatibility:** 1.18.x  
**Patch Type:** Localization & Lore Refinement

---

## Overview

Version 1.3.1 delivers **critical lore refinements** to Aigl Chormana and Blouck cultures, aligning their government descriptions with established worldbuilding. These changes remove inconsistencies and strengthen cultural identity through more accurate philosophical and power structure descriptions.

---

## Changes This Patch

### 🏛️ Government Localization Updates

#### **Aigl Chormana Government** (Nomadic)
**Philosophy Change:** Religious Zealots → Opportunistic Scavengers

**Before:**
- Described as "militant faithful" united by "aggressive doctrines of unrelenting faith or warmonger zeal"
- Emphasized "religious conviction" and "same-faith unity"

**After:**
- Now portrayed as "opportunistic scavengers" with "cynical philosophy of survival and pragmatic opportunism"
- Raiders strike with "coordinated cunning and ruthless efficiency"
- United by "shared scavenger culture" rather than religious fervor

**Rationale:** Aigl Chormana are coastal scavengers who became inland warlords through pragmatic opportunism, not religious zeal. Their philosophy is cynical and survival-focused, making them cunning raiders rather than holy warriors.

---

#### **Blouck Tribal Government**
**Identity Change:** Ritualistic Trophy Hunters → Power-Driven Tribal Hierarchy

**Before:**
- Name: "Blouck Ritual Chiefdom"
- Adjective: "Ritualistic"
- Realm: "Trophy Confederation"
- Contract: "Trophy Oath"
- Vassal: "Trophy Chief"
- Description focused on trophy hunting, skull collecting, and "dark spirituality"

**After:**
- Name: "Blouck Tribal"
- Adjective: "Tribal" (clear government type)
- Realm: "Blouck Confederation"
- Contract: "Strength Pact"
- Vassal: "War Chief"
- Description emphasizes:
  - **Pack-like hierarchy:** "The strong lead, the weak are cast aside"
  - **Formalized combat:** "Strength must be demonstrated through formalized frontal confrontation and ritual combat"
  - **Honor & prestige:** "Earned through displays of physical prowess, courage in battle, and victory in ceremonial duels"
  - **Sanctioned violence:** "Challengers may face the leader in sanctioned combat, with murder being an accepted outcome"

**Rationale:** Blouck society operates like a pack or bandit hierarchy where leadership is proven through strength, not ritual. Rule is based on power, prestige, and physical dominance. The "Tribal" adjective clearly indicates government type (like Feudal, Clan, Nomadic).

---

## File Changes

### Modified Files
- `localization/english/government_l_english.yml`
  - Lines 1027-1035: Aigl Chormana government entries
  - Lines 1230-1238: Blouck tribal government entries

### Lines Changed
- **Total:** 18 localization entries updated
- **Aigl Chormana:** 9 entries (description rewritten)
- **Blouck:** 9 entries (name, adjective, realm, contract, vassal, description)

---

## Lore Consistency Improvements

### Aigl Chormana
✅ Removed religious zeal references (inconsistent with scavenger culture)  
✅ Emphasized opportunistic, cynical philosophy  
✅ Highlighted cunning and pragmatic survival tactics  
✅ Maintained aggressive raider identity without religious framing  

### Blouck
✅ Removed confusing "Ritualistic" adjective (now clearly "Tribal")  
✅ Eliminated trophy/skull collection focus  
✅ Established clear pack-like power hierarchy  
✅ Added formalized combat system with sanctioned murder  
✅ Emphasized honor, prestige, and physical prowess as leadership criteria  

---

## Previous Version (1.3.0) Summary

For full 1.3.0 features, see [CHANGELOG.md](CHANGELOG.md) and [RELEASE.md](RELEASE.md)

### Major 1.3.0 Features
- 🎵 **16 Original Soundtrack Tracks** with dynamic triggers
- ⛪ **43 Fully Detailed Religions** with 3,372 localization lines
- 🛡️ **530+ CoA Templates** across 4 writing systems
- 🏛️ **Writing System-Based Governments** (Aigl Naval first implementation)
- 🧬 **Ancient Genetics** for 3 cultures (Beauty, Strength, Intelligence)
- 🗺️ **Map Polish** (biomes, development, terrain)
- 🔧 **CK3 1.18 Compatibility**

---

## Installation & Compatibility

**Requirements:** CK3 1.18.x, no DLC required

**Save Compatibility:** ✅ Compatible with 1.3.0 saves (localization-only changes)

**Conflicts:** None (text changes only)

---

## Memory Bank & Spec Documentation

### Active Specifications
Located in: `c:/Users/User/OneDrive/Documents/R3_Planet_Thekan/arikuri_scripts_and_specs/docs/concepts/`

**Current Specs:**
- `aixqelt_eniol_empire_complete.md` (42KB) - Aixqelt Eniol Empire complete lore documentation

### Memory Bank Structure
Located in: `c:/Users/User/OneDrive/Documents/R3_Planet_Thekan/arikuri_scripts_and_specs/`

**Key Documentation:**
- `MAINTENANCE_GUIDE.md` - Mod maintenance procedures
- `MEMORY_BANK_RESTRUCTURING_PLAN.md` - Documentation organization
- `STRUCTURE_GUIDE.md` - Project structure reference
- `README.md` - Project overview

**Subdirectories:**
- `backups/` - Configuration backups with timestamps
- `bgk/` - Background knowledge and planning docs
- `char_environments/` - Character environment system docs
- `csv/` - Data analysis and configuration CSVs
- `docs/` - Comprehensive documentation (111 files total)

---

## Credits

**Lore Refinement:** Arikuri Development Team  
**Implementation:** December 2025 Session

---

*"From opportunistic scavengers to power-driven chieftains - every culture tells its truth through governance."*
