import logging
from argh import arg

from pnc_cli import utils
from pnc_cli.swagger_client import RunningbuildrecordsApi

import cli_types
import pnc_cli.user_config as uc

running_api = RunningbuildrecordsApi(uc.user.get_api_client())


@arg("-p", "--page-size", help="Limit the amount of BuildRecords returned")
@arg("-s", "--sort", help="Sorting RSQL")
def list_running_builds(page_size=200, sort=""):
    """
    List all RunningBuilds
    """
    response = utils.checked_api_call(running_api, 'get_all', page_size=page_size, sort=sort)
    if response:
        return response.content


@arg("id", help="ID of the RunningBuild to retrieve.", type=cli_types.existing_running_build)
def get_running_build(id):
    """
    Get info about a specific RunningBuild
    """
    response = utils.checked_api_call(running_api, 'get_specific', id=id)
    if response:
        return response.content
