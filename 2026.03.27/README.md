
1. Файл docker-compose.yaml

![It works](#TODO)


2. Настройка локального домена

Необходимо http://gitlab.local прописать в hosts. Использую macOS.
В терминале поправить файл hosts (потребуется пароль администратора):

```Bash
sudo nano /etc/hosts
```
Добавить в самый конец строку:

```Plaintext
127.0.0.1 gitlab.local
```

3. Запуск сервера

```Bash
docker compose up -d
```

Получение первоначального пароля для входа:
```Bash
docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password
```

Перейти на URL: 
http://gitlab.local, логин — root, пароль — тот, что выдала команда выше.

4. Подключение GitLab Runner
*token - получен из GitLab UI

```Bash
docker exec -it gitlab-runner gitlab-runner register \
  --url "http://gitlab.local" \
  --token "******" \
  --executor "docker" \
  --docker-image alpine:latest \
  --description "Local Shared Runner" \
  --clone-url "http://gitlab.local" \
  --docker-network-mode "host"
```

