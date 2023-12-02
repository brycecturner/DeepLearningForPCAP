from extract_relevant_pcap_data import *
from ip_metadata import *

import os

filtered_pcap_directory = "D:\\Projects\\DeepLearningForPCAP\\data\\isot_app_and_botnet_dataset\\all_filtered_dns\\"
max_packets = None

all_files = os.listdir(filtered_pcap_directory)
#print(all_files)

full_tensor_list = []
full_src_list = []
full_dest_list = []

for using_file in all_files:
    print(using_file)
    tensor_list, max_length, all_transport_layers, src_ip, dest_ip = extract_relevant_DNS_pcap_data(filtered_pcap_directory + using_file, max_packets = max_packets)
    full_tensor_list = full_tensor_list + tensor_list
    full_src_list = full_src_list + src_ip
    full_dest_list = full_dest_list + dest_ip



# Need to add padding in order to combine all packets into a tensor

all_length = [i.shape[0] for i in full_tensor_list]
max_length = max(all_length)

all_padded_tensors = [tf.pad(i, paddings = [[0, max_length - tf.shape(i)[0]]]) for i in full_tensor_list]
pcap_tensor = tf.stack(all_padded_tensors, axis=0)


## Combine src_ip and dest_ip into single, rename, then one_hot
traffic_data = [f"{src} -> {dest}" for src, dest in zip(full_src_list, full_dest_list)]
print(traffic_data[:20])

all_traffic_options = set(traffic_data)
num_traffic_options = len(all_traffic_options)

# Create a mapping from string to numerical indices
string_to_index = {string: index for index, string in enumerate(all_traffic_options)}

# Convert the strings to numerical indices
indices = [string_to_index[string] for string in traffic_data]

# Perform one-hot encoding using tf.one_hot
one_hot_encoded = tf.one_hot(indices, depth=num_traffic_options)

print(one_hot_encoded)