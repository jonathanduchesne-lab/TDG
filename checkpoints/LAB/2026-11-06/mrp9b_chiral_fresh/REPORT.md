# TDG / Root2 — expérience de mémoire fraîche et de désorientation octupolaire

**Date :** 6 novembre 2026 (America/Toronto).  
**Statut :** **CONSTRUCTION CONDITIONNELLE POSITIVE + CONTRÔLES ADVERSARIAUX, PAS UNE DÉRIVATION DE GR DEPUIS Q**.  
**Dépôt :** laboratoire indépendant / append-only, aucune modification de Root1, `Q-B1858L`, `CURRENT_FRONT_LATEST.md`, du Q-B1852 certifié ni des décisions SENTRY STOP.  
**Source historique exacte :** `qb1852_full_refined.py`, SHA-256 `ebbe56f7d9c0b19b5c7e688e2b69c7acd2f9a271d161cf558e50e52cad86b5c7`. La source et ses dépendances sont dans l'archive historique `/TDG/Recovery/Complete_TDG_Root2_FULL_A_TO_Z_THREAD_HANDOFF_QB1860BW_COMPLETE_2026-08-21.tar.gz`.  
**Parent direct :** `checkpoints/LAB/2026-11-06/mrp9b_formal_paths/REPORT.md` (commit `cd0cb998838cb52c2ae923b74157043191dfa649`).

## 0. Question

La séparation des retours B2 (défaut de descente de fibre à l'ordre `z^-3`, `gamma^2 a^3`) répare le transport, mais **ne répare pas** l'obstruction tensorielle `l=2 -> l=1`. Peut-on conserver ce couplage microscopique et neutraliser son influence effective sur les deux polarisations gravitationnelles par une **dynamique d'enregistrement frais** plutôt que par une soustraction ou un paramètre ajusté à Einstein ?

Nous séparons strictement :
1. **ce qui vient du vrai Q** — amplitude, orientation du canal J, bloc B3→B2 pour le registre d'enregistrement ;
2. **ce qui est nouveau** — canal aléatoire de réorientation *physique* du couplage, poids uniformes, rythme des événements, Hamiltonien de comparaison 8×8, projecteur transverse-traceless (TT) de la machine Einstein.

Le but est de falsifier une possibilité d'extension, pas de la promouvoir au statut Root2.

## 1. Extraction du vrai Q-B1852

Le programme `verify_fresh_chiral_octupole.py` exécute la fonction originale `analyze('b4', a, z=2+0.7i, do_second=False)` aux trois échelles `a=0.05,0.025,0.0125`, avec `gamma=1` et `gamma=0`, puis calcule directement :

\[
A_{21}(a)=C(a)_{\mathrm{gradient}}\,[\mathrm{STF}_1,\ldots,\mathrm{STF}_5],
\quad c(a)=\langle A_{21}(a),J\rangle_F,
\]

avec le **rayon unique historique** :

\[
J=-\frac1{\sqrt3}\big[\,yz\mapsto x,\;xz\mapsto y,\;xy\mapsto z\,\big],\quad\|J\|_F=1.
\]

| `a` | `c(a)` Q original, γ=1 | Fraction relative hors rayon `J` | `c(a)` avec B2 déconnecté, γ=0 |
|---:|---:|---:|---:|
| 0,05 | 0,1742740452 | 2,90×10⁻⁴ | 0,1744680761 |
| 0,025 | 0,1744434107 | 7,09×10⁻⁵ | 0,1744913109 |
| 0,0125 | 0,1744851623 | 1,76×10⁻⁵ | 0,1744970986 |

Ce test utilise un **readout spectral fini** `z=2+0.7i` et la normalisation de ce laboratoire ; ce nombre ne remplace pas le coefficient formel/readout-free `~10.769201` du checkpoint du 18 septembre, lequel utilise une autre convention. L'orientation asymptotique du canal est cependant très nettement sur `J`. Éliminer les retours B2 ne le fait pas disparaître.

## 2. Le principe expérimental : randomiser physiquement le canal `J`

Dans une identification **conditionnelle** des modules S4 à des tenseurs spatiaux, les 24 rotations cubiques donnent

\[
R J U_5(R)^{\mathsf T}=\chi(R)J,\quad\chi(R)=\pm1,
\]

avec 12 signes positifs et 12 négatifs. Le couplage est un fond octupolaire, non un opérateur de divergence naturellement SO(3)-covariant. Un **simple changement de coordonnées** transforme aussi les états et **ne change aucune amplitude physique** : contrôle passif à `5.55e-17`. Il n'y a pas de solution en renommant les axes.

Nous introduisons donc volontairement **une nouvelle intervention physique** : pour chaque événement frais, le couplage microscopique prend l'une des deux orientations effectives, sans conserver le signe précédent comme rétroaction active :

\[
H_\pm=H_0\pm V_J,\quad
H_0=\operatorname{diag}(1\times I_5,1.7\times I_3),\quad
V_J=c\begin{pmatrix}0&J^\mathsf T\\J&0\end{pmatrix},\quad c=c_{Q}(0.025).
\]

Les énergies `1` et `1.7`, l'identification des deux polarisations TT, et le couplage fréquentiel avec le temps expérimental sont des **éléments construits**, non des résultats Q. Le choix `1.7` assure un test non trivial avec des Hamiltoniens qui ne commutent pas.

À chaque pas de durée `δ` nous enregistrons le signe dans un nouvel ancilla :

\[
K_+=\sqrt p\,e^{-i\delta H_+},\quad
K_-=\sqrt{1-p}\,e^{-i\delta H_-},\quad
K_+^\dagger K_++K_-^\dagger K_-=I_8.
\]

La carte conditionnellement définie

\[
\Phi_\delta(\rho)=K_+\rho K_+^\dagger+K_-\rho K_-^\dagger
\]

est CPTP. Les ancillas des étapes précédentes sont orthogonaux et ne recouplent pas à la dynamique active. Les poids `p=1/2` sont **imposés** ; il faut encore les dériver de la physique de Q si l'on veut promouvoir cette construction.

## 3. Résultats à horizon fixé : un défaut effectivement supprimable

État de départ `(|+\rangle+|\times\rangle)/\sqrt2` pour `k=z`, temps de comparaison `T=4`, orientation fixée durant tout le trajet ou renouvelée indépendamment à chaque pas.

| Situation | Fuite vers le secteur vectoriel | Distance en trace de la dynamique de référence |
|---|---:|---:|
| Signe équiprobable, **fixé une seule fois** sur T | 0,0377413 (3,774 %) | 0,0560438 |
| Renouvellement équiprobable, N=40 | 0,00201981 | 0,00244046 |
| Renouvellement équiprobable, N=160 | 0,000506650 | 0,000611720 |
| Renouvellement équiprobable, N=640 | 0,000126761 | 0,000153023 |
| Renouvellement équiprobable, N=1 280 | **0,0000633888** (0,00634 %) | **0,0000765192** |
| Renouvellement biaisé, `p=0.7`, N=1 280 | **0,00642021** (0,642 %) | **0,0799682** |

Le couplage du Q original n'est **pas changé ni ajusté**. L'annulation concerne le *Hamiltonien cohérent moyen* dans une dynamique **nouvelle**. À pas fini, le terme quadratique de décohérence demeure.

### Vérification sans projection préalable sur le rayon `J`

Nous avons également utilisé **toute la matrice réelle `A21` à échelle finie**, y compris son petit résidu hors rayon `J`, et les 24 orientations cubiques physiques. La moyenne du couplage est nulle à `~1e-16`, par symétrie de représentation, mais une orientation fixée conserve 3,774 % de fuite. Avec 24 réorientations possibles et enregistrements indépendants, la fuite observée vaut `0,00201980561`, `0,000506650179`, `0,000126761449` pour N=40,160,640 : résultat inchangé à la précision reportée, **sans effacer le reste non-J**.

Le contrôle de complétude du canal à 24 résultats est inférieur à `7e-18` en norme de Frobenius ; tous les opérateurs sont unitaires à la précision machine.

### Directions de propagation non privilégiées

Pour **40 vecteurs d'onde aléatoires**, nous avons imposé *à titre de comparateur* le sous-espace TT à deux dimensions du modèle d'Einstein, sans prétendre le déduire de Q. La fuite maximale hors de ce sous-espace diminue de `0,00494233` (N=32) à `0,00124089` (N=128), puis `0,000310525` (N=512). Cela vérifie que le mécanisme de relaxation n'est pas un artefact du seul axe z, mais **ne dérive ni la contrainte TT ni les équations du mouvement d'Einstein**.

## 4. Contre-expérience impérative : limites temporelles non uniformes

À temps total T fixé, pour p=1/2, la première contribution du couplage linéaire se neutralise :

\[
\Phi_\delta=\operatorname{Ad}_{e^{-i\delta H_0}}
-\frac{\delta^2}{2}[V_J,[V_J,\cdot]]+O(\delta^3)
\]

au sens des coefficients du développement de la superopération complète. La correction cumulée pour N=T/δ est `O(T δ)` ; elle n'est donc pas strictement nulle à pas fini.

**Échec à très grand temps lorsque δ=0.1 reste fixe :**

| T | Population vectorielle (p=1/2) |
|---:|---:|
| 4 | 0,00201981 |
| 40 | 0,0194793 |
| 400 | 0,138919 |
| 1 600 | 0,240256 |

La limite de cette dynamique simplifiée est 0,25 pour l'état sélectionné : **la mémoire fraîche à rythme fixe ne garantit aucune stabilité éternelle**.

## 5. Nouveau lemme : stabilité uniforme sur un horizon arbitraire sous hypothèse de rythme accéléré

Pour un canal renouvelé sans biais, le théorème suivant vaut en dimension finie (sans postuler la gravitation) :

**Lemme.** Si `H0` et `V` sont hermitiens bornés, le pas de temps `δ_n` et le canal frais à signes équilibrés sont comme ci-dessus, alors pour tout N, avec l'état initial identique à celui de la référence unitaire libre :

\[
\frac12\|\rho_N-\rho_{0,N}\|_1\leq
\|V\|_{\mathrm{op}}^2\sum_{n=1}^N \delta_n^2.
\]

*Preuve esquissée sans ajustement de constante.* Écrire `F(λ)=Ad_{exp[-iδ(H0+λV)]}`. Les dérivées secondes par la formule de Duhamel sont majorées en norme induite trace par `4 δ² ||V||²`, grâce à la contractivité des conjugaisons unitaires. La formule intégrale de la différence centrale `½(F(1)+F(-1))-F(0)` donne une erreur en norme trace `≤2 δ²||V||²` à chaque étape. Le télescopage des canaux CPTP ne l'amplifie pas. La distance en trace est la moitié de la norme trace.

Choisissons maintenant une **nouvelle loi de rythme expérimentale** :

\[
\delta_n=\frac{a}{n^p},\qquad \frac12<p\leq1.
\]

Elle donne une durée totale infinie (`Σδ_n=∞`) et une variance cumulée finie (`Σδ_n²=a²ζ(2p)`). Par conséquent :

\[
\boxed{\sup_N D_{\mathrm{trace}}(\rho_N,\rho_{0,N})
\leq a^2\|V\|^2\zeta(2p) \xrightarrow[a\to0]{}0.}
\]

Cet énoncé est **uniforme sur tous les horizons finis** ; il ne dit pas que la fuite exacte est nulle pour un `a` donné. Il suppose une fréquence de renouvellement augmentant sans borne en temps physique, hypothèse exigeante que TDG ne dérive pas.

Vérification `p=0.6`, 12 000 enregistrements :

| a (durée de base imposée) | Temps total accumulé | Distance calculée | Borne pour tous les horizons |
|---:|---:|---:|---:|
| 0,2 | 21,0211 | 0,00117996 | 0,00226873 |
| 0,1 | 10,5105 | 0,000295408 | 0,000567182 |

Le contrôle numérique confirme la borne, sans remplacer sa preuve.

## 6. Les histoires factuelles individuelles ne sont pas une simple moyenne

Le Q de TDG distingue une histoire factuelle particulière d'une mixture non sélectionnée. Nous avons donc simulé **1 600 trajectoires pures conditionnelles** par paramétrage, avec des signes tirés de manière indépendante à chaque pas.

| N | Écart moyen de l'histoire individuelle à la référence (p=0.5) | Fuite vectorielle moyenne |
|---:|---:|---:|
| 128 | 0,02254 | 0,00064448 |
| 512 | 0,01097 | 0,00015417 |
| 2 048 | 0,00554 | 0,000039659 |

L'écart de chaque trajectoire décroît plus lentement (`~√δ`) que celui de la densité moyenne (`~δ`), mais il tend vers zéro **en probabilité**, à horizon fixé. Avec p=0.7, l'écart moyen se stabilise près de `0,08`, donc le biais reste fatal. Ceci est une **simulation de trajectoires proposées**, pas une identification à la vraie loi de sélection `Σ` de TDG ni une preuve de convergence trajectoire par trajectoire pour une histoire infinie.

## 7. Compatibilité algébrique avec l'instrument d'enregistrement B2 précédent

Du **véritable Q** B3→B2 à `a=0.025` (b4), nous reprenons

\[
W=P_{B2}H_QP_{B3}:\mathbb C^2\to\mathbb C^{1020},\quad
\lambda(W^\dagger W)=0.0011811759843\,(\times2).
\]

La complétion nouvellement définie `K0=√(I2-W†W)` donne `K0†K0+W†W=I2` exactement à la précision numérique. La composition tensorielle de cet instrument à sorties « actif »/« enregistré » avec le canal de réorientation octupolaire possède une complétude `||ΣK†K-I16||_F=5.44e-16`.

**Ce contrôle prouve la compatibilité de type et la conservation des probabilités d'un montage combiné.** Il ne prouve **pas** que le même processus physique de Q génère simultanément les deux instruments. De même, la branche « enregistré » dans le modèle est une sortie absorbante *stipulée* ; elle ne suffit pas à démontrer la loi de mise à jour du Q après sélection factuelle.

## 8. Décision scientifique et porte suivante

- **Q canonique — inchangé :** `l2->l1` non nul (survit à gamma=0), couverture historique B5/HDA/GR STOP conservée.
- **Propriété conditionnellement construite — positive :** une dynamique CPTP de réorientation physique non biaisée, avec ancillas fraîches, supprime le couplage cohérent effectif à T fixé ; une loi de rythme à carré sommable offre même une borne uniforme sur l'horizon.
- **Falsification importante :** une simple relecture passive des repères, un tirage de signe effectué une seule fois, un biais statistique, ou un pas de temps fixe à horizon infini ne fournissent pas la réparation recherchée.
- **Deux modes physiques non dérivés :** le projecteur TT, la dynamique cinétique `H0`, l'algèbre des contraintes HDA, le couplage au champ gravitationnel et l'équation d'Einstein restent importés ou ouverts. Le modèle expérimental contient en réalité cinq composantes tensoriales ; il ne déduit pas leur réduction physique à deux.
- **Prochain verrou précis :** démontrer que les transitions Q/actualisation entre cellules produisent une **réorientation active**, pas une symétrie de coordonnées, puis une mesure de rythme/probabilité sans hypothèses nouvelles et les contraintes spatiales pertinentes. Sinon cette solution reste un modèle mathématique artificiellement réalisable, non une dérivation de TDG.

**Verdict :** **PASS de capacité quantique sous nouvelles hypothèses; FAIL de promotion au Q/GR physique**. Aucun ajustement de coefficient à Einstein, mais des primitives ont bel et bien été ajoutées. Archiver sans promotion.

## 9. Reproduction et provenance

Avec l'archive historique Q-B1852 reconstituée et les dépendances NumPy/SciPy :

```sh
export TDG_Q1852_SOURCE=/chemin/vers/qb1852_full_refined.py
sh run_all.sh
```

Les cinq scripts `.py`, leurs résultats `.json`, journaux `.log`, ainsi que `SHA256SUMS.txt` sont dans ce checkpoint. La source historique est **référencée par son SHA-256** (non réécrite). Ce laboratoire ne modifie pas les fichiers canoniques ni le front MRP9B.
