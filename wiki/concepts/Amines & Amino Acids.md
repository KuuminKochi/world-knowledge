---
title: "Amines & Amino Acids"
date: 2026-04-27
tags:
  - concept/chemistry
  - topic/organic-chemistry
  - topic/biochemistry
  - status/seedling
---

# Amines & Amino Acids

Nitrogen-containing organic compounds: amines are derivatives of ammonia, while amino acids are the building blocks of proteins containing both amino and carboxyl groups.

## Amines (RNH₂, R₂NH, R₃N)

### Classification
| Type            | Formula | Example                      |
| --------------- | ------- | ---------------------------- |
| Primary (1°)    | RNH₂    | Methylamine (CH₃NH₂)         |
| Secondary (2°)  | R₂NH    | Dimethylamine ((CH₃)₂NH)     |
| Tertiary (3°)   | R₃N     | Trimethylamine ((CH₃)₃N)     |
| Quaternary (4°) | R₄N⁺X⁻  | Tetramethylammonium chloride |

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
| Tertiary amine | Trimethylamine | `CN(C)C` |
| Aromatic amine | Aniline | `Nc1ccccc1` |
| Quaternary ammonium | Tetramethylammonium | `C[N+](C)(C)C` |

### Nomenclature
- Prefix: amino- or suffix: -amine
- Examples: ethylamine, aniline (phenylamine), diethylamine

### Physical Properties
- Hydrogen bonding (1° and 2° only)
- Lower boiling points than comparable alcohols (N-H weaker than O-H)
- Fishy/amine odor

### Basicity
Amines are basic due to the lone pair on nitrogen:
- Aliphatic: R-NH₂ + H₂O ⇌ R-NH₃⁺ + OH⁻
- Aromatic (aniline): Less basic (lone pair delocalized into ring)

**Basicity order**: Aliphatic 2° > Aliphatic 3° > Aliphatic 1° > NH₃ > Aromatic

### Preparation

#### 1. Reduction of Nitro Compounds (R-NO₂ → R-NH₂)
Reagents: H₂/Ni, Pt, or Pd; Zn/Fe/Sn + HCl; SnCl₂ + HCl; LiAlH₄ + hydrolysis.

```smiles
N(=O)(=O)c1ccccc1>>Nc1ccccc1
```
*Nitrobenzene → Aniline*

#### 2. Reduction of Amides (R-CONH₂ → R-CH₂NH₂)
Reagents: H₂/Ni, Pt, or Pd; LiAlH₄ + hydrolysis.
The carbonyl carbon is reduced to CH₂; **carbon count stays the same**.

```smiles
CC(N)=O>>CCN
```
*Ethanamide → Ethanamine*

#### 3. Reduction of Nitriles (R-CN → R-CH₂NH₂)
Reagents: H₂/Ni, Pt, or Pd; LiAlH₄ + hydrolysis.
Produces **primary amines only**; **carbon count increases by 1**.

```smiles
CC(C)C#N>>CC(C)CN
```
*2-methylpropanenitrile → 2-methylpropan-1-amine*

#### 4. Hoffmann Degradation of Amides
Primary amide + halogen (Cl₂ or Br₂) + strong base (NaOH/KOH) → primary amine with **one carbon removed**.

```smiles
NC(=O)c1ccccc1>>Nc1ccccc1
```
*Benzamide → Aniline (loses C=O carbon)*

#### 5. Alkylation of Ammonia
NH₃ + R-X → mixture of 1°, 2°, 3° amines + quaternary salts.
This is a **poor method** due to multiple alkylations.

```smiles
N.CCCl>>CCN
```
*Ammonia + chloroethane → ethylamine (plus further alkylated products)*

### Reactions

#### 1. Alkylation
Formation of higher order amines and quaternary ammonium salts via nucleophilic substitution.

#### 2. Acylation (Amide Formation)
Amines react with acid chlorides, acid anhydrides, and esters to form amides.

**With acid chlorides:**
```smiles
CC(=O)Cl.CN>>CC(=O)NC
```
*Acetyl chloride + methanamine → N-methylacetamide*

> [!note] 3° amine limitation
> Tertiary amines do **not** react with acid chlorides (no N-H proton to transfer to Cl).

**With acid anhydrides:**
```smiles
CC(=O)OC(C)=O.CN>>CC(=O)NC
```
*Acetic anhydride + methanamine → N-methylacetamide + acetic acid*

**With esters:**
```smiles
COC(C)=O.CCN>>CCNC(C)=O
```
*Methyl acetate + ethanamine → N-ethylacetamide + methanol*

#### 3. Reaction with Nitrous Acid (HNO₂)
Nitrous acid is prepared *in situ* (HCl/NaNO₂ or H₂SO₄/NaNO₂). Different amine classes give different products — used as a **distinguishing test**.

| Amine class | Product | Observation |
|---|---|---|
| 1° aliphatic | Unstable diazonium salt → N₂ + carbocation → mixture of alkene, alcohol, haloalkane | **Bubbles of N₂ gas** |
| 1° aromatic | **Stable arenediazonium salt** (< 5 °C) | No gas at < 5 °C |
| 2° aliphatic & aromatic | *N*-nitrosamine | **Yellow oil** |
| 3° aliphatic | Mixture of trialkylammonium chloride + trialkylnitrosoammonium chloride | **Clear solution** |
| 3° aromatic | *C*-nitrosation at *para* position (or *ortho* if *para* blocked) | **Solid precipitate** |

**Primary aliphatic — N₂ evolution:**
```smiles
CCCN.O=N[O-].[Na+].[Cl-].[Na+].Cl>>C=CC
```
*Propan-1-amine → propene + propan-2-ol + 2-chloropropane + N₂*

**Primary aromatic — diazonium salts:**
```smiles
Nc1ccccc1.O=N[O-].[Na+].[Cl-].[Na+].Cl>>[N+]#Nc1ccccc1.[Cl-]
```
*Aniline → benzenediazonium chloride*

Arenediazonium salts are versatile intermediates. The diazonium group can be replaced by various nucleophiles:

| Reagent | Product |
|---|---|
| H₃O⁺ | Phenol |
| CuCl | Chlorobenzene |
| CuBr | Bromobenzene |
| CuCN | Benzonitrile |
| KI | Iodobenzene |

**Azo coupling:**
```smiles
[Cl-].[N+]#Nc1ccccc1.Oc1ccccc1>>O=S(=O)([O-])c1ccc(N=Nc2ccccc2O)cc1
```
*Benzenediazonium salt + phenol → orange azo dye*

**Secondary amines — yellow oil:**
```smiles
CNC.O=N[O-].[Na+].[Cl-].[Na+].Cl>>CN(C)N=O
```
*Dimethylamine → N,N-dimethylnitrous amide (yellow oil)*

**Tertiary aromatic — C-nitrosation:**
```smiles
CN(CC)c1ccccc1.O=N[O-].[Na+].[Cl-].[Na+].Cl>>CN(CC)c1ccc(N=O)cc1
```
*N-ethyl-N-methylaniline → N-ethyl-N-methyl-4-nitrosoaniline (solid)*

#### 4. Reaction with Bromine Water

Aniline reacts vigorously with aqueous bromine to form **2,4,6-tribromoaniline** (white precipitate). The amino group is strongly activating and ortho-para directing.

```smiles
Nc1ccccc1.[Br-].[Br-].[Br-].[K+].[K+].[K+]>>Nc1c(Br)cc(Br)cc1Br
```
*Aniline + 3 Br₂(aq) → 2,4,6-tribromoaniline (white precipitate) + 3 HBr*

> [!tip] Preliminary test
> This reaction is used as a preliminary test for aniline due to the clear observation (brown bromine decolorizes + white precipitate forms).

#### 5. Hinsberg Test
Distinguishes 1°, 2°, and 3° amines using benzenesulfonyl chloride.

#### 6. Electrophilic Aromatic Substitution
Amino group is strongly activating and **ortho-para directing**.

## Amino Acids (H₂N-CHR-COOH)

### Structure
- α-carbon bonded to: amino group, carboxyl group, hydrogen, and side chain (R)
- Chiral (except glycine, R=H)
- L-configuration in natural proteins

### The 20 Common Amino Acids

#### Non-polar / Hydrophobic

**Glycine (Gly, G)** — non-essential
```smiles
NCC(=O)O
```
Side chain: H | Functional group: none

**Alanine (Ala, A)** — non-essential
```smiles
CC(N)C(=O)O
```
Side chain: -CH₃ | Functional group: alkyl

**Valine (Val, V)** — *essential*
```smiles
CC(C)C(N)C(=O)O
```
Side chain: -CH(CH₃)₂ | Functional group: alkyl

**Leucine (Leu, L)** — *essential*
```smiles
CC(C)CC(N)C(=O)O
```
Side chain: -CH₂-CH(CH₃)₂ | Functional group: alkyl

**Isoleucine (Ile, I)** — *essential*
```smiles
CCC(C)C(N)C(=O)O
```
Side chain: -CH(CH₃)-CH₂-CH₃ | Functional group: alkyl

**Phenylalanine (Phe, F)** — *essential*
```smiles
NC(Cc1ccccc1)C(=O)O
```
Side chain: -CH₂-C₆H₅ | Functional group: aromatic

**Proline (Pro, P)** — non-essential
```smiles
O=C(O)C1CCCN1
```
Side chain: cyclic -CH₂-CH₂-CH₂- | Functional group: rigid cyclic

**Methionine (Met, M)** — *essential*
```smiles
CSCCC(N)C(=O)O
```
Side chain: -CH₂-CH₂-S-CH₃ | Functional group: sulfide

**Tryptophan (Trp, W)** — *essential*
```smiles
NC(Cc1c[nH]c2ccccc12)C(=O)O
```
Side chain: -CH₂-indole | Functional group: indole

#### Polar Uncharged

**Serine (Ser, S)** — non-essential
```smiles
NC(CO)C(=O)O
```
Side chain: -CH₂-OH | Functional group: hydroxyl

**Threonine (Thr, T)** — *essential*
```smiles
CC(O)C(N)C(=O)O
```
Side chain: -CH(OH)-CH₃ | Functional group: hydroxyl

**Tyrosine (Tyr, Y)** — non-essential
```smiles
NC(Cc1ccc(O)cc1)C(=O)O
```
Side chain: -CH₂-C₆H₄-OH | Functional group: phenolic —OH

**Cysteine (Cys, C)** — non-essential
```smiles
NC(CS)C(=O)O
```
Side chain: -CH₂-SH | Functional group: thiol

**Asparagine (Asn, N)** — non-essential
```smiles
NC(=O)CC(N)C(=O)O
```
Side chain: -CH₂-CONH₂ | Functional group: amide

**Glutamine (Gln, Q)** — non-essential
```smiles
NC(=O)CCC(N)C(=O)O
```
Side chain: -CH₂-CH₂-CONH₂ | Functional group: amide

#### Acidic (Negatively charged at pH 7)

**Aspartic acid (Asp, D)** — non-essential
```smiles
NC(CC(=O)O)C(=O)O
```
Side chain: -CH₂-COOH | Functional group: carboxylic acid

**Glutamic acid (Glu, E)** — non-essential
```smiles
NC(CCC(=O)O)C(=O)O
```
Side chain: -CH₂-CH₂-COOH | Functional group: carboxylic acid

#### Basic (Positively charged at pH 7)

**Lysine (Lys, K)** — *essential*
```smiles
NCCCCC(N)C(=O)O
```
Side chain: -(CH₂)₄-NH₂ | Functional group: amino

**Arginine (Arg, R)** — *essential*
```smiles
NC(CCCNC(=N)N)C(=O)O
```
Side chain: -(CH₂)₃-NH-C(=NH)-NH₂ | Functional group: guanidino

**Histidine (His, H)** — *essential*
```smiles
NC(Cc1c[nH]cn1)C(=O)O
```
Side chain: -CH₂-imidazole | Functional group: imidazole

> [!note] Essential Amino Acids
> Ten amino acids must be obtained from diet (body cannot synthesize): Arg, Thr, Lys, Val, Phe, Trp, Met, His, Leu, Ile.

### Classification

Amino acids can be classified in several ways:

1. **By structure**: Based on core functional groups' locations (α-, β-, γ-carbon, etc.)
2. **By polarity**: Grouped by functional groups in the side chain
3. **By pH level**: Acidic (Asp, Glu), Basic (Lys, Arg, His), Neutral (Gly, Ala, etc.)
4. **By nutritional importance**:
   - **Essential**: Must be obtained from diet
   - **Semi-essential**: Required during specific conditions
   - **Non-essential**: Synthesized by the body

### Nomenclature

- Named as derivatives of carboxylic acids
- The carboxyl (-COOH) group is the parent chain (highest priority)
- All other groups (amino, sulfides, hydroxyl) are named as substituents
- **Examples**:
  - Methionine: 2-amino-4-methylthiobutanoic acid
  - Asparagine: 2,4-diamino-4-oxobutanoic acid

### Physical Properties

- **Crystalline solids with high melting points** — strong ionic attractions between zwitterions require more energy to break
- **Solubility in water** — generally soluble; insoluble in non-polar solvents (hydrocarbons); solubility varies based on R-group nature
- **Highly polar molecules** — large dipole moment; high dielectric constant

### Chemical Reactions

#### Reactions of the Carboxylic Acid Group
1. **With NaOH**: Neutralization forming salt and water
2. **With alcohol (Esterification)**: Ester formed when amino acid and alcohol are warmed in presence of acid (HCl/H⁺)

#### Reactions of the Amino Group
1. **With HCl**: Forms aminium salt
2. **With acid chlorides**: Formation of acyl derivatives
3. **With nitrous acid (HNO₂) at 0°C**: Formation of α-hydroxy carboxylic acids; products include alcohols, haloalkanes, and alkenes

### Zwitterions
At neutral pH:
- Amino group protonated: -NH₃⁺
- Carboxyl group deprotonated: -COO⁻
- Net charge = 0, but dipolar
- Amino acids NEVER exist as uncharged molecules
- In solid form, they exist as zwitterions with strong electrostatic attraction causing high melting points

### Isoelectric Point (pI)
The pH at which the amino acid has zero net charge:

- **Neutral side chains**: pI = ½(pKa₁ + pKa₂)
- **Acidic side chains**: pI = average of the two most acidic pKa values
- **Basic side chains**: pI = average of the two least acidic pKa values

**pKa Values**:
- Carboxyl group (-COOH): pKa ≈ 2 (stronger acid)
- Amino group (-NH₃⁺): pKa ≈ 9–10 (weaker acid)
- Example titration: glycine pKa₁ ≈ 2.3, pKa₂ ≈ 9.6, pI = 6.0
- Example: Lysine pI = (10.53 + 8.95)/2 = 9.74
- Neutral amino acids have isoelectric pH slightly acidic (5–6)
- Amino acids are least soluble at pI

### Electrophoresis
- At pH < pI: Net positive → moves toward cathode (-)
- At pH > pI: Net negative → moves toward anode (+)
- At pH = pI: No movement
- A mixture of amino acids can be separated on a buffered medium; when voltage is applied, movement depends on pI relative to solution pH

## Peptides and Proteins

### Peptide Bond
- Amide linkage: -CO-NH-
- Formed by condensation between carboxyl of one amino acid and amino of another
- Planar (partial double bond character)
- Usually trans configuration

### Protein Structure
| Level | Description | Bonds/Forces |
|-------|-------------|--------------|
| Primary | Amino acid sequence | Peptide bonds |
| Secondary | α-helix, β-sheet | Hydrogen bonds |
| Tertiary | 3D folding | Disulfide, H-bonds, ionic, hydrophobic |
| Quaternary | Multiple subunits | Same as tertiary |

## Related Topics
- [[Carboxylic Acids & Derivatives]] — Amide formation
- [[Polymer Chemistry]] — Proteins as natural polymers
- [[Stereochemistry]] — Chirality in amino acids

## Sources
- [[FAD1018 W12 — Amine & Amino Acids]]
- [[FAD1018 - Basic Chemistry II]]
