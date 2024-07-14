# DATA SCIENCE -> DATA ENGINEER

---

##  EX 00  

Open a terminal

Run: 
    make

Execute:
    psql -U dgerwig -d piscineds -h localhost -W

    exit: \q
    list db: \l
    list tables: \dt

Checking changes: 'trust' for 'md5' in pg_hba.conf
    vim /var/lib/postgresql/data/pg_hba.conf

---

##  EX 01 

Open a new terminal to visualize docker logs:
    docker logs -f pgadmin

Open a window in your browser:
    http://localhost:5050

Register a SERVER in pgAdmin:
    Server / Register / Server 
        General:
            Name
        Connection:
            Host name: postgres (the name of docker service)
            Port: 5432
            Maintenance db: piscineds
            Username: POSTGRES_USER (data from docker-compose)
            Password: POSTGRES_PASSWORD (data from docker-compose)

---

##  EX 02  

Open another terminal

Active virtual environment

Execute:
    python3 ex02/table.py

---

##  EX 03  

Execute:
    python3 ex03/automatic_table.py

---

##  EX 04  

Execute:
    python3 ex04/items_table.py

---

### INFO   

Config data base in pgAdmin:
    https://www.youtube.com/watch?v=uKlRp6CqpDg
