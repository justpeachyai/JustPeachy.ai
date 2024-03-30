import os
import sqlite3
from lancedb import LanceDB 

class Memory:
    def __init__(self, worker_id):
        self.worker_id = worker_id
        self.archival = {
            "vectorDatabase": self.initialize_vector_database()
        }
        self.recall = self.initialize_recall_database()

    def initialize_short_term_memory(self):
        file_path = f"justpeachy/memory/shortTerm/memories/{self.worker_id}.txt"
        with open(file_path, 'w') as file:
            file.write("")  
        return file_path

    def initialize_vector_database(self):
        # Initialize the vector database using LanceDB
        db_path = f"justpeachy/memory/longTerm/databases/arhival_vector_{self.worker_id}.db"
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        vector_db = LanceDB(db_path)
        return vector_db # Return the LanceDB instance

    def initialize_recall_database(self):
        # Define the path for the SQLite database
        db_path = f"justpeachy/memory/longTerm/databases/recall_{self.worker_id}.db"
        # Ensure the directory exists
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create the actions table
        cursor.execute('''CREATE TABLE IF NOT EXISTS actions (
                            _id TEXT PRIMARY KEY,
                            type TEXT NOT NULL,
                            role TEXT,
                            content TEXT,
                            created_at DATETIME NOT NULL,
                            conversation_id TEXT,
                            environment_id TEXT,
                            feedback TEXT
                        );''')
        conn.commit()
        conn.close()

        return db_path
