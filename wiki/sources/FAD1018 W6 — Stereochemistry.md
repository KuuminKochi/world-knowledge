---
title: "FAD1018 W6 — Stereochemistry"
date: 2026-04-27
tags:
  - source/lecture
  - course/FAD1018
  - topic/stereochemistry
  - status/seedling
week: 6
lecturer: "[[Mr. Che Mohd Farhan Bin Che Mat Dusuki]]"
---

# FAD1018 W6 — Stereochemistry

Week 6 lecture covering stereochemistry. Source files: `W6 (1).pdf`, `W6 (2).pdf`, `W6 (3).pdf` from lecture notes folders.

## Summary

Introduction to stereoisomerism, chirality, optical activity, and stereochemical nomenclature.

## Key Concepts

- [[Stereochemistry]] — 3D arrangement of atoms
- [[Chirality]] — Non-superimposable mirror images
- Enantiomers — Mirror image stereoisomers
- Diastereomers — Non-mirror image stereoisomers
- [[Optical Activity]] — Rotation of plane-polarized light
- R/S Configuration — Cahn-Ingold-Prelog priority rules
- Fischer Projections — 2D representation of 3D structures
- Meso Compounds — Achiral molecules with chiral centers

## Lecture Coverage

### 1. Isomerism Review (p4)
- Constitutional (structural) isomers: same formula, different connectivity (positional, chain, functional group)
- Stereoisomers: same formula and connectivity, different spatial arrangement
  - Geometric (cis/trans, E/Z)
  - Optical

### 2. Stereocentre / Stereogenic Centre (p6)
A point in a molecule where exchange of substituents leads to different stereoisomers.
- **Chiral Centre**: 4 different substituents, tetrahedral (chiral carbon, or chiral non-carbon: N, P, S)
- **Restricted rotation centre**: double bond, cyclic ring

### 3. Chirality (p7–16)
- **Chiral molecule**: non-superimposable mirror image
  - Usually has ≥1 chiral centre (but not always — *rare case 1*)
  - No internal plane of symmetry (but some achiral molecules also lack it — *rare case 2*)
  - MUST be non-superimposable on its mirror image
  - Optically active (rotates plane-polarized light)
- **Achiral molecule**: superimposable mirror image
  - Usually lacks chiral centre (but having one doesn't guarantee chirality)
  - Typically has internal plane of symmetry
  - Optically inactive

**Lecture examples:**
- **Butan-2-ol** — chiral (1 chiral centre, no internal plane, non-superimposable)
- **Allenes** (e.g. 1,3-dichloroallene derivative) — *rare case 1*: chiral molecule **without** a chiral centre (p12)
- **Propan-2-ol** — achiral (no chiral centre, has internal plane, superimposable mirror image)
- **Cyclohexane derivative** (1,4-disubstituted with Br/Cl) — *rare case 2*: achiral molecule **without** an internal plane of symmetry (p16)

**SMILES examples:**
```smiles
CCC(C)O
CC(C)O
```

### 4. 3D Representations (p18–19)
**Wedge-dash conventions:**
1. Identify chiral centre
2. Draw two solid lines for bonds in the plane of the paper
3. Draw one wedge line for bond projecting out (toward viewer)
4. Draw one dashed line for bond projecting behind (away from viewer)

**Note**: If one solid bond is on top and another on the bottom left, both wedge and dashed bonds go on the bottom right (and vice versa).

### 5. Fischer Projections (p20–24)
- Vertical lines: bonds going **into** the page (away from viewer)
- Horizontal lines: bonds coming **out** of the page (toward viewer)

**Steps to draw:**
1. Draw vertical line for carbon chain; horizontal lines for all middle carbons
2. Place first atom/group (IUPAC numbering) at top; last at bottom
3. Attach remaining atoms/groups to ends of horizontal lines
4. If a non-chiral carbon appears near top or bottom, merge with attached group

**Example — 2-Chlorobutane:**
```smiles
CCC(C)Cl
```

**Enantiomers in Fischer**: Mirror images across the vertical axis.

**No carbon chain case** (e.g., aminochloromethanol):
- Highest-priority group (CIP rules) typically at top
- Lowest-priority group at bottom
```smiles
NC(Cl)O
```

### 6. Converting 3D to Fischer (p25–28)
1. First atom/group (IUPAC numbering) at top; last at bottom
2. Top and bottom groups positioned **away** from observer (into the plane)
3. Remaining two groups positioned **near** observer (out of the plane)

View the molecule so the two groups that should be vertical are pointing away, then project.

### 7. Enantiomers vs Diastereomers (p22, p31–32)
- **Enantiomers**: non-superimposable mirror images. Identical physical properties except optical rotation and interactions with chiral substances.
- **Diastereomers**: stereoisomers that are NOT mirror images. Different physical properties (melting point, boiling point, solubility, density).

**Maximum stereoisomers = 2ⁿ**, where n = number of chiral centres.

### 8. Stereoisomers with >1 Stereocentre (p31–40)

**Acyclic example — 2-bromo-3-chloropentanal:**
```smiles
O=CC(Br)C(Cl)CC
```
Predicted: 2² = 4 stereoisomers (2 pairs of enantiomers).
Diastereomer pairs: any pair from different enantiomeric pairs.

**Acyclic example — 3,4-dimethylhexane:**
```smiles
CCC(C)C(C)CC
```
Predicted: 4 stereoisomers, but **actual = 3** (one is a meso compound).

**Meso Compounds** (p34):
- Compound with chiral centres that has an internal plane of symmetry
- Achiral (optically inactive)
- Different physical properties from enantiomers and diastereomers

**Cyclic example — 1-fluoro-2-methylcyclobutane:**
```smiles
CC1CCC1F
```
Predicted: 4 stereoisomers. No meso compound. Actual: 4.

**Cyclic example — 1,2-dimethylcyclobutane:**
```smiles
CC1CCC1C
```
Predicted: 4 stereoisomers. Meso compound exists (cis form). Actual: 3 stereoisomers.

### 9. Optical Activity (p42–47)
- **Optically active compounds** rotate plane-polarized light
- Must be chiral (lacks internal plane, non-superimposable mirror image)
- Enantiomers rotate by same magnitude but opposite directions

**Levorotatory (l or -)**: rotates counterclockwise (to the left)
**Dextrorotatory (d or +)**: rotates clockwise (to the right)

> [!important] R/S configuration is NOT related to d/l direction.
> A compound with R configuration can be either d or l, and S can be either d or l.
> Example: S-(+)-glyceraldehyde and S-(-)-alanine.

**Enantiomeric excess (ee):**
$$
ee = \frac{\text{Observed rotation}}{\text{Specific rotation of pure enantiomer}}
$$

**Example table from lecture:**
| Sample | Observed Rotation |
|--------|-------------------|
| Pure (+)-enantiomer | +100° |
| Pure (-)-enantiomer | -100° |
| Racemic mixture (50:50) | 0° |
| 75% (+) + 25% (-) | +50° |
| 20% (+) + 80% (-) | -60° |

### 10. Racemic Mixtures (p48–51)
- **Definition**: equal amounts (1:1) of two enantiomers of a chiral compound
- Optically inactive (no net rotation)
- Different physical properties from pure enantiomers (melting point, solubility)

**Formation:**
1. **Mixing**: combining equal amounts of (+) and (-)
2. **Racemization**: pure enantiomer interconverts under heat, acid/base, or specific reactions (e.g., heating 2-chlorobutane)
3. **Synthesis**: non-selective reactions produce racemates (e.g., hydrohalogenation of alkenes)

**Real-world examples:**
- **Thalidomide**: (R)-form safe; (S)-form caused severe birth defects
- **Ibuprofen**: sold as racemic mixture; only (S)-enantiomer biologically active

**Resolution methods:**
- Reaction with chiral reagents (forms diastereomers with different solubility)
- Selective crystallization
- Biological methods (enzymatic resolution)
- Chiral chromatography

### 11. Exercises (p17, p29, p30, p37, p41)
- **Exercise 13.1**: Determine chiral/achiral; mark chiral carbons with *
- **Exercise 13.2**: Determine correct Fischer projection from 3D images
- **Exercise 13.3**: Determine if pairs are enantiomers or identical
- **Exercise 13.4**: Match 3D images with Fischer projections
- **Exercise 13.5**: Determine if pairs are enantiomers, diastereomers, or identical

## Related Topics

- [[Carbonyl Compounds]] — Stereochemistry in reactions
- [[Amines & Amino Acids]] — Chiral centers in biomolecules

## Study Notes

> [!important] High-frequency organic topic
> Stereochemistry appears in 4/5 papers with ~8% average mark weight. Essential for organic chemistry sections.

## Related Course Page

- [[FAD1018 - Basic Chemistry II]]
