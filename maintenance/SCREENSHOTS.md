# Screenshots after the conservative review

Original illustrations remain at their original paths for unchanged sections.
They are historical illustrations retained intentionally, not captures of 9.1.

There are **17 PNG placeholders** under `_static/screenshots/9.1/`:
16 for new or changed controls and one for the calculated-field menu image
missing from the original repository. The My Account section also contains a
plain reStructuredText **Screenshot to update** admonition.

`screenshots-9.1.csv` lists each PNG, its page, caption, old path and placeholder
hash. Line numbers are indicative; use the file name as the stable identifier.

1. Capture the relevant screen in Knowage 9.1.0 with demonstration data.
2. Replace the PNG at the same path and update the caption/alt text as needed.
3. Set the inventory status to `ready` and run `make check`.
4. Replace the My Account admonition with a standard `figure` directive when
   its capture is available; include that file in the inventory.

The checker reports unchanged placeholder hashes as pending captures.
The complete replacement `_static` folder contains only used PNGs and the
documentation stylesheet. Replace the old folder in full, not by merging files,
so obsolete placeholders are removed.
