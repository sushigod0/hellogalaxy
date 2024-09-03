import numpy as np

def combined_vectors(vec_model,opcode_sequence_list):
  # vec_features = []
  # for sequence in opcode_sequence_list:
  vec_features = np.mean([vec_model.wv[opcode] for opcode in opcode_sequence_list], axis=0)
  # print(opcode_embeddings.shape)

  # combined_feature_vector = np.concatenate(opcode_embeddings)
  # vec_features.append(vec_features)
  return vec_features
# print ("run successful")