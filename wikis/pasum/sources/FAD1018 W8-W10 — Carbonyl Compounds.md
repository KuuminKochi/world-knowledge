---
title: "FAD1018 W8-W10 — Carbonyl Compounds"
date: 2026-04-27
tags:
  - source/lecture
  - course/FAD1018
  - topic/carbonyl-compounds
  - topic/aldehydes-ketones
  - status/seedling
week: 8-10
lecturer: "[[Mrs Azlina Puang]]"
institution: "[[Universiti Malaya — Pusat Asasi Sains]]"
---

# FAD1018 W8-W10 — Carbonyl Compounds

Weeks 8–10 lectures covering aldehydes and ketones. Lecturer: Mrs Azlina Puang. Source files: `W8-01.png` through `W8-19.png` (Lecture 1), plus `W9.pdf`, `W10 (1).pdf`, `W10 (2).pdf`, `W10 (3).pdf`, `W10 (4).pdf`.

## Summary

Comprehensive study of carbonyl compounds (aldehydes and ketones) including structure, nomenclature, preparation, reactions, and identification tests.

## Key Concepts

- [[Carbonyl Compounds]] — Compounds with C=O functional group
- [[Aldehydes]] — Carbonyl at carbon chain end (-CHO)
- [[Ketones]] — Carbonyl within carbon chain (>C=O)
- Nucleophilic Addition — Characteristic carbonyl reaction
- Oxidation/Reduction — Redox reactions of carbonyls
- Addition-Elimination — Reactions with nitrogen nucleophiles

---

## W8 — Lecture 1: Introduction, Nomenclature, Preparation & Physical Properties

### 1.1 Introduction

The simplest carbonyl compounds are **aldehydes** (`RCHO`) and **ketones** (`RCOR`). They contain the carbonyl group as the functional group and have a **general formula** of:

$$C_nH_{2n}O$$

In the simplest aldehyde (**formaldehyde**), the carbonyl carbon is bonded to two hydrogens; in other aldehydes it is bonded to one hydrogen and one alkyl/aryl group (`R`). In ketones, the carbonyl carbon is bonded to two alkyl/aryl groups.

Both are similar in structure and properties, but differ in reactivity in oxidation and nucleophilic addition reactions. **Aldehydes are more reactive than ketones.**

Key structures:

```smiles
C=O
CC=O
CC(=O)C
c1ccccc1C=O
C1CCCCC1=O
CC(=O)c1ccccc1
```

### 1.2 Nomenclature

#### Aldehydes
- The **longest chain** containing the functional group is determined.
- The chain is numbered beginning from the functional group (**carbon of carbonyl always has the 1-position**).
- Parent name is terminated with suffix **-al**.
- The location of substituents is denoted with the corresponding number.
- **Cyclic / aromatic aldehydes**: If attached to a ring, add **‘carbaldehyde’** to the cyclic compound name. For aromatic aldehydes, **benzaldehyde** is more commonly used than *benzenecarbaldehyde*.

> [!note] Functional group priority
> If a compound has two functional groups, the one with **lower priority** is indicated by its **prefix** (as substituent). Therefore, the ketone oxygen in a compound that also contains an aldehyde is indicated by the prefix **‘oxo’** (e.g., **4-oxohexanal**).

Aldehyde examples:

| Systematic name | Common name | SMILES |
|-----------------|-------------|--------|
| methanal | formaldehyde | `C=O` |
| ethanal | acetaldehyde | `CC=O` |
| 2-bromopropanal | α-bromopropionaldehyde | `CC(Br)C=O` |
| 3-chlorobutanal | β-chlorobutyraldehyde | `CC(Cl)CC=O` |
| 3-methylbutanal | isovaleraldehyde | `CC(C)CC=O` |
| hexanedial | — | `O=CCCCCC=O` |
| trans-2-methylcyclohexanecarbaldehyde | — | `CC1CCCCC1C=O` |
| benzenecarbaldehyde | benzaldehyde | `c1ccccc1C=O` |

#### Ketones
- The longest chain containing the functional group is determined.
- The chain is numbered beginning from the **terminal closer to the functional group**.
- Parent name is terminated with suffix **-one**.
- The location of substituents is denoted with the corresponding number.
- In cyclic ketones, the carbonyl is assumed to be at the **1-position**.

> [!note] Minimum position
> For acyclic ketones, the carbonyl should be given the **lowest possible locant** (minimum at the 2nd carbon if possible).

Ketone examples:

| Systematic name | Common / derived name | SMILES |
|-----------------|----------------------|--------|
| propanone | acetone / dimethyl ketone | `CC(=O)C` |
| 3-hexanone | ethyl propyl ketone | `CCC(=O)CCC` |
| 6-methyl-2-heptanone | isohexyl methyl ketone | `CC(=O)CCCC(C)C` |
| cyclohexanone | — | `O=C1CCCCC1` |
| butanedione | — | `CC(=O)C(=O)C` |
| 2,4-pentanedione | acetylacetone | `CC(=O)CC(=O)C` |
| 4-hexen-2-one | — | `CC(=O)CC=CC` |

#### Phenyl-substituted Ketones
Common names are also used: the number of carbons (other than those of the phenyl group) is indicated by the common name of the corresponding carboxylic acid, substituting **“-ophenone”** for **“-ic acid”**.

| Systematic name | Common name | SMILES |
|-----------------|-------------|--------|
| phenylethanone | acetophenone / methyl phenyl ketone | `CC(=O)c1ccccc1` |
| 1-phenyl-1-butanone | butyrophenone / phenyl propyl ketone | `CCCC(=O)c1ccccc1` |
| 1-phenyl-2-butanone | — | `CC(=O)Cc1ccccc1` |

---

### 1.3 Synthesis / Preparation

#### Aldehydes & Aliphatic Ketones from Alcohols

**Primary alcohol → Aldehyde**

Use a **mild oxidizing agent**; **PCC (Pyridinium chlorochromate) in CH₂Cl₂** is the only reagent that stops at the aldehyde.

```smiles
RCH2OH.O=[Cr](O)O.c1ccncc1>>RC=O
```

Strong oxidizing agents (`K₂Cr₂O₇ / H₂SO₄`, `CrO₃ / H₂SO₄`, `KMnO₄ / H₂SO₄`) will over-oxidize primary alcohols to **carboxylic acids**.

**Secondary alcohol → Ketone**

Any of the above oxidizing agents (including PCC) can be used. Secondary alcohols oxidize to ketones without over-oxidation.

```smiles
R1R2CHOH.[O]>>R1R2C=O
```

> [!example] Example: Oxidation of secondary alcohol
> 3-tert-butylcyclohexanol → 3-tert-butylcyclohexanone (`CC(C)(C)C1CCCC(=O)C1`)
> Reagent: `Na₂Cr₂O₇ / H⁺`

#### Ozonolysis of Alkenes

Cleavage of the C=C bond in an alkene and insertion of oxygen atoms to obtain carbonyl products.

$$R'CH=CR_2 \xrightarrow[\text{H}_2\text{O / Zn}]{\text{O}_3} R'CHO + R_2C=O$$

> [!example] Example
> `CH₃CH=C(CH₃)₂` (5 C) → `CH₃CHO` (2 C) + `(CH₃)₂C=O` (3 C)
>
> ```smiles
A good method for preparing aromatic ketones:
Benzene reacts with an acyl chloride in the presence of `AlCl₃` (Lewis acid catalyst) to give an aromatic ketone, HCl, and regenerate `AlCl₃`.
Reference comparison (comparable MW):
```smiles
# Cyanohydrin formation
R1R2C=O.HC#N>>R1R2C(O)C#N
```

#### b) Addition of Grignard Reagents
- Formation of alcohols
- Primary, secondary, tertiary alcohol formation

```smiles
R1C(=O)R2.C[Mg]Br>>R1C(R2)([O-])C.[Mg+]Br
```

#### c) Addition of Alcohols
- Acetal and ketal formation
- Protecting groups
- Cyclic acetals

```smiles
RC=O.CO.CO>>RC(OC)OC.O
RC=O.OCCO>>RC1OCCO1.O
```

#### d) Addition of Bisulfite
- Bisulfite addition compounds
- Purification applications

```smiles
RC=O.[Na+].[O-]S(=O)O>>RC(O)S(=O)([O-])O.[Na+]
```

### 5. Addition-Elimination Reactions

#### With Nitrogen Nucleophiles:
- Oxime formation (hydroxylamine)
- Hydrazone formation (hydrazine)
- Phenylhydrazone formation
- 2,4-DNP test (orange/red precipitate)
- Imine/Schiff base formation (primary amines)

```smiles
R1R2C=O.NO>>R1R2C=NO.O
R1R2C=O.NN>>R1R2C=NN.O
R1R2C=O.NNc1ccccc1>>R1R2C=NNc1ccccc1.O
R1R2C=O.NNc1ccc([N+](=O)[O-])cc1[N+](=O)[O-]>>R1R2C=NNc1ccc([N+](=O)[O-])cc1[N+](=O)[O-].O
R1R2C=O.NR3>>R1R2C=NR3.O
```

### 6. Oxidation and Reduction

#### Oxidation:
- Aldehydes → Carboxylic acids
- Ketones — resistant (except under vigorous conditions)
- Tollens' test (silver mirror)
- Fehling's/Benedict's test (brick-red precipitate)

```smiles
RC=O.[O]>>RC(=O)O
```

#### Reduction:
- Aldehydes → Primary alcohols
- Ketones → Secondary alcohols
- Clemmensen reduction
- Wolff-Kishner reduction

```smiles
RC=O.[H]>>RCO
R1R2C=O.[H]>>R1R2CO
RC(=O)R1.[Zn].Cl>>RCR1
RC(=O)R1.NN.[OH-]>>RCR1.N#N.O
```

### 7. Aldol Condensation
- Self-condensation of aldehydes/ketones
- Crossed aldol condensation
- Dehydration to α,β-unsaturated carbonyls

```smiles
CC=O.CC=O.[OH-]>>CC(O)CC=O
CC(O)CC=O>>CC=CC=O.O
c1ccccc1C=O.CC=O.[OH-]>>c1ccccc1C=CC=O.O
```

### 8. Cannizzaro Reaction
- Disproportionation of non-enolizable aldehydes
- Base-catalyzed redox reaction

```smiles
c1ccccc1C=O.c1ccccc1C=O.[OH-]>>c1ccccc1C(=O)[O-].c1ccccc1CO
```

### 9. Haloform Reaction
- Iodoform test for methyl ketones
- Yellow precipitate of CHI₃

```smiles
CC(=O)C.I[I-]I.[OH-]>>CC(=O)[O-].[I-].CI(I)I
```

### 10. Identification Tests Summary
| Test | Aldehydes | Ketones |
|------|-----------|---------|
| Tollens' | Silver mirror | Negative |
| Fehling's | Brick-red Cu₂O | Negative |
| 2,4-DNP | Orange/red ppt | Orange/red ppt |
| Iodoform | Positive if CH₃CHO | Positive if methyl ketone |
| Schiff's | Pink color | Negative |

## Related Topics

- [[Alcohol & Phenol]] — Precursors to carbonyls
- [[Carboxylic Acids & Derivatives]] — Oxidation products
- [[Amines & Amino Acids]] — React with carbonyls

## Study Notes

> [!important] High-frequency organic topic
> Aldehydes & Ketones appear consistently in finals with ~7% average mark weight. Know your identification tests!

## Related Course Page

- [[FAD1018 - Basic Chemistry II]]
