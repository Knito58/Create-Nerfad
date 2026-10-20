# Create: Not Enough Recipes For A Dummy (Nerfad)

Extra recipes for the Create Fly mod (mixing, compacting, crushing, haunting, smoking)
plus a few vanilla crafting recipes, for Minecraft 26.2 and 26.3. Works on Fabric, Forge and NeoForge.

- `create_nerfad/` holds the mod's files exactly as they go into the jar.
- `art/` holds the icon sources (GIMP).
- `removed/` holds recipes that were taken out of the mod.

Build the jar by zipping the *contents* of `create_nerfad/`:

```
cd create_nerfad && zip -r ../create_nerfad-1-2-10.jar . -x todo-after-fly-update.txt
```

The changelog is in [create_nerfad/readme.txt](create_nerfad/readme.txt).
Claude AI does the work; Konitor tests and decides. The first versions had hints from Google AI.
