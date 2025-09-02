echo -e "welcome \n"

chmod +x run.sh

if [ -d "venv" ]; then
    echo -e "venv exists\n"
else
    echo -e "venv does not exist \n"
    python -m venv venv
    echo -e "Activating virtual environment...\n"
    source venv/Scripts/activate
    echo -e "Installing requirements...\n"
    pip install -r requirements.txt
fi


if [ ! -f "data/raw_data.csv" ]; then
    echo -e "⚡ Training Dataset not found. Creating...\n"
    python datasetMaker/training_dataset_maker.py


else
    echo -e "✅ Training dataset already exists.\n"
fi

if [ ! -f "data/processed_data.csv" ]; then
    echo -e "⚡  Preprocessing the dataset...\n"
    python datasetMaker/preprocessing.py


else
    echo -e "✅  preprocessed dataset already exists.\n"
fi

if [ ! -f "model/waste_decomposition_model.pkl" ]; then
    echo -e "⚡ Model not found. Training...\n"
    python Training_model/training.py


else
    echo -e "✅ Model already exists.\n"
fi




# Check and run training dataset maker
if [ ! -f "data/waste_decomposition_with_target.csv" ] || [ ! -f "data/waste_decomposition_without_target.csv" ]; then
    echo -e "⚡ Testing dataset not found. Creating...\n"
    python datasetMaker/testing_dataset_maker.py
else
    echo -e "✅ Testing dataset already exists.\n"
fi



echo -e "🧪 Starting Testing...\n"
python Testing_model/testing.py