# Penjelasan komentar tambahan:

1. x-data = local state untuk satu komponen
2. x-model = two-way binding, otomatis update data saat input berubah
3. x-show / x-transition = conditional render + animasi
4. x-text / x-html = menampilkan reactive data
5. @click / @input = event listener
6. x-for = looping array di DOM
7. Alpine.store() = global reactive state, bisa dipakai di banyak komponen
8. $store = akses store global

# Penerapan Concurrent Limit yang sebaiknya di terapkan (terapkan time limit agar yang lain bisa akses)

## Tabel
| No | Jenis Endpoint / Proses    | Contoh Endpoint     | Alasan                  | Saran Limit |
| -- | -------------------------- | ------------------- | ----------------------- | ----------- |
| 1  | Image / Video Processing   | `/process-image`    | CPU & RAM berat         | 1–2         |
| 2  | AI / ML Inference (GPU)    | `/predict`          | GPU terbatas            | 1           |
| 3  | Generate Report Besar      | `/generate-report`  | Query DB berat + render | 1–3         |
| 4  | Export Data Besar          | `/export-csv`       | Memory & disk IO        | 1–2         |
| 5  | Upload File Besar          | `/upload`           | IO blocking             | 2–5         |
| 6  | Download File Besar        | `/download/bigfile` | IO blocking             | 2–5         |
| 7  | Web Scraping               | `/scrape`           | Lambat + rawan timeout  | 1–2         |
| 8  | Integrasi API Pihak Ketiga | `/send-whatsapp`    | Rate limit eksternal    | 1–3         |
| 9  | Payment Processing         | `/pay`              | Kritis + eksternal      | 1–2         |
| 10 | Update Inventory / Stock   | `/update-stock`     | Race condition          | 1           |
| 11 | Bulk Insert / Migration    | `/bulk-insert`      | DB load tinggi          | 1           |
| 12 | Backup / Restore           | `/backup`           | Disk + DB berat         | 1           |
| 13 | PDF Rendering              | `/render-pdf`       | CPU + font IO           | 1–2         |
| 14 | Email Blast                | `/send-bulk-email`  | SMTP limit              | 1–3         |
| 15 | Video Streaming Transcode  | `/transcode`        | CPU tinggi              | 1           |

## Interpretasi Singkat
| Karakter            | Perlu Concurrent Limit |
| ------------------- | ---------------------- |
| CPU tinggi          | Ya                     |
| RAM tinggi          | Ya                     |
| IO lambat           | Ya                     |
| Resource terbatas   | Ya                     |
| Race condition risk | Ya                     |
| Read-only cepat     | Tidak                  |
