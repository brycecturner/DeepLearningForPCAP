import sys

sys.path.append("/usr/local/lib/python3.10/dist-packages/")
sys.path.append("/content/drive/MyDrive/DeepLearningForPcap/src")


from extract_relevant_pcap_data import *
from ip_metadata import *

import numpy as np
import os

filtered_pcap_directory = "/content/drive/MyDrive/DeepLearningForPcap/data/isot_app_and_botnet_dataset/all_filtered_dns/"
max_packets = None


save_tensor_location = "/content/drive/MyDrive/DeepLearningForPcap/data/tensors/"

print("CONFIGS --------")
print(f"reading data from dir: {filtered_pcap_directory}")
print(f"using max packet count: {max_packets}")
print(f"saving resulting tesnors to dir: {save_tensor_location}")


print("WORKING ----")
all_files = os.listdir(filtered_pcap_directory)


full_tensor_list = []
transport_layer_list = []
full_src_list = []
full_dest_list = []


print("... extracting packet data ...")
for using_file in all_files:
    print(f"        {using_file}")
    extract_relevant_DNS_pcap_data(filtered_pcap_directory + using_file, max_packets = max_packets)
    
    # tensor_list, max_length, all_transport_layers, src_ip, dest_ip = extract_relevant_DNS_pcap_data(filtered_pcap_directory + using_file, max_packets = max_packets)
    # full_tensor_list = full_tensor_list + tensor_list
    # full_src_list = full_src_list + src_ip
    # full_dest_list = full_dest_list + dest_ip
    # transport_layer_list = transport_layer_list + all_transport_layers


# # Need to add padding in order to combine all transmission-packets into a tensor
# print("... padding packet tensors ...")
# all_length = [i.shape[0] for i in full_tensor_list]
# max_length = max(all_length)

# full_tensor_list = [tf.pad(i, paddings = [[0, max_length - tf.shape(i)[0]]]) for i in full_tensor_list]
# pcap_tensor = tf.stack(full_tensor_list, axis=0)

# print("... one hot encoding transport layer and traffic data ...")
# def one_hot_from_list(the_list):
#     """One Hot Encodes elements ina lsit. returns the one_hot_encoded and the indicies"""
#     all_options = set(the_list)
#     num_options = len(all_options)

#     # Create a mapping from string to numerical indices
#     string_to_index = {string: index for index, string in enumerate(all_options)}

#     # Convert the strings to numerical indices
#     indices = [string_to_index[string] for string in the_list]

#     # Perform one-hot encoding using tf.one_hot
#     one_hot_encoded = tf.one_hot(indices, depth=num_options)

#     return one_hot_encoded, indices


# ## Combine src_ip and dest_ip into single, rename, then one_hot
# traffic_data = [f"{src} -> {dest}" for src, dest in zip(full_src_list, full_dest_list)]


# traffic_one_hot, traffic_indices = one_hot_from_list(traffic_data)
# transport_one_hot, transport_indices = one_hot_from_list(transport_layer_list)

# print("RESULTS----")

# def save_to_numpy(object, file):
#     with open(file, 'wb') as f:
#         np.save(f, object)
#     print(f".... saved {file}")


# save_to_numpy(pcap_tensor.numpy(), save_tensor_location + "pcap_tensor.npy")

# save_to_numpy(np.array(traffic_data), save_tensor_location + "traffic_data.npy")
# save_to_numpy(traffic_one_hot.numpy(), save_tensor_location + "traffic_one_hot.npy")
# save_to_numpy(np.array(traffic_indices), save_tensor_location + "traffic_indices.npy")

# save_to_numpy(np.array(transport_layer_list), save_tensor_location + "transport_layer_list.npy")
# save_to_numpy(transport_one_hot.numpy(), save_tensor_location + "transport_one_hot.npy")
# save_to_numpy(np.array(transport_indices), save_tensor_location + "transport_indices.npy")
