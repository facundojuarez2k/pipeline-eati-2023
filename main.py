import os

BUILD_DIR = os.path.join(os.getcwd(), "build")
FILE_PATH = os.path.join(BUILD_DIR, "index.html")

HTML_CONTENT = '''<!DOCTYPE html >
<html lang = "es" >
   <head >
        <meta charset = "UTF-8" >
        <meta name = "viewport" content = "width=device-width, initial-scale=1.0" >
        <meta http-equiv = "X-UA-Compatible" content = "ie=edge" >
        <title > HTML 5 Boilerplate < /title >
    </head >
    <body >
        <h1>Test pipeline</h1>
    </body >
</html >'''


def main():
    # Create build directory
    if not os.path.exists(BUILD_DIR):
        os.mkdir(BUILD_DIR)
    # Create HTML file
    with open(FILE_PATH, "w") as fp:
        fp.write(HTML_CONTENT)
        pass
