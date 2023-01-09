from account_validator import AccountValidator 
from rich.table import Table, Column
from rich.console import Console
from rich import box


def email_slicer(email):
     
    if AccountValidator().email_regex(email):
        username = email[:email.find('@')] 
        domain_name = email[email.find('@')+1:]
        return username, domain_name
    else:
        return '{} is invalid'.format(email)

if __name__ == '__main__':
    email_address = input('[+] Enter email: ')
    check = email_slicer(email_address) 
    if type(check) == tuple:
        username, domain_name = email_slicer(email_address)

        console = Console()
        table = Table(Column(header='username', justify='right'),
                    Column(header='domain name', justify='right'),
                    title='Email Information',
                    box=box.ASCII_DOUBLE_HEAD)
                
        table.add_row(username, domain_name)
        console.print(table) 
    else:
        print(check)
