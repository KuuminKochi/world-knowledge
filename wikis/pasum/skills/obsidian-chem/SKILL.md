---
name: obsidian-chem
description: Help users work with the Obsidian Chem plugin for rendering chemical structures from SMILES strings. Use when the user mentions chemical structures, SMILES, molecular formulas, chemistry notes in Obsidian, the Chem plugin, RDKit, smiles-drawer, or rendering molecules in Obsidian. Also use when discussing chemistry note-taking workflows, converting chemical names to SMILES, or exporting chemical structure images from Obsidian.
---

# Obsidian Chem Plugin Skill

Help users render, configure, and troubleshoot chemical structures in Obsidian using the **Chem** plugin (by Acylation). This plugin renders SMILES strings as 2D chemical structure images using `smiles-drawer` and `RDKit.js`.

## Quick Reference

### Render SMILES as Chemical Structures

**Code block syntax** (recommended for multiple structures):

````markdown
```smiles
C1=CC=CC=C1
CC(=O)OC1=CC=CC=C1C(=O)O
```
````

Each line must contain exactly one valid SMILES string — no labels, comments, or markdown inside the code block. Labels and descriptions go outside. The data is plain text — portable and future-proof.

**Inline syntax** (requires enabling in Settings → Chem → Inline Render):

```markdown
$smiles=C1=CC=CC=C1
```

The prefix `$smiles=` is configurable in settings.

### Plugin Settings Overview

| Setting | What it controls |
|---------|-----------------|
| **Core** | Rendering engine: `smiles-drawer` (default) or `rdkit` |
| **Theme** | Light/dark color scheme for structure images |
| **Scale** | Relative size multiplier for structures |
| **Width** | Fixed image width (overrides scale if set) |
| **Compact Drawing** | Minimize whitespace around structures |
| **Explicit Hydrogens** | Show hydrogen atoms explicitly |
| **Explicit Methyl** | Show terminal methyl groups |
| **Inline Render** | Enable `$smiles=` prefix recognition |
| **Dataview** | Allow Dataview/DataviewJS queries inside `smiles` blocks |
| **Copy/Export** | PNG scale, transparency, and theme for copied images |

### Copy & Export

Right-click any rendered structure → **Copy as PNG**.

Paste into your note to save the image as a file in your attachment folder. Configure export scale, transparency, and theme in plugin settings.

## SMILES Syntax Rules

Correct SMILES syntax is essential for the Chem plugin to render structures properly. These rules are derived from the [OpenSMILES specification](http://opensmiles.org/opensmiles.html) and [Wikipedia's SMILES reference](https://en.wikipedia.org/wiki/Simplified_Molecular_Input_Line_Entry_System).

### Atom Representation

| Rule | Correct | Wrong | Why |
|------|---------|-------|-----|
| Organic subset atoms (B, C, N, O, P, S, F, **Cl**, **Br**, I) can omit brackets only when **neutral**, normal valence, normal isotope, and not chiral | `CCO` (ethanol) | — | Ethanol is neutral with normal valences |
| **Charged atoms MUST use brackets** with explicit charge | `[Cl-]` | `Cl` (means HCl) | Uncharged `Cl` is HCl, not chloride ion |
| Similarly for other ions | `[Na+]`, `[OH-]`, `[NH4+]`, `[Fe+3]`, `[S-2]` | `Na+`, `OH-`, `NH4+` | Unbracketed ions are invalid SMILES |
| Hydrogen on bracketed atoms is explicit | `[NH4+]` (4 hydrogens), `[OH-]` (1 hydrogen implied) | `[N+]` (would mean bare N⁺) | H count follows the element, then charge sign |

### Bonds

| Symbol | Meaning | Example |
|--------|---------|---------|
| (none) | Single bond (implicit) | `CC` = ethane |
| `-` | Single bond (explicit, optional) | `C-C` = same as `CC` |
| `=` | Double bond | `C=O` (formaldehyde), `O=C=O` (CO₂) |
| `#` | Triple bond | `C#N` (HCN), `N#N` (N₂) |
| `$` | Quadruple bond | `[Ga+]$[As-]` |
| `.` | **Non-bond** (disconnected components) | `[Na+].[Cl-]` (NaCl), `[Cu+2].[O-]S(=O)(=O)[O-]` (CuSO₄) |

> [!important] The dot `.` is critical for ionic compounds
> `[Na+].[OH-]` renders NaOH as separated ions — correct.
> `NaOH` without brackets/dots is INVALID (Na and OH are not in organic subset without charge).

### Aromatic Rings

Use **lowercase** letters for aromatic atoms:

| Aromatic atom | SMILES | Example |
|---------------|--------|---------|
| Carbon | `c` | `c1ccccc1` (benzene) |
| Nitrogen | `n` | `n1ccccc1` (pyridine) |
| Oxygen | `o` | `o1cccc1` (furan) |
| Sulfur | `s` | `s1cccc1` (thiophene) |
| N with H | `[nH]` | `n1c[nH]cc1` (imidazole) |

> [!note] Single bonds between aromatic rings must be explicit: `c1ccccc1-c2ccccc2` (biphenyl).

### Branching and Rings

- **Branching**: Parentheses `()` — e.g., `CC(=O)O` (acetic acid), `FC(F)F` (fluoroform)
- **Ring closures**: Digits 1-9 after the atom — e.g., `C1CCCCC1` (cyclohexane)
- **Multi-digit rings**: Precede with `%` — e.g., `C%10` for ring 10
- Ring numbers may be reused after the first ring closes

### Stereochemistry

| Notation | Meaning | Example |
|----------|---------|---------|
| `@` | Counter-clockwise tetrahedral | `N[C@@H](C)C(=O)O` (L-alanine) |
| `@@` | Clockwise tetrahedral | `N[C@H](C)C(=O)O` (D-alanine) |
| `/` and `\` | Directional bonds (E/Z) | `F/C=C/F` (trans), `F/C=C\F` (cis) |

### Special Cases

| Case | Correct SMILES | Note |
|------|---------------|------|
| Generic R-group placeholder | `*` (wildcard) | Do NOT use `[R]` — that is Rutherfordium (element 104) |
| Water | `O` (preferred) or `[OH2]` | Implicit hydrogens fill normal valence |
| Hydrogen gas | `[H][H]` | H is not in organic subset without brackets |
| Diatomic halogens | `BrBr`, `ClCl`, `FF`, `II` | Each halogen has valence 1, single bond implicit |
| Reaction SMILES (extension) | `REACTANT>>PRODUCT` | Separates reactants and products; may not render in all plugins |

### Common SMILES Errors to Avoid

| Error | Wrong | Correct | Explanation |
|-------|-------|---------|-------------|
| Chloride ion without brackets | `Cl` | `[Cl-]` | `Cl` = HCl (neutral); chloride needs `[Cl-]` |
| Bromide ion without brackets | `Br` | `[Br-]` | `Br` = HBr; bromide needs `[Br-]` |
| Sodium ion without brackets | `Na+` | `[Na+]` | All charged atoms need brackets |
| Hydroxide without brackets | `OH-` or `OH` | `[OH-]` | `O` = H₂O; hydroxide must be `[OH-]` |
| Ammonium without brackets | `NH4+` | `[NH4+]` | Charged species need brackets |
| Ionic compound without dots | `NaOH` | `[Na+].[OH-]` | Disconnected ions use `.` separator |
| `[R]` for generic group | `[R]` | `*` | `[R]` is element 104 (Rutherfordium) |
| Uncharged acid instead of ion | `Cl.[NH4+]` | `[Cl-].[NH4+]` | Both components must have correct charges |

> [!tip] Quick self-check
> Before committing SMILES to a note, verify: (1) Are all charged atoms in brackets? (2) Are ionic compounds dot-separated with correct charges? (3) Are aromatic atoms lowercase? (4) Are generic groups using `*` not `[R]`?

### Critical: Do NOT Put Markdown Inside `smiles` Blocks

The Chem plugin renders **every line** inside a `smiles` code block as a SMILES string. Labels, comments, headings, and any markdown must stay **outside** the block — inside, every line must be exactly one valid SMILES string. If you put markdown inside the block, the SMILES parser will reject it with a **SyntaxError**.

> [!danger] This causes SyntaxError
> ```smiles
> # Primary amine: methylamine
> CN
> # Secondary amine: dimethylamine
> CNC
> *Quaternary ammonium: tetramethylammonium*
> C[N+](C)(C)C
> ```
> The plugin tries to render `# Primary amine: methylamine` as SMILES — `#` means triple bond, so it fails. The `*italic*` text also fails because `*` is a wildcard atom followed by text.

**Correct approach** — labels go outside, only SMILES inside:

```smiles
CN
CNC
CN(C)C
Nc1ccccc1
C[N+](C)(C)C
```

| Type | Example | SMILES |
|------|---------|--------|
| Primary amine | Methylamine | `CN` |
| Secondary amine | Dimethylamine | `CNC` |
| Quaternary ammonium | Tetramethylammonium | `C[N+](C)(C)C` |

**Rules for `smiles` code blocks:**
- Each line must be a valid SMILES string
- No headings (`# text`)
- No bullet points (`* text` or `- text`)
- No tables (`| col | col |`)
- No callouts (`> [!note]`)
- No nested code fences (`` ``` ``)
- No LaTeX (`$...$` or `$$...$$`)
- No wikilinks (`[[Note]]`)
- No bold/italic (`**text**` or `*text*`)

If you need to label structures, use a markdown table or list **outside** the `smiles` block.

## Common Workflows

### Writing Chemistry Notes

1. **Get SMILES** for your molecule from:
   - Structure editors: ChemDraw, MarvinJS, Ketcher (or the [Obsidian Ketcher](https://github.com/yuleicul/obsidian-ketcher) plugin)
   - Translators: Open Babel, [Chemical Translation Service](https://cts.fiehnlab.ucdavis.edu/)
   - Manual entry for simple structures

2. **Insert into note** using `smiles` code blocks or inline syntax.

3. **Adjust appearance** via plugin settings (theme, scale, drawing options).

4. **Export** as PNG if you need images for papers or presentations.

### Using Dataview with Chem

Enable **Dataview integration** in settings. Then use Dataview inline queries or DataviewJS inside `smiles` blocks:

````markdown
```smiles
`= this.smiles`
```
````

> Requires the [Dataview](https://github.com/blacksmithgu/obsidian-dataview) plugin.
> DataviewJS uses `eval()` — only use trusted code.

### Switching Rendering Cores

- **smiles-drawer**: Faster, lighter, good for most organic molecules.
- **rdkit**: More accurate, better stereochemistry support. Requires downloading `RDKit_minimal` and `.wasm` files (auto-fetched from GitHub releases; manual download needed if behind a firewall).

If RDKit fails to load, the plugin shows a fallback modal and automatically switches to `smiles-drawer`.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Structures not rendering | Ensure plugin is enabled. Check Restricted Mode is off. Verify SMILES syntax at [OpenSMILES](http://opensmiles.org/opensmiles.html). |
| RDKit not loading | Download `RDKit_minimal.js` and `RDKit_minimal.wasm` from [releases](https://github.com/Acylation/obsidian-chem/releases) manually. Place in `[vault]/.obsidian/plugins/chem/rdkit/`. |
| Inline SMILES not working | Enable **Inline Render** in settings. Check the prefix matches exactly (default: `$smiles=`). |
| Dataview not parsing | Ensure Dataview plugin is installed and enabled. Check that DataviewJS is enabled in Dataview settings if using JS queries. |
| Dark theme looks wrong | Verify **Theme** setting is set to `auto`, `light`, or `dark` as desired. `auto` follows Obsidian's color scheme. |
| Copied image quality is low | Increase **Copy Scale** in settings (default is often 2x; increase for higher resolution). |

## Contributing to the Plugin

### Local Development Setup

```bash
# Recommended: use your dev vault's plugin folder
cd [vault]/.obsidian/plugins/
git clone https://github.com/Acylation/obsidian-chem.git chem
cd chem
npm install
npm run dev        # Watches for changes and rebuilds
```

Enable the [Hot-Reload](https://github.com/pjeby/hot-reload) plugin for smooth debugging.

### Build & Lint

```bash
npm run lint       # Check code style
npm run build      # Production build
npm run test       # Run Jest tests
npm run format     # Auto-format with Prettier
```

### Architecture Overview

```
src/
├── main.ts              # Plugin entry point
├── SmilesBlock.ts       # Code block processor
├── SmilesInline.ts      # Inline renderer + live-preview patch
├── settings/
│   ├── base.ts          # Settings schema + migration (v1→v2→v3)
│   ├── SettingTab.ts    # Settings UI
│   └── v1.ts, v2.ts, v3.ts  # Versioned defaults
├── lib/
│   ├── core/            # smiles-drawer & RDKit wrappers
│   ├── themes/          # Theme observer for auto-switching
│   ├── i18n.ts          # Internationalization
│   └── translations/    # Locale files
└── global/              # Global state (app, blocks, core, dataview)
```

### Design Principles

When proposing features or changes, ensure they meet at least one criterion:
- Helps with chemical research notes (lab records, literature, papers)
- Integrates well with other chemistry tools
- Aids learning chemistry

And adhere to:
- **Localize**: Prefer local packages over remote services
- **Leave No Trace**: Don't leave plugin-specific content in notes
- **Plain Text Central**: Prefer plain text over complex formats

## Resources

- [Plugin Repository](https://github.com/Acylation/obsidian-chem)
- [Obsidian Developer Docs](https://docs.obsidian.md/Plugins/Getting+started/Build+a+plugin)
- [SMILES Specification](http://opensmiles.org/opensmiles.html)
- [RDKit.js](https://github.com/rdkit/rdkit-js)
- [Smiles Drawer](https://github.com/reymond-group/smilesDrawer)
- Companion: [Obsidian Ketcher](https://github.com/yuleicul/obsidian-ketcher) for structure editing
