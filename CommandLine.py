'''This module is for command line management'''
import click , LoggerService



@click.command(LoggerService.__doc__)

#command --version 
@click.version_option(version=LoggerService.service_version,
                      prog_name=LoggerService.service_name)
@click.option('--verbose', is_flag=True, help="Print more output.")
def show_command(verbose):
     click.echo(LoggerService.__doc__)
     if verbose:
         pass

    
