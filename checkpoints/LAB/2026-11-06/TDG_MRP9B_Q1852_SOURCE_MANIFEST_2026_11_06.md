# TDG MRP9B — Provenance et mode de récupération

Date: 2026-11-06.

## Deux archives historiques dans la Library ChatGPT

1. `/TDG/Recovery/Complete_TDG_A_to_Z_QB1592_Handoff_2026-08-15.tar.gz` (SHA256 `8410d8814e2fe15108731de4f9e49046693cbdafd3abb6dc55d47400c6be9bdf`). Son archive imbriquée contient `exploratory/qb1592_semicausal_crossing_SL2_frame_connection_triplet.py` (SHA256 `7bc91553a01e2b5024c9982e2f4bd2a392f612621a826b6f9f5a111739f140ab`) et `cert_qb1592.py` (4/4 PASS).
2. `/TDG/Recovery/Complete_TDG_Root2_FULL_A_TO_Z_THREAD_HANDOFF_QB1860BW_COMPLETE_2026-08-21.tar.gz` (SHA256 `bd4f6171fccc81bf74849162cecdfdd882867ebc4ef8d7715f1ad8fd3e1f7737`). Chemin imbriqué: root -> `PARENT_...PARTIAL` -> `TDG_QB1860BV_LIVE_repro...` -> `TDG_QB1860BU_LIVE_repro...` -> `repro_qb1860bu/deps/repro_qb1852/`. Fichier `qb1852_full_refined.py` (SHA256 `ebbe56f7d9c0b19b5c7e688e2b69c7acd2f9a271d161cf558e50e52cad86b5c7`). La sous-arborescence contient 1902 fichiers dépendants. `qb1852_final_verify.py` = 24 PASS puis `QB1852 FINAL PORTABLE VERIFY PASS`.

## Contenu de l'archive de laboratoire

Le ZIP associe le rapport scientifique, les deux sources originales *sans modification* (snapshot), trois programmes expérimentaux, toutes les données JSON, deux contrôles de lecture spectrale, cinq journaux d'exécution/certification et un fichier de hachage SHA-256. Les scripts locaux requièrent l'arborescence complète de Q-B1852 ci-dessus : les deux fichiers `qb1852_full_refined.py` et `qb1592_...py` seuls ne contiennent PAS toutes leurs dépendances.

Les fichiers originaux restent propriétaires de l'historique scientifique déjà présent dans la Library. Le laboratoire GitHub ne doit pas les reclasser comme nouvelles lois du Root2; les copies sont des snapshots de provenance.

## Critères de rejet / promotion

- Réduction des boucles statiques ~ a^4 et row-space ~a^2 : **ne pas promouvoir** comme courbure physique.
- Réponse de source non nulle ~ a^2 : **capacité mathématique conditionnelle**, non unique au vu des inverses à droite, sensible à z.
- Le vrai front Q-B1858L et `CURRENT_FRONT_LATEST.md` reste inchangé.
