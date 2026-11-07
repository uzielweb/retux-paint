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
O **Retux Paint** é uma recriação moderna, elegante e 100% responsiva para a web do clássico e premiado **Tux Paint**. Desenvolvido com tecnologias modernas da Web (HTML5 Canvas 2D, Web Audio API e Vanilla JavaScript), o aplicativo é auto-contido em um único arquivo, não necessita de frameworks pesados e roda com performance máxima tanto no desktop quanto em smartphones e tablets.

### Principais Funcionalidades

- 📱 **Adaptação Mobile Completa (Canvas-First):**
  - **Área Total de Desenho no Celular:** As barras laterais transformam-se em gavetas deslizantes (*Off-Canvas Drawers*) suaves com backdrop translúcido, liberando 100% da tela para pintura.
  - **Top Bar Compacta:** Botão de ferramentas com badge da ferramenta ativa, atalhos rápidos de Desfazer/Refazer e menu colapsável para ações secundárias.
  - **Paleta por Deslizamento (Swipe):** Círculos táteis de 38px com rolagem horizontal ultra-suave ao toque do polegar.
  - **Mascote Tux Interativo:** O Tux vira um avatar flutuante que, ao ser tocado, expande balões de fala animados com dicas e sons lúdicos.
  - **Prevenção de Gestos:** Bloqueio de gestos acidentais de pull-to-refresh e rolagem nativa durante o traço de pintura.

- 📏 **Barra Rápida de Tamanho Desacoplada (Quick-Size Dock) & Painel Fixo:**
  - **Quick-Size Dock no Canvas:** Barra flutuante elegante integrada no rodapé do canvas para ajuste imediato de espessura (com preview dinâmico em tempo real, slider e atalhos rápidos P, M, G, GG) sem precisar abrir nenhuma gaveta lateral!
  - **Pinned Header na Sidebar:** O controle de tamanho, rotação e modo fica fixo no topo da barra lateral direita e nunca rola para fora da vista, mesmo navegando por centenas de carimbos.
  - **Atalhos de Teclado:** Teclas `[` e `]` para aumentar ou diminuir a espessura na hora.

- 🖌️ **Ferramentas Clássicas & Avançadas de Desenho:**
  - **Pincel (41 Formatos e Ajuste Livre de Tamanho):**
    - Novos pincéis orgânicos: **Arbustos (*Bushes*)** para folhagens exuberantes, **Aquarela (*Watercolor*)** com saturação translúcida e borda úmida, e **Tinta Espalhável (*Spread Paint*)** para misturas cremosas.
    - Círculos, quadrado, triângulo, losango, estrelas (5 e 8 pontas), coração, Cruz Latina tradicional (✝), Sinal de Mais (+), polígonos, florzinha, gotas, lua, raio, seta, caligrafia chanfrada, anel, círculo duplo, alvo, spray/aerógrafo, folha, patinha pet, sol radiante, coleção musical completa (♪, ♫, 𝄞, ♯, ♭, ♩), cerdas peludas e barras direcionais.
  - **Carimbos (139+ Assets no Total com 60 Carimbos Coloríveis):**
    - 60 carimbos dinâmicos em SVG que mudam de cor instantaneamente conforme a cor ativa da paleta (animais fofos, gatinho, cachorrinho, dinossauros, elefante, borboleta, flores, doces, coroa, balões, carros, sol, planetas, foguetes, instrumentos e símbolos).
    - Categorias completas: *Coloríveis, Tux, Animais, Veículos, Natureza, Comidas, HQ/Fantasia e Emojis*.
  - **Formas Geométricas (16 Tipos):** Retângulo, Círculo, Triângulo, Losango, Estrela, Coração, Balões de Fala e Pensamento, Nuvem, Polígonos (5, 6, 8 lados), Seta, Raio e Lua com suporte a rotação 360° e modo Preenchido/Borda.
  - **Preenchimento (Balde de Tinta):** Algoritmo de *Flood Fill* ultrarrápido com tolerância suave.
  - **Mágicas (60 Efeitos Procedurais e Filtros):** Arco-íris, Laser Neon, Florescer, Bolhas, Brilhos, Grama, Giz, Gotejar, Confete, Calidoscópio, Tijolos, Trilhos de Trem, Neve, Chuva, Raios, Fogos de Artifício, Mosaico, Xadrez, Pêlos, Fios, TV Retrô, Pixelizar, Invert, Blur, Darken, Lighten, Tint, Grayscale, Sépia, Emboss, Edges, Fisheye, Twirl, Ondas, Sharpen, Smudge, Tornado, Caligrafia, Espuma, Roseta, Chamas de Fogo, Galáxia, Cristais, Metal Cromado, Hera, Reticulado Pop-Art, Vidro Translúcido, Espelhos Horizontal e Vertical, Azulejos, Nuvens, Trovoada, Fumaça, Laser Beam, Contas, Colmeia, Respingo de Tinta, Ondulações e Chuva de Corações!
  - **Borracha:** Tamanho ajustável com pré-visualização nítida.

- ✍️ **Editor de Texto Interativo & Múltiplos Textos Arrastáveis:**
  - Digitação direta sobre o papel com arrasto livre de qualquer texto criado em qualquer momento, redimensionamento, rotação e edição inline.

- 🎵 **Áudio Duplo (Oficial & Sintético):**
  - Sons originais do Tux Paint (`.wav`/`.ogg`) com sintetizador Web Audio API procedural integrado.

- 📥 **Importador de Carimbos Personalizados:**
  - Suporte a SVG, PNG e JPG locais ou via links da web com conversão para colorível.

---

## 🇺🇸 English

### About the Project
**Retux Paint** is a modern, responsive web reimplementation of the classic and award-winning **Tux Paint**. Built with standard modern Web technologies (HTML5 Canvas 2D, Web Audio API, and Vanilla JavaScript), the application is self-contained in a single file, requiring zero build tools and running smoothly across desktop browsers, smartphones, tablets, and interactive whiteboards.

### Key Features

- 📱 **Complete Mobile Experience (Canvas-First):**
  - **100% Canvas Free Drawing Area:** Sidebars transform into smooth off-canvas drawers with blurred backdrops, reserving the full screen for painting.
  - **Compact Mobile Top Bar:** Quick tool badge, direct Undo/Redo touch buttons, and a collapsible menu for file operations.
  - **Swipeable Color Palette:** 38px touch circles with smooth horizontal swipe gestures.
  - **Interactive Tux Mascot:** Floating avatar that pops up helpful tips and audio giggles on tap.
  - **Touch Gesture Protection:** Prevents unwanted pull-to-refresh or native scrolling during brush strokes.

- 📏 **Decoupled Quick-Size Dock & Pinned Sidebar Header:**
  - **Quick-Size Dock on Canvas:** Floating glassmorphic dock at the bottom of the canvas with real-time dot preview, smooth slider, and S/M/L/XL presets without opening any sidebar drawer!
  - **Pinned Options Header:** Size, scale, and rotation controls remain fixed at the top of the sidebar and never scroll out of view.
  - **Keyboard Shortcuts:** `[` and `]` keys for instant brush sizing.

- 🖌️ **Comprehensive Drawing Tools:**
  - **Paint Brush (41 Shapes & Free Sizing):** Organic **Bushes** for leafy foliage, glazed **Watercolor** with wet pigment edges, and creamy **Spread Paint** blending, alongside 38 classic geometric, musical, and procedural shapes.
  - **Stamps (139+ Total Assets with 60 Dynamic Colorable Stamps):** 60 SVGs that adapt in real time to any chosen color from the palette.
  - **Shapes (16 Types):** Full rotation control, 1:1 proportion lock, and dual fill/stroke modes.
  - **Magic Effects (60 Procedural Tools & Filters):** From classic Rainbow and Neon to Tornado, Calligraphy, Fire, Galaxy, Chrome Metal, Ivy Vines, Pop-Art Halftone, Frosted Glass, Symmetry Mirrors, and Floating Hearts.
  - **Draggable Text Engine:** Place, freely drag, rotate, recolor, and edit multiple texts directly on canvas.
  - **Dual Audio Suite:** Authentic Tux Paint sound effects paired with an offline Web Audio synthesizer fallback.
