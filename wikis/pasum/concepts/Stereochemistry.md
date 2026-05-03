---
title: "Stereochemistry"
date: 2026-04-27
tags:
  - concept/chemistry
  - topic/organic-chemistry
  - status/seedling
---

# Stereochemistry

The study of the three-dimensional arrangement of atoms in molecules and their effects on chemical and physical properties.

## Types of Isomerism

### Constitutional (Structural) Isomers
- Same molecular formula, different connectivity
- Chain, position, functional group isomers

### Stereoisomers
- Same molecular formula and connectivity, different spatial arrangement
- **Configurational**: Cannot interconvert without breaking bonds
- **Conformational**: Can interconvert by rotation around single bonds

## Chirality

A molecule is **chiral** if it is non-superimposable on its mirror image.

### Conditions for Chirality
- No plane of symmetry
- No center of symmetry
- Most commonly: Presence of a carbon with four different groups attached (chiral center/stereocenter)

### Chiral Centre Count & Molecular Chirality
From lecture:
- **0 chiral centres**: Usually achiral, but *not always* (rare cases exist — e.g., allenes with chiral axis)
- **1 chiral centre**: Always a chiral molecule
- **>1 chiral centres**: Can be chiral or achiral (meso compounds are achiral)

### Rare Cases
- **Chiral without a chiral centre**: Certain allenes and biphenyls are chiral due to a chiral axis, even though no single atom has four different groups (p12)
- **Achiral without a plane of symmetry**: Some molecules lack an internal plane of symmetry yet are still achiral because their mirror image is superimposable after rotation (p16)

## Enantiomers

- Mirror images that are non-superimposable
- Identical physical properties (except for optical activity and interactions with other chiral substances)
- Identical chemical properties (except in chiral environments)
- Rotates plane-polarized light in equal but opposite directions

### Optical Activity
- **Dextrorotatory (+ or d)**: Rotates plane-polarized light clockwise (to the right)
- **Levorotatory (- or l)**: Rotates plane-polarized light counterclockwise (to the left)
- **Specific rotation**: [α] = α/(l × c)

> [!important] Direction of rotation (d/l) is NOT related to R/S configuration
> A compound with R configuration can be either d or l, and a compound with S configuration can also be either d or l.
> Example from lecture: S-(+)-glyceraldehyde and S-(-)-alanine.

- S-(+)-Glyceraldehyde (S configuration, dextrorotatory):
```smiles
OC[C@@H](O)C=O
```
- S-(-)-Alanine (S configuration, levorotatory):
```smiles
C[C@@H](N)C(=O)O
```
**Enantiomeric excess (ee):**
$$
ee = \frac{\text{Observed rotation}}{\text{Specific rotation of pure enantiomer}}
$$

## R/S Configuration (Cahn-Ingold-Prelog Priority Rules)

1. Assign priorities to the four groups attached to the chiral center (1 = highest, 4 = lowest)
2. Orient the molecule so that the lowest priority group points away
3. Trace from 1 → 2 → 3:
   - Clockwise = R (Rectus)
   - Counterclockwise = S (Sinister)

### Fischer Projections
- Vertical lines: bonds going away (into the page)
- Horizontal lines: bonds coming toward you (out of page)

**Steps to draw (from lecture):**
1. Draw a vertical line for the carbon chain and horizontal lines for all middle carbon atoms
2. Place the first atom/group (based on IUPAC numbering) at the top and the last at the bottom of the vertical line
3. Attach the remaining atoms/groups to the ends of the horizontal lines
4. If a non-chiral carbon appears near the top or bottom, it can be merged with its attached group to form a larger substituent

**No carbon chain case:** If a molecule has no carbon chain, the highest-priority group (CIP) is typically placed at the top and the lowest-priority at the bottom for consistency.

**Converting 3D to Fischer:**
1. First atom/group (IUPAC numbering) at top; last at bottom
2. Both top and bottom groups should be positioned away from the observer (into the plane)
3. The remaining two groups should be positioned near the observer (out of the plane)

**Example — 2-Chlorobutane:**
```smiles
CCC(C)Cl
```
**Enantiomers with explicit R/S notation (`@` / `@@`):**
- (R)-2-Chlorobutane:
```smiles
CC[C@@H](C)Cl
```
- (S)-2-Chlorobutane:
```smiles
CC[C@H](C)Cl
```
## Stereoisomers with Multiple Chiral Centres

Maximum number of stereoisomers = **2ⁿ**, where n = number of chiral centres.

### Diastereomers

- Stereoisomers that are NOT mirror images
- Different physical properties, including melting points, boiling points, solubility, and density
- Different chemical properties
- Epimers: Diastereomers differing at only one stereocenter

**Acyclic example — 2-bromo-3-chloropentanal (4 stereoisomers):**
```smiles
O=CC(Br)C(Cl)CC
```
**Cyclic example — 1-fluoro-2-methylcyclobutane (4 stereoisomers, no meso):**
```smiles
CC1CCC1F
```
**Cyclic example — 1,2-dimethylcyclobutane (3 stereoisomers, one meso):**
```smiles
CC1CCC1C
```
## Meso Compounds

- Molecules with multiple chiral centers that are achiral overall
- Possess an internal plane of symmetry
- Optically inactive despite having stereocenters
- Have different physical properties from enantiomers and diastereomers due to the symmetry

**Example — 3,4-dimethylhexane (meso form, (3R,4S)):**
```smiles
CC[C@H](C)[C@@H](C)CC
```
## Geometric (Cis-Trans) Isomerism

### Alkenes (E/Z Nomenclature)
- **E** (Entgegen): Higher priority groups on opposite sides
- **Z** (Zusammen): Higher priority groups on same side

**Example — (E)- and (Z)-2-Butene:**
- (E)-2-Butene:
```smiles
C/C=C/C
```
- (Z)-2-Butene:
```smiles
C/C=C\C
```
### Cyclic Compounds
- Cis: Substituents on same side of ring
- Trans: Substituents on opposite sides of ring

## Racemic Mixtures

- 50:50 mixture of both enantiomers (1:1 d:l ratio)
- Optically inactive (no net rotation of light)
- Different physical properties from pure enantiomers, especially melting point and solubility

**Formation:**
1. **Mixing**: Simply combining equal amounts of (+) and (-) enantiomers
2. **Racemization**: A pure enantiomer interconverts into a racemate under heat, acid/base catalysts, or specific reactions (e.g., heating 2-chlorobutane)
3. **Synthesis**: Many non-selective reactions produce racemates due to random formation of chiral centres (e.g., hydrohalogenation of alkenes)

**Real-world examples:**
- **Thalidomide**: (R)-form was safe; (S)-form caused severe birth defects
- **Ibuprofen**: Sold as a racemic mixture; only the (S)-enantiomer is biologically active

**Resolution methods:**
- Reaction with chiral reagents (forms diastereomers with different solubility)
- Selective crystallization
- Biological methods (enzymatic resolution)
- Chiral chromatography

## Related Topics
- [[Carbonyl Compounds]] — Stereochemistry in nucleophilic addition
- [[Amines & Amino Acids]] — Chirality in biomolecules

## Sources
- [[FAD1018 W6 — Stereochemistry]]
- [[FAD1018 - Basic Chemistry II]]
