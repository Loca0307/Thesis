BASE_URL = 'http://localhost:4567'
API_URL = f"{BASE_URL}/api"
BASE_DIR = dirname(abspath(__file__))
DATABASE = join(BASE_DIR, "tmp", "mock.db")
SCHEMA = join(BASE_DIR, "tmp", "schema.sql")