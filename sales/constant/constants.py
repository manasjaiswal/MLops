import os
from datetime import datetime


def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

ROOT_DIR=os.getcwd()
CONFIG_DIR="config"
CONFIG_FILE_NAME="config.yaml"
CONFIG_FILE_PATH=os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

CURRENT_TIME_STAMP=get_current_time_stamp()

#LOGdirectory_name_key
LOG_DIR="sales_logs"

#Trainingpipeline_related_constants
TRAINING_PIPELINE_CONFIG_KEY="trainer_pipeline_config"
TRAINING_PIPELINE_NAME="pipeline_name"
TRAINING_PIPELINE_ARTIFACT_DIR="artifact_dir"

#DataIngestion_related_constants
DATA_INGESTION_CONFIG_KEY="data_ingestion_config"
DATA_INGESTION_DATA_DIR="data_dir"
DATA_INGESTION_ARTIFACT_DIR="data_ingestion"
DATA_INGESTION_TRAIN_NAME_KEY="train_file_name"
DATA_INGESTION_TEST_NAME_KEY="test_file_name"
DATA_INGESTION_INGESTED_TRAIN_DIR="ingested_train_dir"
DATA_INGESTION_INGESTED_TEST_DIR="ingested_test_dir"
DATA_INGESTION_INGESTED_DIR="ingested_dir"

#DataValidation_related_constants
DATA_VALIDATION_CONFIG_KEY="data_validation_config"
DATA_VALIDATION_SCHEMA_DIR="schema_dir"
DATA_VALIDATION_SCHEMA_FILE_NAME_KEY="schema_file_name"
DATA_VALIDATION_REPORT_FILE_NAME="report_file_name"
DATA_VALIDATION_REPORT_PAGE_FILE_NAME="report_page_file_name"
DATA_VALIDATION_ARTIFACT_DIR="datavalidation"

#DataTranformation_related_constants
DATA_TRANSFORMATION_CONFIG_KEY="data_transformation_config"
DATA_TRANSFORMATION_ARTIFACT_DIR="datatransformation"
DATA_TRANSFORMATION_TRANSFORMED_DIR="transformed_dir"
DATA_TRANSFORMATION_TRANSFORMED_TRAIN_DIR="transformed_train_dir"
DATA_TRANSFORMATION_TRANSFORMED_TEST_DIR="transformed_test_dir"
DATA_TRANSFORMATION_PREPROCESSING_DIR="preprocessing_dir"
DATA_TRANSFORMATION_PREPROCESSING_FILE_NAME_KEY="preprocessed_object_file_name"

#ModelTrainer_related_constants
MODEL_TRAINER_CONFIG_KEY="model_trainer_config"
MODEL_TRAINER_ARTIFACT_DIR="modeltraining"
MODEL_TRAINER_TRAINED_MODEL_DIR="trained_model_dir"
MODEL_TRAINER_MODEL_FILE_NAME_KEY="model_file_name"
MODEL_TRAINER_BASE_ACCURACY_KEY="base_accuracy"
MODEL_TRAINER_MODEL_CONFIG_DIR="model_config_dir"
MODEL_TRAINER_MODEL_CONFIG_FILE_NAME_KEY="model_config_file_name"


#ModelEvaluation related constants
MODEL_EVALUATION_CONFIG_KEY="model_evaluation_config"
MODEL_EVALUATION_ARTIFACT_DIR="modelevaluation"
MODEL_EVALUATION_FILE_NAME="model_evaluation_file_name"

#ModelPusherConfig
MODEL_PUSHER_CONFIG_KEY="model_pusher_config"
MODEL_PUSHER_MODEL_EXPORT_DIR="model_export_dir"

#schemarelated constants
SCHEMA_CONFIG_DATA_TYPES_KEY="DataTypes"
SCHEMA_CONFIG_CATEGORICAL_COLUMNS_KEY="categorical_columns"
SCHEMA_CONFIG_CATEGORIES_KEY="categories"
SCHEMA_CONFIG_NUMERICAL_COLUMNS_KEY="numerical_columns"
SCHEMA_CONFIG_TARGET_COLUMN_KEY="target_column"



#Data transformation Component Related Constants
COLUMN_ITEM_VISIBILITY="Item_Visibility"
COLUMN_ITEM_WEIGHT="Item_Weight"
COLUMN_ITEM_TYPE="Item_Type"
COLUMN_OUTLET_SIZE="Outlet_Size"
COLUMN_ITEM_OUTLET_SALES="Item_Outlet_Sales"
COLUMN_OUTLET_ESTABLISHMENT_YEAR="Outlet_Establishment_Year"
COLUMN_ITEM_IDENTIFIER="Item_Identifier"
COLUMN_FAT_CONTENT="Item_Fat_Content"
COLUMN_OUTLET_LOCATION_TYPE="Outlet_Location_Type"
COLUMN_OUTLET_IDENTIFIER_KEY="Outlet_Identifier"
COLUMN_ITEM_MRP="Item_MRP"
COLUMN_OUTLET_TYPE="Outlet_Type"


#ModelTraining related constants
GRID_SEARCH_KEY="grid_search"
MODULE_KEY="module"
CLASS_KEY="class"
PARAM_KEY="params"
MODEL_SELECTION_KEY="model_selection"
SEARCH_PARA_GRID_KEY="search_param_grid"

TOLERANCE_LIMIT=0.08

#Model evaluation related constants
BEST_MODEL_KEY="best model"
HISTORY_KEY="history"
MODEL_PATH_KEY="model_path"

EXPERIMENT_DIR_NAME="experiment"
EXPERIMENT_FILE_NAME="experiment.csv"


#Classification if need arises, 1 is taken as default
F_BETA_VALUE=1