# Import the SyntheticDataGenerator class from the appropriate file in the package
from app.synthetic_data_generator.src.data_generator import SyntheticDataGenerator

# Instantiate the generator object, setting a random seed to ensure reproducibility
generator = SyntheticDataGenerator(seed=42)

# Use the generator to create a synthetic dataset
# Parameters:
# - 2 continuous features (numeric data)
# - 1 categorical feature (e.g., discrete categories)
# - 1000 samples in total
# - Include a time-series feature (e.g., a sequence of data over time)
df = generator.create_synthetic_dataset(
    continuous_features=2,  # Number of continuous (numeric) features
    categorical_features=1,  # Number of categorical (discrete) features
    num_samples=1000,  # Total number of samples (rows)
    include_time_series=True  # Include a time-series feature in the dataset
)

# Add noise to the generated dataset to make it more realistic
# Parameters:
# - continuous_noise_level: the amount of noise to add to the continuous features (5%)
# - categorical_noise_level: the amount of noise to add to the categorical features (10%)
noisy_df = generator.add_noise(
    df,  # The original synthetic dataset
    continuous_noise_level=0.05,  # 5% noise for continuous features
    categorical_noise_level=0.1  # 10% noise for categorical features
)

# Display the first few rows of the noisy dataset for inspection
print(noisy_df.head())
