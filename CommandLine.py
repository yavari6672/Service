'''This module is for command line management'''
import click,Service,sh,os



@click.command(Service.__doc__)
@click.version_option(version=Service.service_version,
                      prog_name=Service.service_name)
@click.option('--verbose', is_flag=True, help="Print more output")
@click.option('--start-service', is_flag=True, help="Starting service")
def show_command(verbose,start_service):
     click.echo(Service.__doc__)
     if verbose:
         pass
     elif start_service:
         os.system('nameko run Service --config config.yaml')
         

    
