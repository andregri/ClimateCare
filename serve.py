from waitress import serve
import app
import os



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    serve(app.create_app(), host='0.0.0.0', port=port)