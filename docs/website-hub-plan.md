# TheHoboKingdom Hub Plan

## Durable save point

- Corrected baseline commit: `909b2372bc5ebf4ef88d941b142044dfe15a61f9`
- Recovery branch: `archive/pre-hub-v2-2026-07-23`
- Foundation merge: `027e4b8e6cc3123ef72c133b5de754e0f912b75a`
- Save-point date: 23 July 2026

The recovery branch preserves the site exactly as it existed before the hub overhaul. Its history was rewritten on 28 July 2026 to correct two malformed author emails; the preserved website files did not change.

## Intended navigation

The permanent navigation is:

1. Home
2. Projects
3. Guides
4. Tools
5. Downloads
6. About

Individual games live in the project directory rather than expanding the permanent navigation.

## Shared page structure

Every project hub should include:

1. Overview and honest status
2. Start-here links
3. Active work
4. Published guides
5. Downloads or releases
6. Recent changes
7. Planned additions

Every guide should include its scope, supported version or mod context, update date, main instructions, and revision notes.

## Milestones

### Foundation v2

- Repair routes and malformed pages.
- Add shared Jekyll layout, navigation, footer, and project data.
- Add Projects, Guides, Downloads, About, and 404 pages.
- Migrate legacy game placeholders into folder-based hubs.
- Preserve old addresses with redirect stubs.
- Add responsive and printable styling.
- Add an automated Jekyll build and internal-link check.

### Content pass

1. Maintain and expand the Dominions reference. The three-age catalogue and starting-game guide were added on 2 August 2026; Edition 26 of the complete Knowledge Library followed on 26 August 2026.
2. Publish the complete StalkerNet release history. The confirmed v4.3.0-v4.3.6 chain now has a public changelog; older milestones remain to be recovered.
3. Record the Minecraft Forge modpack and installation process. The design and troubleshooting records are public; the exact pack manifest remains pending.
4. Add safe public D&D campaign and character material. The completed Stormwreck Isle arc and public resource structure are now available.
5. Add versioned tabletop project pages and printables. Project records are available; stable printable bundles remain pending.

### Discovery pass

Completed on 27 August 2026:

- Extended search across the main site and the Dominions library index.
- Added related project and guide routes throughout the active hubs.
- Added the StalkerNet changelog and clearer release records.
- Updated the current Dominions cover and social-sharing image to Edition 26.
- Added an Atom update feed and sitemap.
- Added consistent official, tested, strategy, modded, research, and playtest labels.
- Added browser-local reading history, section-link copying, and reading progress to the Dominions library.

### Expansion pass

Completed on 27 August 2026:

- Added AURA and Vintage Story as active project hubs.
- Expanded Minecraft with its active pack record and a common-fixes guide.
- Added Stalkers' Ends and the accepted StalkerNet recovery chain.
- Added the player-safe Stormwreck Isle chronicle and D&D resource structure.
- Added permanent project routes for Z-Land and The Last of Us: Escape the Dark fan expansion.
- Added the planned Armoury & History hub.
- Expanded the Dominions field toolkit to eighteen tools covering pinned base-game records, nations, Pretenders, economy, recruitment, gems, magic, commander scripts, full battle plans, research, turns, diplomacy, reading progress, multiplayer settings, and a recoverable named-Throne victory register.
- Added a site-wide Tools hub with exportable mod-manifest and multiplayer-session records.
- Added JSON export and restoration to the newest private local records so they can be moved between browsers without sending their contents to the site.

Still dependent on future project work:

- Real application screenshots and stable downloadable AURA or StalkerNet builds.
- A frozen Minecraft or Vintage Story pack manifest and tested public profile.
- Finished, versioned tabletop printable bundles.
- The completed Sten video and its researched companion article.

## Publishing principles

- Do not list unfinished files as stable downloads.
- Keep large archives in GitHub Releases.
- Keep public player material separate from unrevealed GM notes.
- Mark modded Dominions advice separately from the unmodded game.
- Keep a confirmed rollback point for StalkerNet and other versioned projects.
