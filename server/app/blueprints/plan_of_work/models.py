import datetime
from lib.util_sqlalchemy import ResourceMixin, AwareDateTime
from app.extensions import db
from collections import OrderedDict

class PlanOfWork(ResourceMixin, db.Model):
    __tablename__ = 'plan_of_work'

    id = db.Column(db.Integer, primary_key=True) # Primary key

    status = db.Column(db.String(120), default='Draft')
    cohort = db.Column(db.String(120), nullable=False)
    exec_summary = db.Column(db.Text)
    merit_peer_review = db.Column(db.Text)
    stakeholder_actions = db.Column(db.Text)
    stakeholder_id_methods = db.Column(db.Text)
    stakeholder_collection_method = db.Column(db.Text)
    stakeholder_how_considered = db.Column(db.Text)

    critical_issues = db.relationship('CriticalIssue',
                        backref='planofwork', lazy=True)

    @property
    def serialize(self):
        return {
                    'status': self.status,
                    'cohort': self.cohort,
                    'summary': self.exec_summary,
                    'merit_peer_review': self.merit_peer_review,
                    'stakeholder_actions': self.stakeholder_actions,
                    'stakeholder_id_methods': self.stakeholder_id_methods,
                    'stakeholder_collection_method':
                        self.stakeholder_collection_method,
                    'stakeholder_how_considered':
                    self.stakeholder_how_considered
                }

class CriticalIssue(ResourceMixin, db.Model):
    __tablename__ = 'critical_issue'
    TERM = OrderedDict([
        ('short', 'Short-Term: Under 1 year'),
        ('intermediate', 'Intermediate: 1 to 5 years'),
        ('long', 'Long-Term: 5 or more years')
    ])
    id = db.Column(db.Integer, primary_key=True)
    # Foreign Key
    plan_id = db.Column(db.Integer, db.ForeignKey('plan_of_work.id'),
        nullable=False)

    order = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    term = db.Column(db.Enum(*TERM, name='plan_terms', native_enum=False),
        index=True, nullable=False, server_default='short')


