import json
import os
import click
import snyk as s

from dataclasses import asdict

from cli import allowed_projects
from helpers.click.click_outputs import output_info
from helpers.snyk.issues_aggregator import IssuesAggregator


class IssueDataCtx(object):
    def __init__(self,orgid, api_token, project, output_file):
        self.orgid = orgid
        self.api_token = api_token
        self.project = project
        self.output_file = output_file


@click.group()
def snyk_agg_fixes():
    pass


@snyk_agg_fixes.command()
@click.option("-o", "--orgid", required=True)
@click.option("-a", "--api-token", required=True)
@click.option("-p", "--project", required=False)
@click.option("-d", "--output-directory")
@click.pass_context
def generate_issues_data(ctx, orgid, api_token, project, output_directory):

    # set the context object for later
    ctx.obj = IssueDataCtx(orgid, api_token, project, output_directory)

    output_info(f'ORGID: {orgid}')
    output_info(f'PROJECT: {project}')

    output_info('---------------------------------------------------------')
    output_info(f'Gathering issues for organization with id: {orgid}')
    output_info(f'Gathering issues for project with id: {project}')
    output_info('---------------------------------------------------------')

    snyk = s.SnykClient(api_token)
    snyk_org = snyk.organizations.get(orgid)

    projects = [snyk_org.projects.get(project)] if project is not None else snyk_org.projects.all()

    issues_aggregator = IssuesAggregator()

    [
        issues_aggregator.aggregate_new_issues(project)
        for project in projects
    ]

    dest_file = output_directory if output_directory else f'{os.getcwd()}/results.json'

    output_info(f'Writing file to {dest_file}')

    with open(dest_file, 'w') as f:
        f.write(json.dumps(asdict(issues_aggregator.agg_proj_issues)))
        output_info(f'File saved at {dest_file}')


if __name__ == '__main__':

    # run local tests here
    generate_issues_data([
        '--orgid','<ORG>',
        '--api-token','<TOKEN>',
        '--project','<PROJECT>',
        '--output-file', None
    ])










