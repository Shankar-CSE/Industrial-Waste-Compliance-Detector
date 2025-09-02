echo "welcome"

chmod +x run.sh

if [ -d "venv" ]; then
    echo "venv exists"
else
    echo "venv does not exist"
    python -m venv venv
    echo "Activating virtual environment..."
    source venv/Scripts/activate
    echo "Installing requirements..."
    pip install -r requirements.txt
fi


if [ ! -f "data/waste_decomposition_dataset.csv" ]; then
    echo "⚡ Testing dataset not found. Creating..."
    python datasetMaker/testing_dataset_maker.py

    echo "🚀 Starting Training..."
    python Training_model/training.py

else
    echo "✅ Testing dataset already exists."
fi

# Check and run training dataset maker
if [ ! -f "data/waste_decomposition_with_target.csv" ] || [ ! -f "data/waste_decomposition_without_target.csv" ]; then
    echo "⚡ Training dataset not found. Creating..."
    python datasetMaker/training_dataset_maker.py
else
    echo "✅ Training dataset already exists."
fi



echo "🧪 Starting Testing..."
python Testing_model/testing.py