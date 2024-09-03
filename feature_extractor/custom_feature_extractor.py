from sklearn.base import BaseEstimator, TransformerMixin
from feature_extractor.opcode_sequence_extraction import opcode_sequence_extraction
class CustomFeatureExtractor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        # Implement your feature extraction logic here
        return self

    #For production
    def transform(self, X):
      # Extract relevant feature (e.g., opcode sequences) from each JSON object
      bytecode = X.get("bytecode", "")  # Extract bytecode from the JSON object
      # Remove '0x' from bytecode
      cleaned_bytecode = bytecode[2:]
      # Create sequence from cleaned bytecode
      opcode_sequence = opcode_sequence_extraction(cleaned_bytecode)
    #   print(opcode_sequence)

      return opcode_sequence