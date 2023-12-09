import pyotp
import typer

from src.utils.utils import stand_by
from src.config.constants import (
    MAIN_USERNAME,
    MAIN_PASSWORD,
    MAIN_PHONENUMBER,
    EMAIL_GOOGLE_APP,
    MAIN_GOOGLE_APP_PASSWORD
)

# from src.config.constants import CHAT_GPT_SECRET_KEY


app = typer.Typer()


@app.command()
def interactive_own_vault():
    """
        Interactive CLI tool to securely store your
        passwords in your own personalized and personal vault
    """

    def __generating_new_random_base32() -> str :
        '''
            ### This function will generate a new random base32.

            ##### ( OBS.: Only use this function if you wanna generate a new random base32 string! )
        '''
        new_random_base32 = pyotp.random_base32()

        return new_random_base32



    def authenticate_with_2fa(username, password):
        master_key = "VYHOZGVCQOUJTSFVE7IRTOG7PJAS36WM"

        code = pyotp.TOTP(master_key)

        typer.echo(code.now())

        user_code = typer.prompt("Enter your code")

        if username.strip() == MAIN_USERNAME and password.strip() == MAIN_PASSWORD and code.verify(user_code.strip()):
            typer.echo("Login successful with 2FA.")
        else:
            typer.echo("Invalid credentials or 2FA code.")

    username = typer.prompt("Enter your username")
    password = typer.prompt("Enter your password")

    authenticate_with_2fa(username, password)



if __name__ == '__main__':
    app()