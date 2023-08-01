from dataclasses import dataclass, field

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Issue:
    id: str = None
    priority_score: int = 0
    severity: str = None


@dataclass_json
@dataclass
class Fix:
    fix_package: str = None
    issues_fixed: list[Issue] = field(default_factory=list)


@dataclass_json
@dataclass
class ProjectIssues:
    project_id: str = None
    fixes: list[Fix] = field(default_factory=list)


@dataclass_json
@dataclass
class AggregatedIssues:
    issues: list[ProjectIssues] = field(default_factory=list)


if __name__ == '__main__':
   pass





