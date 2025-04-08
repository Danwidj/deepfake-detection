import tensorflow as tf
import pandas as pd
import os

def read_tfrecord(tfrecord_path):
    # Create a dataset from the TFRecord file
    dataset = tf.data.TFRecordDataset(tfrecord_path)
    
    # First, let's examine the first record to understand its structure
    for raw_record in dataset.take(1):
        example = tf.train.Example()
        example.ParseFromString(raw_record.numpy())
        print("Feature keys in the TFRecord:")
        for key in example.features.feature:
            feature = example.features.feature[key]
            # Determine the type of feature
            if feature.HasField('float_list'):
                print(f"{key}: float_list with {len(feature.float_list.value)} values")
            elif feature.HasField('int64_list'):
                print(f"{key}: int64_list with {len(feature.int64_list.value)} values")
            elif feature.HasField('bytes_list'):
                print(f"{key}: bytes_list with {len(feature.bytes_list.value)} values")
        break
    
    return dataset

def convert_tfrecord_to_df(dataset, tfrecord_path):
    data = []
    base_filename = os.path.basename(tfrecord_path)
    
    for raw_record in dataset:
        example = tf.train.Example()
        example.ParseFromString(raw_record.numpy())
        feature_dict = {'filename': base_filename}  # Add filename to each record
        
        for key, feature in example.features.feature.items():
            # Extract values based on feature type
            if feature.HasField('float_list'):
                values = list(feature.float_list.value)
            elif feature.HasField('int64_list'):
                values = list(feature.int64_list.value)
            elif feature.HasField('bytes_list'):
                values = [v.decode() for v in feature.bytes_list.value]
            
            # If it's a single value, store it directly instead of as a list
            if len(values) == 1:
                feature_dict[key] = values[0]
            else:
                feature_dict[key] = values
        
        data.append(feature_dict)
    
    return pd.DataFrame(data)

def main():
    # Use the full path for the input and output files
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tfrecord_path = os.path.join(script_dir, 'eval_features.tfrecord')
    output_csv = os.path.join(script_dir, 'eval_features.csv')
    
    print(f"Reading TFRecord file: {tfrecord_path}")
    dataset = read_tfrecord(tfrecord_path)
    
    print("\nConverting to DataFrame...")
    df = convert_tfrecord_to_df(dataset, tfrecord_path)
    
    print("\nSaving to CSV...")
    df.to_csv(output_csv, index=False)
    print(f"Saved to {output_csv}")
    print("\nFirst few rows of the DataFrame:")
    print(df.head())
    print("\nDataFrame info:")
    print(df.info())

if __name__ == "__main__":
    main() 