all:
	docker compose up --build -d

clean:
	docker compose down

fclean:
	docker compose down -v
	docker system prune -f
	docker image prune -af

re: fclean all