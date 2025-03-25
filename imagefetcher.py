import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FetchImageFromCache:
    """
    This code is created with help of Gemini 2.0 pro Experimental.
    Fetches and reconstructs image data from Chrome cache files.
    """
    SIGNATURES = {
        "jpeg": (b"\xFF\xD8", b"\xFF\xD9"),  # JPEG Start & End
        "png": (b"\x89PNG\r\n\x1A\n", b"IEND\xAE\x42\x60\x82"),  # PNG Start & End
        "gif": (b"GIF89a", None),  # GIF Start, no definite end but works per file
        "webp": (b"RIFF", b"WEBP")  # WebP container format
    }

    def __init__(self, cache_dir: str, output_dir=None):
        """
        Initializes the FetchImageFromCache class.

        Args:
            cache_dir (str, optional): The directory containing the Chrome cache.
                Defaults to the standard Chrome cache directory if None.
            output_dir (str, optional): The directory to save extracted images.
                Defaults to "extracted_images" in the current directory if None.
        """

        self.cache_dir = cache_dir
        if output_dir is None:
            self.output_dir = "extracted_images"
        else:
            self.output_dir = output_dir

        os.makedirs(self.output_dir, exist_ok=True)
        logging.info(f"Output directory set to: {self.output_dir}")
        if not os.path.exists(self.cache_dir):  # Check cache directory existence here.
            logging.error(f"Cache directory not found: {self.cache_dir}")
            raise FileNotFoundError(f"Cache directory does not exist: {self.cache_dir}")



    def find_images_in_cache(self):
        """
        Finds and extracts images from the specified cache directory.
        """
        image_count = 0
        try:
            # Iterate over files in the cache directory
            for file_name in os.listdir(self.cache_dir):
                file_path = os.path.join(self.cache_dir, file_name)

                # Skip directories and focus on cache files only
                if os.path.isfile(file_path):
                    try:
                        with open(file_path, "rb") as file:
                            file_data = file.read()

                            # Search for each image format in the file data
                            for img_format, (start_marker, end_marker) in self.SIGNATURES.items():
                                start_index = 0
                                while True:
                                    # Find the start marker for the image format
                                    start_index = file_data.find(start_marker, start_index)
                                    if start_index == -1:
                                        break  # No more images of this format in the file

                                    if img_format == "webp":
                                        # For WebP, ensure "WEBP" follows "RIFF" to confirm the image
                                        if file_data[start_index+8:start_index+12] != b"WEBP":
                                            start_index += len(start_marker)
                                            continue

                                    # Define end index based on end marker, if available
                                    if end_marker:
                                        end_index = file_data.find(end_marker, start_index)
                                        if end_index == -1:
                                            # logging.warning(f"Malformed or incomplete {img_format} in {file_name}") # Removed to make concise output
                                            start_index += len(start_marker)  # search from next byte
                                            continue  # Malformed or incomplete image
                                        end_index += len(end_marker)
                                    else:
                                        # For formats without a clear end marker, we may use a fixed length, after initial bytes
                                        end_index = start_index + 1024  # Example, adjust as needed

                                    # Extract and save the image
                                    image_data = file_data[start_index:end_index]
                                    output_path = os.path.join(self.output_dir, f"image_{image_count}.{img_format}")
                                    try:
                                        with open(output_path, "wb") as img_file:
                                            img_file.write(image_data)
                                        logging.info(f"Extracted {img_format.upper()} image to {output_path}")
                                        image_count += 1
                                    except Exception as e:
                                        logging.error(f"Error writing image {image_count}: {e}")

                                    # Move the start index forward to search for additional images
                                    start_index = end_index
                    except Exception as e:
                        logging.error(f"Error reading file {file_path}: {e}")
                #else: # Removed to make concise output
                    #logging.debug(f"Skipping directory: {file_path}")
        except FileNotFoundError:
            logging.error(f"Cache directory not found: {self.cache_dir}")
            return  # Exit the function if the cache directory does not exist.
        except OSError as e:
            logging.error(f"Error accessing cache directory: {self.cache_dir} - {e}")
            return # Exit if OS error
        logging.info("Image extraction complete.")