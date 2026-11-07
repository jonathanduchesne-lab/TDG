# TDG / Root2 — MRP9B : le retour B3→B2→B3 explique le premier défaut de descente de Q

**Date du laboratoire :** 6 novembre 2026 (America/Toronto).  
**Statut :** IDENTITÉ DE SOURCE VERIFIÉE dans le Hamiltonien historique Q-B1852; RÉPARATION CONDITIONNELLE ET LOCALE; OBSTRUCTION GR NON RÉPARÉE.  
**Niveau de preuve :** calculs numériques et vérifications de matrices sur le véritable constructeur `qb1852_full_refined.py`, plus un instrument neuf de type Stinespring utilisant ses couplages. Pas de preuve que cet instrument soit la dynamique fondamentale de TDG.  
**Source certifiée :** `qb1852_full_refined.py`, SHA-256 `ebbe56f7d9c0b19b5c7e688e2b69c7acd2f9a271d161cf558e50e52cad86b5c7` (récupéré de l'archive originale Library, non modifié).  
**Portée :** MRP9B, carte candidate Q-B1592 transplantée sur la fibre bright du vrai RefinedQ. La validité physique de cette transplantation reste **OUVERTE**.

## 1. Question et méthode

Notre contrôle précédent avait isolé un défaut de raccordement de deux cellules partageant une face B3. La connexion 2x2 calculée par la convention de Moore–Penrose n'était pas unique, et son jet était sensible au readout spectral `z`. Nous cherchons cette fois l'origine **dans les moments de Q avant toute inversion**.

On part de l'Hamiltonien global certifié `H` et de deux sélecteurs exacts : `P_T`, pour le cœur parent B4 à six dimensions, et `P_F`, pour la fibre *bright* B3 à deux dimensions. Nous utilisons `C = A[f] Bcanon[f]`, exactement comme dans le script source. Pour `R(z)=(zI-H)^{-1}` :

```
L_pre(z)  = C^† (P_T^† R(z) P_T)            [2 x 6]
L_post(z) = (P_F^† R(z) P_F)^(-1) (P_F^† R(z) P_T) [2 x 6]
```

Un véritable transport `K(z): C² -> C²` descend exactement des six degrés de liberté si et seulement si `L_post(z) = K(z) L_pre(z)`. Un théorème d'algèbre linéaire donne la condition nécessaire et suffisante, sans métrique choisie :

> **ker(L_pre) est inclus dans ker(L_post).**

Si la condition échoue, l'inverse de Moore–Penrose ne *résout pas* le défaut; il ne donne qu'un représentant à la convention euclidienne. Au readout `z=2+0.7i` les cartes calculées sur le vrai Q-B1852 ont une restriction de `L_post` au noyau de `L_pre` de **rang 2**, donc aucun transport 2x2 exact n'est induit par les seules réponses proposées.

## 2. Développement formel, sans `z` privilégié

Posons `t=1/z`. Avant d'évaluer `z`, nous générons les vrais moments du Hamiltonien par multiplications creuses :

\[
R(z)=t\sum_{k\geq0}t^kH^k.
\]

Les coefficients matriciels de `L_pre` et `L_post` se déduisent de `P_X^† H^k P_Y`, puis on cherche `K(t)=K_0+tK_1+...` ordre par ordre. Le coefficient initial est `K_0=a I_2`; l'obstruction à l'ordre n est le résidu de `L_post,n - sum(K_j L_pre,n-j)` sur le noyau de `C^†`.

**Résultat :** ordre 1 satisfait, ordre 2 satisfait à ~1e-16, premier défaut non nul à **l'ordre 3**, c'est-à-dire en `z^-3`. Ce résultat ne dépend pas d'un point de lecture spectral, ni d'un fit des coefficients de transport, ni du choix de Moore–Penrose pour la *nullité* de l'obstruction.

### Amplitude du premier défaut en fonction de la grille et de la force des B3–B2

Sous `gamma !=0`, pour les cas testés :

\[
\boxed{\|D_3\|=c_{\mathrm{schéma}}\,\gamma^2a^3}
\]

| Schéma original Q-B1852 | `c_schéma` brut à la normalisation de sa grille | Exposant mesuré en a |
|---|---:|---:|
| b4 (dimension globale 5 570) | 2,9096630293 | 3,0000000000 |
| b24 (dimension globale 29 370) | 0,5337497579 | 3,0000000006 |

Les essais incluent `a=0.05, 0.025, 0.0125` et `gamma=0, 0.5, 1, 2`. Les coefficients bruts des deux schémas ne sont **pas** interchangeables : leurs normalisations et multiplicités de présentation diffèrent. Cette expérience n'établit ni une nouvelle universalité b4/b24 ni son échec au quotient prédictif.

## 3. Identification du trajet microscopique responsable

Nous avons isolé dans la matrice H les chemins orientés à trois arêtes :

```
Parent T (B4) -> face fine B3 -> paire B2 -> face observée F (B3)
```

Soit `P_B3` le projecteur sur toutes les faces B3 et `P_B2` celui sur les paires B2, et `Pi_ker = I_6 - (C^†)^+ C^†`. Le premier résidu vaut dans les configurations examinées :

\[
\boxed{D_3\Pi_{\rm ker}=P_F^\dagger H P_{B2}H P_{B3}H P_T\Pi_{\rm ker}.}
\]

La reconstruction indépendante du côté droit reproduit le membre gauche sur les 24 cas (`2 schémas x 3 cutoffs x 4 valeurs de gamma`) avec une différence absolue maximale de **2,27e-15**. Pour `gamma=0`, le canal retourné est exactement nul et les petites valeurs résiduelles d'ordre 3 sont au plancher machine. Ce n'est donc pas une simple corrélation de lois d'échelle : nous avons identifié la **classe de chemins de H** responsable du premier défaut.

Cela rejoint les anciennes observations de TDG sur les effets de retour B3↔B2, mais il serait prématuré de déclarer chaque B2 du Q global un « enregistrement factuel retiré ». L'identité est de type **Hamiltonien / support**, tandis que cette distinction est une question de processus quantique conditionnel.

## 4. Expérience de contre-modèle : « mémoire fraîche, sans retour »

Nous avons construit pour diagnostic un opérateur triangulaire `H_sink` qui conserve `H_{B2,B3}` (écriture vers B2) et met `H_{B3,B2}=0` (retour vers B3 bloqué). Il est expressément **non hermitien** : il ne représente pas le Hamiltonien fondamental gelé de TDG et n'est pas lui-même une preuve de canal CP.

| a (b4) | Défaut de descente dans Q original | Défaut avec `H_sink` | Facteur d'amélioration |
|---:|---:|---:|---:|
| 0,05 | 8,13783e-4 | 4,94640e-7 | ~1 645 |
| 0,025 | 2,00605e-4 | 3,04730e-8 | ~6 583 |
| 0,0125 | 4,99750e-5 | 1,89773e-9 | ~26 334 |

Ces chiffres sont obtenus au **même point spectral de contrôle `z=2+0.7i`**, uniquement pour mesurer le progrès du comparateur. Sur les moments, le défaut d'ordre 3 disparaît; un défaut d'ordre 5 demeure et suit `a^5` : coefficients bruts `4,94265` (b4) et `4,59393` (b24) pour `gamma=0`.

La correction est donc **réelle mais partielle**. Le facteur de réduction ne prouve pas une causalité physique réalisée par le Q original.

## 5. Instrument quantique frais construit avec les couplages de Q

Pour vérifier qu'un dépôt de mémoire sans rétroaction n'est pas mathématiquement incohérent, nous avons extrait de la véritable matrice H le bloc de transfert `V=P_{B2}HP_F` depuis une fibre bright M2. Pour les six configurations vérifiées (b4/b24 et trois `a`), `V^† V` est positif et strictement inférieur à `I_2`. Nous pouvons alors construire un instrument de Kraus **nouveau** :

\[
K_{\mathrm{actif}}=\sqrt{I_2-V^\dagger V},\qquad K_{\mathrm{enregistrement}}=V,
\]

\[
K_{\mathrm{actif}}^\dagger K_{\mathrm{actif}}+K_{\mathrm{enregistrement}}^\dagger K_{\mathrm{enregistrement}}=I_2.
\]

L'isométrie associée peut être prolongée à une unitaire sur un espace plus grand. Les sorties « enregistrées » sont ensuite laissées dans des canaux frais qui n'influencent pas les prochaines étapes actives. Jusqu'à huit étapes, la norme de complétude vaut `<= 1.89e-15` (précision machine).

Cette réalisation conserve l'ancienne mémoire dans les branches de sortie et ne requiert pas d'ajustement vers Einstein. Cependant :

- elle **ajoute une prescription d'instrument/actualisation**; elle n'est pas le selected-future process unique dérivé de l'ancien Q;
- les valeurs propres de `V^†V` sont ici égales, donc la seule étiquette « émission ou non » ne sélectionne pas une direction spinorielle privilégiée ni ne dérive la règle de Born;
- la matrice triangulaire `H_sink` et cet instrument CP sont **deux comparateurs distincts**. Nous n'avons pas montré que leurs fonctions de réponse sont identiques.

## 6. Contrôle adversarial obligatoire : l'obstruction tensorielle GR survit

Pour ne pas confondre réparation du transport et gravitation, nous avons réexécuté le calcul historique des réponses/mémoires `F,V,C` de Q-B1852 sur b4, avec `gamma=1` puis `gamma=0` (aucune réécriture de `C`, des coefficients de source ou de la géométrie). Nous avons projeté `C` sur les cinq bases STF `l=2` disponibles via `irreps()`, puis mesuré la norme du bloc gradient `l=1` :

| a | `gamma=1` (Q historique) | `gamma=0` (comparateur) |
|---:|---:|---:|
| .05 | 0,1742740525 | 0,1744680773 |
| .025 | 0,1744434111 | 0,1744913110 |
| .0125 | 0,1744851625 | 0,1744970986 |

Une extrapolation élémentaire linéaire en `a^2` donne `~0,17449947` (`gamma=1`) et `~0,17449904` (`gamma=0`). Ces valeurs sont des **diagnostics normalisés de ce laboratoire** et ne doivent pas être confondues sans conversion avec les autres normalisations historiques de `A21` ou `STF->gradient`.

**Verdict contraignant :** le couplage interdit `l=2 -> l=1` survit quasiment inchangé lorsque nous éliminons complètement les interactions B3/B2. L'amélioration du transport **n'est pas** une solution de GR. Elle répare une porte nécessaire, mais pas l'autre porte indépendante.

## 7. Synthèse : qu'avons-nous probablement mal identifié dans TDG ?

L'objet spectral d'un **Hamiltonien hermitien global** fait revenir une amplitude de B2 vers B3. Il décrit une évolution prédictive réversible. Mais la mise à jour après **actualisation factuelle** est censée conserver un registre historique sans le laisser recoupler spontanément aux alternatives futures. Ces deux usages ne devraient peut-être pas employer indistinctement le même résolvant.

**Hypothèse de recherche nouvellement ciblée (NON DÉRIVÉE) :** le pont vers la géométrie devrait prendre sa connexion dans une *réponse sélectionnée et causale du processus de Q*, pas dans le résolvant persistant pris comme si toutes les informations passées restaient actives. Le premier défaut de descente calculé ici identifie le prix précis de cette confusion.

Pour construire le pont complet, deux portes **indépendantes** restent ouvertes :

1. Déduire un instrument **fresh-comb Q-natif** sur toutes les faces et prouver l'identification des M2 communes **sans inverse arbitraire** et avec covariance au raffinement; il ne suffit pas d'en montrer une possibilité locale.
2. Traiter séparément la dynamique `l=2 -> l=1`, la courbure interne SU2/frame, les contraintes HDA et les degrés de liberté d'Einstein. Le test ci-dessus interdit de considérer que la première porte suffit à fermer la seconde.

**Aucun résultat nouveau ne démontre les équations d'Einstein ni une amélioration quantitative de la convergence gravitationnelle du Q original.** L'ancienne version canonique et ses STOP restent inchangés. Ce dossier est un checkpoint de laboratoire append-only.

## 8. Reproduction et intégrité

Les scripts utilisent l'archive historique : `/TDG/Recovery/Complete_TDG_Root2_FULL_A_TO_Z_THREAD_HANDOFF_QB1860BW_COMPLETE_2026-08-21.tar.gz`, dans laquelle `qb1852_full_refined.py` a été retrouvé avec son arborescence `deps/`. Sa somme SHA-256 doit correspondre à celle écrite ci-dessus. La présence des dépendances historiques de ce script est nécessaire : ce laboratoire ne simule pas leur absence par un modèle inventé.

Après installation des dépendances NumPy et SciPy et matérialisation de la source complète :

```sh
export TDG_Q1852_SOURCE=/chemin/vers/qb1852_full_refined.py
sh run_all.sh
```

Les sources d'exécution sont les scripts `verify_*.py`, `test_gamma_effect_on_l2l1.py` et `build_summary.py`. Les résultats JSON et journaux console de chaque expérience sont fournis en parallèle; `SHA256SUMS.txt` fige les empreintes de fichiers de ce checkpoint. Ce dossier n'écrit pas dans le `CURRENT_FRONT_LATEST.md` canonique.
