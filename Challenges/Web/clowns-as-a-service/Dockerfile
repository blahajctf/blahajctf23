# docker build -t clowns-as-a-service .
# docker run -d -p 2345:80 clowns-as-a-service
FROM php:7.2-apache
COPY src/ /var/www/html/
#COPY src/000-default.conf /etc/apache2/000-default.conf
COPY src/000-default.conf /etc/apache2/sites-available/000-default.conf
COPY src/ports.conf /etc/apache2/ports.conf
RUN addgroup --gid 1001 nonroot && \
    adduser --uid 1001 --gid 1001 --disabled-password --gecos "" nonroot && \
    echo 'nonroot ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers
USER 1001
EXPOSE 8000
CMD ["apache2-foreground"]