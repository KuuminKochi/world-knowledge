---
title: "FAD1018 W12 — Amine & Amino Acids"
date: 2026-04-27
tags:
  - source/lecture
  - course/FAD1018
  - topic/amines
  - topic/amino-acids
  - status/seedling
week: 12
lecturer: "[[Dr Syazreen Nadia Sulaiman]]"
---

# FAD1018 W12 — Amine & Amino Acids

Week 12 lecture covering amines and amino acids. Lecture 3 on amino acids presented by Dr Syazreen Nadia Sulaiman. Source files: `W12 (1).pdf`, `W12 (2).pdf`, `W12 (3).pdf` from lecture notes folders.

## Summary

Study of amines (classification, properties, reactions) and amino acids as building blocks of proteins.

## Key Concepts

- [[Amines & Amino Acids]] — Nitrogen-containing organic compounds
- Primary, Secondary, Tertiary Amines — Classification
- Quaternary Ammonium Salts — R₄N⁺
- Amino Acids — Building blocks of proteins
- Fischer Projection — D- and L-amino acid configuration
- Essential Amino Acids — Must be obtained from diet
- Zwitterions — Dipolar ions
- Isoelectric Point (pI) — pH of zero net charge
- pKa Values — Ionizable groups in amino acids
- Electrophoresis — Separation based on pI
- Peptide Bond — Amide linkage between amino acids

---

## W12 (2) — Amine Lecture 2: Preparation & Chemical Reactions

**Lecturer:** Dr Syazreen Nadia Sulaiman  
**Scope:** Preparation methods of amines and their chemical reactions with acyl chlorides, acid anhydrides, esters, nitrous acid, and bromine water.

### Learning Outcomes

1. Categorize amines as primary, secondary, or tertiary
2. Draw and name amines according to IUPAC nomenclature
3. Explain physical properties (boiling points, solubility)
4. Compare basicity of ammonia, aliphatic amines, and aromatic amines
5. Explain preparation of aromatic amines, primary aliphatic amines (via nitriles), and primary/secondary/tertiary amines (via amides, Hoffmann degradation)
6. Explain chemical properties with reference to reactions with acyl chloride, acid anhydrides, nitrous acid, bromine water

---

### Preparation of Amines

#### 1. Reduction of Nitro Compounds

Nitro compounds can be reduced to **primary amines** using one of the following reagents:

- H₂ with Ni, Pt, or Pd catalyst
- Zn, Fe, or Sn with HCl
- SnCl₂ + HCl
- LiAlH₄ followed by hydrolysis

**General reaction:**

```smiles
*N(=O)=O>>*N
```

**Specific examples:**

```smiles
CC[N+](=O)[O-]>>CCN
```
*Ethylnitrobenzene → Ethanamine (catalytic hydrogenation with H₂/Ni)*

```smiles
N(=O)(=O)c1ccccc1>>Nc1ccccc1
```
*Nitrobenzene → Aniline (Fe/HCl or Sn/HCl)*

> [!note] Aromatic nitro compounds
> Nitrobenzene (C₆H₅NO₂) reduced with Sn/HCl gives aniline (C₆H₅NH₂).

---

#### 2. Reduction of Amides

Converting amides to amines. The carbonyl carbon is reduced to CH₂.

**Key reagents:**
- H₂ with Ni, Pt, or Pd catalyst
- LiAlH₄ followed by hydrolysis

**General reactions:**

| Starting amide | Product |
|---|---|
| 1° amide (R-CONH₂) | 1° amine (R-CH₂-NH₂) |
| 2° amide (R-CONHR') | 2° amine (R-CH₂-NHR') |
| 3° amide (R-CONR'R'') | 3° amine (R-CH₂-NR'R'') |

**Specific examples:**

```smiles
CC(N)=O>>CCN
```
*Ethanamide → Ethanamine (LiAlH₄ / H₃O⁺)*

```smiles
CC(=O)N(C)C>>CCN(C)C
```
*N,N-dimethylethanamide → N,N-dimethylethanamine (LiAlH₄ / H₃O⁺)*

> [!tip] Carbon count
> Reduction of amides does **not** change the carbon count. R-C(=O)-NH₂ → R-CH₂-NH₂

---

#### 3. Reduction of Nitriles

Reduction of nitriles produces **primary amines** only.

**Key reagents:**
- H₂ with Ni, Pt, or Pd catalyst
- LiAlH₄ followed by hydrolysis

**General reaction:**

```smiles
*C#N>>*CCN
```

**Specific examples:**

```smiles
CC(C)C#N>>CC(C)CN
```
*2-methylpropanenitrile → 2-methylpropan-1-amine*

```smiles
CC(C)CC#N>>CC(C)CCN
```
*3-methylbutanenitrile → 3-methylbutan-1-amine*

> [!note] Carbon count increases by 1
> R-C≡N → R-CH₂-NH₂. The nitrile carbon becomes the extra carbon in the amine.

---

#### 4. Hoffmann's Degradation of Amides

In the presence of a strong base, a **primary amide** reacts with halogen (Cl₂ or Br₂) to form a **primary amine** with the **loss of its carbonyl group** (one carbon is removed).

**Key reagents:** Br₂ + NaOH (strong base & halogen)

**General reaction:**

```smiles
*C(N)=O.O=C([O-])[O-].[Na+].[Na+].[OH-].[OH-].[Br][Br]>>*N.O=C([O-])[O-].[Na+].[Na+].[Br-].[Br-]
```

**Specific examples:**

```smiles
NC(=O)c1ccccc1>>Nc1ccccc1
```
*Benzamide → Aniline (Cl₂/KOH or Br₂/KOH)*

```smiles
CC(C)C(N)=O>>CC(C)N
```
*2-methylpropanamide → propan-2-amine (Br₂/KOH)*

> [!important] Carbon chain shortening
> Hoffmann degradation converts primary amides to primary amines while **removing one carbon atom**.

**Summary: Starting from 2-methylpropan-1-ol**

Depending on the method chosen, three different primary amines can be prepared:

| Method | Carbon count | Product |
|---|---|---|
| Reduction of amide (same C) | Same as starting alcohol | 2-methylpropan-1-amine |
| Hoffmann degradation (lose 1 C) | Less by one C | propan-2-amine |
| Reduction of nitrile (gain 1 C) | Greater by one C | 3-methylbutan-1-amine |

---

#### 5. Alkylation of Ammonia or Alkylamines

Ammonia and amines are good nucleophiles, thus react with haloalkanes to give the appropriate amines.

**General reaction:**

```smiles
N.*X>>*N
```

However, this is a **poor method** of amine preparation since 1°, 2°, and 3° amines have similar reactivity. Multiple alkylations occur, giving a **mixture of 1°, 2°, 3° amines** and quaternary ammonium salts.

---

### Chemical Reactions of Amines

Due to their lone pair, amines react as nucleophiles.

| Reagent | Product | Mechanism |
|---|---|---|
| haloalkane | substituted amine | nucleophilic substitution |
| acyl chloride | N-substituted amide | addition elimination |

---

#### 1. Acylation

Amines react with acid derivatives (acid chlorides, acid anhydrides, and esters) to produce amides.

##### a) Reaction with Acid Chlorides

**General reactions:**

- 1° amine + acid chloride → 2° amide + ammonium chloride salt
- 2° amine + acid chloride → 3° amide + ammonium chloride salt
- 3° amine + acid chloride → **no reaction** (no H on nitrogen to attach to Cl)

**Specific examples:**

```smiles
CC(=O)Cl.CN>>CC(=O)NC
```
*Acetyl chloride + methanamine → N-methylacetamide*

```smiles
CC(=O)Cl.CNC>>CC(=O)N(C)C
```
*Acetyl chloride + dimethylamine → N,N-dimethylacetamide*

##### b) Reaction with Acid Anhydrides

**General reactions:**

- 1° amine + acid anhydride → 2° amide + carboxylic acid
- 2° amine + acid anhydride → 3° amide + carboxylic acid

**Specific examples:**

```smiles
CC(=O)OC(C)=O.CN>>CC(=O)NC
```
*Acetic anhydride + methanamine → N-methylacetamide + acetic acid*

```smiles
CC(=O)OC(C)=O.CNC>>CC(=O)N(C)C
```
*Acetic anhydride + dimethylamine → N,N-dimethylacetamide + acetic acid*

##### c) Reaction with Esters

**General reactions:**

- 1° amine + ester → 2° amide + alcohol
- 2° amine + ester → 3° amide + alcohol

**Specific examples:**

```smiles
COC(C)=O.CCN>>CCNC(C)=O
```
*Methyl acetate + ethanamine → N-ethylacetamide + methanol*

```smiles
CCOC(C)=O.CN(C)CC>>CCN(C)C(C)=O
```
*Ethyl acetate + N-methylethanamine → N-ethyl-N-methylacetamide + ethanol*

---

#### 2. Reaction with Nitrous Acid (HNO₂)

Nitrous acid is a weak acid. It is **unstable** and always prepared *in situ*:

- HCl + NaNO₂(aq) → HO-NO(aq) + NaCl(aq)
- H₂SO₄ + NaNO₂(aq) → 2 HO-NO(aq) + Na₂SO₄(aq)

Nitrous acid reacts with all amines. However, amines of different classes yield **different products**. This reaction is used as a laboratory test to differentiate amines.

##### a) Primary Aliphatic Amines

The reaction yields highly unstable aliphatic diazonium salts which decompose spontaneously, even at low temperature (0-5 °C), to form carbocations by evolving N₂ gas.

The carbocation stabilizes by losing a proton to form **alkenes**, and reacts with nucleophiles in the mixture (water to form **alcohols**, X⁻ to form **haloalkanes**).

**General reaction:**

```smiles
*N.O=N[O-].[Na+].[Cl-].[Na+].Cl>>[R+].[Cl-].*O*.*C=C*.[N-]=[N+]=[N-]
```

**Specific example:**

```smiles
CCCN.O=N[O-].[Na+].[Cl-].[Na+].Cl>>C=CC.CC(C)O.CC(C)Cl
```
*Propan-1-amine + NaNO₂/HCl (0-5 °C) → propene + propan-2-ol + 2-chloropropane + N₂*

> [!note] Products are a mixture
> Primary aliphatic amines give a mixture of alkene, alcohol, and haloalkane due to carbocation rearrangement and nucleophilic attack.

##### b) Primary Aromatic Amines

Reactions of nitrous acid with primary aromatic amines yield **arenediazonium salts** which are stable at temperatures < 5 °C.

**Formation:**

```smiles
Nc1ccccc1.O=N[O-].[Na+].[Cl-].[Na+].Cl>>[N+]#Nc1ccccc1.[Cl-]
```
*Aniline + NaNO₂/HCl (0-5 °C) → benzenediazonium chloride + NaCl + 2H₂O*

**Substitutions of the diazonium group:**

Arenediazonium salts are highly useful intermediates. The diazonium group can be substituted by almost any nucleophile:

| Reagent | Product | Name |
|---|---|---|
| H₃O⁺ | Ph-OH | Phenol |
| CuCl | Ph-Cl | Chlorobenzene |
| CuBr | Ph-Br | Bromobenzene |
| CuCN | Ph-CN | Benzonitrile |
| KI | Ph-I | Iodobenzene |

> [!tip] Temperature sensitivity
> Arenediazonium salts are unstable at temperatures above 5-10 °C. Most substitution reactions do not require their isolation — reagents are added directly and warmed gently with evolution of N₂ gas.

**Azo coupling reactions:**

Arenediazonium ions are weak electrophiles and undergo coupling reactions with aromatic compounds containing strong electron-donating groups (-OH, -NR₂) at the *para* position to yield **azo compounds**.

```smiles
[Cl-].[N+]#Nc1ccccc1.Oc1ccccc1>>O=S(=O)([O-])c1ccc(N=Nc2ccccc2O)cc1
```
*Benzenediazonium salt + phenol → orange azo dye*

```smiles
[Cl-].[N+]#Nc1ccccc1.CN(C)c1ccccc1>>CN(C)c1ccc(N=Nc2ccccc2)cc1
```
*Benzenediazonium salt + N,N-dimethylaniline → yellow azo dye*

> [!note] Azo dyes
> Azo compounds are usually intensely colored and relatively inexpensive, used extensively as dyes.

##### c) Secondary Amines (Aliphatic & Aromatic)

Secondary aliphatic amines and aromatic amines react with nitrous acid to form **N-nitroso-N-alkylalkanamine** and **N-nitroso-N-alkylaniline** respectively as an **oily yellow liquid**.

**General reaction:**

```smiles
*N*O=N[O-].[Na+].[Cl-].[Na+].Cl>>*N(*)N=O
```

**Specific examples:**

```smiles
CNC.O=N[O-].[Na+].[Cl-].[Na+].Cl>>CN(C)N=O
```
*Dimethylamine + NaNO₂/HCl → N,N-dimethylnitrous amide (yellow oil)*

```smiles
CNc1ccccc1.O=N[O-].[Na+].[Cl-].[Na+].Cl>>CN(c1ccccc1)N=O
```
*N-methylaniline + HNO₂ → N-methyl-N-phenylnitrous amide*

##### d) Tertiary Aliphatic Amines

Tertiary aliphatic amines react with nitrous acid to form a **mixture of salts**:

1. The amine reacts as a base and accepts a proton from HCl to form **trialkylammonium chloride**
2. The amine can also react as a Lewis base by donating the lone pair to a nitroso ion (NO⁺) to form **trialkylnitrosoammonium chloride**

These salts are soluble in water (clear solution).

**Specific example:**

```smiles
CCN(C)C.O=N[O-].[Na+].[Cl-].[Na+].Cl>>CC[NH+](C)C.[Cl-].CC[N+](C)(C)N=O.[Cl-]
```
*N,N-dimethylethanamine + NaNO₂/HCl → N,N-dimethylethanammonium chloride + N,N-dimethyl-N-nitrosoethanammonium chloride*

##### e) Tertiary Aromatic Amines

Tertiary aromatic amines react with nitrous acid to form **solid products** with a nitroso group attached to the **para position** in the benzene ring. If the para position is not available, the nitroso group attaches to the **ortho** position.

**Specific example:**

```smiles
CN(CC)c1ccccc1.O=N[O-].[Na+].[Cl-].[Na+].Cl>>CN(CC)c1ccc(N=O)cc1
```
*N-ethyl-N-methylaniline + NaNO₂/HCl → N-ethyl-N-methyl-4-nitrosoaniline (solid)*

##### Summary Table: Reaction with Nitrous Acid

| Amine | Observation |
|---|---|
| 1° aliphatic | Bubbles of N₂ gas |
| 1° aromatic | No bubble of gas at < 5 °C |
| 2° aliphatic & aromatic | Yellow oil |
| 3° aliphatic | Clear solution |
| 3° aromatic | Precipitate (solid) |

---

#### 3. Reaction of Aniline with Bromine Water

The amino group (-NH₂) is an **activating group** and an **ortho-para director**, just like the -OH group in phenol.

Aniline reacts easily with aqueous bromine to give a high yield of **2,4,6-tribromoaniline** as a **white precipitate**.

```smiles
Nc1ccccc1.[Br-].[Br-].[Br-].[K+].[K+].[K+]>>Nc1c(Br)cc(Br)cc1Br
```
*Aniline + 3 Br₂(aq) → 2,4,6-tribromoaniline (white precipitate) + 3 HBr*

The bromine decolorizes and hydrogen bromide is given off.

> [!important] Preliminary test
> Due to the readiness of the reaction which gives a very clear observation, this reaction is used as a preliminary test to identify the presence of aniline.

---

## Amino Acids — Lecture 3 Details (Dr Syazreen Nadia Sulaiman)

### Learning Outcomes
1. Identify the general structure of amino acids
2. Identify the structures of 20 standard amino acids
3. Name amino acids according to IUPAC rules
4. Define zwitterion and isoelectric point
5. Draw amino acid structures in acidic, basic, and at pI media
6. Explain reactions of amino acids
7. Describe peptide bond formation in polypeptides
8. Explain protein structure and importance

### Structure & Chirality
- Amino acids are carboxylic acids containing an amino (-NH₂) group attached to the α-carbon
- General structure: H₂N-CHR-COOH

```smiles
N[C@@H](*)C(=O)O
```

- Simplest amino acid: Glycine (NH₂-CH₂-COOH), IUPAC: 2-aminoethanoic acid

```smiles
NCC(=O)O
```
- All α-amino acids except glycine contain a stereocenter/chiral center → optically active
- Exist in L- and D-forms based on molecular configuration (Fischer projection)
- **L-amino acid**: amino group on the left in Fischer projection (natural form in proteins)
- **D-amino acid**: amino group on the right in Fischer projection

### The 20 Common (Standard) α-Amino Acids

#### Non-polar Side Chain (H or Alkyl)
- **Glycine (Gly, G)**: H — none — non-essential
- **Alanine (Ala, A)**: -CH₃ — alkyl — non-essential
- **Valine (Val, V)***: -CH(CH₃)₂ — alkyl — essential
- **Leucine (Leu, L)***: -CH₂-CH(CH₃)₂ — alkyl — essential
- **Isoleucine (Ile, I)***: -CH(CH₃)-CH₂-CH₃ — alkyl — essential
- **Phenylalanine (Phe, F)***: -CH₂-C₆H₅ — aromatic — essential
- **Proline (Pro, P)**: cyclic — rigid cyclic — non-essential
- **Methionine (Met, M)***: -CH₂-CH₂-S-CH₃ — sulfide — essential
- **Tryptophan (Trp, W)***: -CH₂-indole — indole — essential

```smiles
N[C@@H](C)C(=O)O
```
*Alanine (Ala)*

```smiles
CC(C)[C@@H](N)C(=O)O
```
*Valine (Val)*

```smiles
CC(C)C[C@@H](N)C(=O)O
```
*Leucine (Leu)*

```smiles
CC[C@H](C)[C@@H](N)C(=O)O
```
*Isoleucine (Ile)*

```smiles
N[C@@H](Cc1ccccc1)C(=O)O
```
*Phenylalanine (Phe)*

```smiles
OC(=O)[C@@H]1CCCN1
```
*Proline (Pro)*

```smiles
CSCC[C@@H](N)C(=O)O
```
*Methionine (Met)*

```smiles
N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O
```
*Tryptophan (Trp)*

#### Polar Side Chain (contains -OH or non-basic nitrogen)
- **Serine (Ser, S)**: -CH₂-OH — hydroxyl — non-essential
- **Threonine (Thr, T)***: -CH(OH)-CH₃ — hydroxyl — essential
- **Tyrosine (Tyr, Y)**: -CH₂-C₆H₄-OH — phenolic-OH — non-essential
- **Cysteine (Cys, C)**: -CH₂-SH — thiol — non-essential
- **Asparagine (Asn, N)**: -CH₂-CONH₂ — amide — non-essential
- **Glutamine (Gln, Q)**: -CH₂-CH₂-CONH₂ — amide — non-essential

```smiles
OC[C@@H](N)C(=O)O
```
*Serine (Ser)*

```smiles
C[C@H](O)[C@@H](N)C(=O)O
```
*Threonine (Thr)*

```smiles
N[C@@H](Cc1ccc(O)cc1)C(=O)O
```
*Tyrosine (Tyr)*

```smiles
SC[C@@H](N)C(=O)O
```
*Cysteine (Cys)*

```smiles
NC(=O)C[C@@H](N)C(=O)O
```
*Asparagine (Asn)*

```smiles
NC(=O)CC[C@@H](N)C(=O)O
```
*Glutamine (Gln)*

#### Acidic Side Chain
- **Aspartic acid (Asp, D)**: -CH₂-COOH — carboxylic acid — negatively charged at pH 7
- **Glutamic acid (Glu, E)**: -CH₂-CH₂-COOH — carboxylic acid — negatively charged at pH 7

```smiles
N[C@@H](CC(=O)O)C(=O)O
```
*Aspartic acid (Asp)*

```smiles
N[C@@H](CCC(=O)O)C(=O)O
```
*Glutamic acid (Glu)*

#### Basic Side Chain
- **Lysine (Lys, K)***: -(CH₂)₄-NH₂ — amino — positively charged at pH 7 — essential
- **Arginine (Arg, R)***: -(CH₂)₃-NH-C(=NH)-NH₂ — guanidino — positively charged at pH 7 — essential
- **Histidine (His, H)***: -CH₂-imidazole — imidazole — positively charged at pH 7 — essential

```smiles
NCCCC[C@@H](N)C(=O)O
```
*Lysine (Lys)*

```smiles
NC(=N)NCCC[C@@H](N)C(=O)O
```
*Arginine (Arg)*

```smiles
N[C@@H](Cc1c[nH]cn1)C(=O)O
```
*Histidine (His)*

> [!note] Essential Amino Acids
> Ten amino acids marked with * must be obtained from diet: Val, Leu, Ile, Phe, Met, Trp, Thr, Lys, Arg, His

> [!note] Abbreviations
> Most abbreviations are the first three letters. Exceptions: Ile, Trp, Asn, Gln. One-letter symbols are usually the first letter, with exceptions: Phe (F), Trp (W), Asn (N), Gln (Q), Tyr (Y), Asp (D), Glu (E), Lys (K), Arg (R).

### Rare Amino Acids
- **4-Hydroxyproline & 5-Hydroxylysine** — found in collagen
- **D-Glutamic Acid** — present in bacterial cell walls
- **D-Serine** — found in earthworms, neurological signaling
- **GABA** — neurotransmitter, regulates brain activity
- **Beta-Alanine** — component of pantothenic acid (Vitamin B5)

```smiles
OC(=O)[C@@H]1C[C@H](O)CN1
```
*4-Hydroxyproline*

```smiles
N[C@@H](CCCC(CN)O)C(=O)O
```
*5-Hydroxylysine*

```smiles
N[C@H](CCC(=O)O)C(=O)O
```
*D-Glutamic acid*

```smiles
N[C@H](CO)C(=O)O
```
*D-Serine*

```smiles
NCCCC(=O)O
```
*GABA*

```smiles
NCCC(=O)O
```
*Beta-Alanine*

### Classification
1. **By structure**: Based on functional group location (α, β, γ, etc.)
2. **By polarity**: Grouped by side chain functional groups
3. **By pH level**: Acidic (Asp, Glu), Basic (Lys, Arg, His), Neutral (Gly, Ala, etc.)
4. **By nutritional importance**: Essential, Semi-essential, Non-essential

### Nomenclature
- Named as derivatives of carboxylic acids
- The carboxyl (-COOH) group is the parent chain
- All other groups are named as substituents
- Examples: Methionine = 2-amino-4-methylthiobutanoic acid; Asparagine = 2,4-diamino-4-oxobutanoic acid

### Physical Properties
1. **Crystalline solids with high melting points** — strong ionic attractions between zwitterions
2. **Solubility in water** — generally soluble; insoluble in non-polar solvents; varies with R-group
3. **Highly polar molecules** — large dipole moment; high dielectric constant
4. **Zwitterion formation** — dominant form in solution (no net charge, but dipolar)

```smiles
[NH3+][C@@H](*)C(=O)[O-]
```
*General amino acid zwitterion*

```smiles
[NH3+]CC(=O)[O-]
```
*Glycine zwitterion, pI = 6.0*

### Chemical Properties

#### Reactions of the Carboxylic Acid Group
1. **With NaOH**: Neutralization → salt + water
2. **With alcohol (Esterification)**: Ester formed with alcohol in presence of acid (HCl/H⁺)

```smiles
[NH3+]CC(=O)[O-].[Na+].[OH-]>>[NH3+]CC(=O)[O-].[Na+].[OH-]
```
*Glycine zwitterion + NaOH → sodium glycinate + H₂O*

```smiles
[NH3+]CC(=O)[O-].CO.[H+].[Cl-]>>[NH3+]CC(=O)OC.[Cl-]
```
*Glycine + methanol (H⁺) → glycine methyl ester*

#### Reactions of the Amino Group
1. **With HCl**: Forms aminium salt
2. **With acid chlorides**: Formation of acyl derivatives
3. **With nitrous acid (HNO₂) at 0°C**: Formation of α-hydroxy carboxylic acids; products include alcohols, haloalkanes, and alkenes

```smiles
[NH3+]CC(=O)[O-].[H+].[Cl-]>>[NH3+]CC(=O)O.[Cl-]
```
*Glycine zwitterion + HCl → glycinium chloride*

```smiles
N[C@@H](C)C(=O)O.O=N[O-].[Na+].[Cl-].[Na+].Cl>>CC(O)C(=O)O
```
*Alanine + HNO₂ → 2-hydroxypropanoic acid + N₂*

### Peptide Bond Formation

Amino acids link together through amide bonds (peptide bonds) between the α-COOH of one amino acid and the α-NH₂ of another, with elimination of water.

```smiles
NCC(=O)O.N[C@@H](C)C(=O)O>>NCC(=O)N[C@@H](C)C(=O)O
```
*Glycine + Alanine → glycylalanine (dipeptide) + H₂O*

> [!note] Peptide bond
> The peptide bond (-CO-NH-) is an amide linkage. Polypeptides are chains of amino acids; proteins consist of one or more polypeptide chains.

### Acid-Base Properties

#### Amphoteric Nature
- Can act as both acids and bases
- -NH₂ group → base (accepts protons)
- -COOH group → acid (donates protons)

#### pH-Dependent Forms
- **Low pH (Acidic)**: Ammonium Carboxylic Acid — fully protonated cation (+ charge)
- **Neutral pH (pI)**: Zwitterion — no net charge
- **High pH (Basic)**: Amino Carboxylate Ion — fully deprotonated anion (- charge)

```smiles
[NH3+][C@@H](*)C(=O)O
```
*Low pH (acidic) — fully protonated cation*

```smiles
[NH3+][C@@H](*)C(=O)[O-]
```
*Neutral pH (pI) — zwitterion, no net charge*

```smiles
N[C@@H](*)C(=O)[O-]
```
*High pH (basic) — fully deprotonated anion*

#### pKa Values
- Carboxyl group (-COOH): pKa ≈ 2
- Amino group (-NH₃⁺): pKa ≈ 9–10
- Example: glycine pKa₁ ≈ 2.3, pKa₂ ≈ 9.6, pI = 6.0

#### Isoelectric Point (pI)
- Neutral side chains: pI = ½(pKa₁ + pKa₂)
- Acidic side chains: average of two most acidic pKa values
- Basic side chains: average of two least acidic pKa values
- Example: Lysine pI = (10.53 + 8.95)/2 = 9.74
- Neutral amino acids: isoelectric pH slightly acidic (5–6)
- Least soluble at pI

### Separation by Electrophoresis
- pI > solution pH → +ve charge → moves toward cathode (-)
- pI < solution pH → -ve charge → moves toward anode (+)
- pI = solution pH → no movement

## Related Topics

- [[Carboxylic Acids & Derivatives]] — Amide formation
- [[Polymer Chemistry]] — Proteins as natural polymers

## Study Notes

> [!important] Key biomolecular topic
> Amino acids and proteins are fundamental to biochemistry. Know the 20 common amino acids and their classifications.

## Related Course Page

- [[FAD1018 - Basic Chemistry II]]
