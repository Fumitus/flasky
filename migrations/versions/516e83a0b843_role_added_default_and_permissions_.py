"""Role added default and permissions columns

Revision ID: 516e83a0b843
Revises: 99c654184d6b
Create Date: 2019-07-03 11:14:13.515303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '516e83a0b843'
down_revision = '99c654184d6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'default')
    # ### end Alembic commands ###
