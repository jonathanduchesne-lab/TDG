# TDG — laboratoire du 6 novembre 2026 (non canonique)

Ce répertoire conserve les expériences reproductibles de la conversation du 6 novembre 2026, sans modifier le front scientifique canonique (`Q-B1858L`, `CURRENT_STATE.md`, `CURRENT_FRONT_LATEST.md`). Les programmes, rapports et sorties numériques sont des artefacts de laboratoire; leur dépôt ne signifie pas validation physique.

## Ordre de lecture

1. `tdg_rapport_lentille_actualisation_2026_11_06.md` : décohérence et mémoire.
2. `tdg_projection_horizon_infini_2026_11_06.md` : deux limites asymptotiques distinctes.
3. `tdg_bridge_sans_barrieres_rapport_2026_11_06.md` : extensions gravitationnelles volontairement hypothétiques.
4. `tdg_machine_etalon_rapport_2026_11_06.md` : machine Einstein de référence et injection de J.
5. `tdg_q_pont_geometrique_diagnostic_2026_11_06.md` : octupôle spin-3, signe S4 et divergence covariante.
6. **`TDG_LAB_2026_11_06_TWIST_NO_GO.md`** : nouveau test, impossibilité de la correction par changement de base, contraintes topologiques Z2, scission des polarisations TT.

## Verdict actuel

La représentation cubique `J` est exactement équivariante vers un vecteur *twisté* de S4, mais les deux représentations tridimensionnelles ne sont pas isomorphes (rang 9/9 des contraintes d'entrelacement). Le twist local seul n'apporte ni la direction `k` ni le transport nécessaires pour obtenir une divergence SO(3)-covariante. Il n'y a **aucune nouvelle dérivation de GR à partir de Q**.

## Provenance et reproduction

Les scripts `.py` et sorties `.json`/`.txt` accompagnent les rapports disponibles. Les fichiers canoniques n'ont pas été modifiés. Les scripts de la première partie du travail sont des modèles d'essai, pas des exécutions du vrai Q microscopique. Le dossier utilise un archivage append-only: ne pas modifier les documents déjà enregistrés; créer de nouveaux checkpoints pour les futurs tests.

**Gap toujours ouvert :** reconstruction exacte de la carte prédictive Q-B1592 / MRP9B.

## 2026-11-06 — MRP9B : transport de repères et twirling

- `TDG_LAB_2026_11_06_MRP9B_TRANSPORT_TWIRLING.md` : démonstration conditionnelle de transport SO(3) localement covariant, limites d'une moyenne cubique/icosaédrique du canal J, tests sur maillage à sept cellules et holonomie.
- `tdg_mrp9b_transport_twirling_2026_11_06.py` : programme Python reproductible (numpy/scipy).
- `tdg_mrp9b_transport_twirling_resultats_2026_11_06.json` : valeurs calculées.
- `tdg_mrp9b_transport_twirling_execution_2026_11_06.txt` : journal d'exécution brut.
- `TDG_MRP9B_TRANSPORT_TWIRLING_SHA256.txt` : empreintes des pièces du checkpoint.

**Classification :** test mathématique de capacité **non Q-dérivé**. MRP9B et récupération de la carte prédictive Q-B1592 **restent ouverts**. Aucune promotion vers GR ni modification des états canoniques.

## 2026-11-06 — MRP9B : réponse de Feshbach / holonomie

- `TDG_LAB_2026_11_06_MRP9B_FESHBACH_HOLONOMY.md` : nouvelle condition de non-factorisation cellule×face, modèle Schur/Feshbach 6×2→2×2, holonomie et loi de raffinement.
- `tdg_mrp9b_feshbach_holonomy_2026_11_06.py` : source complète exécutable (NumPy / SciPy).
- `tdg_mrp9b_feshbach_holonomy_resultats_2026_11_06.json` : toutes les données numériques.
- `tdg_mrp9b_feshbach_holonomy_execution_2026_11_06.txt` : sortie brute.
- `TDG_MRP9B_FESHBACH_HOLONOMY_SHA256.txt` : empreintes de la sauvegarde locale reproductible.

**Verdict :** construction de capacité bien typée, mais H synthétique et attachage Σ non attesté comme carte réelle Q-B1592. Holonomie non triviale possible sans pseudo-inverse ; attention, ses commutateurs engendrent précisément le secteur vertical SU2 rang3 qui demeure un obstacle à HDA. **MRP9B reste ouvert.** Aucun fichier canonique modifié.
