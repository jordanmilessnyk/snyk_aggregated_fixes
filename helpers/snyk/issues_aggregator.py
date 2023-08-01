from snyk.models import Project

from helpers.click.click_outputs import output_info
from models.agg_issues_model import (
    ProjectIssues,
    Fix,
    Issue,
    AggregatedIssues
)


class IssuesAggregator:

    def __init__(self):
        self.agg_proj_issues = AggregatedIssues(issues=list())

    def aggregate_new_issues(self, project: Project):

        # encapsulate this to make it private
        def map_remediation_to_fix(remediation, project_vulns):

            new_fix = Fix()
            new_fix.fix_package = f'{remediation[0]} -> {remediation[1]["upgradeTo"]}'
            new_fix.issues_fixed = [
                Issue(
                    id=vulnerability.id,
                    priority_score=vulnerability.priorityScore,
                    severity=vulnerability.severity)
                for issue_fix_id in remediation[1]['vulns']
                for vulnerability in project_vulns
                if vulnerability.id == issue_fix_id
            ]

            return new_fix

        project_upgrades = project.remediation['upgrade']
        project_vulns = project.vulnerabilities

        new_agg_proj_issues = ProjectIssues()
        new_agg_proj_issues.project_id = project.id
        new_agg_proj_issues.fixes = [
            map_remediation_to_fix(remediation, project_vulns) for remediation in project_upgrades.items()]

        self.agg_proj_issues.issues=new_agg_proj_issues













