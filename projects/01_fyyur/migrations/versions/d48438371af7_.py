"""empty message

Revision ID: d48438371af7
Revises: 4990cad8cc41
Create Date: 2020-02-27 15:51:28.734383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd48438371af7'
down_revision = '4990cad8cc41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('artist_id', sa.Integer(), nullable=False))
    op.add_column('shows', sa.Column('venue_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'shows', 'venues', ['venue_id'], ['id'])
    op.create_foreign_key(None, 'shows', 'artists', ['artist_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.drop_column('shows', 'venue_id')
    op.drop_column('shows', 'artist_id')
    # ### end Alembic commands ###
