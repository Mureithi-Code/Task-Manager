"""Add task_users many-to-many relationship

Revision ID: 2b9a280cf9dc
Revises: 98be8e6b4bcb
Create Date: 2024-12-18 12:57:43.297909

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b9a280cf9dc'
down_revision: Union[str, None] = '98be8e6b4bcb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###