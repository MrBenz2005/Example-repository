from PIL import Image, ImageDraw


def create_image_with_kert(width, height, kert_x, kert_y, kert_size):
    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.ellipse((kert_x, kert_y, kert_x + kert_size, kert_y + kert_x), fill='red')
    return img

frames = []
x, y = 0, 0
for i in range(10):
    new_frame = create_image_with_kert(400, 400, x, y, 40)
    frames.append(new_frame)
    x += 40
    y += 40

# Save into a GIF file that loops forever
frames[0].save('moving_ball.gif', format='GIF', append_images=frames[1:], save_all=True, duration=100, loop=0)