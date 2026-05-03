---
title: "Carbonyl Compounds"
date: 2026-04-27
tags:
  - concept/chemistry
  - topic/organic-chemistry
  - status/seedling
---

# Carbonyl Compounds

Organic compounds containing the carbonyl group (C=O), including aldehydes and ketones. They have the **general formula**:

$$C_nH_{2n}O$$

## Structure

The carbonyl carbon is sp² hybridized with trigonal planar geometry:
- Carbon-oxygen double bond (one σ, one π)
- Polar bond (oxygen is more electronegative)
- Partial positive charge on carbon, partial negative on oxygen

```smiles
C=O
```
```smiles
CC=O
```
```smiles
CC(=O)C
```
```smiles
c1ccccc1C=O
```
```smiles
O=C1CCCCC1
```
```smiles
CC(=O)c1ccccc1
```
## Aldehydes vs Ketones

| Feature | Aldehydes | Ketones |
|---------|-----------|---------|
| General formula | R-CHO | R-CO-R' |
| Carbonyl position | Terminal | Internal |
| Oxidation | Easily oxidized to carboxylic acids | Resistant to oxidation |
| Reactivity | More reactive | Less reactive |
| IUPAC suffix | -al | -one |
| Example (SMILES) | `CCC=O` (propanal) | `CCC(=O)C` (butan-2-one) |

## Nomenclature

### Aldehydes
- Replace -e with -al
- **Numbering always starts at carbonyl carbon** (carbonyl carbon always has the 1-position)
- Choose the **longest chain** containing the functional group
- Substituent locations denoted with the corresponding number
- **Cyclic / aromatic aldehydes**: If attached to a ring, add **‘carbaldehyde’** to the cyclic compound name. For aromatic aldehydes, **benzaldehyde** is more commonly used than *benzenecarbaldehyde*.
- Examples: methanal (formaldehyde, `C=O`), ethanal (acetaldehyde, `CC=O`), 3-methylbutanal (isovaleraldehyde, `CC(C)CC=O`)

> [!note] Functional group priority
> If a compound has two functional groups, the one with **lower priority** is indicated by its **prefix** (as substituent). A ketone oxygen in a compound that also contains an aldehyde is indicated by the prefix **‘oxo’** (e.g., **4-oxohexanal**, `O=CCCCC(=O)C`).
> The prefix **‘formyl’** (`–CH=O`) is used when aldehyde is the lower-priority group.

### Ketones
- Replace -e with -one
- Number the chain from the **terminal closer to the functional group** to give the carbonyl the **lowest possible locant** (minimum at the 2nd carbon for acyclic ketones)
- In **cyclic ketones**, the carbonyl is assumed to be at the **1-position**
- Examples: propanone (acetone / dimethyl ketone, `CC(=O)C`), butan-2-one (`CCC(=O)C`), cyclohexanone (`O=C1CCCCC1`)

#### Phenyl-substituted Ketones
Common names are used for some phenyl-substituted ketones: the number of carbons (other than those of the phenyl group) is indicated by substituting **“-ophenone”** for **“-ic acid”** in the corresponding carboxylic acid name.

| Systematic name | Common name | SMILES |
|-----------------|-------------|--------|
| phenylethanone | acetophenone / methyl phenyl ketone | `CC(=O)c1ccccc1` |
| 1-phenyl-1-butanone | butyrophenone / phenyl propyl ketone | `CCCC(=O)c1ccccc1` |
| 1-phenyl-2-butanone | — | `CC(=O)Cc1ccccc1` |

## Physical Properties

- **Dipole-dipole interactions**: Higher boiling points than alkanes/ethers
- **No H-bonding**: Lower boiling points than alcohols
- **Solubility**: Lower members soluble in water

Reference comparison (similar molecular weight):

| Compound | Type | Boiling point |
|----------|------|---------------|
| `CH₃CH₂CH₂OH` (propan-1-ol) | Alcohol | 97.4 °C |
| `CH₃COCH₃` (propanone) | Ketone | 56 °C |
| `CH₃CH₂CHO` (propanal) | Aldehyde | 49 °C |
| `CH₃CH₂OCH₃` (ethyl methyl ether) | Ether | 10.8 °C |

## Preparation

### Aldehydes
- **Oxidation of primary alcohols** — must use a **mild oxidizing agent**: **PCC (Pyridinium chlorochromate) in CH₂Cl₂** is the only reagent that stops at the aldehyde. Strong oxidizing agents (`K₂Cr₂O₇ / H₂SO₄`, `CrO₃ / H₂SO₄`, `KMnO₄ / H⁺`) over-oxidize to carboxylic acids.
- **Ozonolysis of alkenes** — cleavage of C=C with `O₃ / H₂O / Zn` yields aldehydes (from monosubstituted alkene carbons)
- Hydroformylation of alkenes

### Ketones
- **Oxidation of secondary alcohols** — any oxidizing agent (`K₂Cr₂O₇ / H₂SO₄`, `CrO₃ / H₂SO₄`, `KMnO₄ / H⁺`, or PCC/CH₂Cl₂) converts secondary alcohols to ketones without over-oxidation
- **Ozonolysis of alkenes** — cleavage of C=C with `O₃ / H₂O / Zn` yields ketones (from disubstituted alkene carbons)
- **Friedel-Crafts acylation** — aromatic ketones prepared from benzene + acyl chloride (`RCOCl`) in presence of `AlCl₃` (Lewis acid catalyst)
- Hydration of alkynes (Markovnikov)

## Reactions

### 1. Nucleophilic Addition
General mechanism: Nu⁻ attacks electrophilic carbonyl carbon, followed by protonation.

#### With HCN (Cyanohydrin formation)
- Product: α-hydroxynitrile
- Base-catalyzed
- One carbon extension

#### With Grignard Reagents
- Aldehydes → Secondary alcohols
- Ketones → Tertiary alcohols

#### With Alcohols (Acetal/Ketal formation)
- Hemiacetal/hemiketal intermediate
- Acetals/ketals as protecting groups

#### With NaHSO₃
- Addition compounds (crystalline solids)
- Purification technique

### 2. Addition-Elimination with Nitrogen Nucleophiles

| Reagent | Product | Test |
|---------|---------|------|
| Hydroxylamine (NH₂OH) | Oxime | - |
| Hydrazine (NH₂NH₂) | Hydrazone | - |
| 2,4-Dinitrophenylhydrazine | 2,4-DNP derivative | Orange/red ppt (positive test) |
| Primary amine (RNH₂) | Imine (Schiff base) | - |

### 3. Oxidation/Reduction

#### Oxidation (Aldehydes only)
- **Tollens' test**: [Ag(NH₃)₂]⁺ → Ag (silver mirror)
- **Fehling's/Benedict's test**: Cu²⁺ → Cu₂O (brick-red precipitate)
- **Schiff's test**: Pink color

#### Reduction
- Aldehydes → Primary alcohols
- Ketones → Secondary alcohols
- Reagents: NaBH₄ (mild), LiAlH₄ (strong), catalytic H₂

### 4. Special Reactions

#### Aldol Condensation
- Two molecules of carbonyl compound
- α-H required
- β-hydroxy carbonyl → α,β-unsaturated carbonyl (on heating)

#### Cannizzaro Reaction
- Non-enolizable aldehydes (no α-H)
- Disproportionation: One molecule oxidized, one reduced

#### Haloform Reaction
- Methyl ketones (CH₃-CO-)
- Iodoform test: Yellow CHI₃ precipitate

## Identification Tests Summary

| Test | Aldehydes | Ketones |
|------|-----------|---------|
| Tollens' | Silver mirror | Negative |
| Fehling's | Brick-red ppt | Negative |
| Benedict's | Brick-red ppt | Negative |
| 2,4-DNP | Orange/red ppt | Orange/red ppt |
| Iodoform | Positive if CH₃CHO | Positive if methyl ketone |
| Schiff's | Pink color | Negative |

## Carbonyl Compounds in Nature

### Natural Products

Many biologically important molecules contain aldehyde or ketone groups:

```smiles
COc1cc(C=O)ccc1O
```
```smiles
O=CC=Cc1ccccc1
```
```smiles
CC12CCC(CC1=O)C2(C)C
```
```smiles
CC1=CC[C@@H](C(C)C)CC1=O
```
- **Aldehydes** generally have **pungent odors**
- **Ketones** tend to smell **sweet**

### Carbohydrates as Carbonyl Compounds

Monosaccharides (simple sugars) are carbonyl compounds that cannot be hydrolyzed further.

#### Classification

| Class | Carbonyl Type | Example | Carbon Count |
|-------|---------------|---------|--------------|
| Aldose | Aldehyde | Glucose | Hexose (6C) |
| Ketose | Ketone | Fructose | Hexose (6C) |

#### D and L Configuration

- Based on the configuration of the **chiral carbon furthest from the carbonyl group**
- **D-sugar**: OH on the **right** in Fischer projection (bottom chiral center)
- **L-sugar**: OH on the **left** in Fischer projection
- **D forms predominate in nature**; D-glucose and L-glucose are **enantiomers**

#### Glucose (Aldohexose)

```smiles
O=C[C@H](O)[C@@H](O)[C@H](O)[C@H](O)CO
```
- Polyhydroxyaldehyde
- In solution, forms a cyclic **hemiacetal** via intramolecular nucleophilic attack of the C₅ hydroxyl on the C₁ aldehyde
- **Reducing sugar**: the hemiacetal ring can open to expose the free aldehyde, which is oxidized by Tollens' or Benedict's reagent

#### Fructose (Ketohexose)

```smiles
O=C(CO)C(O)C(O)C(O)CO
```
- Polyhydroxy ketone
- Forms a cyclic **hemiacetal** via intramolecular attack of the C₅ hydroxyl on the C₂ ketone
- Also a **reducing sugar** (hemiacetal-reducing sugar)

#### Reducing vs Non-Reducing Sugars

**Reducing sugars** (positive Tollens'/Benedict's test):
- All monosaccharides with a **hemiacetal** group (glucose, fructose)
- Ketoses are converted to aldoses under alkaline conditions, then oxidized

**Non-reducing sugars** (negative Tollens'/Benedict's test):
- Sugars in **acetal** form (e.g., glycosides, disaccharides like sucrose)
- No free hemiacetal hydroxyl; cannot open to reveal a carbonyl

| Test | Reducing Sugar | Non-Reducing Sugar |
|------|----------------|--------------------|
| Tollens' | Silver mirror | No reaction |
| Benedict's | Brick-red precipitate | No reaction |

## Examples with SMILES

```smiles
CCC=O
```
```smiles
CCC(=O)C
```
```smiles
CC(Br)C=O
```
```smiles
CC(Cl)CC=O
```
```smiles
CC(C)CC=O
```
```smiles
O=CCCCCC=O
```
```smiles
CC1CCCCC1C=O
```
```smiles
c1ccccc1C=O
```
```smiles
CC(=O)C
```
```smiles
CCC(=O)CCC
```
```smiles
O=C1CCCCC1
```
```smiles
CC(=O)C(=O)C
```
```smiles
CC(=O)CC(=O)C
```
```smiles
CC(=O)CC=CC
```
```smiles
CC(=O)c1ccccc1
```
```smiles
CCCC(=O)c1ccccc1
```
```smiles
CC(=O)Cc1ccccc1
```
```smiles
CC(C)(C)C1CCCC(=O)C1
```
## Related Topics
- [[Alcohol & Phenol]] — Precursors and reduction products
- [[Carboxylic Acids & Derivatives]] — Oxidation products of aldehydes
- [[Carbohydrates]] — Sugars containing carbonyl groups

## Sources
- [[FAD1018 W8-W10 — Carbonyl Compounds]]
- [[FAD1018 - Basic Chemistry II]]
