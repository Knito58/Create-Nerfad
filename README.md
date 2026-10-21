# Create: Nerfad

**Create: Not Enough Recipes For A Dummy**

Extra recipes for Create Fly and Create Fly Fly (mixing, compacting, crushing, haunting, smoking)
plus a few vanilla crafting recipes, for Minecraft 26.2 and 26.3. Works on Fabric, Forge and NeoForge.

- `create_nerfad/` holds the mod's files exactly as they go into the jar.
- `art/` holds the icon sources (GIMP).
- `removed/` holds recipes that were taken out of the mod.

Build the jar by zipping the *contents* of `create_nerfad/`:

```
cd create_nerfad && zip -r ../create_nerfad-1-2-10.jar . -x todo-after-fly-update.txt
```

The changelog is in [create_nerfad/readme.txt](create_nerfad/readme.txt).

## How this mod is made

This mod is written by Claude AI: the recipes, the metadata and the descriptions.
Konitor decides what goes in and tests every version in game.
The first versions were made with hints from Google AI.
The icon is hand-made by Konitor in GIMP; no images are AI-generated.
