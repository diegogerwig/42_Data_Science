# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dgerwig- <dgerwig-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/02 14:09:10 by dgerwig-          #+#    #+#              #
#    Updated: 2024/03/15 20:29:16 by dgerwig-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

all: start init_docker

start:
	@echo "🟢 Starting Docker"
	docker-compose up -d

restart:
	@echo "🟢 Restarting Docker"
	docker-compose restart

stop:
	@echo "🔴 Stopping Docker"
	docker-compose down

init_docker:
	docker exec -i pgadmin psql -h postgres -U postgres < /scripts/create_connection.sql
	docker exec -it data_science_postgres sed -i 's/trust/md5/g' /var/lib/postgresql/data/pg_hba.conf
	docker exec -it data_science_postgres bash

clean:
	@echo "🟡 Cleaning files & dir"
	rm -rf */__pycache__
	rm -rf ./*.csv
	rm -rf ./pgadmin
	rm -rf ./postgres_data

fclean: stop clean
	@echo "🟡 Cleaning Docker"
	docker system prune -af

re:	fclean all

phony: all clean fclean re start restart stop init_docker