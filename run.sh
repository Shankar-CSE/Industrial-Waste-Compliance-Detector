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


if [ ! -f "data/raw_data.csv" ]; then
    echo "⚡ Training dataset not found. Creating..."
    python datasetMaker/training_dataset_maker.py


else
    echo "✅ Training dataset already exists."
fi

if [ ! -f "data/preprocessed_data.csv" ]; then
    echo "⚡ Preprocessed dataset not found. Creating..."
    python datasetMaker/preprocessing.py


else
    echo "✅  preprocessed dataset already exists."
fi

if [ ! -f "model/waste_decomposition_model.pkl" ]; then
    echo "⚡ Model not found. Creating..."
    python Training_model/training.py


else
    echo "✅ Model already exists."
fi




# Check and run training dataset maker
if [ ! -f "data/waste_decomposition_with_target.csv" ] || [ ! -f "data/waste_decomposition_without_target.csv" ]; then
    echo "⚡ Testing dataset not found. Creating..."
    python datasetMaker/testing_dataset_maker.py
else
    echo "✅ Testing dataset already exists."
fi



echo "🧪 Starting Testing..."
python Testing_model/testing.py