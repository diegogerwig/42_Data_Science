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
	docker stop $(docker ps -aq) || true

init:
	@echo "🟢 Starting Docker"
	docker-compose up -d --remove-orphans
	@echo "⏳ Waiting for Postgres to be ready..."
	@while ! docker exec postgres pg_isready -h localhost -p 5432; do sleep 1; done
	@echo "🔄 Postgres is ready"
	@docker exec -di postgres sed -i 's/trust/md5/g' /var/lib/postgresql/data/pg_hba.conf
	@while true; do \
		docker exec -it postgres bash -c "psql -U dgerwig -d piscineds -h localhost -W"; \
		if [ $$? -eq 0 ]; then \
			break; \
		fi; \
	done

clean:
	@echo "🟡 Cleaning files & dir"
	@rm -rf */__pycache__
	@rm -rf ./*.csv
	@rm -rf ./pgadmin
	@rm -rf ./postgres_data

fclean: stop clean
	@echo "🟡 Cleaning Docker (docker system prune -af)"
	@docker rm $(docker ps -aq) || true
	@docker rmi $(docker images -q) || true
	@docker volume rm $(docker volume ls -q) || true
	@docker system prune -af || true

re:	fclean all

phony: all clean fclean re start restart stop init
