from app import create_app

app = create_app()

if __name__ == '__main__':
    from config import Config
    app.run(debug=Config.DEBUG, port=Config.PORT)
