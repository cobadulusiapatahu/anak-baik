# Anak Baik

A small points-and-rewards web app for families, built with Flask. Adults add child profiles, mark tasks as done to earn points, and redeem points for rewards.

**Demo only. This repository contains no real personal or child data.** Sample tasks, rewards and the default avatar are generic.

**Source-available, NOT open source.** Free for personal and non-commercial use under the PolyForm Noncommercial License 1.0.0. Commercial use needs written permission: hello@cobadulu.id.

## How to run

Requires Python 3.10 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Set a random secret key (required, there is no default)
export SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')

export FLASK_APP=run.py
flask init-db      # creates the local SQLite database with generic sample tasks and rewards
flask run
```

Open http://127.0.0.1:5000.
Note: `flask init-db` drops and recreates all tables. Only run it on a fresh install.

Tests (installs pytest): `pip install -r requirements-dev.txt && python -m pytest`

## Environment variables

| Variable | Required | Description |
|----------|----------|-------------|
| `SECRET_KEY` | Yes | Random secret used to sign sessions. The app refuses to start without it. See `.env.example`. |
| `DATABASE_URL` | No | SQLAlchemy database URL. Defaults to a local SQLite file `anak_baik.db`. |

Never commit a `.env` file. `.gitignore` excludes `.env*` except `.env.example`.

## Data note

- No real child data is included in this repository. Sample tasks, rewards and the default avatar are generic.
- Photos you upload are stored locally in `app/static/assets/kids/` and are excluded from version control.
- The app has no login, no analytics and no third-party scripts. It is meant for local or private-network use.
- Do not deploy it publicly with real children's data without understanding the privacy duties that apply
  (consent, access control, data protection law in your country).

## Assets

See [ASSETS.md](ASSETS.md) for the source and licence of every asset.

## Licence

- Code: [PolyForm Noncommercial License 1.0.0](LICENSE) (personal and non-commercial use only). This is not an OSI-approved open source licence.
- Original SVG artwork in `app/static/assets/` and the documentation: [CC BY-NC 4.0](LICENSE-ASSETS-AND-DOCS.txt). Credit: "Coba Dulu".
- Commercial use of any part requires written permission via hello@cobadulu.id.

## Credits and third-party notices

Built with Flask, Flask-SQLAlchemy and Werkzeug (BSD-3-Clause licensed, installed from PyPI, not bundled). See [ASSETS.md](ASSETS.md) for the source of every asset.

## Bahasa Indonesia

Anak Baik adalah aplikasi web kecil untuk keluarga: orang tua membuat profil anak, mencatat tugas yang selesai untuk mendapat poin, lalu menukar poin dengan hadiah. Ini hanya demo, tanpa data pribadi atau data anak yang asli. Kode boleh dipakai gratis untuk keperluan pribadi dan nonkomersial (source-available, bukan open source). Penggunaan komersial memerlukan izin tertulis lewat hello@cobadulu.id. Cara menjalankan ada di bagian "How to run" di atas.

## Contact

hello@cobadulu.id

A Coba Dulu project
