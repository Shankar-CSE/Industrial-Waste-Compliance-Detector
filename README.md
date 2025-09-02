# Industrial Waste Compliance Detector

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.9%2B-brightgreen.svg)

A machine learning project to detect whether industrial facilities have the necessary waste decomposition systems, ensuring environmental compliance.



## 🛠️ Tech Stack

- Python
- (Potentially) Scikit-learn for data analysis

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- `pip` package manager
- `bash` shell


### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/Shankar-CSE/Industrial-Waste-Compliance-Detector.git
    cd Industrial-Waste-Compliance-Detector
    ```

2.  **Running**
    Open bash shell and move to the diretory 
    then run this:
    ```
    bash run.sh
    ```
    or
    ```
    ./run.sh
    ```


   

## 🏃 manual testing 

create venv and install requirements
```sh
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```

To Create training Dataset  

```sh
python training_dataset_maker.py
```

For preprocess the data
```sh
python preprocess.py
```
To  train The Model  

```sh
python training.py
```
or directly run the training.ipynb file

To Create training Dataset  

```sh
python testing_dataset_maker.py
```

To Test The Model  

```sh
python testing.py
```
or directly run the testing.ipynb file


*(Please update current directory to the root directory.)*

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes and commit them (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/your-feature-name`).
5.  Open a Pull Request.

Please make sure to update tests as appropriate.


