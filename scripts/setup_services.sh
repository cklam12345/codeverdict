#!/bin/bash
# scripts/setup_services.sh

echo "🚀 Starting CodeVerdict Services..."
echo "⚖️  Where AI Code Stands Trial"

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Create necessary directories
mkdir -p mlruns logs

echo "📦 Starting MLflow Server..."
mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root ./mlruns \
    --host 0.0.0.0 \
    --port 5000 \
    > logs/mlflow.log 2>&1 &

echo "🔍 Starting Argilla Server..."
docker run -d \
    --name codeverdict-argilla \
    -p 6900:6900 \
    -e ARGILLA_HOME_PATH=/var/lib/argilla \
    -v $(pwd)/argilla_data:/var/lib/argilla \
    argilla/argilla-server:latest > logs/argilla.log 2>&1

echo "⏳ Waiting for services to start..."
sleep 15

echo "✅ CodeVerdict Services Started Successfully!"
echo ""
echo "📊 MLflow UI: http://localhost:5000"
echo "👥 Argilla UI: http://localhost:6900"
echo "🔧 CodeVerdict API: http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"
echo ""
echo "💡 To start evaluation: python -m codeverdict.api.main"