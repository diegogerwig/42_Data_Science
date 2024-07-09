all: init

start:
	@echo "🟢 Starting Docker"
	docker-compose up -d
	# docker exec -it data_science_postgres psql -U postgres -c '\du'

restart:
	@echo "🟢 Restarting Docker"
	docker-compose restart

stop:
	@echo "🔴 Stopping Docker"
	docker-compose down

init:
	@echo "🟢 Starting Docker"
	docker-compose up -d --remove-orphans
	@echo "⏳ Waiting for Postgres to be ready..."
	@while ! docker exec postgres pg_isready -h localhost -p 5432; do sleep 1; done
	@echo "🔄 Postgres is ready"
	docker exec -i postgres sed -i 's/trust/md5/g' /var/lib/postgresql/data/pg_hba.conf
	docker exec -it postgres bash -c "psql -U dgerwig -d piscineds -h localhost -W"
	# docker exec -it postgres bash
	# docker exec -i pgadmin bash -c "cat /scripts/create_connection.sql | psql -h postgres -U postgres"
	# docker exec -it data_science_postgres sed -i 's/trust/md5/g' /var/lib/postgresql/data/pg_hba.conf
	# docker exec -i pgadmin bash -c "psql -h postgres -U dgerwig -d piscineds -f /scripts/create_connection.sql"

clean:
	@echo "🟡 Cleaning files & dir"
	@rm -rf */__pycache__
	@rm -rf ./*.csv
	@rm -rf ./pgadmin
	@rm -rf ./postgres_data

fclean: stop clean
	@echo "🟡 Cleaning Docker (docker system prune -af)"
	@ docker system prune -af

re:	fclean all

phony: all clean fclean re start restart stop init
