"""empty message

Revision ID: 2c67653c39ea
Revises: 18d6095002ef
Create Date: 2015-05-02 16:16:31.400485

"""

# revision identifiers, used by Alembic.
revision = '2c67653c39ea'
down_revision = '18d6095002ef'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('kaharesource', sa.Column('datasource', sa.String(length=20), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('kaharesource', 'datasource')
    ### end Alembic commands ###