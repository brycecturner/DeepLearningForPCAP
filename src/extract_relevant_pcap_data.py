import pyshark
import tensorflow as tf

from ip_metadata import *

def extract_relevant_DNS_pcap_data(pcap_file, max_packets = None):
    cap = pyshark.FileCapture(pcap_file, use_json = True, include_raw=True)

    packet_count = 0

    all_pkt_tensors = []
    all_transport_layers = []
    all_lengths = []
    src_ip = []
    dest_ip =[]

    for packet in cap:
        
        if 'IP' in packet and 'DNS' in packet:
    
            packet_tensor = tf.io.decode_raw(packet.get_raw_packet(), out_type = tf.uint8)
            transport_layer_str= packet.transport_layer

            all_pkt_tensors.append(packet_tensor)
            all_transport_layers.append(transport_layer_str)
            all_lengths.append(packet.length)
            src_ip.append(packet.ip.src)
            dest_ip.append(packet.ip.dst)
            packet_count += 1
        
        if max_packets is not None:
            if packet_count >= max_packets:
                break


    # Tuning Raw-Packet Tensors to ensure same size 
    max_length = (max(all_lengths))
    # all_padded_tensors = [tf.pad(i, paddings = [[0, max_length - tf.shape(i)[0]]]) for i in all_pkt_tensors]

    # pcap_tensor = tf.stack(all_padded_tensors, axis=0)
    
    cap.close()

    return all_pkt_tensors, max_length, all_transport_layers, src_ip, dest_ip

if __name__ == "__main__":
    test_data = "D:\\Projects\\DeepLearningForPCAP\\data\\isot_app_and_botnet_dataset\\all_filtered_dns\\init_dns_only.pcap"
    tns, layers, _, _ = extract_relevant_DNS_pcap_data(test_data)

    print(layers[0:10])
    print(tns.shape)