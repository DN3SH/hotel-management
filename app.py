import streamlit as st
from PIL import Image
import subprocess
import webbrowser
import io

def main():
    st.title("Identity Card Scanner")

    st.write("Please capture images of the front and back sides of your identity card.")

    # Capture front side image
    front_image = capture_image("Front Side")

    # Capture back side image
    back_image = capture_image("Back Side")

    # Display captured images and save them
    if front_image and back_image:
        st.image(front_image, caption="Front Side", use_column_width=True)
        st.image(back_image, caption="Back Side", use_column_width=True)

        # Run model.py after capturing images
        subprocess.run(["python", "main.py"])  # Replace with the correct filename

        # Open details.html in the default web browser
        webbrowser.open("details.html")  # Replace with the correct filename

def capture_image(side):
    st.write(side + ":")
    img_file_buffer = st.camera_input(f"Take a picture of {side}")

    if img_file_buffer is not None:
        # To read image file buffer with Pillow (PIL):
        bytes_data = img_file_buffer.getvalue()
        pil_img = Image.open(io.BytesIO(bytes_data))

        # Determine the filename based on the side
        filename = "front.png" if side.lower() == "front side" else "back.png"

        # Save the captured image with the appropriate filename
        pil_img.save(filename)

        st.image(pil_img, caption=side + " Side", use_column_width=True)

        return pil_img

if __name__ == "__main__":
    main()
