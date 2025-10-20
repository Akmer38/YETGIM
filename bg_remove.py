from rembg import remove

input_path = "lion.jpg"
output_path = "lion_bg_no.jpg"

with open(input_path, "rb") as i:
    with open( output_path, "wb") as o:
        input_data = i.read()
        output_data = remove(input_data)
        o.write(output_data)