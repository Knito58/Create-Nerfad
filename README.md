# Create: Not Enough Resources For A Dummy (Nerfad)

Extra recipes for the Create Fly mod (mixing, compacting, crushing, haunting, smoking)
plus a few vanilla crafting recipes. Works on Fabric, Forge and NeoForge.

- `create_nerfad/` holds the mod's files exactly as they go into the jar.
- `art/` holds the icon sources (GIMP).
- `removed/` holds recipes that were taken out of the mod.

Build the jar by zipping the *contents* of `create_nerfad/`:

```
cd create_nerfad && zip -r ../create_nerfad-1-2-9.jar . -x todo-after-fly-update.txt
```

The changelog is in [create_nerfad/readme.txt](create_nerfad/readme.txt).
Made with help from Google AI and Claude.
