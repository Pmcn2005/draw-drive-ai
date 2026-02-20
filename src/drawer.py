import pyray as pr
import os


def iniciar_desenho():
    largura = 800
    altura = 600

    pr.init_window(
        largura,
        altura,
        "Desenhar Pista - Pressiona 'S' para Guardar\n",
    )
    pr.set_target_fps(120)

    # Criar a "tela" em memória onde vamos pintar
    tela = pr.load_render_texture(largura, altura)

    pr.begin_texture_mode(tela)
    pr.clear_background(pr.DARKGREEN)
    pr.end_texture_mode()

    tamanho_pincel = 25
    cor_estrada = pr.DARKGRAY

    if not os.path.exists("assets"):
        os.makedirs("assets")

    while not pr.window_should_close():

        if pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT):
            pos_rato = pr.get_mouse_position()

            pr.begin_texture_mode(tela)
            pr.draw_circle_v(pos_rato, tamanho_pincel, cor_estrada)
            pr.end_texture_mode()

        if pr.is_key_pressed(pr.KEY_S):
            # Extrair a imagem da nossa tela em memória
            imagem_final = pr.load_image_from_texture(tela.texture)

            # O Raylib inverte as imagens na RenderTexture, por isso temos de a virar
            pr.image_flip_vertical(imagem_final)

            pr.export_image(imagem_final, "./assets/pista.png")
            print("Pista guardada com sucesso em assets/pista.png!")

            pr.unload_image(imagem_final)

        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

        # Desenhar a nossa tela no ecrã (novamente, temos de ajustar a inversão)
        pr.draw_texture_rec(
            tela.texture,
            pr.Rectangle(0, 0, tela.texture.width, -tela.texture.height),
            pr.Vector2(0, 0),
            pr.WHITE,
        )

        pr.draw_text(
            "Usa o rato para desenhar. Pressiona 'S' para guardar.\nAperta 'ESC' para sair.",
            10,
            10,
            20,
            pr.BLACK,
        )
        pr.end_drawing()

    pr.unload_render_texture(tela)
    pr.close_window()


if __name__ == "__main__":
    iniciar_desenho()
