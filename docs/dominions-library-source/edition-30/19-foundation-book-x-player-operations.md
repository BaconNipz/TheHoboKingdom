# Foundation Book X - Playing and Hosting Dominions 6

## Interface, Game Setup, Orders, and the First Campaign

Baseline: Dominions 6.36; vanilla procedure unless a ruleset is named; research edition 20 August 2026.

## 1. Purpose

Dominions is not played only on the battlefield. It is played in setup screens, message lists, province windows, recruitment queues, army panels, item treasuries, order menus, network lobbies, and the short interval between finishing a turn and committing it to the host. A commander can have the correct statistics, the right troops, and a sound strategic purpose and still fail because one operational detail was missed.

Book X is the operating manual for the library. It explains how to create and join a game, read the interface, translate intentions into legal orders, submit a turn safely, host a fair campaign, recover from common mistakes, and guide a first nation through its opening months. It is written for two readers at once:

- the new player who needs a complete route from the title screen to the end of a campaign;
- the experienced player who needs an exact procedural reference when the interface, network, or order system becomes the binding constraint.

Book X does not repeat mechanics owned elsewhere. [Book I](#b1-foundation-book-i-rulesets-language-and-the-anatomy-of-a-turn) owns hosting order and evidence; [Book II](#b2-foundation-book-ii-economy-provinces-and-the-machinery-of-state) owns the state economy; [Book III](#b3-foundation-book-iii-pretenders-dominion-scales-and-blessings) owns Pretenders and dominion; [Book IV](#b4-foundation-book-iv-armies-and-battle) owns battle; [Book V](#b5-foundation-book-v-magic) owns magic; and [Book VI](#b6-foundation-book-vi-strategy-and-campaign-conduct) owns campaign doctrine. Book X explains how players operate those rules.

## 2. Three Layers of Operational Knowledge

Every instruction belongs to one of three layers.

| Layer | Question | Typical failure |
| --- | --- | --- |
| Ruleset | What game is being played? | The wrong patch, map, mod stack, age, or setting is assumed. |
| Interface | What is the game showing, and where is the control? | Information is overlooked or a control is mistaken for the underlying rule. |
| Commitment | What will the host attempt to resolve? | An arrow, queue, script, or submitted file does not express the intended action. |

The layers should be checked in that order. An unexplained result is rarely clarified by studying battle arithmetic if the game was created with a different mod list. A legal order cannot be inferred from an arrow alone. A completed local turn is not necessarily a received network submission.

### 2.1 The operational chain

A reliable turn follows one chain:

`identify ruleset -> read new information -> inspect state -> choose priorities -> enter orders -> audit dependencies -> submit -> confirm receipt`

The chain is simple enough to memorize and strict enough to prevent most administrative losses. Expert play adds better judgment at each step; it does not remove the steps.

### 2.2 Interface facts and game facts

An interface fact describes what a control does. A game fact describes how the engine resolves the resulting order. The distinction matters:

- Clicking a province creates a movement instruction; [Book I](#b1-phase-iii-movement-and-conquest) explains when movement resolves.
- Pressing **Patrol** assigns an order; [Book II](#b2-part-v-unrest-and-coercive-economy) owns patrol strength and unrest consequences.
- Placing a spell in a script requests it; [Books IV](#b4-part-v-orders-and-scripting) and [V](#b5-part-v-the-anatomy-of-battle-magic) explain legality, targeting, gems, fatigue, and spellcasting behaviour.
- Pressing **End Turn** commits or hosts the local orders depending on game type; it does not certify that every planned action remains legal when hosting occurs.

The interface is a contract-writing system. It records requests to the host. Resolution belongs to the engine.

# Part I: Ruleset, Installation, and Local Continuity

## 3. Establish the Exact Ruleset

Before creating a game or interpreting an old save, record:

1. Dominions version;
2. enabled mods and their versions;
3. mod load order where relevant;
4. map and map version;
5. age;
6. participating nations and teams;
7. game settings;
8. victory conditions;
9. hosting method and timetable.

The title of a mod or map is not a sufficient identifier. Workshop content can change while retaining its public name. A file name, declared version, release date, and hash provide a stronger frozen record. Book IX demonstrates that practice for the supplied Dominions Enhanced and Divinitus files.

### 3.1 Current official baseline

The current baseline is Dominions 6.36, released 17 August 2026 UTC. It includes interface and operational changes from the 6.2x-6.36 series: expanded order copying, gem-transfer shortcuts, treasury sorting, clearer province and message displays, lobby safeguards, touchscreen operation, research navigation, and the ability of teleport-moving commanders to leave a besieged fort.

The patch baseline is not decorative. A player returning from an older release may remember a limitation that no longer exists, while a guide written for a later patch may recommend a control unavailable to an older host.

## 4. Find the User Data Directory

The safest route is the in-game **Game Tools** menu and **Open User Data Directory**. This avoids guessing whether the operating system, storefront, or installation has placed personal files somewhere unexpected.

Common default locations are:

| Platform | Usual user-data root |
| --- | --- |
| Windows | `%APPDATA%\dominions6\` |
| Linux | `~/.dominions6/` |
| macOS | `~/.dominions6/` |

Important subdirectories commonly include `mods`, `maps`, and `savedgames`. These are user-data locations, not the installed game directory. The distinction matters during reinstalls and updates: personal game material should not depend on editing installation files.

Book VIII owns the full [directory and packaging procedure](#b8-the-user-data-directory). The practical rule here is narrower: open the directory from the game, confirm the exact folder before copying anything, and preserve original downloaded files separately from edited working copies.

## 5. Install and Freeze Mods Safely

### 5.1 A reproducible mod stack

A reproducible stack has four properties:

- every participant has the same files;
- every participant enables the same releases;
- the host records any meaningful load-order requirement;
- the stack is not changed after pretenders or turns have been created unless every participant accepts the consequences.

The modern lobby performs a safety check intended to ensure that required mods have been uploaded, but it cannot replace a written baseline. The lobby can distribute what the host provides; it cannot prove that a public guide, local source inspection, or remembered balance rule refers to that exact file.

### 5.2 Installation procedure

1. Close any game session that is using the files.
2. Place the mod's `.dm` file and required asset folders in the user-data `mods` directory.
3. Preserve the supplied directory structure. Image paths in a `.dm` file are relative and can fail if folders are flattened or renamed.
4. Start Dominions and open **Game Tools** to enable the required mods.
5. Confirm that each mod is listed without a load error.
6. Create a small disposable game if the stack is unfamiliar.
7. Record file versions and, for a long campaign, checksums.

The procedure for maps is similar: place the `.map` file and associated images under `maps`, preserve relative paths, and test the map before committing a multiplayer group.

### 5.3 Never repair the live baseline casually

An apparent spelling error, duplicate definition, broken image, or balance problem in a live mod is not permission to edit the campaign copy. A local change creates a distinct ruleset. Repair experiments belong in a separate working file with a new version label. Book VIII owns [safe release engineering](#b8-part-xii-testing-validation-and-release-engineering).

## 6. Backups and Campaign Continuity

Backups are useful before a version change, a computer migration, a host transfer, or any repair attempt. Copy the specific game or content directory to a clearly dated destination. Do not replace the only working copy while diagnosing a problem.

For an ordinary campaign, preserve:

- the frozen map and mod files;
- the game-creation settings;
- the current saved game or host state;
- any separately distributed pretender or turn material;
- the hosting schedule and player roster;
- a short incident log when a stale, rollback, substitution, or disputed resolution occurs.

A backup is not a sanctioned alternate timeline. Multiplayer hosts should state in advance when restoration is permitted. A rollback can expose hidden orders or battle information and alter the competitive game even when the technical state is restored perfectly.

## 7. The Pregame Record

The following compact record is sufficient for most private games:

| Field | Record |
| --- | --- |
| Game name | Unique, filename-safe identifier |
| Dominions version | Host version and intended lock |
| Map | Exact title and release/file identity |
| Mods | Ordered list with versions |
| Age | Early, Middle, or Late |
| Nations | Player, nation, team, human/AI status |
| Pretender rules | Password requirement, disciples, design restrictions |
| Economy | Gold, sites, independents, research, special limits |
| Information | Scoregraph setting and diplomacy convention |
| Victory | Throne requirements, conquest, Cataclysm |
| Hosting | Lobby/private/PBEM/hotseat, timer, extensions, stale policy |
| Administration | Host, backup host, substitution and rollback policy |

Experts often retain this record because it lets later analysis separate a game result from a ruleset mismatch. New players benefit for the same reason.

# Part II: Creating the World

## 8. Create, Continue, or Join

The title screen divides three different acts:

- **Create World** establishes a new game's map, participants, settings, and victory conditions.
- **Continue Old Game** opens a local game that already exists.
- **Network** leads to multiplayer connections, including the official lobby.

Treat these as different workflows. Creating a world is an act of ruleset authorship. Continuing a game is a state-loading act. Joining a network game is a compatibility and identity check.

## 9. Choose the Map

A game can use a premade map or a generated world. The correct choice depends less on visual novelty than on whether the map supports the intended player count and game character.

Check at least:

- land and water province counts;
- required start positions and whether they are appropriate for the chosen age;
- wraparound behaviour;
- cave or plane structure;
- chokepoints, island isolation, and unusually dense water barriers;
- map-specific victory locations or scenario rules;
- whether every participant possesses the exact file and images.

A visually striking map may still be unsuitable for a competitive game if starting regions differ drastically or one nation begins without meaningful routes. Book VI owns [map structure and strategic geography](#b6-part-iv-map-structure-borders-and-infrastructure); Book VIII owns map-file construction.

## 10. Choose the Age and Participants

The age determines which nations are available and changes the broad magical and military environment. Early Age nations tend, as a general pattern rather than a universal law, to have stronger magical access and less developed mundane equipment or institutions. Later ages tend toward heavier conventional equipment, more organized states, and diminished magical abundance. Nation-specific exceptions are extensive.

On the participant screen:

1. add each nation;
2. set it to human or AI;
3. confirm that no nation is duplicated;
4. assign teams if using disciples;
5. verify that water nations and unusual starts are compatible with the map.

Do not use AI difficulty as a substitute for a stated learning purpose. A new player's test game, a balance test, and an expert's endurance game require different opposition.

## 11. Disciple Games

Enable the disciple option before assigning teams. Each team must contain exactly one Pretender and may contain disciples. Current releases support up to twenty teams.

The official rules create important design differences:

- a disciple receives 400 design points;
- a disciple does not choose dominion strength or scales;
- awakening time is half that of the team's Pretender;
- a team with disciples cannot appoint ordinary prophets.

Book III owns the divine mechanics. The setup obligation is to verify team composition before creation. A nation placed on the wrong team cannot be treated as a harmless lobby typo after designs and diplomacy have been built around it.

## 12. Create and Protect Pretenders

The Pretender-design screen supports saving and loading designs with **Ctrl+S** and **Ctrl+L**. Saving a tested design avoids reconstruction errors and gives the campaign a recoverable baseline.

For network play:

- use a player password where the workflow permits it;
- do not reuse an important real-world password;
- confirm the chosen nation, age, team, and active mods before submission;
- keep the local design file until the game has begun successfully.

Cheat prevention is useful but does not protect players from a malicious or careless host. The host necessarily holds privileged game state. Trust and administrative policy remain part of multiplayer security.

Pretender design itself belongs to [Book III](#b3-part-i-pretender-design-as-a-national-system). Book X adds only the operational rule: save, label, verify, and submit the design that was actually tested.

## 13. Game Settings by Consequence

Game settings should be chosen by the experience they create, not by habit.

| Setting | What it changes operationally | Questions for the host |
| --- | --- | --- |
| Starting gold | Opening purchasing power | Is the game meant to accelerate first forts or preserve normal scarcity? |
| Magic-site frequency | Gem and site density | Will this support the intended map size and magic level? |
| Independent strength | Expansion danger | Are players expected to use tested expansion parties or learn against forgiving provinces? |
| Research or magic setting | Time to research thresholds | Does the timer match the intended campaign length? |
| Scoregraphs | Public strategic information | Are graphs visible, hidden, or recoverable through intelligence? |
| Master password | Emergency administrative access | Who holds it, and under what written circumstances may it be used? |
| Limited artifact forging | Competition for unique artifacts | Is the default one unique artifact per game turn retained? |
| Limited legendary research | Competition at level nine | Is only one level-nine discovery permitted at a time, with repeat research required? |
| Commander renaming | Information organization and deception | Is renaming allowed, and are naming conventions restricted? |
| Cheat prevention | Detectable file manipulation | Is it enabled, and do players understand its limits? |
| Throne settings | Victory arithmetic | How many Ascension Points exist and how many are required? |
| Cataclysm | Endgame clock | When does it begin, and how will Throne loss alter the required total? |

### 13.1 Scoregraphs

Scoregraphs change diplomacy because they change common knowledge. Visible army, income, research, fort, province, dominion, or gem trends allow coalitions to form around measurable growth. Hidden graphs place more weight on scouting and negotiation. Spies operating in an enemy capital can reveal graphs, so hidden does not mean unobtainable.

At victory, current versions reveal scoregraphs and the hidden map to players who remain until the end; an eliminated player does not receive that later revelation. This makes post-game review stronger than mid-game speculation. Book VI owns the strategic use of information.

### 13.2 Master password

A master password can rescue a game by allowing an absent player to be set to AI or by permitting necessary administration. It also provides broad access. It should be held by the host and, if desired, a trusted backup under a written policy. Its use should be logged.

### 13.3 Limited artifacts and legendary research

Under the usual limited-artifact setting, a particular unique artifact may be forged only once per game turn. Several players can race for it in the same month. Under limited legendary research, only one level-nine spell in a school can be completed at a time; the level can be researched again to reach another. These settings turn a menu choice into an initiative contest.

### 13.4 Renaming

When enabled, most commanders can be renamed by opening their statistics and pressing **R**. Pretenders, disciples, prophets, and famous heroes are exceptions. Good internal names encode function or theatre without exposing more than necessary in multiplayer screenshots or streams.

## 14. Victory Conditions

The standard route is control of enough Ascension Points from Thrones. The setup screen can use recommended/default Throne distributions or a custom arrangement. A conquest game instead requires elimination or control on the specified terms.

Cataclysm creates a hardening endgame. It destroys Thrones over time and reduces the Ascension Points required for victory. The finishing line moves while the map deteriorates. Record the starting turn and make sure every player understands the interaction before play begins.

Book VI owns [Throne arithmetic and victory conversion](#b6-part-xii-thrones-cataclysm-and-endgame-conversion). The setup standard is exactness: state the number and level of Thrones, total points, points required, and Cataclysm turn.

## 15. Host Setup Sheet

Before pressing the final creation control, the host should be able to answer every row:

| Check | Pass condition |
| --- | --- |
| Version | Host is on the announced patch. |
| Content | Exact map and mod stack are installed and tested. |
| Participants | Nations, human/AI status, and teams match the roster. |
| Settings | Every non-default setting is written down. |
| Victory | Throne or conquest conditions are explicit. |
| Security | Player passwords, master-password custody, and host trust are addressed. |
| Schedule | First hosting time, regular timer, and extension channel are known. |
| Recovery | Backup and substitution policy exists. |

Creating the world should feel like signing the campaign charter, because that is what it is.

# Part III: Starting, Joining, and Hosting

## 16. Game Modes

Dominions supports several multiplayer patterns.

| Mode | Best use | Principal operational risk |
| --- | --- | --- |
| Single-player | Learning, testing, and private analysis | **End Turn** hosts immediately; there is no submission grace period. |
| Hotseat | Several players on one machine | Hidden information and passwords require disciplined handoff. |
| Official lobby | Most online groups | Identity, version, mod, password, and timer errors. |
| Private server | Controlled communities and persistent hosts | Server setup and maintenance depend on the current executable and network environment. |
| PBEM/file exchange | Asynchronous groups using external coordination | Wrong or missing files, weak confirmation, and manual version control. |

The official lobby is the recommended online route for ordinary groups. Private servers and PBEM remain valid when the group has a reason to manage its own infrastructure, but exact command-line instructions are version-sensitive and should be taken from the current official documentation or executable help rather than copied uncritically from an older guide.

## 17. Official Lobby Workflow

### 17.1 Joining

1. Start the announced Dominions version.
2. Enable or install the required mods.
3. Select **Network** and **Enter Game Lobby**.
4. Locate the exact game name rather than a similar title.
5. Check nation, status, remaining time, and any displayed content requirements.
6. Enter the player password if required.
7. Inspect the loaded turn before issuing orders.

If the game cannot be entered, stop before changing local files at random. Compare version, mod list, mod file identity, map, password, and whether the game is awaiting pretenders, running, finished, or currently hosting.

### 17.2 Creating or administering a lobby game

The lobby host should keep the game name distinctive, publish the ruleset separately, and test the connection before the first real deadline. Current releases have improved lobby validation and handling of larger turn files, but administrative clarity remains necessary.

Do not change mods or the map to make one client connect unless the host has first confirmed the canonical campaign files. The correct repair is to bring the client to the baseline, not to create competing baselines.

## 18. Turn Submission and Revision

In network multiplayer, **End Turn** saves and submits the turn. The player can normally revise and resubmit before hosting. In single-player, **End Turn** immediately resolves the month.

That difference changes the safe habit:

- In single-player, perform the complete audit before ending the turn.
- In multiplayer, early submission can protect against a missed deadline, but a later revision still requires confirmation that the replacement was received.

A submitted marker is evidence of receipt, not evidence of strategic quality. The final pre-host check remains necessary.

### 18.1 Submission protocol

1. Save enough time before the deadline for a connection failure.
2. Finish a complete local audit.
3. Press **End Turn** and allow the transfer to finish.
4. Re-enter or refresh the game state if necessary to confirm the nation is marked submitted.
5. If revising, make the change, submit again, and confirm the new submission.
6. Notify the host immediately if the status is uncertain near the deadline.

### 18.2 Stales

A stale is a hosted turn without a valid new submission for that nation. The engine must continue the game from existing state and default order persistence. The result may preserve some standing behaviour but it does not replace active planning.

The host should distinguish:

- an ordinary missed deadline governed by the published stale policy;
- a platform or host failure affecting several players;
- an announced emergency for which an extension was requested;
- strategic regret after the player already had a fair opportunity to submit.

These are not ethically identical events, even if all can produce a missing turn file.

## 19. Hosting Policy

A healthy campaign states its administrative rules before they become politically useful.

### 19.1 Minimum charter

- regular hosting interval and timezone;
- how automatic hosting interacts with all turns being submitted;
- extension request channel and expected notice;
- maximum ordinary extension, if any;
- stale and consecutive-stale policy;
- substitution and AI-conversion procedure;
- rollback conditions;
- rules for diplomacy, trades, concessions, and coordinated victory;
- rules for bugs, exploits, and prohibited file inspection;
- who can administer the game if the host is unavailable.

### 19.2 Extensions

Extensions protect the quality of a long game when real life intervenes. They also delay every participant. A good rule is predictable and symmetric: ask as early as possible, give a new exact deadline, and record it in the common channel. Do not make the host infer that an unsubmitted nation wants more time.

### 19.3 Substitutions

A substitute needs the nation password, current turn access, public rules, diplomatic obligations, and enough strategic context to avoid accidental treaty breaches. Private intelligence should be transferred only as the game permits. The original player should not continue advising several sides after departure unless the group explicitly allows it.

### 19.4 Rollbacks

Rollback is a last resort for technical corruption or a clearly defined administrative failure. It is not a remedy for a forgotten script, a bad move, or a surprising battle. Once players have seen hosted information, replaying the month changes their knowledge. If a rollback is unavoidable, document the reason, restored point, affected submissions, and any required order-repetition rule.

## 20. Security and Trust

Use unique game passwords. Do not send credentials through public channels. The master password and host files deserve the same care as any private competitive record.

Cheat detection can identify some forms of manipulation, but it cannot make an untrusted host trustworthy. The host has privileged access by design. Choose a host who treats the role as custodial, preserve administrative logs, and settle disputes through evidence instead of speculation.

# Part IV: The Main Interface

## 21. The Map as a Control Surface

The strategic map is simultaneously a world view, an order editor, and an information filter. The default interaction pattern is:

- right-click a province or object for information;
- left-click a commander to select it;
- left-click a destination to issue movement;
- use the province and nation controls for recruitment, messages, research, and overviews.

Mouse behaviour can be altered in preferences, so a player following instructions on another machine should confirm whether selection and information buttons have been swapped.

### 21.1 Selection discipline

Before entering an order, identify three things:

1. the selected province;
2. the selected commander or group of commanders;
3. the destination or target province.

Most accidental orders are selection failures. The map arrow can look plausible even when the wrong commander is carrying the order.

## 22. Province and Nation Controls

The standard controls include:

| Control | Function | Operational use |
| --- | --- | --- |
| **E** | End Turn | Save/submit in multiplayer; host immediately in single-player. |
| **T** | Army Setup | Organize commanders and troops in the selected province. |
| **Y** | Army Setup at Destination | Inspect or organize the destination context. |
| **U** | Patrolling Army Setup | Work with forces assigned to patrol. |
| **R** | Recruit Units | Open the local recruitment screen. |
| **B** | Mercenaries | Review and bid on available mercenaries. |
| **I** | Province Chronicles | Review the province's recorded history. |
| **M** | Read Messages | Open the month's messages. |
| **S** | Send Messages | Open diplomacy and transfer messaging. |
| **F1** | Nation Overview | Inspect commanders, provinces, and national administration. |
| **F2** | Scoregraphs | View information allowed by the game setting and intelligence. |
| **F3** | Hall of Fame | Inspect experience leaders and heroic abilities. |
| **F4** | Pretenders | Review known divine players and status. |
| **F5** | Research | Set school priorities and inspect progress. |
| **F6** | Global Enchantments | Review active globals and available public information. |
| **F7** | Magic Item Treasury | Store, equip, and manage items where access permits. |
| **F8** | Magic Item Overview | Find items and their holders across the nation. |
| **F9** | Thrones | Review known Thrones and Ascension Point information. |
| **Esc** | Options/menu | Access preferences, save/quit controls, and other session options. |

The letter shortcuts are efficient because they reduce navigation cost, but context still controls what can be done. **R** opens local recruitment only where the province and ownership permit it. **F7** does not make a remote commander share a laboratory treasury.

## 23. Map Navigation Shortcuts

| Key | Result |
| --- | --- |
| Arrow keys | Scroll the map. |
| **Home** | Centre on the home province. |
| **Ctrl+Home** | Centre on the Pretender or disciple. |
| **G** or **#** | Go to a province by number. |
| **End** | Set half-scale zoom. |
| **Insert** | Zoom to cover the screen. |
| **Delete** | Fit the whole map. |
| **Page Up** or **Ctrl+Up** | Zoom in. |
| **Page Down** or **Ctrl+Down** | Zoom out. |
| **Ctrl+F** | Open map filtering. |
| **H** | Hide interface buttons and commanders. |
| **?** | Show contextual shortcut help on supported screens. |

The **?** control deserves special emphasis. Dominions exposes more context-sensitive shortcuts than any static summary can comfortably hold. When a selection, army, recruitment, or treasury screen feels slow, open the contextual help before assuming the operation requires repeated clicking.

### 23.1 Touchscreen mode

Version 6.36 adds a touchscreen mode for play with little or no keyboard use. In that mode, a long-click is interpreted as a right-click and the map can be scrolled by dragging broadly rather than relying on a narrow scroll region. The settings popup remains the release-specific control reference. Because long-click changes the meaning of a press, practise opening and closing popups before entering time-sensitive orders.

## 24. Strategic Map Filters

| Shortcut | Filter or overlay |
| --- | --- |
| **Ctrl+1** | Flags and forts |
| **Ctrl+2** | Armies |
| **Ctrl+3** | Dominion |
| **Ctrl+4** | Income |
| **Ctrl+5** | Thrones and events |
| **Ctrl+6** | Own troops in allied provinces |
| **Ctrl+7** | Allied troops in own provinces |
| **Ctrl+8** | Neighbour relationships |
| **Ctrl+9** | Province names |
| **Ctrl+0** | Remote rituals |

A filter is an analytical lens. Income view finds economic discontinuities; dominion view finds religious fronts; army view finds exposed force; neighbour view tests movement assumptions. Use several filters in sequence rather than treating the default map as complete information.

### 24.1 Planes

Plane controls switch among accessible realms: the Pantokrator's realm, the realm beneath, and the Void. A control is grey when the nation lacks access. A plane is more than another zoom layer; it can have its own movement, access, provinces, and strategic relationships. Verify the active plane before issuing or diagnosing a movement order.

## 25. Right-Click, Tooltips, and Popups

Right-click is the first research tool inside the game. Use it on units, weapons, armour, abilities, provinces, paths, items, and other interface elements. Hover text and popups often expose the difference between a familiar name and the actual current ruleset.

Recent releases have expanded popups for areas of effect, movement destinations, Ascension Point information, ritual targets, and other state. Treat a tooltip as a current local clue, then distinguish three cases:

- the popup states an exact game value;
- the popup summarizes a mechanic owned by the manual;
- the popup describes an effect whose full result still depends on hidden state or hosting order.

The first can be recorded directly. The second should be linked to its canonical rule. The third requires evidence, not confident interpolation.

## 26. Current Operational Additions Worth Learning

Players returning from earlier Dominions 6 releases should learn these accumulated improvements:

- **Ctrl+A** can sort the item treasury automatically.
- Gem transfers have fast keyboard controls in several screens; for example, hovering a commander and using **Alt+F** adds a Fire gem, while **Alt+Backspace** removes the corresponding gem in the supported context.
- Order copying is available more broadly, including army positioning; **0** is used for order copy/paste in supported screens, while squad scripting also retains numbered script storage.
- The bless interface can repeat the last effect with **X** and remove an effect with **Backspace**.
- In version 6.35, the Nation Overview's **L** filter isolates commanders assigned to Pillage.
- Ritual messages and destination displays provide stronger province navigation.
- Teleport-moving commanders can leave a besieged fort in 6.35.
- In 6.36, right-clicking the supported Province Defence increase or decrease control changes PD by ten, and right-clicking the **T** Army Setup control invokes the **Y** destination form.
- The 6.36 Research screen uses **Up** and **Down** to swap research targets and includes **?** help.
- In the 6.36 battle overview, **S** hides temporary summons; in spell selection, **Space** clears the active filter.
- Current victory review reveals scoregraphs and the hidden map for players who remain until the end.

Shortcuts are not all global. If a key does nothing, confirm the active screen and open **?** rather than assuming the rule has failed.

# Part V: Reading and Preparing a Turn

## 27. Begin with Messages, Not with Memory

Every hosted month can invalidate part of the plan made in the previous one. A border changed, a commander died, a site was discovered, a fort completed, a ritual failed, an enemy army appeared, or a diplomatic promise became due. Read the new state before continuing yesterday's intentions.

A strong review order follows causation:

1. hosting and administrative notices;
2. battles, assassinations, and movement outcomes;
3. province gains, losses, sieges, and unrest events;
4. new commanders, troops, construction, and recruitment;
5. research, spells, items, sites, and rituals;
6. dominion, Throne, and global changes;
7. diplomacy and transfers;
8. attrition, disease, desertion, and other end-state changes.

This mirrors the principle in [Book I's hosting sequence](#b1-the-complete-63-step-hosting-sequence): consequences should be read in the order that explains them. The message list is not always displayed as a complete causal proof, so province state, commander state, and the battle replay may need to be compared.

## 28. Message Triage

Classify each message before acting.

| Class | Meaning | Immediate question |
| --- | --- | --- |
| Fatal dependency | A commander, fort, laboratory, army, or route no longer exists | Which downstream orders are now impossible? |
| Strategic change | A war, Throne, global, border, or alliance changed | Does the monthly priority still hold? |
| Resource change | Gold, gems, research, recruitment, or items changed | Which queue or package is now underfunded? |
| Local exception | An event or isolated result needs attention | Is it urgent, or can it wait behind national priorities? |
| Informational | The message confirms an expected result | Can it be archived after verification? |

The greatest danger is not the most dramatic message. It is the message that silently invalidates several orders: a laboratory loss that strands gem transfers, a dead ferry commander that leaves troops behind, or a captured province that breaks a movement chain.

### 28.1 Use message navigation

Where a message offers a province or unit link, use it. Current versions provide better destination and ritual-message navigation than early releases. After arriving at the province, inspect the surrounding map; a message's named location may be only one part of the consequence.

## 29. Battle Review as Evidence

A battle replay answers more than “who won?” Record:

- initial formation and whether expected squads appeared;
- actual scripts and whether requested spells were cast;
- first contact timing;
- important damage, fatigue, morale, and targeting failures;
- retreats and the provinces into which survivors escaped;
- commander and specialist losses;
- whether the result achieved the campaign purpose.

Book IV owns the [post-battle audit](#b4-post-battle-audit), while Book VI owns conversion. The operational duty is to preserve enough evidence to tell a bad plan from a mis-entered plan.

### 29.1 Replay version awareness

Battle displays are interpretations of a hosted result. Version mismatches can create misleading replays. In supported versions, **Ctrl+I** during battle can display host and current version information. If the visible replay appears impossible, compare the host version before constructing a new theory of combat.

## 30. The Nation Overview as an Administrative Ledger

**F1** is the broadest audit screen. It makes dispersed national state searchable without clicking every province. Use its columns, filters, and sorting to answer questions such as:

- Which commanders have no useful order?
- Which mages are researching, moving, forging, searching, or idle?
- Which provinces are recruiting commanders or troops?
- Where are unrest, low income, fortification, or siege problems developing?
- Which forces are pillaging, patrolling, or otherwise assigned to exceptional work?

The overview is most valuable near the end of the turn, after local plans have been entered. It reveals omissions that province-by-province work hides.

On version 6.35, press **L** within the Nation Overview to isolate Pillage orders. This is especially useful before submission: a commander left pillaging after an emergency can permanently damage a province that has already returned to ordinary economic use.

## 31. Establish the Monthly Priorities

Before issuing many orders, state the month in a few lines:

- primary strategic objective;
- threat that must be answered;
- research threshold being pursued;
- infrastructure or recruitment commitment;
- gem or item package that must be delivered;
- diplomatic obligation due this month;
- acceptable loss and reserve requirement.

The statement prevents locally attractive actions from consuming resources required by the national plan. It also makes the final audit intelligible: each essential order can be checked against a declared purpose.

## 32. Work from Dependencies Outward

Enter fragile, dependent orders before routine orders.

1. confirm irreplaceable commanders and movement leaders;
2. assign magic, gems, items, and ritual targets;
3. organize armies and scripts;
4. enter movement, stealth, patrol, siege, and special orders;
5. complete recruitment and construction;
6. adjust research and recurring administration;
7. send diplomacy and transfers;
8. audit the entire nation.

This is not the engine's hosting sequence. It is a human error-control sequence. A recruitment queue is easy to reconstruct; a multi-province communion package assembled after movement orders is easy to break.

## 33. The End-of-Turn Audit

Run four passes.

### 33.1 Commanders

- Every important commander has the intended order.
- Movement arrows belong to the intended units.
- Stealth, normal movement, and attack-current-province choices are distinguished.
- Researchers, site searchers, forgers, preachers, blood hunters, and builders are not accidentally idle.
- Besieged commanders have legal orders for their side of the walls.

### 33.2 Armies

- Troops are assigned to commanders rather than left unintentionally in the garrison.
- Leadership type and capacity are sufficient.
- Formation, orders, scripts, gems, and items belong to the correct commander.
- Retreat routes and supply are plausible.
- A moving commander is actually carrying the intended squads.

### 33.3 State

- Capital and fort recruitment queues are funded as intended.
- Commander Points, Recruitment Points, resources, Holy Points, and gold bind where expected.
- Forts, temples, laboratories, Province Defence, and repairs match the budget.
- Research is assigned to the intended schools.
- Treasury gems and items are where next month's plan expects them.

### 33.4 Campaign

- Border gaps, Throne approaches, and known raiders were inspected.
- Treaties, trades, warnings, and extension needs were communicated.
- The action creates a useful position if it succeeds and a survivable position if it fails.
- The turn is submitted and receipt confirmed.

# Part VI: Recruitment, Army Setup, and Inventories

## 34. Recruitment Is Local

The recruitment screen converts local capacity into a future force. National troops are usually available in the capital and in forts, subject to nation and unit rules. Some troops are capital-only; some require terrain, a particular site, a foreign-recruitment condition, or recruitment outside a fort.

A unit or commander can be constrained by several independent resources:

- gold;
- local resources;
- Recruitment Points;
- Commander Points;
- Holy Points;
- a per-turn or per-location recruitment limit;
- a fort, site, terrain, dominion, or other prerequisite.

Book II owns [recruitment constraints](#b2-part-iv-resources-and-recruitment). The recruitment screen expresses those constraints locally.

## 35. Reading a Recruitment Queue

### 35.1 Immediate gold, later local capacity

The game will not queue a purchase that cannot be afforded with current gold. Some shortages in resources, Recruitment Points, or Holy Points can remain in a queue for later turns. A dimmed entry needs to be diagnosed: inspect every cost and prerequisite instead of assuming gold is the problem.

### 35.2 Queue behaviour

- Hold **Shift** while selecting a recruit to add ten at a time.
- A queue can hold up to 250 entries.
- Commanders are separately restricted by local Commander Points.
- Units with a limited recruitment rate cannot exceed that local monthly rate.
- Newly recruited units arrive early enough in the hosted month to defend the province.
- Recruits in a fort that becomes besieged are placed within the besieged fort.
- New units enter the unassigned garrison until deliberately organized.

### 35.3 Queue audit

For each recruiting centre, ask:

1. What role is being purchased?
2. Which resource is binding?
3. Will the queue complete this month or spill into the next?
4. Is a commander being produced to lead or use the troops?
5. Can the province survive long enough for the investment to matter?

An overflowing queue is not a plan. It is a claim on future capacity.

## 36. Army Setup

Open Army Setup with **T**. The screen is where troops are transferred, grouped, positioned, and given battle orders.

### 36.1 The unassigned garrison

Unassigned units are not attached to a commander.

- In a fort, they remain inside unless assigned or used in a relevant patrol or defensive arrangement.
- Outside a fort, unassigned defenders join a battle as a central squad.

Leaving troops in the garrison can be deliberate. Leaving the only troops meant to move there is an operational failure.

### 36.2 Forming squads

A commander can lead up to five squads, subject to leadership type and capacity. Select units and then a squad box to add them. Dropping selected units on a commander can create a new squad when a slot is available.

Useful selection controls include:

- double-click to select matching units;
- **Shift-click** to build a selection;
- hover a squad and press **W** to select afflicted units;
- **E** to select units with at least two experience stars in the supported context;
- **M** to select the slowest units;
- **Enter** to clear a selection;
- **?** to display the complete contextual shortcut list.

Selection shortcuts are tools for preserving composition. They allow the wounded, experienced, or slowest part of a formation to be separated without checking every card.

### 36.3 Leadership audit

The army screen may permit a visually convincing group that performs poorly because the commander lacks appropriate ordinary, undead, magical, or special leadership. Before leaving the screen, compare:

- number and type of units;
- commander leadership categories;
- command penalties or bonuses;
- squad morale;
- movement compatibility.

Book IV owns [leadership and army construction](#b4-part-iii-command-squads-and-army-construction).

## 37. Positioning and Battle Orders

Each squad and commander has a placement box. Selected formations can be repositioned by right-clicking in the battlefield diagram. Colour and order indicators distinguish assigned behaviour, but the order text remains the authoritative check.

### 37.1 Squad orders

Assign orders based on delivery rather than theme. A missile squad, bodyguard group, flanking force, line holder, and attack squad have different contact problems. The detailed order and targeting analysis belongs to [Book IV](#b4-part-v-orders-and-scripting).

### 37.2 Commander scripts

A commander can receive up to five specific scripted orders before falling back to the standing order or spellcasting AI. In the army screen:

- **Ctrl+number** stores a script in the supported context;
- pressing the corresponding number pastes it;
- **X** can repeat the same requested order while constructing the script;
- current versions also support broader order copy/paste, including **0** in supported screens.

After copying a script, re-check gems, paths, equipment, range, fatigue, and spell availability. Copying transfers instructions; it does not make commanders interchangeable.

### 37.3 The script audit

For each important caster or specialist:

1. confirm the current unit, not merely its name;
2. confirm paths after items and modifiers;
3. confirm required gems are personal or otherwise accessible under the rule;
4. confirm the spell is researched and legal in the expected battle;
5. confirm the army will create the intended range and timing;
6. define acceptable fallback behaviour.

## 38. Items, Treasury, and Equipment

Clicking an empty item slot opens the treasury when the commander has laboratory access. Body form determines available slots. A mounted commander may have foot equipment disabled while mounted; barding belongs to the mount through the commander's mounted equipment relationship.

Some units have standard equipment that returns when a magical replacement is removed. This can make an inventory look as if an item appeared from nowhere. Inspect the unit's normal equipment before treating the result as duplication.

### 38.1 Treasury controls

- **F7** opens the Magic Item Treasury.
- **F8** opens the national Magic Item Overview.
- **Ctrl+A** sorts the treasury in current versions.
- Right-click items to inspect exact abilities and restrictions.
- Verify laboratory access before assuming an item can be equipped or returned.

Use the overview to locate a missing artifact before recreating it. An item on a remote or hidden commander is still part of national inventory but may not be transferable this month.

## 39. Gems and Gem Squiring

Any commander can carry up to forty gems. This permits non-mage commanders to transport gems as squires, even though they may not be able to spend them as a mage would.

Gem logistics has three distinct questions:

1. Does the nation possess the gems?
2. Can this commander access or carry them now?
3. Can the intended caster legally spend them for the order or battle?

The transfer interface and fast shortcuts answer the second question only. Book V owns [gem spending and magical logistics](#b5-part-iv-gems-slaves-and-magical-logistics).

### 39.1 Safe gem procedure

1. Open the relevant laboratory or transfer context.
2. Move the exact battle or ritual allocation.
3. Add a reserve only if the script and AI are permitted to spend it.
4. Check the commander's personal gem display.
5. Re-check after changing items, scripts, or movement.
6. Use the national overview or treasury controls to catch stranded stock.

Fast keys save time, but they can also create off-by-one errors. The final displayed count is authoritative.

## 40. Mounted Units and Reclaiming Mounts

Mounted units can lose or change their mounted state through battle and end-of-turn systems. Where the unit supports it, **Reclaim Mount** allows the rider to recover the appropriate mount relationship. Current versions also include end-of-turn handling for mounts.

Do not assume that a rider and mount remain a single unchanging card. Check movement, equipment slots, size, protection, and battlefield function after a mount loss or recovery. The combat consequences belong to [Book IV's mount chapter](#b4-part-ix-mounts-trampling-and-size).

# Part VII: Strategic Order Reference

## 41. Orders Are Requests with Preconditions

An order is checked when entered, but some preconditions can change before hosting reaches it. A legal movement arrow may remain visible even if an item that enabled the movement is removed. A ritual can fail because the caster, gems, laboratory, target, or path state changed. An army can reach a destination without the troops that were left in the garrison.

Every important order needs two checks:

- **entry legality:** the interface accepted it now;
- **resolution viability:** the required commander, route, army, item, gem, building, and target are expected to exist when the engine reaches it.

## 42. Ordinary Movement

A movement arrow connects origin and destination. It is not a promise that the commander will follow a particular visible route. Entering an enemy province generally creates combat; entering a friendly province containing a fort normally places the force inside that fort.

Friendly movement and hostile movement have different resolution relationships. Opposing forces can meet on either side or pass into one another's provinces depending on orders and the hosting sequence. Use [Book I](#b1-phase-iii-movement-and-conquest) for exact timing and [Book VI](#b6-friendly-hostile-and-intercepting-movement) for interception doctrine.

### 42.1 Movement audit

- movement mode is correct;
- commander and all squads can make the move;
- no item or shape change is providing a fragile movement entitlement;
- destination ownership is interpreted correctly;
- entering a friendly fort is intended;
- retreat and supply consequences are understood.

## 43. Sneak, Hide, and Attack Current Province

**Sneak** is the default movement mode for an eligible stealthy commander whose entire army can move stealthily. Holding **Ctrl** while selecting the destination can request normal movement instead. Removing the last non-stealth unit does not necessarily restore a previously changed defensive order to Sneak; inspect the displayed order.

**Hide** is the stationary default for a stealthy force in suitable circumstances. Hidden forces do not join an ordinary battle merely because friendly conventional troops fight there. If discovered, they can fight a separate detection battle.

**Attack Current Province** lets a hidden force in an enemy province emerge and attack without moving to another province. It can join friendly attackers arriving there. The distinction among Sneak, Hide, and Attack Current Province is operationally decisive:

| Intent | Correct family |
| --- | --- |
| Move unseen to another province | Sneak |
| Remain concealed here | Hide |
| Reveal and fight in this province | Attack Current Province |

## 44. Patrol and Move-and-Patrol

**Patrol** searches for hidden enemies and reduces unrest according to the patrolling force. A patroller outside a fort participates in exterior combat. Where there is no unrest, ordinary patrolling does not damage population merely for being performed.

**Move and Patrol** is assigned after entering movement into a friendly fort province. It can also be requested with the supported **Shift+Ctrl** destination shortcut. The force arrives outside the fort and is available to fight there; it becomes an ordinary Patrol order in the following month. It does not provide the same-turn stealth-search result that a stationary patrol would.

Use Move and Patrol when relief must arrive on the exterior rather than disappear inside a friendly fort. Verify the displayed compound order before leaving the province.

## 45. Defend

**Defend** means remain and fight without patrolling. In a friendly fort it generally concedes the exterior and places the force inside. A stealthy commander on Defend fights openly rather than remaining hidden.

This is one of the most common interface traps: “do nothing” is not a single order. Defend, Hide, Patrol, Research, and the relevant siege order have different participation in battle and control of the fort exterior.

## 46. Siege Orders

### 46.1 Maintain Siege

Only forces assigned to **Maintain Siege** contribute to breaking the walls. An army in the province performing another order should not be counted in the siege calculation.

### 46.2 Storm Castle

**Storm Castle** becomes available after fortification defence has been reduced to zero, and the assault occurs in the following hosted month. A relief battle or another exterior event can intervene before the storm. A zero-wall message gives permission to prepare an assault; it does not mean the fort has already fallen.

### 46.3 Break Siege

The besieged force uses **Break Siege** to sortie. Retreating survivors may return inside or escape to a legal adjacent friendly province according to the rules. If both sides try to force the decisive siege action at once, the relevant contest can determine which proceeds.

Book II owns [siege calculation](#b2-part-viii-siege-and-fort-control); Book IV owns the assault battle; Book VI owns the campaign clock.

### 46.4 Teleport movement from a siege

Since 6.35, commanders using teleport movement can move out of a besieged fort. Do not generalize this to ordinary strategic movement or to every ritual movement effect. Confirm the actual movement mode and current version.

## 47. Construction and Demolition Orders

The ordinary construction relationships are:

- a fort can be started by a commander allowed to construct it;
- a temple requires an eligible sacred commander;
- a laboratory requires an eligible mage.

Costs, nation modifiers, terrain, and completion timing belong to Book II and Book I.

**Demolish** takes one month for an eligible building. A temple cannot simply be voluntarily demolished under the ordinary rule; an enemy temple is destroyed when the province is captured. A fort cannot be demolished while it is under siege. Because demolition removes national infrastructure and can change access, it deserves the same audit as a movement order.

## 48. Religious and Divine Orders

### 48.1 Preach

An eligible priest can preach to strengthen friendly dominion, subject to Holy level and local limits. Book III owns the formula and strategic religious system.

### 48.2 Blood Sacrifice

An eligible national unit at a temple can sacrifice blood slaves where the nation permits it. Possessing slaves, priesthood, and a temple separately does not imply the order exists; the nation or unit must have the relevant ability.

### 48.3 Become Prophet

A nation can normally have one prophet. An eligible commander becomes a priest one level higher than before, or Holy 3 if that is higher, and gains prophet-related dominion effects. After a prophet dies, a six-turn interval applies before another can be appointed under the ordinary rule.

The order is both a religious investment and an opportunity cost for that commander during the appointment month. Book III owns the full consequences.

## 49. Research, Search, Forge, and Cast Ritual

These magic orders share a dependency pattern:

| Order | Essential checks |
| --- | --- |
| Research | Mage can research; school allocation still serves the target; local events have not removed the mage. |
| Search | Correct province and search mode; caster paths are relevant; movement and stealth expectations are not confused with the order. |
| Forge | Laboratory, path, research, gems, item availability, and artifact race. |
| Cast Ritual | Laboratory or specific exception, path, research, gems, target legality, range, and hosting timing. |

Ritual caster order is not a safe basis for precise informal sequencing. If two rituals depend on one another in the same month, verify the documented hosting relationship or separate them across months. Book I owns resolution order; Book V owns magical legality.

## 50. Pillage and Raid

**Pillage** converts local destruction into immediate gain. It raises unrest, kills population, damages supply conditions, and can produce gold and temporary provisions. Large, fast, frightening, barbarian, or otherwise suitable troops can be effective pillagers. The economic arithmetic belongs to Book II.

**Raid** is movement combined with pillaging under a commander with the Pillager ability and sufficient strategic army movement, ordinarily at least 20. Only units with the Pillager ability contribute to the pillaging component, and at half their ordinary pillage value. The force must win the province fight before the pillage occurs.

The order distinction is:

- Pillage destroys the province currently occupied.
- Raid attempts to move, win, and then damage the destination.

Both should be evaluated as campaign acts. Damage to a province that must soon be governed can cost more than the gold obtained.

## 51. Blood Hunt

An eligible blood hunter searches the province for blood slaves. The order risks unrest, population loss through subsequent enforcement conditions, and opportunity cost. High population and controlled unrest are operational considerations; exact hunting probability and economic doctrine belong to [Book II](#b2-part-xi-blood-economy).

Before assigning the order, confirm that patrol capacity, laboratory access for collection where needed, and a plan for transporting or spending slaves exist. Blood hunting without administration can immobilize the province that funds it.

## 52. Reanimate, Manikin, Contact Allies, and Capture Slaves

These are nation- or unit-specific orders rather than universal controls.

- **Reanimate** produces a permitted undead type. Ghouls consume population, Soulless draw on corpses, and Longdead can be raised without those two local stocks under the ordinary distinctions. Available forms depend on the reanimator.
- **Manikin** is associated with Asphodel's nature-death system and can depend on human population, corpses, and hostile dominion.
- **Contact Allies** occupies the commander for the month while gathering the defined allied troops.
- **Capture Slaves** is available to specific national actors, including ordinary manual examples in Mictlan and Nazca, and produces a small random group under the documented order.

The interface presence of one variant should never be generalized to every unit with similar lore. Right-click the actor and treat the exact ruleset as authoritative.

## 53. Espionage Orders

### 53.1 Instill Uprising

A Spy can increase unrest in an enemy province. This is an economic and administrative attack rather than a direct attempt to capture the province.

### 53.2 Infiltrate

Infiltration is performed in an enemy capital by a Spy. It can reveal mundane scoregraph information, with additional categories available when the infiltrator is a spellcaster or priest. The attempt can fail and expose the infiltrator; the official manual describes the ordinary success chance as roughly even before relevant conditions.

The order should be judged against the intelligence actually needed. Risking an established scout network to learn a graph already inferable from the map may be poor value.

## 54. Assassination and Abduction Orders

### 54.1 Assassinate

An assassin selects a random eligible enemy commander in the province. Bodyguards can accompany the victim when their individual checks succeed; the ordinary base is one chance in two per bodyguard before relevant modifiers. The victim is caught unprepared and does not follow an ordinary prepared battle script.

Assassination battlefields can include local features or bystanders. Fort walls block ordinary attempts into or out of a siege unless the actor has a relevant bypass such as Scale Walls, flight, or teleportation.

### 54.2 Seduction

Seduction targets an eligible commander of the opposite sex and tests morale. A successful target may escape toward a friendly adjacent province or, for some flying movement, toward the capital. Beauty improves the attempt. Failure can lead to an assassination battle.

### 54.3 Dream Seduction

Dream Seduction first confronts Magic Resistance and then morale. Penetration and Beauty can matter to the respective checks. Failure can create the special confrontation defined by the ability.

### 54.4 Corruption

Corruption resembles seduction in strategic purpose but Beauty does not improve it. Its exact actor and target restrictions remain ability-specific.

### 54.5 Lure of the Sirens

This coastal order tests resistance and morale without using Beauty. A successful victim can drown or face an underwater battle; failure does not create the same assassination response as ordinary seduction. Penetration can improve the magical component.

All five orders are asymmetric operations. The target pool, fort state, bodyguards, escape geography, actor survival, and information gained should be considered before the order is entered.

## 55. Strategic Order Quick Reference

| Intended act | Order | Principal operational trap |
| --- | --- | --- |
| Move openly | Move | Arrow survives a lost movement prerequisite or enters a friendly fort unexpectedly. |
| Move covertly | Sneak | A non-stealth unit prevents the army from sneaking. |
| Remain covert | Hide | Hidden force does not join an ordinary friendly battle. |
| Emerge here | Attack Current Province | Confused with movement to a neighbouring province. |
| Defend openly | Defend | Force inside a fort concedes the exterior. |
| Find hidden units/reduce unrest | Patrol | Not the same as Move and Patrol or Defend. |
| Arrive outside a friendly fort | Move and Patrol | Does not conduct a same-month stealth search on arrival. |
| Break walls | Maintain Siege | Other orders do not contribute siege strength. |
| Assault zero walls | Storm Castle | Relief and exterior battles can occur first. |
| Sortie | Break Siege | Retreat and concurrent siege action require careful interpretation. |
| Build | Construct Fort/Temple/Lab | Actor eligibility, cost, terrain, and timing differ. |
| Remove infrastructure | Demolish | Temples and besieged forts have special restrictions. |
| Produce research | Research | Mage-turn opportunity cost is easy to overlook. |
| Strategic magic | Cast Ritual | Lab, path, gems, range, target, and timing all bind. |
| Produce an item | Forge | Artifact competition and remote treasury access matter. |
| Find sites | Search | Search mode and paths may not match the province. |
| Strengthen dominion | Preach | Holy level and local dominion conditions govern effect. |
| Appoint religious leader | Become Prophet | One-prophet limit and six-turn replacement interval. |
| Extract blood slaves | Blood Hunt | Unrest and administrative support can bind. |
| Damage current province | Pillage | Permanent economic damage may exceed immediate return. |
| Move and damage | Raid | Requires Pillager commander, movement, qualifying units, and victory. |
| Raise special troops | Reanimate/Manikin/Contact Allies | Output and local inputs are unit-specific. |
| Attack administration | Instill Uprising/Infiltrate | Exposure risk and target value. |
| Remove or convert commanders | Assassin/Seduction family | Target pool, bodyguards, walls, escape, and actor survival. |

# Part VIII: A Guided First Campaign

## 56. The Learning Campaign

The first campaign should expose the whole game without hiding mistakes behind excessive advantages. A useful environment is:

- a small or medium land map with enough space for several expansion routes;
- a nation with understandable conventional troops and mages;
- ordinary or slightly forgiving independent strength;
- standard research and broadly standard economy;
- a clear Throne victory condition;
- few or no overhaul mods during the first pass;
- several AI opponents, followed by a second game against people.

The purpose is not to guarantee victory. It is to make every failure legible.

## 57. Before Turn One

Complete five preparations.

### 57.1 State the national idea

Write one paragraph covering:

- how the nation expands;
- what the capital produces every month;
- what the first non-capital fort contributes;
- the first two research objectives;
- how the Pretender supports the opening;
- what threatens the plan.

If the paragraph cannot be written, return to Books II, III, V, and VI. A list of strong units is not a national idea.

### 57.2 Test the expansion party

Use a disposable game to test the intended commander, troop count, formation, and orders against several independent types. Record losses rather than remembering only victories. Book VI owns [expansion testing](#b6-expansion-testing).

### 57.3 Save the Pretender

Save the actual design with **Ctrl+S** and label it with nation, age, ruleset, and purpose. A changed blessing, scale, or awakening state makes it a new design.

### 57.4 Prepare a simple turn record

Keep:

- province targets;
- recruitment plan;
- research target and expected arrival;
- fort and laboratory schedule;
- important gem and item commitments;
- contacts, borders, and treaty terms.

### 57.5 Learn the five screens

Before playing, open and close Army Setup, Recruitment, Nation Overview, Research, and Messages. The goal is familiarity, not optimization.

## 58. Turn One

Turn one is an allocation problem.

1. Read the starting messages and inspect the capital, commanders, troops, scales, sites, treasury, and neighbours.
2. Recruit the commander or mage required by the national plan.
3. Queue the tested expansion troops within the actual gold, resource, and Recruitment Point limits.
4. Set the first research target.
5. Organize the starting army. Confirm leadership, squad orders, formation, and commander script.
6. Decide whether the Pretender acts, researches, forges, searches, preaches, or remains unavailable according to awakening.
7. Inspect every adjacent province before choosing expansion direction.
8. Run the four-pass audit and end the turn.

The first turn should create a repeatable monthly process. Spending all gold can be correct; spending it without knowing which local constraint limited the queue is not.

## 59. Turns Two to Four: Establish the Expansion Cycle

The opening cycle is:

`recruit -> assemble -> capture -> reinforce -> launch the next party`

During these turns:

- review every expansion battle rather than accepting the flag change;
- separate recoverable attrition from a failed party design;
- keep capital commander production aligned with troop output;
- identify the first fort location from income, resources, recruitment purpose, geometry, and safety;
- start scouting beyond the immediate expansion ring;
- watch supply and movement compatibility;
- preserve enough gold to avoid delaying the first key infrastructure decision by accident.

### 59.1 When an expansion battle fails

Diagnose in order:

1. Was the province scouted accurately?
2. Did the intended troops and commander arrive?
3. Did formation and orders match the tested version?
4. Was the independent type a known bad matchup?
5. Was the loss statistical variation or a structural weakness?
6. Can the survivors retreat, regroup, or defend?
7. Does the recruitment cycle need revision?

Do not answer a formation failure by buying more of the same formation without review.

## 60. Turns Five to Eight: Build the Second Centre

By this stage, the nation should be converting expansion into administration.

### 60.1 First fort purpose

Choose the fort for a declared function:

- recruit a valuable non-capital mage or troop;
- collect regional resources;
- shorten reinforcement routes;
- secure a chokepoint or rich cluster;
- establish a laboratory and research centre;
- support a future border.

The fort is not finished strategy. It still needs the right laboratory, temple where required, commander recruitment, roads of movement, and defensible surroundings.

### 60.2 Research checkpoint

At the end of this interval, compare expected and actual research. A shortfall can result from:

- too few recruited mages;
- mages diverted to expansion or infrastructure;
- unexpected deaths;
- Drain or other ruleset consequences;
- the chosen fort not yet producing researchers;
- research points assigned across too many schools.

Book V owns the solution tree. Book X's contribution is to make the discrepancy visible early.

### 60.3 First magical package

Prepare one package that can actually be delivered: a small battlefield script, a site-search route, a useful item chain, or a ritual with a clear strategic purpose. Confirm research, path, gems, laboratory, caster turn, and destination.

## 61. Turns Nine to Twelve: Form the National Shape

The nation should now have:

- a capital role that is not constantly improvised;
- at least one expansion or security formation that can be reproduced;
- a second recruitment or research centre under construction or active;
- scouts watching likely borders;
- a research threshold with a force attached to it;
- a reserve plan for an unexpected neighbour.

This is also the moment to inspect inefficiency. Use **F1** to find idle commanders, stalled queues, excessive garrisons, researchers carrying unused items, and provinces whose unrest or infrastructure does not match their purpose.

## 62. First Contact

On meeting another player, separate facts from stories.

Facts include visible provinces, army icons, dominion, fort locations, scouts lost, public graphs, and direct messages. Stories include guessed research, supposed weakness, claimed enemies, and implied peaceful intent.

A useful first-contact record states:

- exact border proposal by province number or unmistakable landmark;
- whether movement, scouting, preaching, raiding, and remote magic are addressed;
- duration and cancellation terms of any non-aggression pact;
- communication channel and timing convention;
- unresolved provinces or Thrones.

Book VI owns diplomacy and intelligence. The operational standard is that the agreement can be read later without reconstructing tone.

## 63. Preparing the First War

Do not begin with “attack the neighbour.” Define:

1. the political purpose;
2. the first-turn objectives;
3. the enemy response most likely to break the plan;
4. the research and magic package available on the attack turn;
5. the routes for main force, raiders, scouts, and reinforcements;
6. the siege force and assault plan;
7. the point at which the war is no longer worth its cost.

Then translate the plan into interface commitments:

- commanders selected correctly;
- squads transferred and led;
- movement arrows checked;
- stealth forces using the intended mode;
- gems and items delivered;
- scripts legal;
- recruitment continuing behind the front;
- diplomacy sent before the deadline;
- turn submitted and confirmed.

The last list is deliberately mundane. Wars are lost by mundane omissions.

## 64. The First Siege

When a hostile fort is reached:

1. confirm which units are assigned to Maintain Siege;
2. estimate wall-breaking strength using Book II;
3. screen the exterior against relief and raiding;
4. preserve supply and reinforcement routes;
5. prepare the storming formation before the walls fall;
6. monitor enemy movement, magic, and possible break-siege force;
7. when defence reaches zero, assign Storm Castle and re-check for relief sequencing;
8. after capture, decide immediately whether the fort is a front, a recruitment centre, a trap, or a demolition candidate.

A siege is not a pause between real battles. It is an administrative contest conducted under threat.

## 65. Entering the Midgame

The learning campaign has reached the midgame when decisions are governed by interacting systems rather than a single expansion loop. Typical signs are:

- several forts and laboratories compete for gold;
- research opens multiple viable packages;
- gems must be allocated among battle, ritual, forging, and reserve;
- more than one border can become active;
- diplomacy changes which military move is safe;
- Thrones become practical objectives;
- specialist commanders require items, gems, and transport.

At this point, use the [Reader's Guide](#guide-readers-guide-and-concordance) by live problem. The foundation has succeeded when the next question can be located precisely.

## 66. Ending the First Game Well

Play through the endgame if possible. Dominions changes when armies become magically dense, globals alter the world, Thrones can be claimed in combinations, and research approaches its final tiers. A player who restarts every imperfect opening never learns conversion.

After victory or defeat, review:

- revealed scoregraphs and map;
- first divergence between plan and result;
- recruitment and research bottlenecks;
- battles whose replay contradicted expectations;
- wasted gems, items, forts, or commander turns;
- diplomatic predictions that proved wrong;
- the final opportunity to contest or secure victory.

Write three changes for the next game. More than three often turns evidence into a wish list.

# Part IX: Troubleshooting by Symptom

## 67. Cannot Find or Join the Game

Check in this order:

1. exact game name and lobby/server;
2. network connection and lobby availability;
3. game status: pretender collection, running, hosting, or finished;
4. Dominions version;
5. required mod files and activation;
6. map availability where locally required;
7. player or game password;
8. whether the nation is already claimed or was set to AI;
9. host announcements or maintenance.

Preserve the error text. “It does not work” discards the best evidence.

## 68. Mod or Map Mismatch

Symptoms include refusal to load, missing graphics, different unit cards, checksum complaints, or impossible replay behaviour.

Repair procedure:

1. stop changing files;
2. obtain the host's exact file identity;
3. compare names, versions, sizes, and hashes where available;
4. remove only the incorrect campaign copy from active use without destroying the archive;
5. install the canonical file with its directory structure;
6. restart Dominions;
7. test in a disposable game if the error persists.

Do not download “the latest” unless the latest is the frozen campaign version.

## 69. A Commander Will Not Move

Inspect:

- commander is selected and has not been given another order;
- destination is a legal neighbour or special-movement target;
- strategic movement allowance and terrain costs;
- all assigned troops and mounts can accompany the commander;
- stealth mode and non-stealth units;
- immobility, shape, item, disease, or other status;
- siege restrictions and the exact movement method;
- plane and map layer;
- whether the visible arrow depends on an item already removed.

If the interface accepted an arrow but hosting did not move the force, compare entry legality with resolution viability.

## 70. A Force Entered a Fort or Missed the Exterior Battle

Ordinary movement into a friendly fort commonly enters it. To arrive outside for immediate exterior duty, use Move and Patrol where legal. A force on Defend inside the fort concedes the exterior. A hidden force does not automatically join conventional allies.

Diagnose by displayed order, fort ownership, stealth state, and hosting phase—not by where the arrow seemed to end.

## 71. An Order Disappeared or Changed

Common causes include:

- another order was entered afterward;
- army composition changed the legality of Sneak or movement;
- the commander changed shape, mount, item, or path state;
- a copied order was not legal for the recipient;
- the commander became besieged or changed sides;
- the order completed and returned to a default state;
- a stale preserved or replaced behaviour differently than expected.

Use **F1**, inspect the commander, and reconstruct the last legal state. Do not infer an engine bug before checking the dependency that disappeared.

## 72. Recruitment Is Dimmed or Stalled

Check gold first, then local resources, Recruitment Points, Commander Points, Holy Points, recruitment limits, fort/site/terrain prerequisites, and whether the unit is capital-only. Inspect the queue order: an expensive earlier unit can consume capacity needed by later entries.

If the province has changed ownership or become besieged, re-evaluate where recruits appear and whether the national roster remains available.

## 73. Troops Did Not Move with the Commander

Open Army Setup and confirm that the units were in that commander's squads rather than in the unassigned garrison or under another commander. Then check leadership type, leadership capacity, movement compatibility, and whether the commander survived an earlier hosting event.

An army icon in the same province does not prove command attachment.

## 74. An Item or Gem Cannot Be Used

Check:

- laboratory access for treasury transfers;
- body slots and mounted slot restrictions;
- item ownership and unique status;
- path and research requirements;
- commander's personal gem allocation;
- maximum carried gems;
- whether the resource is national stock, local treasury access, or personal inventory;
- whether the relevant order permits that gem or item effect.

Use **F8** to find items nationally. For gems, inspect both national totals and the actual commander.

## 75. A Ritual or Forge Order Is Unavailable

Confirm laboratory, research school and level, path after current items and shapes, gem stock, target range and type, ritual or item restrictions, artifact availability, and current ruleset. A commander who moved, was sieged, or lost laboratory access may no longer meet the order's conditions.

If several rituals were intended to enable one another in one month, revisit [Book I's hosting sequence](#b1-the-complete-63-step-hosting-sequence).

## 76. A Siege Is Not Progressing

Check that the relevant force is on Maintain Siege, not Defend, Patrol, Research, Pillage, or another order. Compare siege strength with fortification repair and defender strength. Confirm whether a battle, movement, relief, or supply problem removed key siegers.

Zero wall defence does not capture the fort. Storming is a separate order for the next resolution.

## 77. Scoregraphs Are Missing or Incomplete

The game may have hidden graphs. Intelligence may reveal only some categories. A Spy in an enemy capital can infiltrate, while spellcaster or priest qualities can broaden obtainable information. Confirm the game setting and current intelligence before treating an empty graph as a display fault.

## 78. A Turn Staled

Preserve the submission status, deadline, host messages, and any connection error. Notify the host without editing files. The response depends on the published policy: continuation, extension before hosting, substitution, or a rare rollback for verified technical failure.

Afterward, reduce recurrence:

- submit an early complete version;
- confirm receipt;
- request extensions earlier;
- avoid making the only final submission in the last minutes;
- maintain a backup connection method if the campaign warrants it.

## 79. A Battle Replay Looks Impossible

Compare host and client versions, mod identity, and whether the replay is being viewed under the ruleset that generated it. Inspect messages and final unit state. Visual playback can diverge from the hosted result when versions differ. Preserve the turn and replay evidence before updating or replacing files.

## 80. Performance or Large-Turn Problems

Current versions have improved handling of larger network turns, but late games can still be demanding. Close unnecessary applications, preserve disk space, avoid repeatedly interrupting transfers, and allow the client to finish processing. If a file appears corrupt, retain it and compare with a fresh host download rather than overwriting the only copy.

Performance diagnosis should separate:

- slow local interface;
- slow battle replay;
- network transfer delay;
- lobby or server availability;
- hosting computation;
- a genuinely damaged file.

## 81. Recovery Principle

Use the least destructive repair:

`observe -> record -> compare baseline -> copy/backup -> test separately -> replace only the confirmed faulty component`

Random reinstallations, live mod edits, and broad deletion destroy evidence. Recovery should make the campaign more reproducible, not only make the current error disappear.

# Part X: Hosting as a Competitive Institution

## 82. The Host Is Custodian, Not Author of Outcomes

The host establishes procedure, keeps the service available, applies announced rules consistently, and preserves recoverability. The host should not use privileged knowledge or flexible administration to shape the strategic result.

A host decision is strongest when it can be explained as:

1. the published rule;
2. the observed event;
3. the evidence preserved;
4. the same remedy that would apply to any player.

## 83. Hosting Runbook

### 83.1 Before launch

- freeze version, map, and mods;
- publish settings and victory conditions;
- test lobby/server and content distribution;
- collect pretenders with passwords;
- verify roster and teams;
- publish timer, extension, stale, substitution, and rollback policy;
- establish a backup host or continuity plan.

### 83.2 During the campaign

- announce deadline changes with an exact date, time, and timezone;
- check that hosting completed and clients can receive the new turn;
- preserve periodic backups appropriate to the hosting system;
- record stales, substitutions, rollbacks, and version incidents;
- avoid inspecting privileged player information except when technically required and allowed;
- resolve disputes from the charter and evidence.

### 83.3 At campaign end

- preserve final state long enough for review;
- publish result and any shared post-game materials;
- permit scoregraph and map analysis;
- record ruleset and notable administrative incidents;
- archive or remove credentials securely.

## 84. Tournament and Expert Records

Serious competitive play benefits from a more exact record:

- file hashes for map and mods;
- host executable and operating environment;
- creation settings captured in text or screenshots;
- player/nation/team roster;
- every hosting timestamp;
- stales, extensions, substitutions, and connection incidents;
- mod or patch deviation, even if accidental;
- final victory state.

This is not bureaucracy for its own sake. It permits later rulings and analysis without relying on the memory of interested parties.

## 85. Dispute Handling

When a dispute occurs:

1. pause any irreversible administrative action if the schedule permits;
2. identify the exact claim;
3. preserve messages, timestamps, versions, files, and settings;
4. consult the charter and official rule source;
5. distinguish interface misunderstanding, engine behaviour, technical failure, and conduct;
6. apply the narrowest consistent remedy;
7. record the decision.

Not every bug justifies a rollback. Not every surprising result is a bug. Not every policy omission can be repaired fairly after hidden information has changed hands.

# Part XI: Operational Checklists

## 86. New Installation

- Launch the game and confirm version.
- Open the user data directory from Game Tools.
- Install required maps and mods with directory structure intact.
- Enable the exact stack.
- Test a disposable world.
- Save a labelled Pretender design.
- Learn Messages, Recruitment, Army Setup, Nation Overview, and Research.

## 87. Create World

- Confirm map and player count.
- Choose age.
- Add every participant and set human/AI status.
- Verify disciple teams if used.
- Record all non-default settings.
- Record scoregraph, security, artifact, and legendary-research rules.
- Set and verify victory conditions and Cataclysm.
- Protect Pretenders and administrative access.
- Publish hosting policy before launch.

## 88. Join a Lobby Game

- Match Dominions version.
- Match map and mod files.
- Enter Network, then the official lobby.
- Select the exact game.
- Confirm nation and status.
- Use the game password securely.
- Inspect the current turn before entering orders.
- Confirm submission after End Turn.

## 89. Build an Army

- Choose role and campaign purpose.
- Recruit within all local constraints.
- Provide suitable leadership.
- Transfer troops from the garrison.
- Divide no more than five squads per commander.
- Position squads and commanders.
- Assign squad orders and scripts.
- Equip items and gems.
- Confirm movement and supply compatibility.
- Re-open the screen after major transfers.

## 90. Issue a Special Order

- Confirm actor has the ability.
- Confirm province and target.
- Confirm building, terrain, path, gem, population, corpse, or other input.
- Check siege and fort-wall restrictions.
- Check hosting timing and opportunity cost.
- Enter the order.
- Inspect the displayed result.
- Re-check after changing movement, army, items, or infrastructure.

## 91. Submit a Turn

- Read all new messages.
- Review battles and changed provinces.
- State monthly priorities.
- Enter fragile dependent orders first.
- Audit commanders, armies, state, and campaign.
- Submit before the deadline margin disappears.
- Confirm receipt.
- If revising, resubmit and confirm again.

## 92. Host a Campaign

- Freeze and publish ruleset.
- Test creation and connection.
- Publish timer and policies.
- Protect passwords and host state.
- Announce exact deadline changes.
- Back up without creating unapproved alternate histories.
- Apply rules symmetrically.
- Preserve incident evidence.
- Arrange substitution or AI conversion according to policy.
- Archive the final game for review.

# Part XII: Essays

## Essay I: Interface Literacy Is Strategic Power

The interface is often treated as a transparent layer between a player and the “real” game. In Dominions it is closer to a language. Province filters determine which relationships become visible. Army Setup determines whether a force exists as an army or as unrelated bodies in one province. A movement arrow records an intention but carries hidden dependence on leadership, terrain, items, stealth, siege state, and hosting order. The Nation Overview converts a sprawling realm into an administrative object that can actually be governed.

This creates a form of power that is easy to undervalue because it does not appear on a unit card: the ability to ask the game the right question quickly. Where are the idle mages? Which forts are producing commanders? Which province changed income? Which movement depends on one item? Which caster holds the gems? Which squad was left unassigned? Each answer recovers a little national capacity.

For a new player, interface literacy reduces cognitive load. Shortcuts and filters stop ten provinces from feeling like ten separate games. For an expert, the same literacy increases strategic bandwidth. Less time spent finding information means more time comparing lines, testing assumptions, communicating, and auditing adversarial possibilities.

There is no need to memorise every key. What matters is building reliable routes through the interface. Messages begin the month. F1 surveys the nation. Map filters expose one strategic concern at a time. Army Setup proves attachment and command. F7 and F8 prove equipment location. The final audit proves commitment. Once those routes become habitual, the game's complexity becomes searchable instead of overwhelming.

## Essay II: Administrative Failure Is Still Strategic Failure

Dominions rewards elaborate plans, which makes clerical errors feel somehow beneath strategy. They are not. If a commander moved without the intended squad, the nation did not possess that army at the decisive place. If a caster lacked one gem, the spell package did not exist. If a turn was not received, the plan was absent from the shared game. The reason may be administrative, but the strategic world contains only the result.

This does not mean every mistake deserves punishment without context. Technical services fail, emergencies happen, and hosts need humane policies. It means that personal preparation should treat operational reliability as part of force design. A formation includes its transfer procedure. A ritual includes laboratory access and target selection. A timing attack includes submission before the timer. A long campaign includes passwords, backups, and substitution rules.

The best control is a short, repeatable audit, not constant anxiety: important commanders, armies, state, campaign, receipt. It turns a vague fear of forgetting something into a bounded procedure. It also improves analysis after failure. When the submitted orders are known, tactical and strategic theories can be tested against evidence instead of reconstructed from regret.

## Essay III: The Host as Custodian

The host occupies an unusual position. The role is technically powerful but should be strategically neutral. A host determines deadlines, operates the game state, holds recovery tools, and may be able to access information unavailable to ordinary players. The campaign remains legitimate only when that power is exercised as custody rather than ownership.

Custody begins before turn one. Rules are published while no one knows whom they will favour. Extension and rollback standards exist before a leading army is at risk. A backup host is chosen before absence becomes leverage. Version and mod records are frozen before an update offers convenient ambiguity.

During play, good administration is conspicuously exact: a deadline includes date, time, and timezone; an extension is visible to everyone; a stale is recorded; a substitute receives the same access process another substitute would receive; a rollback requires a narrow technical reason. The host does not need to eliminate judgment, which is impossible. The host needs to make judgment reviewable.

That standard protects the host as much as the players. Evidence replaces accusation. A charter replaces improvised favour. A campaign can survive mistakes because its continuity does not depend on one person's memory or goodwill.

# Part XIII: Authority, Version Notes, and Research Boundaries

## 93. Sources Used

Book X is based primarily on:

- the official *Dominions 6 Manual* for creation, interface, multiplayer modes, recruitment, army setup, inventories, movement, and strategic orders;
- Illwinter's official Dominions 6 documentation index;
- Illwinter's official Steam announcements through Dominions 6.36 for current interface, lobby, network, mount, siege-movement, and post-game changes;
- the official modding and file-format manuals where local data structure is relevant;
- the verified foundation books in this library for mechanics whose canonical explanations already exist.

Official documentation:

- https://www.illwinter.com/dom6/docs.html
- https://www.illwinter.com/dom6/dom6manual.pdf
- https://steamcommunity.com/app/2511500/announcements/

## 94. Version-Sensitive Boundaries

Exact private-server command lines, unattended host options, and external PBEM automation are not frozen here. They depend on the current executable, platform, and hosting environment. The official manual itself refers some private-server and PBEM detail to earlier documentation. Copying old commands into a current operational encyclopaedia would create false certainty.

Keyboard shortcuts are context-sensitive and continue to evolve. Book X records verified high-value controls, but **?** in the active screen and current official patch notes remain the authority for a specific release.

## 95. Evidence Labels for Operational Reports

When a result differs from Book X, record it as one of:

- **confirmed interface fact:** reproduced on the named version and screen;
- **confirmed engine result:** reproduced through hosting under a frozen ruleset;
- **version divergence:** host and client or guide and executable differ;
- **mod divergence:** a mod changes or replaces the ordinary control or order;
- **unresolved report:** evidence is incomplete or reproduction has not succeeded.

This protects the library from turning a single surprising turn into a universal rule.

## 96. Closing Principle

Dominions becomes manageable when intentions are converted into inspectable commitments. Freeze the ruleset. Read the new state. Use the interface as an analytical instrument. Enter orders with their dependencies. Audit the nation. Confirm submission. Preserve evidence when reality disagrees.

The process is not separate from mastery. It is the structure that allows mastery to survive contact with a live game.
