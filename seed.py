from database import SessionLocal, engine
import models

def seed_db():
    # Only create if empty
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    if db.query(models.Agent).count() == 0:
        print("Seeding agents...")
        agents = [
            models.Agent(name="Alice Smith", expertise="Billing, Refunds, General", capacity=3),
            models.Agent(name="Bob Jones", expertise="Technical, Bug, Crash", capacity=5),
            models.Agent(name="Charlie Brown", expertise="General, Information", capacity=4)
        ]
        db.add_all(agents)
        db.commit()
        print("Agents seeded.")
    else:
        print("Database already contains agents. Skipping seed.")
        
    db.close()

if __name__ == "__main__":
    seed_db()
