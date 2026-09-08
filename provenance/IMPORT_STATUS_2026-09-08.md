# TDG — Statut d'import Library → GitHub

**Date : 2026-09-08**

## Importé et vérifiable dans GitHub

- `CURRENT_STATE.md` — front scientifique et firewalls de Sentinelle.
- `history/README.md` — carte patrimoniale.
- `history/ADDONS_STATUS.md` — disposition des add-ons historiques #0–22.
- `provenance/HISTORICAL_LIBRARY_INVENTORY_2026-09-08.md` — inventaire des sources retrouvées.
- `provenance/TDG_WORK_A2Z_MANIFEST_SHA256_2026-09-06.txt` — manifeste Work original.
- `checkpoints/P10O/TDG_A2Z_DELTA_P10N_TO_P10O_2026-09-06.md` — delta P10N→P10O.

## Sources retrouvées dans la Library et matérialisées localement

| Source | Taille brute | SHA-256 / ancre |
| --- | ---: | --- |
| `Complete_TDG_ROOT2_A_TO_Z_GRANDMOTHER_WORK_RECOVERY_P10O_CLOSED_P10P_NOT_STARTED_2026-09-06.md` | 6,607,314 octets | `c31639d0ae6c07037120e69dfcf65f114acf094efd705356660d914567923d26` |
| `Complete_TDG_MASTER_AUDIT_HISTORIQUE_2026-09-03.md` | 62,338 octets | source Library retrouvée; annexe E contient les hashes de ses sources de travail |
| `TDG_Root_Reconstruction_Recovery_2026-08-10.md` | 44,705 octets | source Library retrouvée |
| `TDG_A2Z_DELTA_P10N_TO_P10O_2026-09-06.md` | 1,824 octets | importé |
| `TDG_WORK_A2Z_MANIFEST_SHA256_2026-09-06.txt` | 2,130 octets | importé |

## Limite actuelle du connecteur GitHub

Le connecteur d'écriture accepte du contenu UTF-8 fourni directement à l'API, mais ne possède pas actuellement un paramètre permettant de prendre un fichier local matérialisé et de l'uploader byte-for-byte. Une tentative d'encoder un fichier compressé dans un gros payload textuel a été détectée comme tronquée; le fichier fautif a été supprimé immédiatement du dépôt.

Conséquence : **aucun fichier volumineux ne doit être marqué “importé intégralement” tant qu'une lecture de contrôle n'en confirme pas l'intégrité**.

Le recovery P10O complet reste donc ancré par sa source Library et son SHA-256 ci-dessus jusqu'à ce qu'un chemin d'upload binaire/local fiable soit disponible.

## Gaps documentaires à ne jamais interpoler

- Q-B506→555 : détail historique partiellement perdu.
- Q-B759→878 : aucun delta autonome retrouvé.
- certains raw repro Q-B1831→1835 : manquants.

## Règle

`RETROUVÉ DANS LA LIBRARY` ≠ `IMPORTÉ DANS GITHUB` ≠ `CANONIQUE` ≠ `VALIDÉ PHYSIQUEMENT`.

La migration doit rester additive, auditable et sans promotion scientifique implicite.
