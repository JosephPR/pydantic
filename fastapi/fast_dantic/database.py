from sqlmodel import SQLModel, create_engine, Session

# ==========================================
# Database Configuration
# ==========================================

# 1. Define the connection URL. We are using a local SQLite file named 'database.db'.
# If you wanted to use PostgreSQL, you would just change this string!
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# 2. Create the Engine. 
# The Engine is the core interface to the database. "check_same_thread": False is needed 
# for SQLite specifically when used with FastAPI so multiple web requests can access the DB.
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    # This reads all classes that inherit from SQLModel (like Product, Order) 
    # and automatically creates the corresponding SQL tables if they don't exist yet out of thin air!
    SQLModel.metadata.create_all(engine)

def get_session():
    # A Session is a temporary connection to the database. 
    # We yield it here so FastAPI can use it as a "Dependency" in our routes.
    # At the end of the web request, the `with` block closes the connection automatically securely.
    with Session(engine) as session:
        yield session
