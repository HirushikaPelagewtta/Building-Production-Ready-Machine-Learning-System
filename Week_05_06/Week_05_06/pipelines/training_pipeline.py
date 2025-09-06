import os
import sys
import logging
import pandas as pd
import joblib
from typing import Dict, Any, Tuple, Optional
from data_pipeline import data_pipeline
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))


from model_training import ModelTrainer
#from model_evaluation import ModelEvaluator
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from config import get_model_config
logging.basicConfig(level=logging.INFO, format=
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# def training_pipeline(
#         data_path: str='data/raw/ChurnModelling.csv', 
#         modelparams: Optional[Dict[str, Any]] = None, 
#         test_size: float=0.2, 
#         random_state: int = 42,
#         model_path: str='artifacts/models/random_forest_cv_model.joblib'
# ):

print("Hello world")