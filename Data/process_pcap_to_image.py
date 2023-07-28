import os
import numpy as np
from PIL import Image
from tqdm import tqdm

class PcapToImageConverter:
    def pcap_to_image(self, pcap_file_path, output_file_path):
        try:
            with open(pcap_file_path, "rb") as pcap_file:
                packets = pcap_file.read()  # Assuming PCAP file format

                # Stack the bytes of each packet
                stacked_bytes = np.frombuffer(packets, dtype=np.uint8)

                # Calculate the dimensions of the image
                num_pixels = stacked_bytes.shape[0]
                num_cols = int(np.ceil(np.sqrt(num_pixels)))  # Calculate the number of columns based on square root
                                                            # By taking the square root of the total number of pixels
                                                            # you can approximate the dimensions that will result in a square image when reshaped.

                # Handle the case when num_cols is zero or very close to zero
                if num_cols == 0:
                    print(f"Skipping {pcap_file_path} - Empty or corrupted pcap file.")
                    return

                num_rows = int(np.ceil(num_pixels / num_cols))  # Calculate the number of rows

                # Pad the stacked bytes with zeros to match the dimensions of the image
                stacked_bytes = np.pad(stacked_bytes, (0, num_rows * num_cols - num_pixels), mode='constant')

                # Reshape the stacked bytes into a 2D image representation
                image = stacked_bytes.reshape((num_rows, num_cols))

                # Convert the image array to a PIL Image object
                image_gray = Image.fromarray(image, mode="L")  # Use "L" mode for grayscale images

                # Convert the grayscale image to RGB format
                image_rgb = image_gray.convert("RGB")

                # Resize the image to 128x128 while maintaining aspect ratio
                image_resized = image_rgb.resize((128, 128))

                # Save the RGB image as a file
                image_resized.save(output_file_path)

        except Exception as e:
            print(f"An error occurred while processing {pcap_file_path}: {e}")


    def find_folders(self, directory_path):
        folders = []

        for root, dirs, files in os.walk(directory_path):
            if not dirs:  # Check if there are no subdirectories
                folder_path = os.path.abspath(root)
                folders.append(folder_path)

        return folders

    def convert_raw_to_processed(self, path):
        parts = path.split(os.sep)
        try:
            index = parts.index("Raw")
        except ValueError:
            return path

        parts[index] = "Processed"
        new_path = os.sep.join(parts)
        return new_path

    def process_raw_data(self, input_folder, output_folder):
        folders = self.find_folders(input_folder)

        for folder in folders:
            output_dir = self.convert_raw_to_processed(folder)
            os.makedirs(output_dir, exist_ok=True)

            for filename in tqdm(os.listdir(folder)):
                pcap_file_path = os.path.join(folder, filename)

                if os.path.isfile(pcap_file_path):
                    output_file_path = os.path.join(output_dir, f"{filename}.png")
                    # Conversion process and saving the image
                    self.pcap_to_image(pcap_file_path, output_file_path)


if __name__ == "__main__":
    input_folder = "C:\\Users\\alexk\\sensor_pcap_classification\\Data\\Raw" #Enter input folder name
    output_folder = "C:\\Users\\alexk\\sensor_pcap_classification\\Data\\Processed" #Enter output folder name

    converter = PcapToImageConverter()
    converter.process_raw_data(input_folder, output_folder)
