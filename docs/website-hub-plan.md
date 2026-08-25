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
4. Downloads
5. About

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

1. Maintain and expand the Dominions reference. The three-age catalogue and starting-game guide were added on 2 August 2026; Edition 24 of the complete Knowledge Library followed on 25 August 2026.
2. Publish the complete StalkerNet release history.
3. Record the Minecraft Forge modpack and installation process.
4. Add safe public D&D campaign and character material.
5. Add versioned tabletop project pages and printables.

### Discovery pass

- Extend the library's client-side search into the wider guide index when the other project sections have enough material to justify it.
- Add related-guide links.
- Add release records and changelogs.
- Add social-sharing imagery and project screenshots.
- Add update feeds if the volume of published work justifies them.

## Publishing principles

- Do not list unfinished files as stable downloads.
- Keep large archives in GitHub Releases.
- Keep public player material separate from unrevealed GM notes.
- Mark modded Dominions advice separately from the unmodded game.
- Keep a confirmed rollback point for StalkerNet and other versioned projects.
