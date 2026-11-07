# Complete TDG — MRP9B : récupération des vraies sources, transport sur deux cellules et réponse de courbure

**Date :** 2026-11-06 (America/Toronto)  
**Statut :** SOURCE Q-B1592 RETROUVÉE ET REJOUÉE / Q-B1852 SOURCE EXACTE REJOUÉE / MRP9B SAME-FACE CHART = CANDIDAT NON PROMU / RÉPONSE DE BOUCLE À L'ORDRE a² = POSITIVE ET READOUT-DÉPENDANTE / PAS DE GR DÉRIVÉE.  
**Autorité canonique :** `Q-B1858L` et `CURRENT_FRONT_LATEST.md`, inchangés.  
**Branche :** laboratoire exploratoire, aucune modification des coefficients de Q, ni du modèle canonique.

## 1. Question et élément nouveau

MRP9A, le 2026-10-14, avait correctement constaté que la formule exécutable exacte Q-B1592 n'était pas accessible dans les sources alors disponibles. Une recherche ciblée dans la Library `/TDG/Recovery` permet maintenant de retrouver une archive contenant **la vraie source historique** et son exécutable de certification. La même recherche récupère aussi le Q-B1852 RefinedQ exact, SHA-256 identique au checkpoint Q-B1852.

**Cette récupération clôt le trou documentaire Q-B1592, mais non le théorème de transport physique MRP9B.** Une transposition de l'ancienne formule de raccordement H160 vers la fibre bright-M2 de RefinedQ nécessite encore un contrôle de typage et de naturalité.

## 2. Provenance exacte et vérifications exécutées

Source historique Q-B1592 :

- Archive Library `/TDG/Recovery/Complete_TDG_A_to_Z_QB1592_Handoff_2026-08-15.tar.gz` : `8410d8814e2fe15108731de4f9e49046693cbdafd3abb6dc55d47400c6be9bdf`.
- Archive interne `TDG_QB1540_QB1592_repro_2026-08-15.tar.gz`.
- Fichier historique `exploratory/qb1592_semicausal_crossing_SL2_frame_connection_triplet.py` : `7bc91553a01e2b5024c9982e2f4bd2a392f612621a826b6f9f5a111739f140ab`.
- `cert_qb1592.py` REJOUÉ : les 4 tests passent, à savoir persistent-vs-semicausal 2-jet, non-rétroaction, signature lorentzienne/rang10, instrument BSR unitaire.
- Programme Q-B1592 historique REJOUÉ : rang du triplet = 3 sur les 4 cutoffs `.05,.025,.012,.006`, défaut maximal d'alignement des rangées = `1.68e-6 -> 3.46e-10`, fraction rotationnelle décroissante.

Source Q-B1852 :

- Archive Library `/TDG/Recovery/Complete_TDG_Root2_FULL_A_TO_Z_THREAD_HANDOFF_QB1860BW_COMPLETE_2026-08-21.tar.gz` : `bd4f6171fccc81bf74849162cecdfdd882867ebc4ef8d7715f1ad8fd3e1f7737`.
- Descente interne : handoff complet -> `PARENT_...PARTIAL` -> repro QB1860BV -> repro QB1860BU -> `deps/repro_qb1852/` (1902 fichiers, dépendances incluses).
- `qb1852_full_refined.py` : SHA-256 `ebbe56f7d9c0b19b5c7e688e2b69c7acd2f9a271d161cf558e50e52cad86b5c7`, exactement celui du checkpoint du 16 septembre.
- `qb1852_final_verify.py` REJOUÉ : manifeste PASS, topologie 101 parents PASS, 120/120 diamants PASS, données b4/b24/covariances historiques PASS, nouveau smoke b4 PASS, 24 lignes PASS et verdict `QB1852 FINAL PORTABLE VERIFY PASS`.

Ces fichiers sont des sources historiques. Leur provenance est distincte des scripts de diagnostic récents.

## 3. Opérateur Q et transposition expérimentale de la carte Q-B1592

L'ancienne carte Q-B1592 sur H160 utilise, pour une cellule B4 T et une face B3 F :

```
R = (z I - H)^{-1}
Lpre  = (A[f] Bcanon[f])^dag R_TT
Lpost = (R_FF)^{-1} R_FT
K_TF  = Lpost pinv(Lpre)
S_TF  = K_TF / sqrt(det K_TF)
```

**Point de provenance crucial :** l'exécutable historique utilise effectivement `np.linalg.pinv(Lpre)`. Il s'agit de l'inverse de Moore–Penrose, une convention mathématique déterministe, mais dont la *nécessité physique* n'a pas été dérivée.

Pour le véritable Q-B1852, nous conservons **son Hamiltonien global exact** et son LU sparse, mais nous remplaçons les sous-espaces B3 bruts par les seules combinaisons bright autorisées dans la source :

```
P_F = (1/sqrt(n_F)) sum_{f in groupF(F)} P_f
R_FF = P_F^T R P_F
R_FT = P_F^T R P_T
R_TT = P_T^T R P_T
```

La transposition `K_TF` ci-dessus est une **hypothèse de correspondance de laboratoire** entre Q-B1592 et Q-B1852 : on utilise les opérateurs de Q réel, mais pas encore une preuve que la même carte est l'instrument de future-selection légitime de RefinedQ.

Les liens sur une face commune sont ceux de Q-B746 :

```
S_{T<-U;F} = S_TF (S_UF)^{-1}.
```

Les boucles ont trois cellules parentales T,U,V et trois faces successives. Si les trois faces sont la même face, les liens télescopent et l'holonomie doit être l'identité, à la précision numérique. Les boucles sur trois faces distinctes testent la non-factorisabilité cellule×face. Le défaut observé est `||P - tr(P)/2 I2|| / ||P||` dans une base de comparaison fixe ; **sa magnitude n'est pas invariante sous conjugaison SL2 générale**, mais sa nullité l'est.

## 4. Test historique H160 sur deux cellules

Le modèle BSR H160 possède 15 B4, 20 B3 et 15 B2. La comparaison porte sur 60 liens entre B4 ayant une B3 commune, 20 triangles utilisant une seule face et 60 triangles entre faces distinctes.

| a | boucle médiane, mémoire fraîche | erreur row-space max | boucle médiane, couplage persistant |
|---:|---:|---:|---:|
| 0.0500 | 1.6660771e-6 | 1.6836970e-6 | 5.1817971e-5 |
| 0.0250 | 1.0349139e-7 | 1.0452171e-7 | 1.2968868e-5 |
| 0.0125 | 6.4582950e-9 | 6.5216084e-9 | 3.2486566e-6 |

Les régressions donnent :

- mémoire fraîche, boucle médiane : **ordre 4.011** ; défaut de rangées : **ordre 4.012** ;
- retour persistant, boucle médiane : **ordre 1.998** ; défaut de rangées : **ordre 2.014** ;
- tous les triangles utilisant une seule face télescopent au plancher numérique ;
- la variante semicausale avec `q=0` et celle avec `q=0.2` donnent les mêmes boucles (absence de retour du secteur B2 sous cette projection).

**Interprétation :** sous la mise à l'échelle géométrique conditionnelle `aire ~ a²`, la courbure effective statique du modèle à mémoire fraîche s'annule. La variante persistante possède un signal d'ordre a², mais elle viole précisément le contrôle de non-rétroaction et son défaut row-space est du même ordre. On ne doit pas retenir cette variante comme une réparation physique.

## 5. Véritable Q-B1852 : résultats b4, 101 parents, opérateur global dimension 5570

Dans `RefinedQ('b4',a,z=2+.7j,need_edges=False)`, la reconstruction a utilisé :

- exactement 101 cellules parentales provenant de la grammaire Q-B1852 et 404 B4 fines ;
- l'opérateur global de dimension 5 570, sans changer la loi ;
- 17 cellules autour de T0, 46 faces différentes, 68 attachements cellule-face ;
- 46 arêtes partagées, 40 triangles mono-face, 10 triangles multi-faces.

| a | boucle multi-face médiane | raccordement row-space maximal | boucle/a² | boucle/a⁴ |
|---:|---:|---:|---:|---:|
| .05 | 2.89312068e-6 | 8.16865566e-4 | .0011572483 | .4628993 |
| .025 | 1.77635534e-7 | 2.00794224e-4 | .0002842169 | .4547470 |
| .0125 | 1.10529761e-8 | 4.99867940e-5 | .0000707390 | .4527299 |

Les inversibilités locales passent (`cond(K_TF)` < 1.000005). Les boucles mono-face sont identités à environ 4e-16.

**Conclusion statique :** sous `aire ~ a²`, le candidat de courbure tend vers zéro (`~a⁴`), tandis que la non-colinéarité des espaces de réponse décroît seulement comme `~a²`. Le modèle actuel ne fournit pas par cette carte une courbure statique finie *physiquement unique*.

## 6. Test adversarial : aucune unicité du raccordement par égalité de rangées

Pour `Lpre : C6 -> C2` surjectif, tous ses inverses à droite ont la forme

```
Y = pinv(Lpre) + N W
Lpre N = 0,       Lpre Y = I2,
```

où `N` engendre les 4 dimensions du noyau. Si `Lpost` ne s'annule pas sur `ker(Lpre)`, les cartes `K=Lpost Y` dépendent du choix de `W`.

Nous avons construit une autre inverse à droite de norme comparable, en utilisant un `W` déterministe enregistré par graine SHA-256. **Cette alternative n'est pas une loi de Q ; elle sert seulement à réfuter l'unicité mathématique à partir des seules rangées.**

| a | boucle médiane, convention historique | boucle médiane, autre inverse à droite |
|---:|---:|---:|
| .05 | 2.8931e-6 | 1.2465e-3 |
| .025 | 1.7764e-7 | 3.0705e-4 |
| .0125 | 1.1053e-8 | 7.6479e-5 |

Au point `.025`, l'écart est environ 1 700 fois. La méthode de Moore–Penrose peut encore être retenue si Q sélectionne *physiquement* la structure métrique qui la rend canonique ; ce théorème n'existe pas encore dans le dossier MRP9B.

## 7. Résultat constructif : la réponse de la boucle aux sources de Q est d'ordre a²

Cette fois, nous modifions une unique cellule-parent T0 avec les quatre opérateurs Hermitiens locaux originaux `O[b]` et suivons la variation du résolvant exact, sans refactoriser un Hamiltonien différent pour chaque perturbation :

```
R'_{XY} = R_{XY} + R_{XT} [ epsilon O_b (I - epsilon R_TT O_b)^(-1) ] R_{TY}.
```

Contrôle indépendant à `.05` : la même modification du Hamiltonien recomputée avec une nouvelle factorisation sparse produit des blocs avec erreur relative maximale **9.22e-16**.

Sur une boucle multi-faces réellement présente dans la grammaire de Q-B1852 :

| a | boucle statique | réponse médiane traceless de la boucle / a² |
|---:|---:|---:|
| .05 | 3.35131614e-6 | .0876888145 |
| .025 | 2.05879931e-7 | .0864550511 |
| .0125 | 1.28121862e-8 | .0861491730 |

Exposants ajustés : boucle statique `4.016`, réponse source `2.013`, défaut row-space `2.015`. Les quatre insertions localisées, projetées sur le triplet A4/S4, ont **trois valeurs singulières non nulles**. La singularité du quatrième mode est ~`1e-21`, compatible avec une triplicité dans cette famille.

Le signal est constructif dans la *carte expérimentale*, pas encore un observable physique : **sa réponse est du même ordre a² que le défaut row-space**.

## 8. Dépendance au point de lecture spectral z : test d'universalité négatif

À `a=.025`, la norme de réponse de boucle divisée par `a²` dépend de z :

| z | réponse/a² | fraction de rotation interne dans le jet |
|---|---:|---:|
| 1.4+0.5i | .04411610 | .83149 |
| 2+0.7i | .08645505 | .71142 |
| 3+0.8i | .19902199 | .57308 |

La structure de triplet existe, mais son amplitude et la division boost/rotation sont sensibles au readout spectral choisi. Il est donc interdit de la qualifier de courbure universelle sans construction formelle/readout-free (par exemple des moments de l'opérateur H avant toute inversion).

## 9. Verdict scientifique et pièges écartés

**GAGNÉ :**

1. Le vrai code Q-B1592 a été récupéré et réexécuté, ce qui clôt un trou de provenance historique.
2. Le vrai code Q-B1852 a été récupéré byte-exact et sa certification historique passe.
3. Les liens de deux cellules ayant la même face sont calculables depuis le **même opérateur global Q-B1852** et vérifiés sur une famille de cutoffs b4.
4. Le test de boucle distingue géométrie de jauge pure et défaut non-factorisable à cutoff fini.
5. Un jet de courbure non nul, d'ordre `a²`, apparaît sous des sources locales de Q, avec trois directions de réponse et identité Woodbury/factorisation sparse vérifiée.

**NON GAGNÉ :**

- L'application de la carte Q-B1592 aux fibres bright de Q-B1852 n'est **pas** un théorème de selected-future process. Elle reste une transplantation diagnostique.
- Les liens issus de Moore–Penrose ne sont pas uniques à partir des données row-space approximatives.
- Le jet est **readout-dependent** et le défaut row-space a le même ordre, donc le signal n'est pas encore une observable physique.
- Le programme actuel couvre `b4`, pas `b24` ni les contrôles inter-schémas, et n'établit pas le secteur causal d'un instrument fresh-comb réel.
- Le secteur de rotation interne SU2 n'est toujours pas démontré comme jauge first-class ; le défaut `l=2 -> l=1` et l'algèbre HDA ne sont pas recalculés ni réparés.
- Il n'y a **aucune démonstration de la relativité générale** ni confirmation de convergence quantitative vers Einstein.

## 10. Prochaine expérience prioritaire

1. Retrouver ou dériver une réduction **exacte** de la fibre prédictive M2 pour le processus **selected-future/fresh-comb** du Q actuel ; obtenir `Lpost = K Lpre` sans noyau ambigu, ou caractériser le seul quotient de réponses qui rend `K` naturel.
2. Calculer les jets de liens sous interventions depuis les **moments formels de H**, avant fixation de z, et tester leur classe de conjugaison/projective, pas simplement leur norme de Frobenius.
3. Répéter le test b4/b24 seulement après fermeture de la première porte de provenance/typage, et distinguer modules `SO3` internes et géométriques.
4. Si le signal d'ordre a² survit sans convention de Moore–Penrose et sans z arbitraire, ouvrir seulement alors le contrôle de courbure/gauge first-class et de dynamique HDA.

**Règle :** ce checkpoint est `LAB`, append-only, ne modifie pas le `CURRENT_FRONT_LATEST.md`, Root1, `Q-B1858L` ni les vérificateurs historiques. Il ne remplace pas les STOP conditionnels antérieurs : il apporte une nouvelle capacité numérique diagnostique et une cible mathématique précisément localisée.
