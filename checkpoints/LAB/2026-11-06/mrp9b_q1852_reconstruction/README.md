# TDG MRP9B — archive scientifique du 6 novembre 2026

Ce dossier est **exploratoire** et n'est pas le noyau officiel de TDG. Il rassemble la récupération des vrais programmes historiques Q-B1592 et Q-B1852, trois sondes de transport, les sorties numériques et les journaux de vérification. Les deux fichiers originaux copies `tdg_mrp9b_recovered_qb1592_original.py` et `tdg_mrp9b_recovered_qb1852_original.py` nécessitent leurs dépendances historiques présentes dans les archives sources de la Library.

## Provenance / rejouabilité
- Q-B1592 : `/TDG/Recovery/Complete_TDG_A_to_Z_QB1592_Handoff_2026-08-15.tar.gz`, sous-archive `TDG_QB1540_QB1592_repro_2026-08-15.tar.gz`.
- Q-B1852 : `/TDG/Recovery/Complete_TDG_Root2_FULL_A_TO_Z_THREAD_HANDOFF_QB1860BW_COMPLETE_2026-08-21.tar.gz`, chaîne interne `PARENT_PARTIAL -> repro_QB1860BV -> repro_QB1860BU -> deps/repro_qb1852`.
- Packages Python : NumPy et SciPy. Exécuter avec `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1` dans un environnement contenant les dépendances extraites.
- La projection de la carte Q-B1592 sur le modèle Q-B1852 est une hypothèse **non encore autorisée** par un théorème d'identification des fibres prédictives ; les résultats ne prouvent pas la relativité générale.

Voir `TDG_MRP9B_Q1852_RECONSTRUCTION_2026_11_06.md` pour le statut exact des contrôles, leurs limites et les prochaines étapes.
