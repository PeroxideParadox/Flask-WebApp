#just bcuz of __init__.py as we have studies that it initializes a python package in any folder 
#helps for importing 
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

#debug=true here as we want to reflect the changes here 