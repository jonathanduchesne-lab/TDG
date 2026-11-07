# TDG — Laboratoire Q → géométrie : nature du défaut et pont minimal

**Date du laboratoire :** 6 novembre 2026 (heure de Toronto).  
**Statut :** DÉRIVÉ dans le modèle représentatif conditionnel / NON PROMU comme dérivation physique de la relativité générale.  
**Sources TDG :** `CURRENT_FRONT_LATEST.md`, `TDG_FORMAL_READOUT_FREE_DYNAMIC_L2_TO_L1_NONZERO_2026-09-18.md`, `TDG_B5_TO_GR_BRANCH_STOP_CURRENT_ROOT2_2026-10-06.md`, `TDG_MRP9A_SAME_FACE_LINK_PROVENANCE_GAP_2026-10-14.md` du dépôt `jonathanduchesne-lab/TDG`.  
**Protocole :** aucune modification du Q canonique, des checkpoints ou des coefficients historiques; scripts expérimentaux autonomes.

## 1. Question précise

La carte entre les modules discrets de TDG et les champs spatiaux physiques est-elle incorrecte, ou bien la dynamique Q elle-même produit-elle un opérateur incompatible avec la covariance continue ?

Le checkpoint formel certifié de TDG donne un unique rayon S4 non nul de couplage `l2 -> l1` :

\[
J=-\frac1{\sqrt3}[yz\mapsto x,\ xz\mapsto y,\ xy\mapsto z],
\qquad c_{\infty}\approx10.769201\ne0.
\]

Ce coefficient est **celui du protocole formel spécifique du checkpoint**, et non une constante physique mesurée. D'autres readouts donnent d'autres amplitudes. Aucun `Q` microscopique modifié n'a été calculé ici.

## 2. Diagnostic nouveau : J est un octupôle pur si les modules deviennent physiques

Choisir une base orthonormée `E_a` de `STF^2(R^3)` : deux diagonales sans trace et `xy,xz,yz` hors diagonale, toutes normalisées. Définir :

\[
T_{ijk}=\sum_a J_{ia}(E_a)_{jk}.
\]

Les scripts vérifient à la précision machine que :

- `T_ijk` est invariant sous les six permutations de `(i,j,k)`;
- toutes les contractions `T_ijj` valent zéro;
- les six entrées où `(i,j,k)` sont tous différents valent `-1/sqrt(6)`; les autres sont nulles.

On obtient le polynôme homogène harmonique de degré 3 :

\[
H(x,y,z)=T_{ijk}x_i x_j x_k=-\sqrt6\,xyz,\qquad \nabla^2H=0.
\]

**Conclusion conditionnelle stricte :** sous l'identification `l2 = STF^2` et `l1 = vecteur physique`, le couplage J est un objet d'ordre octupolaire (représentation de spin angulaire `l=3`). Ce n'est pas un nouveau graviton spin-3 déduit de TDG : c'est le **type de son coefficient de couplage** dans ce dictionnaire physique d'essai.

Une rotation de 90° autour de z transforme `J` en `-J`; un retournement de 180° autour de z ou une permutation cyclique xyz le laisse inchangé. Il existe donc une anisotropie *de représentation*, pas seulement un problème d'ajustement d'amplitude.

### Point plus profond : un twist discret de la représentation vectorielle

Sous l'identification du groupe abstrait S4 aux 24 rotations propres du cube (matrices de permutation signées de déterminant +1), l'expérience exacte établit :

\[
R J U_5(R)^{\mathsf T}=\chi(R)J,\quad
\chi(R)=\pm1.
\]

Pour 12 rotations, `chi=+1`; pour les 12 autres, `chi=-1`. Ici `chi` est la parité de la permutation des axes. Le défaut maximal de la loi **twistée** est `1.93e-16`.

Ainsi, **J est bien un entrelaceur vers un module tridimensionnel discret twisté** `rho_3(R)=chi(R) R`, mais pas vers le vecteur spatial ordinaire `R` de cette immersion. Ce twist ne peut pas se prolonger comme caractère de signe continu non trivial sur le groupe connexe SO(3).

Ceci suggère un diagnostic très concret : la conversion d'un `Standard3` discret de TDG en vecteur spatial physique peut requérir un véritable transport / changement de type. C'est une hypothèse sur la bonne identification des modules, **pas** une preuve que la correspondance de groupes retenue ici soit déjà la correspondance physique imposée par Q.

## 3. Théorème de forme du pont minimal

Sous SO(3), `STF^2(R^3)` est irréductible de spin `l=2`, le vecteur est de spin `l=1`.

1. Par le lemme de Schur, il n'existe **aucune** application linéaire SO(3)-équivariante non nulle `STF2 -> V` d'ordre spatial zéro.
2. À un facteur du nombre d'onde, les applications linéaires de premier ordre sont classées par `1 \otimes 2 = 1\oplus2\oplus3`. Le sous-espace qui ressort en spin 1 est **de dimension un** :

\[
D_{\mathbf k}(h)_i=k^j h_{ij}.
\]

Vérification par matrices de contraintes de covariance pour 14 rotations générales :

| Famille | Coefficients libres | Rang des contraintes | Dimension de l'espace équivariant |
|---|---:|---:|---:|
| Sans dérivée (M constant) | 15 | 15 | 0 |
| Un vecteur k (M linéaire en k) | 45 | 44 | 1 |

Le vecteur du noyau à un paramètre coïncide avec l'opérateur divergence avec un recouvrement `~1` et un résidu `1.42e-15`.

Cela est plus fort qu'une correction ad hoc : la bonne forme d'une **liaison minimale** est mathématiquement sélectionnée par la covariance SO(3), **si** la cible physique est un vecteur gradient et la source un STF2.

## 4. Machine constructible : divergence discrète par incidence / transport

Construire un maillage spatial avec pas `a`. Dans un repère plat avec transport de cellules identique, l'opérateur central du second ordre est :

\[
(D_a h)_i(x)=\sum_j\frac{h_{ij}(x+a e_j)-h_{ij}(x-a e_j)}{2a}.
\]

Pour une onde plane `h e^(ikx)`, le symbole est `i sin(a k_j)/a` et tend vers `i k_j`.

L'opérateur amélioré de quatrième ordre remplace ce symbole par

\[
\frac{i}{6a}\left[8\sin(ak_j)-\sin(2ak_j)\right].
\]

Les deux opérateurs ne sont pas parfaitement isotropes à pas fini sur une grille cubique **fixe**, mais ils retrouvent la divergence covariante quand `a -> 0`.

Tests sur 300 directions de propagation et 300 rotations indépendantes (nombres d'onde unitaires); fuite moyenne d'un tenseur transverse-traceless de référence :

| a | Couplage fixe J | Divergence discrète ordre 2 | Divergence discrète ordre 4 |
|---:|---:|---:|---:|
| 0.8 | 0.631254 | 0.01908196 | 0.00212805 |
| 0.4 | 0.631254 | 0.00487444 | 0.00013921 |
| 0.2 | 0.631254 | 0.00122518 | 0.00000880 |
| 0.1 | 0.631254 | 0.00030671 | 0.0000005516 |
| 0.05 | 0.631254 | 0.00007670 | 0.0000000345 |

Ajustements de pente log-log : `1.99077` et `3.98048`. Le défaut moyen de rotation de l'opérateur discret décroît selon les mêmes ordres. L'obstruction J, si elle garde un coefficient non nul et son identification physique, ne converge **pas** vers zéro en raffinant simplement le maillage.

Il s'agit d'une **machine candidate, pas de Q TDG**. Les transports véritables entre cellules nécessitent une connexion calculée de Q, pas une connexion choisie par commodité.

Une extension géométrique courbe utiliserait un transport physique `T_(x<-y)` dans la différence des valeurs de h. En régime infinitésimal, elle pourrait produire `nabla^j h_ij`, si la connexion est compatible avec la métrique effective. Le vrai test de TDG est de dériver ces liens, notamment via le problème de la fibre prédictive/MRP9B, et de vérifier les boucles/holonomies, la localité, le raffinement et le caractère non arbitraire.

## 5. Pourquoi une moyenne de domaines ne règle pas tout

Le groupe octaédrique complet annule exactement la moyenne linéaire de J : `mean J_R=0`. Cependant :

\[
\langle J_R^{\mathsf T}J_R\rangle_{O}=\mathrm{diag}(0,0,1/3,1/3,1/3)
\]

pour la base STF utilisée. La correction quadratique demeure non nulle et **anisotrope** sous le seul groupe octaédrique.

Sous un mélange uniforme de toutes les orientations SO(3), la moyenne quadratique devient isotrope, mais reste non nulle :

\[
\mathbb E_{SO(3)}[J_R^{\mathsf T}J_R]=\tfrac15 I_5.
\]

Monte-Carlo 6 000 orientations : écart Frobenius `0.00364`. La moyenne linéaire d'un ensemble de `N` domaines indépendants diminue comme `1/sqrt(N)`, mais l'intensité locale quadratique ne s'annule pas par ce seul argument. Elle peut alimenter des corrections effectives, selon la dynamique exacte; cela **ne prouve pas** une masse du graviton TDG.

Il serait donc incorrect de dire « la décohérence moyenne l'anisotropie et Einstein apparaît automatiquement ».

## 6. Ce que le laboratoire suggère de changer dans TDG

Une architecture candidate autorisée **uniquement comme laboratoire** :

\[
Q\overset{\mathrm{response/Cons}}{\longrightarrow}
\{\text{faces communes, attaches prédictives}\}
\overset{\mathrm{transport}}{\longrightarrow}
\nabla_Q
\longrightarrow
\text{contraintes de géométrie}
\longrightarrow
\text{GR effective, si l'algèbre se ferme}.
\]

Le diagnostic suggère de ne plus identifier automatiquement un module `Standard3` discret avec un vecteur physique SO(3). Il faut vérifier le signe, le type de fibre, les changements de repère, et la covariance des liaisons entre cellules. La signature `chi` non triviale observée dans l'immersion octaédrique est une piste concrète pour tester un **twist de représentation** avant de réécrire le Q lui-même.

Tests décisifs à appliquer à des données Q réellement récupérées :

1. Reconstruire l'attachement prédictif `Q-B1592/Q-B1602` sans fit, ce qui reste bloqué par la provenance `MRP9B`.
2. Calculer comment le vecteur source/gradient et l'espace STF2 se transforment sous les générateurs discrètement reconstruits, **sans présupposer** le vecteur physique `R`.
3. Tester si le canal J se reclasse en connexion/transport (avec dépendance à k) ou s'il conserve une composante octupolaire `O(1)` physique.
4. Démontrer que le canal physique interdit s'annule dans la limite IR, ou que son effet est entièrement de jauge via un vrai quotient prédictif, pas via une annulation numérique forcée.
5. Seulement ensuite reconstruire les contraintes scalaires B5, les contraintes de frame, l'algèbre HDA et la limite non linéaire d'Einstein.

## 7. Verdict

**DÉRIVÉ (dans le dictionnaire conditionnel) :** J est octupolaire pur `l=3`; son action viole les rotations continues; la loi de signe twistée est exacte pour les 24 rotations de la réalisation cubique choisie. Aucune liaison constante STF2->vecteur n'est compatible SO3. La première liaison différentielle covariante est la divergence; deux discrétisations locales montrent une restauration en `a²` et `a⁴`.

**STRUCTUREL / NOUVELLE HYPOTHÈSE :** le mauvais passage de représentation S4 -> SO3 pourrait expliquer pourquoi un intertwinement discret excellent donne une mauvaise dynamique gravitationnelle. Une construction Q-native de transport géométrique pourrait produire le bon objet différentiel, mais elle n'est pas établie.

**OUVERT :** retrouver le vrai chart Q-B1592/MRP9B, savoir quelle représentation spatiale est réellement retenue par Q, montrer les lois IR et la fermeture non linéaire. Aucune dérivation nouvelle de GR n'est revendiquée.

**Bibliographie de principe :** PDG, « Experimental Tests of Gravitational Theory » (polarisation TT à deux degrés de liberté); Davoudi et Savage, *Phys. Rev. D* 86, 054505 (2012) (récupération de la covariance rotationnelle dans la limite de réseau).

## 8. Reproduction

- `tdg_q_bridge_spin3_diagnostic_2026_11_06.py` : tenseur T, octupôle, S4 sign twist, tests de divergence sur maillage, moyennes orientées.
- `tdg_q_bridge_covariance_rank_2026_11_06.py` : classification de covariance, matrices de rang 15 et 44.
- fichiers JSON correspondants : valeurs exactes et approximations numériques.

Les calculs ne touchent **aucun** artefact canoniquement gelé et n'utilisent pas de faux paramètres Q.
