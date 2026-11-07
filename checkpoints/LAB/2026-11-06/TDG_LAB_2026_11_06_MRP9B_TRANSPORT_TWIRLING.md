# Complete TDG / Root2 — Laboratoire MRP9B : twirling des orientations contre transport entre cellules

**Date locale :** 6 novembre 2026 (America/Toronto)  
**Statut :** **DEUX TESTS CONSTRUCTIFS/NÉGATIFS CONDITIONNELS ; AUCUNE NOUVELLE DÉRIVATION MICROSCOPIQUE Q/GR ; MRP9B RESTE OUVERT**.  
**Branche :** laboratoire distinct ; aucun checkpoint canonique de TDG n'est altéré.  
**Ancres :** `CURRENT_FRONT_LATEST.md`, `CURRENT_STATE.md`, `checkpoints/SENTRY/2026-09-18/TDG_FORMAL_READOUT_FREE_DYNAMIC_L2_TO_L1_NONZERO_2026-09-18.md`, `checkpoints/SENTRY/2026-10-14/TDG_MRP9A_SAME_FACE_LINK_PROVENANCE_GAP_2026-10-14.md`, `checkpoints/LAB/2026-11-06/TDG_LAB_2026_11_06_TWIST_NO_GO.md`.

## 1. Objectif et frontière documentaire

L'expérience précédente a démontré dans l'immersion cubique testée que le simple *twist* de signe de S4 ne transforme pas le module tridimensionnel de TDG en vecteur spatial ordinaire : rang d'entrelacement 9/9, pas d'isomorphisme constant. L'obstruction sous forme d'entrelaceur `J` du secteur `l=2 -> l=1` reste non nulle dans le Q historique.

Le front **MRP9B** recherche l'exacte carte de fibre prédictive B4<->B3 de Q-B1592/Q-B1602, puis son lien entre deux cellules partageant la même face. Le dépôt GitHub donne les verdicts historiques (rang 3, tangente majoritairement de type *boost*), mais **pas la formule exécutable suffisante pour réobtenir le lien**. Le présent laboratoire ne prétend pas combler cette lacune par un ajustement ou une pseudo-inverse. Il détermine seulement les propriétés nécessaires d'un transport géométrique candidat.

**Hypothèse de dictionnaire (non démontrée depuis Q) :** on identifie les représentations `(l=2,l=1)` avec `STF_2(R^3)` (5 composantes) et le vecteur `R^3` (3 composantes). On normalise le rayon unique certifié :

`J = -(1/sqrt(3)) [ yz->x, xz->y, xy->z ]`, `Tr(J^T J)=1`.

Le coefficient physique non nul du modèle de référence n'est ni supprimé ni réétalonné. Les paramètres auxiliaires qui suivent ne sont pas des paramètres de Q.

## 2. Hypothèse A — l'orientation moyenne efface-t-elle la panne ?

Pour une rotation physique `R` et sa représentation tensorielle `U_5(R)` :

`J_R = R J U_5(R)^T`.

Distinguons impérativement :

- le **couplage moyen** `A_G = (1/|G|) sum_R J_R` ;
- la **réponse quadratique** `B_G = (1/|G|) sum_R J_R^T J_R`.

Les deux ne s'interchangent pas avec l'élimination d'un auxiliaire. Le calcul numérique sur des groupes finis complets donne :

| Groupe de rotations | Nombre | `||A_G||_F` | Spectre de `B_G` | Défaut isotrope `||B_G - Tr(B_G) I_5/5||_F` |
|---|---:|---:|---|---:|
| Tétraédrique T | 12 | 1 | `0,0,1/3,1/3,1/3` | 0,36514837 |
| Cubique O (~S4) | 24 | 2,4e-16 | `0,0,1/3,1/3,1/3` | 0,36514837 |
| Icosaédrique I (~A5) | 60 | 9,1e-17 | `1/5` répété cinq fois | 4,75e-16 |

**Théorème pour ce modèle :** le secteur `l=2` devient irréductible sous le groupe rotationnel icosaédrique de 60 éléments. `B_I` commute avec toute son action et, par le lemme de Schur et `Tr(B_I)=1`, `B_I=I_5/5` exactement. Inversement, le groupe cubique distingue deux sous-espaces, de dimensions 2 et 3, et laisse leur anisotropie quadratique intacte.

*Source externe pour la décomposition `l=2 -> H` sous la symétrie icosaédrique :* <https://pmc.ncbi.nlm.nih.gov/articles/PMC2711457/>.

**Important :** le Q de TDG ne contient pas une loi établie donnant accès à ces 60 rotations. Le twirling icosaédrique est un **contrôle de capacité**, pas une réparation existante.

### Contrôle dynamique de la réponse quadratique

Modèle auxiliaire volontairement simple : `M_eff = k^2 I_5 -(g^2/m^2) B_G`, avec `k^2=1`, `g=1`, `m^2=25`, pour les deux polarisations TT d'une onde dirigée suivant `z`.

| Orientation | Valeurs propres TT | Écart |
|---|---|---:|
| Couplage J initial | 0,9866666667 ; 1 | 0,0133333333 |
| Moyenne cubique | 0,9866666667 ; 1 | 0,0133333333 |
| Moyenne icosaédrique | 0,992 ; 0,992 | 0 |

**Verdict A :** une moyenne *cubique* n'enlève pas l'anisotropie du couplage effectif. Une moyenne *icosaédrique* enlève la séparation entre polarisations mais conserve une correction isotrope d'ordre zéro, `g^2/(5 m^2)`. Sa présence ne démontre ni une dynamique sans masse, ni l'invariance de jauge d'Einstein. Prendre `A_G=0` pour déclarer `B_G=0` serait une erreur.

## 3. Hypothèse B — un transport parallèle discret corrige-t-il le type géométrique ?

On construit **sept sites** : un site central et six voisins `+/-` le long de trois axes. Chaque site possède un repère local indépendant `R_s ∈ SO(3)`. Les tenseurs physiques sont décrits localement par `h_s=R_s^T H(x_s) R_s`. Le transport du site `s` vers le centre est

`L_(0<-s) = R_0^T R_s` ; `h_(s->0)=L_(0<-s) h_s L_(0<-s)^T`.

La divergence centrée emploie les différences centrales *après* transport, puis contracte avec les composantes de l'axe de dérivation dans le repère central :

`(D_a h)_b = sum_{i,c} R_0[i,c] (h_(+i->0)-h_(-i->0))[b,c]/(2a)`.

Pour une transformation arbitraire de repère locale `R_s -> R_s G_s`, la loi de transport est `L_(0<-s) -> G_0^T L_(0<-s) G_s`, ce qui implique `D h -> G_0^T D h`. Le test utilise sept repères et sept transformations aléatoires indépendantes, graine fixée.

Pour une onde plane à deux composantes TT arbitrairement combinées, de vecteur `k` proportionnel à `(0.3, 0.5, 0.8124...)`, la divergence continue est exactement nulle. Le résidu discret devrait donc tendre à zéro comme `a^2` :

| Pas `a` | Divergence **avec** transport | Divergence **sans** transport | Défaut covariance de jauge locale |
|---:|---:|---:|---:|
| 0,4 | 0,0023604034 | 0,45008145 | 4,1e-16 |
| 0,2 | 0,0005930786 | 0,87851804 | 5,9e-16 |
| 0,1 | 0,0001484562 | 1,77768871 | 5,6e-16 |
| 0,05 | 0,0000371257 | 3,59801324 | 3,5e-15 |
| 0,025 | 0,00000928216 | 7,24943245 | 3,5e-15 |

Pente de convergence mesurée : **1,9978446**. Le transport correct est donc exactement covariant sous le changement de repères testé et converge à l'ordre 2. La version qui soustrait naïvement des composantes écrites dans des repères différents diverge comme `1/a`.

**Verdict B :** dans ce laboratoire, un transport de repères plus une vraie dérivée spatiale construit une divergence géométrique fonctionnelle, sans supprimer manuellement une polarisation TT. C'est une **machine témoin constructive**. Mais les transports sont construits avec des repères SO3 *donnés*, non extraits du Q microscopique. Leur caractère *plat* dans le test à sept sites n'a aucune portée gravitationnelle.

## 4. Courbure et holonomie : contrôle indépendant

Une boucle à quatre liens contient une rotation interne de `0,41` radian. L'holonomie a une trace `1+2 cos(0,41)=2,8342416456`. Sous quatre changements de repère indépendants, sa trace est conservée à `4,4e-16` et sa conjugaison à `9,35e-16`.

Cela montre qu'une connexion non plate **peut être décrite de façon covariante**, mais ne dit rien sur son lien physique à la courbure de Riemann, aux contraintes de Gauss dérivées de Q ou à la fermeture HDA.

## 5. Ce que nous avons effectivement appris sur TDG

1. Un simple changement de base S4 ne répare pas J (checkpoint précédent).
2. Une moyenne d'orientations cubiques annule `E[J]` mais **pas** `E[J^T J]` ni la séparation TT.
3. Une moyenne icosaédrique supprime l'anisotropie quadratique par représentation, **pas** sa correction scalaire ni une masse/gauge physique.
4. Une **véritable connexion entre cellules** fournit un objet mathématique capable de différencier des tenseurs de manière indépendante des repères et d'annuler la divergence TT en limite continue.
5. Ni `I_5/5` ni le transport `R_0^T R_s` ne sont aujourd'hui une formule démontrée de `Q-B1592`.

**Diagnostic :** la piste la plus sélective est **la dérivation d'un transport entre cellules à partir du véritable Q et de sa fibre prédictive**. Une simple suppression par moyenne est insuffisante. Il faut garder distincts `SL2` prédictif/non compact et `SO3` du repère physique : on ne peut pas inventer une carte entre ces groupes.

## 6. Prochain test légal (MRP9B reste ouvert)

- Récupérer ou reconstruire d'abord la **carte exécutable Q-B1592/Q-B1602** depuis son résolvant, sans polar compression ni pseudo-inverse arbitraire du bloc 6×2.
- Sur **deux cellules réelles** partageant un même B3/M2, obtenir les attachements `Khat_CF, Khat_C'F` et former le lien relatif de Q-B746.
- Tester covariance de réétiquetage, non-centralité projective, holonomie, et limites sous raffinements b4/b24.
- Ensuite seulement rechercher un transport de repère/direction issu de Q et vérifier, sans cible GR imposée, la fermeture des contraintes et l'absence de fuite TT.
- Si la carte reste introuvable, classer le blocage comme **lacune de provenance**, pas comme falsification scientifique.

## 7. Reproduction et catégories de preuve

- Script : `tdg_mrp9b_transport_twirling_2026_11_06.py` (`numpy`, `scipy`).
- Résultats : `tdg_mrp9b_transport_twirling_resultats_2026_11_06.json`.
- Journal texte : `tdg_mrp9b_transport_twirling_execution_2026_11_06.txt`.
- Sommes de contrôle : `TDG_MRP9B_TRANSPORT_TWIRLING_SHA256.txt`.

**DÉRIVÉ conditionnel :** les identités de groupes finis, les valeurs propres, l'ordre 2 de convergence, l'invariance de jauge locale de la machine à sept sites, la trace d'holonomie.

**ASSUMÉ :** interprétation physique du rayon J en termes de tenseurs et vecteurs continus; ensembles rotationnels proposés; métrique Euclidienne locale; présence d'un auxiliaire massique du modèle d'essai.

**OUVERT :** extraction du lien Q-B1592, structure effective issue de Q, contrainte scalaire B5 sous évolution, premier ordre HDA, absence de masse gravitationnelle, dynamique d'Einstein.

**RÉSULTAT PHYSIQUE NON PROMU :** aucune modification du front `CURRENT_FRONT_LATEST.md` ni de la référence `Q-B1858L` n'est justifiée par ce laboratoire.
