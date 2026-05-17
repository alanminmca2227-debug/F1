# Apex Archive

A premium, Formula 1-inspired digital archive and telemetry museum. The project includes a Next.js frontend and a FastAPI backend, with cached data sources and placeholders for custom 3D car scenes.

## Folder Structure

- frontend/ - Next.js + Tailwind + Framer Motion UI
- backend/ - FastAPI + SQLAlchemy services and cache

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Copy the environment example and add your Spline or Omma scene URLs:

```bash
copy .env.example .env.local
```

### Frontend Environment Variables

- NEXT_PUBLIC_API_BASE: Backend API base URL
- NEXT_PUBLIC_SPLINE_HERO: Hero 3D scene URL
- NEXT_PUBLIC_SPLINE_DRIVER: Driver profile 3D scene URL
- NEXT_PUBLIC_SPLINE_1950: 1950s car scene URL
- NEXT_PUBLIC_SPLINE_1980: 1980s car scene URL
- NEXT_PUBLIC_SPLINE_2000: 2000s car scene URL
- NEXT_PUBLIC_SPLINE_2022: 2022+ car scene URL

## Backend Setup

```bash
cd backend
python -m venv .venv
.\venv\Scripts\activate
pip install -r requirements.txt
python -m app.main
```

Seed development data:

```bash
python scripts/seed_data.py
```

Run database migrations (from the backend folder):

```bash
alembic upgrade head
```

### Backend Environment Variables

Copy the example file and edit as needed:

```bash
copy .env.example .env
```

- DATABASE_URL: Database connection string
- FRONTEND_ORIGIN: Frontend origin for CORS
- JOLPICA_BASE_URL: Historical F1 data endpoint
- OPENF1_BASE_URL: Modern telemetry endpoint
- FASTF1_CACHE_DIR: Cache path for FastF1
- CACHE_TTL_SECONDS: Cache TTL in seconds

## Data Sources

- Jolpica / Ergast compatible for historical drivers, seasons, constructors, results
- OpenF1 for modern sessions, laps, weather, race control
- FastF1 for session results and telemetry

## Notes

- All 3D scenes are placeholders and should be replaced with original assets.
- The UI uses fictional livery placeholders and avoids official team branding.
- API responses include metadata for data source and last updated timestamps.
