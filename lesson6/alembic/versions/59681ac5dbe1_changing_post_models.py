"""changing post models

Revision ID: 59681ac5dbe1
Revises: ba2e30fadb3c
Create Date: 2024-03-01 20:37:56.934378

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59681ac5dbe1'
down_revision: Union[str, None] = 'ba2e30fadb3c'
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
