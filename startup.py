import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    if os.environ.get('PORT') is None:
        PORT = 5000
    else:
        PORT = os.environ.get('PORT')
        
    app.run(host='0.0.0.0', port=PORT)