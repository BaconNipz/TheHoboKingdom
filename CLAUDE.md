# Working on TheHoboKingdom

Claude is the main editor of this site. Keep changes small, show before-and-after screenshots for visual work, and wait for approval before anything reaches `main`.

## Build and check

GitHub Pages builds the site with Jekyll from `main`.

```sh
gem install jekyll --no-document          # once per container
ruby "$(gem contents jekyll | grep 'exe/jekyll$')" build -d <out>
node scripts/check-built-site.mjs <out>   # internal links
node scripts/check-toolkit.mjs            # tools, records, library manifest
```

CI (`.github/workflows/check-site.yml`) also runs `node --check` on every file in `assets/*.js`.

## Where things live

- `_data/projects.yml`: one record per project. It feeds the cards, hub status strips, and the homepage. Optional `logo:` replaces the letter `mark` on the card.
- `_data/updates.yml`: the homepage update list, update archive, and feed.
- `_data/search.yml`: site-search entries. Rename a project here too.
- `_layouts/default.html`: sets `data-project` on `<body>` from `project_id` or the first URL segment. It adds `has-compact-hero` on individual tool pages.
- `assets/site.css`: design tokens at the top. Project accent colours are in the "Project accent colours" block near the end.
- `assets/fonts/`: self-hosted Inter (OFL). Do not load fonts or scripts from third-party hosts.
- `assets/images/projects/`: project artwork. Use WebP for page images and a 1200×630 JPG for `og_image`.

## Conventions

- Public copy follows `docs/site-writing-voice.md`.
- `nav_section` is one of home, projects, guides, tools, downloads, about, search. Tool pages use `tools`.
- Only projects with real substance or development get a hub. Early ideas stay off the site until they have something to show.
- Keep private material off the site: personal business details, study notes, and anything a project's owner has not cleared for publication.
