# TDG / Root2 - Laboratoire de diagnostic Q-vers-geometrie: le twist S4 ne suffit pas

**Date du test :** 2026-11-06 (America/Toronto)  
**Statut :** NO-GO exact dans l'immersion cubique conditionnelle; aucun nouveau theoreme GR issu de Q.  
**Source canonique :** `CURRENT_FRONT_LATEST.md`, `CURRENT_STATE.md`, checkpoint `TDG_FORMAL_READOUT_FREE_DYNAMIC_L2_TO_L1_NONZERO_2026-09-18.md`, `TDG_B5_TO_GR_BRANCH_STOP_CURRENT_ROOT2_2026-10-06.md`, `TDG_MRP9A_SAME_FACE_LINK_PROVENANCE_GAP_2026-10-14.md`.  
**Filiation :** tests du 6 novembre: lentille de decoherence, horizon infini, pont exploratoire B5/GR, machine etalon, diagnostic Q-geometrie `spin3`/`covariance_rank`.  
**Protocole de securite :** aucun fichier canonique modifie. Aucun parametre microscopique de Q ni coefficient historique recalcule. Les valeurs choisies pour le modele auxiliaire sont illustratives, non mesurees.

## 1. Question experimentale

Le signe supplementaire identifie dans la carte canonique `J` de TDG est-il seulement une erreur de choix de base, reparable par une transformation locale? Si oui, le defaut physique SO(3) pourrait disparaitre sans modifier Q. Sinon, il manque une loi de transport/une dynamique differente.

On reprend le rayon TDG `J=-(1/sqrt(3))[yz->x, xz->y, xy->z]` au sein d'une identification conditionnelle `l=2=STF2(R3)`, `l=1=R3`. La realisation cubique du groupe abstrait S4 utilise les 24 matrices de permutation signee de determinant +1. `U5(R)` est l'action induite sur STF2. Le caractere chi(R) est la parite de la permutation des axes, PAS le determinant spatial.

## 2. Controle du twist et de sa coherence

Pour les 24 rotations et les 576 paires:

- `chi(RS)=chi(R)chi(S)` : erreur exacte **0**;
- `R J U5(R)^T = chi(R) J` : erreur maximale **1.923e-16**;
- 12 rotations ont `chi=+1`, 12 ont `chi=-1`.

Donc le twist est un vrai caractere discret. Ce n'est pas une anomalie numerique.

## 3. Test de reparabilite par changement de base

On cherche une matrice constante inversible `T` telle que

`R T = T (chi(R) R)` pour les 24 rotations.

Les 9 coefficients de T satisfont un systeme lineaire de **rang 9**; l'espace des solutions a **dimension 0**. Sa plus petite valeur singuliere vaut **6.92820323** (avec les matrices d'equations non normalisees).

**Resultat :** les deux modules tridimensionnels (vecteur standard et vecteur twisté) ne sont pas isomorphes comme representations cubiques. Un simple changement de base ne peut pas guerir le pont. Un caractere de signe non trivial ne s'etend pas non plus en caractere continu sur le groupe connexe SO(3).

Cela n'exclut PAS un transport Q dynamique avec d'autres donnees ou une identification physique differente; cela exclut uniquement la reparation par identification constante dans ce dictionnaire.

## 4. Le twist peut etre localement plat, sans etre physiquement suffisant

On assigne quatre repères cubiques `R_a` a un circuit. Les signes de lien `epsilon_ab=chi(R_a^T R_b)` donnent un holonomie `prod epsilon=+1` exactement: le twist local engendre par repères est un cocycle pur de jauge Z2. Une seule liaison frustree donne une holonomie `-1`, invariante sous les changements de signe aux sommets.

**Ce que cela prouve :** le transport de signes peut etre trivial sur une cellule simplement couverte, mais un secteur frustré ne l'est pas. **Ce que cela ne prouve pas :** que Q produit de telles holonomies ou une vraie connexion physique SO(3).

## 5. Test sur les deux vraies polarisations TT

Pour une onde de direction `k=(0,0,1)`, les tenseurs TT `h_plus=(xx-yy)/sqrt(2)` et `h_cross=(xy+yx)/sqrt(2)` donnent

`(J TT)^T (J TT) = diag(0,1/3)`;

alors que la divergence géometrique `D_k(h)_i = k^j h_ij` satisfait `D_k TT = 0` exactement.

La mere requalification en vecteur twiste ne transforme donc pas ce couplage d'ordre zero en une divergence: il manque la direction k et sa loi de transport.

## 6. Integration d'un champ vectoriel auxiliaire: defaut d'onde residuel

On examine un modele quadratique volontairement simple

`M = [[k^2 I_5, c J^T], [c J, m^2 I_3]]`.

En integrant le vecteur auxiliaire de masse m>0, l'operateur effectif tensoriel devient

`M_eff = k^2 I_5 - (c^2/m^2) J^T J`.

Sur les deux polarisations TT selon z, les valeurs propres sont separees de `c^2/(3m^2)`. Pour les choix *illustratifs* `c=1`, `m=5`, `k^2=1`, elles valent **0.9866666667** et **1**, ecart **0.0133333333**. Si l'on remplace le couplage par la divergence covariante D_k, les deux valeurs propres valent **1**, sans separation.

Il s'agit d'une birefringence statique effective *dans ce modele quadratique*, pas d'une prediction physique de TDG et pas d'une masse de graviton mesuree. Le resultat montre que l'elimination d'un secteur auxiliaire ne fait pas automatiquement disparaitre l'anisotropie.

## 7. Controle des rotations continues

Le defaut de covariance de `J` sous la rotation propre de 90 degres autour de z vaut exactement **2** en norme de Frobenius. Pour 60 degres il vaut **sqrt(3)=1.73205080757**. Aucun ajustement de pas de reseau ne fera tendre une de ces valeurs constantes vers 0 tant que J conserve ce role physique.

## 8. Diagnostic et choix de recherche

- **DERIVE dans le dictionnaire conditionnel:** twist S4 coherent, non-isomorphie lineaire avec le vecteur spatial, deux polarisations affectees de facon inequivalente dans un modele d'integration de vecteur, besoin d'une direction/derivation pour retrouver la divergence continue.
- **PROVENANCE TDG:** la non-annulation du canal J a ete etablie independamment dans les checkpoints de septembre; pas de nouvelle extraction de ce coefficient depuis le Q microscopique.
- **HYPOTHESES NOUVELLES:** identification cubique des modules S4 avec champs physiques, modele quadratique auxiliaire, signaux de liaison sur quatre sites.
- **NON PROUVE:** transport Q donnant D_k, passage geometrique continu, algebre HDA, equ. Einstein non lineaires, classe du lien MRP9B.
- **NEXT:** retrouver Q-B1592/MRP9B, extraire le vrai transport predictif entre deux faces, calculer la representation physique sous transport avec une direction relative obtenue de Q; si le defaut spin-3 conserve une intensite IR non nulle, classer une violation de covariance au lieu de fabriquer un contre-terme. Ensuite seulement tester les contraintes et la fermeture non lineaire.

Aucune conclusion n'est promue dans les fichiers historiques `Q-B1858L`, B5, MRP. Le present laboratoire est une nouvelle piece append-only, distincte du modele de reference.

## 9. Reproduction et integrite

Programme autonome: `tdg_q_twist_no_go_2026_11_06.py` (NumPy), sortie JSON `tdg_q_twist_no_go_results_2026_11_06.json`, execution brute `tdg_q_twist_no_go_execution_2026_11_06.txt`. Voir `MANIFEST_SHA256.txt` pour l'integrite des fichiers du laboratoire et de ses predecesseurs conserves.
