# Retux Paint 🎨🐧

> **Tux Paint Moderno para Web** | **Modern Tux Paint for the Web**  
> Desenho e criatividade digital para crianças, educadores e artistas de todas as idades.  
> Digital drawing and creativity for kids, educators, and artists of all ages.

[![GitHub Pages](https://img.shields.io/badge/demo-online-brightgreen.svg)](https://uzielweb.github.io/retux-paint/)
[![License: GPL v2+](https://img.shields.io/badge/License-GPL_v2%2B-blue.svg)](https://www.gnu.org/licenses/gpl-2.0.html)
[![HTML5 Canvas](https://img.shields.io/badge/HTML5-Canvas%202D-orange.svg)](#)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20JS)-success.svg)](#)

![Retux Paint Preview](assets/og-image.png)

---

## 🇧🇷 Português

### Sobre o Projeto
O **Retux Paint** é uma recriação moderna, elegante e 100% responsiva para a web do clássico e premiado **Tux Paint**. Desenvolvido com tecnologias modernas da Web (HTML5 Canvas 2D, Web Audio API e Vanilla JavaScript), o aplicativo é auto-contido em um único arquivo, não necessita de instaladores ou frameworks pesados e roda com performance máxima no desktop, smartphones, tablets e lousas digitais interativas.

### Principais Inovações & Funcionalidades

- 📄 **Folha de Desenho Autêntica (Zero Border-Radius):**
  - A folha de pintura e o canvas possuem cantos estritamente retos (`border-radius: 0`), reproduzindo com fidelidade a experiência de desenhar em uma folha de papel de arte real.

- 📱 **Nova Arquitetura Mobile (Barra Única & Gavetas em Tela Cheia):**
  - **Barra Única de Ações Rápidas no Topo:** Acesso imediato sem sobreposições:
    - `[ 🛠️ Ferramentas ]` (com badge dinâmico da ferramenta ativa)
    - `[ ↩️ Desfazer ]` e `[ ↪️ Refazer ]`
    - `[ ➕ Novo ]` e `[ 💾 Salvar ]`
    - `[ 🎵 Modo de Som ]` e `[ 🇧🇷 Idioma PT/EN ]`
    - `[ 🎨 Opções da Ferramenta ]`
  - **Gavetas em Tela Cheia (100vw × 100dvh):** As sidebars abrem em tela cheia suavemente animada. Ao clicar em "Novo", "Abrir" ou selecionar qualquer ferramenta, carimbo, forma ou mágica no catálogo, a gaveta se fecha automaticamente trazendo o usuário de volta à pintura.
  - **Chips Deslizantes de Categorias:** No painel de Carimbos, as categorias são dispostas em linha única de chips com deslizamento horizontal suave, liberando espaço vertical e exibindo até 7 linhas de carimbos simultaneamente.
  - **Paleta Mobile Otimizada (Touch-Friendly):** Círculos de cor de 40px com deslizamento horizontal contínuo preenchendo toda a largura da tela sem lacunas vazias.
  - **Mascote Tux com Dicas Ampliadas:** Balão de fala com tipografia legível (14px), botão de fechar manual `✕` e tempo de leitura estendido para 15 segundos.

- 🎵 **Sistema de Áudio Unificado de 3 Estados & Traço Suave:**
  - **Seletor Cíclico de 3 Modos:**
    - 🎵 **Sons Oficiais:** Efeitos originais `.wav` do Tux Paint com buffer decodificado em memória (*zero-latency* e sem cortes).
    - 🎹 **Sons Sintéticos:** Síntese procedural leve em Web Audio API retrô.
    - 🔇 **Sem Som (Mudo):** Silêncio absoluto para salas de aula, escritórios ou noite.
  - **Cadência Sonora Anti-Engasgo:** O som contínuo do pincel e da borracha agora é sincronizado por distância percorrida (~28px) com limitador temporal de 110ms, eliminando estalos de áudio e travamentos.

- 🎨 **Seletor de Cores Mágico Próprio (Custom Color Picker):**
  - Substitui totalmente o seletor nativo do sistema operacional por um modal integrado:
    - **Mapa 2D de Saturação e Brilho:** Gradiente contínuo com cursor de arrasto de alta precisão.
    - **Slider Arco-Íris de Matriz (Hue):** Espectro 360° para seleção infinita de tonalidades.
    - **Entrada HEX Direta:** Sincronização bidirecional instantânea.
    - **32 Cores Rápidas (Swatches):** Coleção curada das tonalidades mais populares.

- 🪄 **61 Efeitos Mágicos 100% Funcionais:**
  - Todas as 61 ferramentas do catálogo agora contam com manipuladores completos no motor de desenho:
    - **Novo: Disco Voador / UFO:** Desenha naves espaciais metálicas com cúpula de vidro, luzes piscantes e feixe de abdução neon translúcido!
    - Arco-íris, Laser Neon, Florescer, Bolhas, Brilhos, Grama, Giz, Gotejar, Confete, Calidoscópio, Tijolos, Trilhos de Trem, Neve, Chuva, Raios, Fogos de Artifício, Mosaico, Xadrez, Pêlos, Fios, TV Retrô, Pixelizar, Invert, Blur, Darken, Lighten, Tint, Grayscale, Sépia, Emboss, Edges, Fisheye, Twirl, Ondas, Sharpen, Smudge, Tornado, Caligrafia, Espuma, Roseta, Chamas de Fogo, Galáxia, Cristais, Metal Cromado, Hera, Reticulado Pop-Art, Vidro Translúcido, Espelhos Horizontal e Vertical, Azulejos, Nuvens, Trovoada, Fumaça, Laser Beam, Contas, Colmeia, Respingo de Tinta, Ondulações e Chuva de Corações!

- ✍️ **Editor de Texto Interativo Aprimorado:**
  - Digitação direta sobre o papel com arrasto livre, rotação e botões táteis de Confirmar (`✓`) e Cancelar (`✕`) com touch-target de 28px totalmente responsivo no mobile e desktop.

---

## 🇺🇸 English

### About the Project
**Retux Paint** is a modern, responsive web reimplementation of the classic and award-winning **Tux Paint**. Built with standard modern Web technologies (HTML5 Canvas 2D, Web Audio API, and Vanilla JavaScript), the application is self-contained in a single file, requiring zero build tools and running smoothly across desktop browsers, smartphones, tablets, and interactive whiteboards.

### Key Innovations & Features

- 📄 **Authentic Drawing Paper (Zero Border-Radius):**
  - Crisp straight corners (`border-radius: 0`) reflecting physical drawing paper.

- 📱 **Mobile First Experience:**
  - Unified single top bar, full-screen overlay drawers, auto-closing on modal actions, 42px touch-friendly swatches, and enlarged Tux tips with manual close `✕`.

- 🎵 **3-State Unified Audio Engine & Smooth Brush Stroke:**
  - Official Tux Paint `.wav` sounds, Web Audio synthetic retro tones, and a dedicated **Muted** mode.
  - Continuous strokes cadence by distance without clipping or audio stutter.

- 🪄 **61 Fully Operational Magic Effects:**
  - Complete engine coverage including the brand-new **Disco Voador / UFO**, Tornado, Ivy, Mirroring, Plasma, Galaxy, and Hearts.
