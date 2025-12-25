# Arikuri Mod - Version 1.4 Release Notes

**Status**: DRAFT  
**Release Date**: TBD (January 2025)  
**Last Updated**: December 25, 2025

---

## Why Version 1.4?

This release was originally planned as version 1.3, but the scope expanded significantly during development. We skipped one release cadence to incorporate substantial additional content, including:
- Extended flavor implementation for 5 complete writing systems (originally 4 planned)
- Preliminary CoA and GFX implementation across all 17 remaining writing systems
- Complete government system scaffolding for all 22 writing systems
- Comprehensive religion overhaul with 43 streamlined faiths
- New frontend design and loading screens
- Major ethnicity and doctrine polish

The volume of new content warranted the version bump to 1.4.

---

## Major Features & Content

### Visual & Audio Expansion

- **Thumbnail, Logo, and Paper Map Revamp** - Complete visual identity refresh
- **Soundtrack Doubled** 🎵 - Soundtrack size doubled with new original tracks
- **New Frontend Design** - Redesigned main menu panel (will be improved in future updates)
- **Improved Loading Screens** - Enhanced visual experience during load times

### Writing Systems - Complete Flavor Design (5 Systems)

The following writing systems now feature **complete extended flavor implementation**:

1. **Plith** (Northwest jungle, logo-syllabary)
2. **Queekwa** (Northwest coastal, alphasyllabary)
3. **Gleuncti** (West mountains, evolved pictograph alphabet)
4. **Pfaunkti** (North-Central highlands, crystal-optimized alphabet)
5. **Aixqelt** (Eniol Empire, impure abjad RTL)

Each includes:
- Complete CoA design templates and color palettes
- Flavorful religion banners
- Background flavors for faith screen and temple events
- Unique tenet banner art
- Character background environments
- Clothing selection integration
- Full linguistic compendium with IPA phonology

### Writing Systems - Preliminary Flavor (17 Systems)

All 17 remaining writing systems now have **preliminary/partial flavor implementation** covering the full map:

- Unique CoA design templates and palettes for every writing system
- Partial implementation of various GFX features including:
  - GUI flavors
  - Architecture/character backgrounds
  - Tenet banners
  - Clothing selection mechanics

**Every culture, religion, and writing system/civilization now has unique CoA design templates and palettes.** The 5 complete systems have more elaborate implementations; the remaining 17 are work-in-progress with varying levels of feature completion.

### CoA System 🛡️

- **530+ CoA Templates** - Unique designs across all writing systems
- **285 Colored Emblems** - Custom emblem library for Arikuri civilizations

### Writing System Families & Religion Organization

- **20+ Writing Systems** now form cohesive religion families
- Hostility doctrines properly set between families
- Main faith languages assigned
- Unifying factors established for each religion family
- **House CoA Frames** - Writing system specific frames implemented

### Religions & Faiths Overhaul ⛪

- **43 Distinct Religions** with **3,372 localization lines** - Each with unique gameplay, faction mechanics, and thematic elements
- **Complete Faith Descriptions** - All 43 religions have flavorful, lore-rich descriptions with well-defined concepts
- **Major Lore/Description Update** - Almost every non-orthodox faith within each religion received expanded lore and descriptions
- **Color Mapping System** - Visual mapping creating color relationships between religions and heritages:
  - Each base religion has distinct color theme
  - Related faiths use variations of that color
  - Heritage groups share color palettes with subtle variations
  - Instantly recognizable religious families and cultural groups on map
- **Polished Ethnicity Specifics** - Refined per-religion ethnicity configurations
- **Tenets and Doctrines Polish** - Comprehensive refinement across all faiths
- **Gender Doctrines Overhauled** - Refined gender policies per religion to create interesting factions and groups that interact with each other
- **Localization Gaps Resolved** - Cultures, heritages, and religions

### Holy Site System

- **Complete Refactor** - Placements, bonuses, balance, and flavor completely reworked
- Core/common site distribution system
- Faith-specific site ownership logic

### Government System

**18 Custom Government Files** covering 100% of all 22 writing systems:

| Government | Base | Writing Systems |
|-----------|------|-----------------|
| Aigl Maritime | Feudal | Aigl |
| Chormana Nomads | Steppe Admin | Qormaic, Gleuncti, Ioddrik, Xacra, Aigl |
| SE Family Clan | Clan | Preolyth, Qieulbaia, Floicht, Wusaun |
| Ineoism Mandala | Mandala | Gleuncti |
| Kioq Mandala | Mandala | Kioq |
| Livetower Mandala | Mandala | Floicht |
| Inner Sea Raiders | Wanua | Thramptith, Qieulbaia |
| Mercenary Nomad | Nomad | Broulqen, Floicht |
| Broulqen Bureaucracy | Administrative | Broulqen |
| Qeomoq Communal | Celestial | Qeomoq |
| Eniol Oppressive | Japan Feudal | Aiexqelt |
| Eniol Progressive | Japan Admin | Aiexqelt |
| Malachite Mountain | Feudal | Xacra |
| Pfaunkti Trade Guild | Meritocratic | Pfaunkti |
| Veuqrit Scholastic | Meritocratic | Veuqrit |
| Paladinical Hosts | Clan | Aelwrid |
| Tribal Wanderers | Nomad | Thramptith |
| Blouck Tribal | Tribal | Blouck |

**Coverage**: 22/22 writing systems (100%), 85+ heritages assigned

**DLC Integration:**
- Base Game Only: 7 governments (39%)
- Roads to Power Required: 4 governments (22%)
- Trails & Treasures Required: 7 governments (39%)

### Culture Innovation Seeding

**6 Writing System Civilizations with Historically Advanced Tech Grants:**

Cultures now start with thematically appropriate technologies reflecting their historical advancement level:

| Civilization | Tech Count | Key Technologies |
|-------------|------------|------------------|
| Eniol Empire | 5-7 per faction | Faction-specific: casus_belli, city_planning, ledger, bannus, quilted_armor + faction bonuses |
| Broulqen | 3 | ledger, plenary_assemblies, currency_01 (Byzantine bureaucracy) |
| Aigl | 3 | casus_belli, bannus, longboats (maritime raiders) |
| Qeomoq | 3 | city_planning, crop_rotation, plenary_assemblies (communal harmony) |
| Livetower | 4 | city_planning, plenary_assemblies, development_01, motte (temple-citadels) |
| Gleuncti | 2 | city_planning, plenary_assemblies (temple authority) |

### Map & Titles

- **Title Consolidation** - Tiny kingdoms and empires removed for better balance
- **Heritage Aesthetics Polish** - Visual refinement of heritage-specific elements

### Technical

- **CK3 1.18 Compatibility** - Full compatibility with Crusader Kings 3 version 1.18
- **Localization Fixes** - Various text and translation corrections

---

## What's NOT in This Patch

The following features were originally expected in 1.3/1.4 but are deferred to future releases:

### Deferred to Next Patch (per-civilization rollout):
- **Religion-Specific Decisions** - Unique decisions per writing system/civilization
- **Religion-Specific Doctrines** - Custom doctrine mechanics
- **Religion-Specific Activities and Events** - Unique events per faith
- **Religion Uniqueness Mechanics** - Starting "Observer Effect" implementation
  - Will begin implementation per writing system/civilization from next patch

### Deferred (Timeline TBD):
- **Map Polish** - Including potential rescale to vanilla size, proper rivers
- **Balance Pass** - Please report any balance issues you encounter!

---

## Known Issues & Feedback

This release includes extensive new content. Balance has not been fully tested across all configurations.

**Please report any issues through:**
- Discord channel (linked on Steam Workshop page)
- Steam Workshop comments

---

## Coverage Statistics

| Category | Coverage |
|----------|----------|
| Writing Systems | 22/22 (100%) |
| Complete Flavor WS | 5/22 |
| Preliminary Flavor WS | 17/22 |
| Religions | 43 |
| Religion Localization Lines | 3,372 |
| CoA Templates | 530+ |
| Colored Emblems | 285 |
| Heritages Assigned | 85+ |
| Government Types | 18 custom + vanilla fallbacks |

---

## Discord-Ready Patch Notes

```
🎮 **Arikuri Mod - Version 1.4 Release**

📌 **Why 1.4?** Originally planned as 1.3, but scope expanded significantly - we skipped a release cadence to include substantially more content!

🎨 **Visual & Audio**
> • Complete visual identity refresh (thumbnail, logo, paper map)
> • 🎵 Soundtrack size DOUBLED
> • New frontend/main menu design (WIP - will improve)
> • Improved loading screens

✍️ **Writing Systems**
> • **5 complete flavor systems**: Plith, Queekwa, Gleuncti, Pfaunkti, Aixqelt
> • **17 preliminary systems**: All remaining WS have unique CoA templates, palettes, partial GFX features
> • Every culture/religion/civilization now has unique CoA designs!
> • Character backgrounds, tenet banners, clothing selection, and more
> • 20+ writing systems forming religion families

🛡️ **CoA System**
> • **530+ CoA Templates**
> • **285 Colored Emblems**

⚔️ **Governments**
> • 18 custom Arikuri-exclusive government types
> • 100% coverage of all 22 writing systems
> • DLC integration (Roads to Power, Trails & Treasures)

⛪ **Religions**
> • **43 religions** with **3,372 localization lines**
> • Major lore/description update for non-orthodox faiths
> • Polished ethnicity specifics, tenets, doctrines
> • Gender doctrines refined per religion
> • Holy site refactor complete
> • Color mapping for visual religion/heritage relationships

🎓 **Culture Tech**
> • 6 civilizations with historically advanced starting techs
> • Thematically appropriate innovations per writing system

🗺️ **Map & Titles**
> • Title consolidation (tiny kingdoms/empires removed)
> • Heritage aesthetics polish

⏳ **Not in this patch** (coming next):
> • Religion-specific decisions, activities, events
> • "Observer Effect" mechanics (per-WS rollout starts next patch)
> • Map polish / potential rescale
> • Balance pass - please report issues!

🔧 **Technical**
> • CK3 1.18 compatibility
> • Localization fixes
```

---

## Source References

### Project Documentation:
- `governments/COMPLETION_SUMMARY.md`
- `governments/FINAL_IMPLEMENTATION_SUMMARY.md`
- `specs/AIXQELT_CONSOLIDATED_STATUS.md`
- `workflows/FINAL_IMPLEMENTATION_REPORT.md`
- `writing_systems/README.md`

### GitHub:
- Repository: AbstractBlackstork/arikuri
- Note: Check CHANGELOG.md and RELEASE.md for additional context

---

*Draft release notes - verify all completion statuses before publishing*