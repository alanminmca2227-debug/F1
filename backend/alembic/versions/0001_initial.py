"""initial schema

Revision ID: 0001_initial
Revises: 
Create Date: 2026-05-17 19:31:00

"""
from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "constructors",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("nationality", sa.String(), nullable=True),
        sa.Column("active_years", sa.String(), nullable=True),
        sa.Column("championships", sa.Integer(), server_default=sa.text("0"), nullable=True),
        sa.Column("wins", sa.Integer(), server_default=sa.text("0"), nullable=True),
        sa.Column("podiums", sa.Integer(), server_default=sa.text("0"), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_constructors_id", "constructors", ["id"], unique=False)

    op.create_table(
        "drivers",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("permanent_number", sa.Integer(), nullable=True),
        sa.Column("code", sa.String(), nullable=True),
        sa.Column("given_name", sa.String(), nullable=False),
        sa.Column("family_name", sa.String(), nullable=False),
        sa.Column("full_name", sa.String(), nullable=False),
        sa.Column("date_of_birth", sa.String(), nullable=True),
        sa.Column("nationality", sa.String(), nullable=True),
        sa.Column("active_status", sa.Boolean(), server_default=sa.text("0"), nullable=True),
        sa.Column("first_season", sa.Integer(), nullable=True),
        sa.Column("last_season", sa.Integer(), nullable=True),
        sa.Column("championships", sa.Integer(), server_default=sa.text("0"), nullable=True),
        sa.Column("wins", sa.Integer(), server_default=sa.text("0"), nullable=True),
        sa.Column("podiums", sa.Integer(), server_default=sa.text("0"), nullable=True),
        sa.Column("poles", sa.Integer(), server_default=sa.text("0"), nullable=True),
        sa.Column("fastest_laps", sa.Integer(), server_default=sa.text("0"), nullable=True),
        sa.Column("starts", sa.Integer(), server_default=sa.text("0"), nullable=True),
        sa.Column("points", sa.Float(), server_default=sa.text("0"), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_drivers_id", "drivers", ["id"], unique=False)

    op.create_table(
        "cars",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("constructor_id", sa.String(), nullable=False),
        sa.Column("season", sa.Integer(), nullable=False),
        sa.Column("chassis_name", sa.String(), nullable=True),
        sa.Column("engine", sa.String(), nullable=True),
        sa.Column("tyre_supplier", sa.String(), nullable=True),
        sa.Column("era", sa.String(), nullable=True),
        sa.Column("drivers", sa.String(), nullable=True),
        sa.Column("wins", sa.Integer(), server_default=sa.text("0"), nullable=True),
        sa.Column("podiums", sa.Integer(), server_default=sa.text("0"), nullable=True),
        sa.Column("poles", sa.Integer(), server_default=sa.text("0"), nullable=True),
        sa.Column("championships", sa.Integer(), server_default=sa.text("0"), nullable=True),
        sa.Column("notes", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(["constructor_id"], ["constructors.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_cars_id", "cars", ["id"], unique=False)

    op.create_table(
        "seasons",
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("rounds", sa.Integer(), server_default=sa.text("0"), nullable=True),
        sa.Column("champion_driver_id", sa.String(), nullable=True),
        sa.Column("champion_constructor_id", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("year"),
    )
    op.create_index("ix_seasons_year", "seasons", ["year"], unique=False)

    op.create_table(
        "telemetry_sessions",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("session_key", sa.String(), nullable=True),
        sa.Column("meeting_key", sa.String(), nullable=True),
        sa.Column("season", sa.Integer(), nullable=True),
        sa.Column("track_name", sa.String(), nullable=True),
        sa.Column("session_name", sa.String(), nullable=True),
        sa.Column("start_time", sa.String(), nullable=True),
        sa.Column("end_time", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_telemetry_sessions_id", "telemetry_sessions", ["id"], unique=False)

    op.create_table(
        "driver_career_entries",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("driver_id", sa.String(), nullable=False),
        sa.Column("season", sa.Integer(), nullable=False),
        sa.Column("constructor_id", sa.String(), nullable=True),
        sa.Column("team_name", sa.String(), nullable=True),
        sa.Column("car_id", sa.String(), nullable=True),
        sa.Column("races", sa.Integer(), server_default=sa.text("0"), nullable=True),
        sa.Column("wins", sa.Integer(), server_default=sa.text("0"), nullable=True),
        sa.Column("podiums", sa.Integer(), server_default=sa.text("0"), nullable=True),
        sa.Column("poles", sa.Integer(), server_default=sa.text("0"), nullable=True),
        sa.Column("points", sa.Float(), server_default=sa.text("0"), nullable=True),
        sa.Column("championship_position", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["car_id"], ["cars.id"]),
        sa.ForeignKeyConstraint(["constructor_id"], ["constructors.id"]),
        sa.ForeignKeyConstraint(["driver_id"], ["drivers.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "results",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("race_id", sa.String(), nullable=True),
        sa.Column("driver_id", sa.String(), nullable=False),
        sa.Column("constructor_id", sa.String(), nullable=True),
        sa.Column("season", sa.Integer(), nullable=False),
        sa.Column("round", sa.Integer(), nullable=True),
        sa.Column("circuit", sa.String(), nullable=True),
        sa.Column("grid", sa.Integer(), nullable=True),
        sa.Column("position", sa.Integer(), nullable=True),
        sa.Column("status", sa.String(), nullable=True),
        sa.Column("points", sa.Float(), server_default=sa.text("0"), nullable=True),
        sa.Column("fastest_lap", sa.String(), nullable=True),
        sa.Column("laps", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["constructor_id"], ["constructors.id"]),
        sa.ForeignKeyConstraint(["driver_id"], ["drivers.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "cache_entries",
        sa.Column("key", sa.String(), nullable=False),
        sa.Column("payload", sa.Text(), nullable=False),
        sa.Column("expires_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("key"),
    )
    op.create_index("ix_cache_entries_key", "cache_entries", ["key"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_cache_entries_key", table_name="cache_entries")
    op.drop_table("cache_entries")
    op.drop_table("results")
    op.drop_table("driver_career_entries")
    op.drop_index("ix_telemetry_sessions_id", table_name="telemetry_sessions")
    op.drop_table("telemetry_sessions")
    op.drop_index("ix_seasons_year", table_name="seasons")
    op.drop_table("seasons")
    op.drop_index("ix_cars_id", table_name="cars")
    op.drop_table("cars")
    op.drop_index("ix_drivers_id", table_name="drivers")
    op.drop_table("drivers")
    op.drop_index("ix_constructors_id", table_name="constructors")
    op.drop_table("constructors")
