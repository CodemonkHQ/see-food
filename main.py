import flet
import label_dog


hot_dog_image_path = f"/images/cool_hot_dog.png"


def main(page: flet.Page):
    selected_image = flet.Image(
        height=325,
        width=325,
        src=hot_dog_image_path,
        border_radius=20,
        fit="contain",
    )
    loading_text = flet.Text("",size=20, color="black", weight="bold")

    intro_text1 = flet.Text("See Food", size=24, color="black", weight="bold")
    intro_text2 = flet.Text("We help you to identify hot dogs using our proprietary algorithm,\n"
                       "See Food is built with Python and power of Flet.\n"
                       "\n"
                       "Join our journey to make the world a better place\n", size=13, color=flet.colors.BLUE_GREY_800,
                       weight="w400",
                       )
    
    footer_text= flet.Container(flet.Text("Built with 💕 in India\n",size=13, color=flet.colors.BLUE_GREY_800,
                       weight="w400",) ,padding=16,)

    intro_text = flet.Container(flet.Column(
        [
            intro_text1,
            intro_text2

        ],
        wrap=True,
        tight=True,
        alignment="center",
        horizontal_alignment="start"
    ),
        padding=16,
        width=page.width / 3,
        height=300,
    )

    intro_container = flet.Container(flet.Row(
        [
            flet.Container(
                selected_image
            ),
            intro_text
        ],
        wrap=True,
        tight=True,
        alignment="start",
        vertical_alignment="start"
    ), width=page.width
    )

    button_default = flet.Container(flet.FilledTonalButton(text="Upload File",
                                                      height=50,
                                                      on_click=lambda _: pick_files_dialog.pick_files(
                                                          allow_multiple=False
                                                      ),
                                                      ),
                               )

    button = button_default

    def pick_files_result(e: flet.FilePickerResultEvent):
        loading_text.value="Loading. Please wait."
        page.update()
        text = label_dog.hot_dog_or_not(e.files[0].path)
        global hot_dog_image_path
        if text == "hot dog":
            hot_dog_image_path = f"/images/positive.png"
            intro_text1.value = "Yeah !! It's a hot-dog 😁"
        else:
            hot_dog_image_path = f"/images/negative.png"
            intro_text1.value = "Oops !! Not a hot-dog 🥹"
        selected_image.src = hot_dog_image_path
        intro_text2.value = "Pick another file to try again"
        loading_text.value=""
        selected_image.update()
        page.update()

    pick_files_dialog = flet.FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.bgcolor = "white"

    page.add(
        flet.AppBar(
            title=flet.Text("Welcome", size=24, color="black", weight="bold", ), bgcolor="white"),
        flet.Column(
            [
                intro_container,
                loading_text,
                button,
                footer_text
             
            ],
            wrap=True,
            tight=True,
            alignment="center",
            horizontal_alignment="center"
        )
    )


flet.app(target=main, assets_dir="assets")