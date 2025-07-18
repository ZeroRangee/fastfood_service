


ENVIRONMENT=${1:-dev}


cp ".env.$ENVIRONMENT" .env


podman-compose up --build