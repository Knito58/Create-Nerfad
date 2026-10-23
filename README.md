# Create: Nerfad

**Create: Nerfad – Not Enough Recipes For A Dummy**

Extra recipes for Create Fly and Create Fly Fly (mixing, compacting, crushing, haunting, smoking)
plus a few vanilla crafting recipes, for Minecraft 26.1.2, 26.2 and 26.3. Fabric only (the fluid amounts are in Fabric units).

- `create_nerfad/` holds the mod's files exactly as they go into the jar.
- `art/` holds the icon sources (GIMP) and `add_ring.py`, which makes the ringed icons (white ring, transparent outside) from `new_nerfad_icon2.png`.
- `removed/` holds recipes that were taken out of the mod.

Build the jar with `./build.sh` (needs `zip`); it lands in `build/`.
Publishing to CurseForge and GitHub Releases: Actions tab → Publish → Run workflow.

The changelog is in [create_nerfad/readme.txt](create_nerfad/readme.txt).

## How this mod is made

This mod is written by Claude AI: the recipes, the metadata and the descriptions.
Konitor decides what goes in and tests every version in game.
The first versions were made with hints from Google AI.
The icon is hand-made by Konitor in GIMP; no images are AI-generated. Claude only added the white ring and the transparent outside with `art/add_ring.py`.
