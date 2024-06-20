#!/bin/bash
# entrypoint.sh

# Load environment variables from the specified .env file
if [ -f "$ENV_FILE" ]; then
    export $(grep -v '^#' "$ENV_FILE" | xargs)
fi

#True or False
echo "DJANGO_DEBUG: $DJANGO_DEBUG"

# Make migrations
echo "Making migrations..."
python manage.py makemigrations


# Run database migrations
echo "Running migrations..."
python manage.py migrate

# Run collectstatic if not in debug mode
if [ "$DJANGO_DEBUG" != "True" ]; then
    echo "Collecting static files..."
    python manage.py collectstatic --noinput
fi

# Run compress if COMPRESS_OFFLINE is set to True
if [ "$COMPRESS_OFFLINE" = "True" ]; then
    echo "Compressing files..."
    python manage.py compress
fi

# Check the DEBUG environment variable and start the appropriate server
if [ "$DJANGO_DEBUG" = "True" ]; then
    exec python manage.py runserver 0.0.0.0:8000
else
    exec gunicorn JMW.wsgi -b 0.0.0.0:8000
fi
