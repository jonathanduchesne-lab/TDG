# TDG — Projection asymptotique de la lentille d'actualisation

**Expérience exploratoire, 6 novembre 2026.**  
**Statut : diagnostic analytique et numérique conditionnel, non une nouvelle loi physique de TDG.**  
**Source canonique :** dépôt `jonathanduchesne-lab/TDG`, `CURRENT_FRONT_LATEST.md` ; état de référence post-initiale `S_n=(K_n,Q_n,P_n,L_n)` ; B5 v0.3/v0.4 et arrêt B5→GR (6 octobre 2026).  
**Aucune modification** des lois, codes ni checkpoints canoniques. La projection utilise la lentille scientifique de décohérence à l'interface `Sigma` et le registre B5 certifié, pas une simulation intégrée de tout `Q`.

## 1. Hypothèse opératoire, sans effondrement ajouté

L'interaction système–environnement est globale et unitaire ; la décohérence locale résulte de la trace partielle. Un fait effectif est un enregistrement persistant et suffisamment redondant. Ce critère **ne prouve pas** un effondrement ontologique ni un seuil absolu d'irréversibilité. Les probabilités d'instruments quantiques restent celles de la règle de Born, qui n'est pas dérivée dans TDG.

## 2. Limite N→∞ — système à deux chemins

Modèle unitaire de collisions indépendantes avec recouvrement environnemental par fragment `c=cos(0.7)=0.7648421873`. La visibilité locale est `V_N=c^N`. L'état réduit d'un état initial |+> est

`rho_N = [[1/2, c^N/2], [c^N/2, 1/2]]`.

| Nombre de fragments N | Visibilité V_N | Distance de trace à la mixture classique |
|---:|---:|---:|
| 0 | 1 | 0.500000 |
| 16 | 0.013713533 | 0.006856767 |
| 32 | 0.00018806099 | 0.00009403049 |
| 128 | 1.25082e-15 | 6.25410e-16 |
| 1024 | 5.99182e-120 | 2.99591e-120 |
| infini | 0 | 0 |

**Résultat :** la décohérence locale devient complète, mais l'état limite `rho_infty=diag(1/2,1/2)` reste à **distance de trace 1/2 de chaque état de résultat pur**. Un résultat individuel n'est pas sélectionné par ce canal non conditionné.

En utilisant l'information mutuelle d'une mesure de Helstrom sur un fragment de m sous-environnements idéaux, `m=6` suffit ici pour obtenir au moins 0,9 bit d'information sur l'état pointer ; avec N=1024, au maximum `floor(1024/6)=170` groupes disjoints peuvent satisfaire ce seuil **dans ce modèle de fragments indépendants qui conservent leurs corrélations**. C'est une illustration de redondance, non une mesure de la mémoire universelle TDG.

Limite : si les fragments interagissent et mélangent l'information (*scrambling*), une mémoire observable redondante peut également diminuer à temps long. Un horizon temporel infini n'assure pas à lui seul une mémoire éternelle.

## 3. Registre B5 Standard5 — évolution répétée de la lentille symétrique

La structure certifiée est `L_B5=6I_6-J_6=6P5`. La direction constante `P1` est redondante, le sous-espace `P5=I-P1` est de dimension 5. Nous utilisons uniquement l'instrument complètement positif illustratif déjà défini dans `tdg_lentille_decoherence_2026_11_06.py` :

`M_j = sqrt(6/5) P5 |j><j| P5`, `E(rho)=sum_j M_j rho M_j^T`.

Le canal est complètement positif, préserve la trace *sur Standard5*, est covariant sous les permutations des six étiquettes et n'injecte aucun mode singlet. Il n'est **pas** une dérivation physique depuis le Q microscopique.

Les 25 valeurs propres du superopérateur sur les opérateurs 5×5 sont exactement :

- `1` (multiplicité 1)
- `0.8` (multiplicité 5)
- `0` (multiplicité 19)

Le seul état fixe est `rho_* = P5/5`. Pour l'état initial du test, la distance de Frobenius à l'état fixe suit **exactement** :

`||E^N(rho0)-P5/5||_F = sqrt(4/5) × 0.8^N`.

| N | Distance de Frobenius |
|---:|---:|
| 0 | 0.89442719 |
| 8 | 0.15005998 |
| 16 | 0.025175887 |
| 32 | 0.0007086382 |
| 64 | 5.6144e-7 |
| 128 | 3.5282e-13 |
| infini | 0 |

**Résultat :** la répétition infinie de cette lentille sur un secteur de registres *sans conserver les issues individuelles* homogénéise l'état du registre ; elle ne fabrique ni nouvelle direction privilégiée, ni nouveau tenseur gravitationnel, ni événement factuel unique. Cette invariance sous permutations des six étiquettes n'est pas la symétrie SO(3) de l'espace physique.

Cela éclaire pourquoi TDG doit garder un `ledger` de faits séparé et append-only : **l'état non conditionné du système peut perdre une information prédictive, tandis que les enregistrements conditionnés d'une histoire demeurent dans un support physique distinct**. Le canal de ce test ne représente pas ce support complet.

## 4. Non-commutation des limites « horizon infini » et « continuum »

Pour vérifier que l'infini ne cache pas un choix de mise à l'échelle, introduisons des collisions faibles :

`theta(a)=sqrt(2g) a`, `c(a)=cos(theta(a))`, `V(a,N)=c(a)^N`, avec `g=0.3` illustratif.

Alors :

- À `a>0` fixé, `lim_{N→∞} V(a,N)=0`.
- À `N` fixé, `lim_{a→0} V(a,N)=1`.
- Pour `N(a)=T/a²` et `a→0`, `V(a,N(a))→exp(-gT)`.

Donc **les limites ne commutent pas** :

`lim_{a→0} lim_{N→∞} V=0`, tandis que `lim_{N→∞} lim_{a→0} V=1`.

À `T=1` :

| a | N=T/a² | V du chemin conjoint | V à N=16 constant |
|---:|---:|---:|---:|
| 0.250000 | 16 | 0.73941646 | 0.73941646 |
| 0.125000 | 64 | 0.74047017 | 0.92763450 |
| 0.062500 | 256 | 0.74073136 | 0.98141750 |
| 0.031250 | 1024 | 0.74079651 | 0.99532301 |
| 0.015625 | 4096 | 0.74081279 | 0.99882878 |
| a→0 | N=T/a² | **0.74081822** | **1** |

**Signification pour TDG :** il manque une *loi microscopique de mise à l'échelle du taux d'enregistrement avec le raffinement réel*, y compris les schémas historiques b4 et b24. Choisir un ordre de limites ou une échelle favorable pour obtenir un résultat cible serait une hypothèse nouvelle, pas une projection neutre.

## 5. Obstructions gravitationnelles — ce que la projection conserve

Le dernier checkpoint canonique B5→GR documente une correction pure trace

`DeltaW=(15/4)|I><I|`.

Pour toute déformation `X` symétrique sans trace, `DeltaW X=0` exactement. Un calcul sur cinq bases STF donne un défaut maximal d'environ `2.7e-17`. Cela signifie que cette correction et un instrument agissant indépendamment sur B5 ne peuvent pas effacer automatiquement le canal dynamique STF→gradient dont le checkpoint rapporte une obstruction d'environ **11.6773**. Le défaut historique SAME-h d'environ **0.74596** est lui aussi toujours ouvert. Ces valeurs sont **celles des sources canoniques**, elles n'ont pas été recalculées avec un Q modifié dans cette expérience.

Plus généralement, si la lentille agit uniquement sur un espace d'enregistrements séparé du processus Q, alors `D⊗Id` commute avec `Id⊗T_Q`. Un calcul donne défaut de commutation **0**, mais il s'agit d'une conséquence élémentaire de l'indépendance des facteurs, pas d'une preuve que toutes les interactions réelles de décohérence sont spectatrices. Une interaction dérivée du Q microscopique pourrait changer le verdict ; elle n'est pas encore construite.

Dans TDG, `Sigma` (sélection/statistiques) et `U_e` (mise à jour structurelle conditionnelle) sont déjà séparés. Changer le mécanisme d'interface peut modifier les poids relatifs des histoires, mais **à histoire factuelle fixée il ne change pas les cartes U_e sans nouvelle dépendance démontrée**. En particulier, rien ici ne crée la transition constitutive `beta=0 -> beta!=0` recherchée dans B5, ni la contrainte frame/Gauss manquante, ni une clôture HDA / GR non linéaire.

## 6. Verdict et classification

**DÉRIVÉ DANS LE MODÈLE ILLUSTRATIF :** limite de décohérence locale vers un mélange diagonal, redondance croissante pour fragments indépendants, limite fixe B5 `P5/5`, non-commutation des limites de raffinement et d'interactions.

**RETENU DU PROJET CANONIQUE (NON REPROUVÉ ICI) :** structure post-initiale `S_n`, quotient Q/Cons, B5 Standard5, obstruction STF dynamique et décision B5→GR.

**ASSUMÉ POUR CE TEST :** unitarité des collisions, couplage theta=.7, fragments indépendants, canal B5 symétrique illustratif, loi theta(a)=sqrt(2g)a.

**OUVERT :** mécanisme physique unique d'enregistrement, probabilité et factualisation d'un résultat individuel dans TDG, taux de mémoire issu du Q, source exacte MRP9B Q-B1592, limites de cofinalité b4/b24, causalité et métrique émergente, présent universel, O(3) dynamique, HDA, spin-2 et relativité générale non linéaire.

**VERDICT :** la lentille donne une projection asymptotique cohérente de l'objectivité *effective* par mémoire et décohérence sous les hypothèses testées. Elle ne démontre pas de convergence supplémentaire vers la relativité générale. Surtout, l'« horizon infini » ne produit pas un résultat physique unique tant que la relation microscopique entre interactions, mémoire retenue et raffinement n'est pas spécifiée.

Aucun checkpoint ni source canonique n'a été modifié : ce document est un diagnostic de laboratoire externe au programme TDG.

## Sources

- TDG latest : https://github.com/jonathanduchesne-lab/TDG/blob/main/CURRENT_FRONT_LATEST.md
- TDG CURRENT_STATE : https://github.com/jonathanduchesne-lab/TDG/blob/main/CURRENT_STATE.md
- TDG B5→GR stop : https://github.com/jonathanduchesne-lab/TDG/blob/main/checkpoints/SENTRY/2026-10-06/TDG_B5_TO_GR_BRANCH_STOP_CURRENT_ROOT2_2026-10-06.md
- Schlosshauer, *Decoherence, the measurement problem, and interpretations of quantum mechanics*, Reviews of Modern Physics (2005): https://doi.org/10.1103/RevModPhys.76.1267
- SEP, *The Role of Decoherence in Quantum Mechanics* (rev. 2025): https://plato.stanford.edu/entries/qm-decoherence/
- Zurek, *Quantum Darwinism*, Nature Physics (2009): https://www.nature.com/articles/nphys1202
- Riedel, Zurek & Zwolak, *Rise and Fall of Redundancy*, NJP (2012): https://doi.org/10.1088/1367-2630/14/083010
- Ciccarello et al., *Quantum Collision Models: A Beginner Guide* (2022): https://doi.org/10.3390/e24091258
