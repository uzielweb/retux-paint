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
  - A folha de pintura e a superfície do canvas possuem cantos estritamente retos (`border-radius: 0`), reproduzindo fielmente a experiência física de desenhar em uma folha de papel de arte real, sem cortes ou curvas artificiais nos cantos.

- 📱 **Nova Arquitetura Mobile (Barra Única & Gavetas em Tela Cheia):**
  - **Barra Única de Ações Rápidas no Topo:** Acesso imediato aos botões essenciais sem menus ocultos ou submenus truncados:
    - `[ 🛠️ Ferramentas ]` (com badge dinâmico da ferramenta ativa)
    - `[ ↩️ Desfazer ]` e `[ ↪️ Refazer ]`
    - `[ ➕ Novo ]` e `[ 💾 Salvar ]`
    - `[ 🎵 Som Oficial/Sintético ]` e `[ 🇧🇷 Idioma PT/EN ]`
    - `[ 🎨 Opções da Ferramenta ]`
  - **Gavetas em Tela Cheia (100vw × 100dvh):** As barras laterais abrem como painéis deslizantes em tela cheia suavemente animados:
    - **Gaveta de Ferramentas:** Grade ergonômica de 3 colunas com botões grandes, ícones vetoriais nítidos e botão de fechar proeminente no topo.
    - **Gaveta de Opções:** Grade densa estilo *sticker-book* (até 7 colunas), controles de espessura com slider e atalhos P, M, G, GG.
  - **Área do Canvas Desobstruída:** O canvas ocupa a área livre total sem nenhum elemento ou dock flutuando sobre a pintura.
  - **Paleta por Deslizamento Horizontal (Swipe):** Círculos táteis de cor com rolagem horizontal ultra-suave ao toque do polegar.
  - **Mascote Tux Interativo:** Avatar que reage ao toque com dicas animadas e sons lúdicos originais.
  - **Bloqueio de Gestos Acidentais:** Prevenção ativa de pull-to-refresh e scroll nativo durante o traço de pintura.

- 🎨 **Seletor de Cores Mágico Próprio (Custom Color Picker):**
  - Substitui totalmente o seletor nativo do sistema operacional por um modal integrado e lúdico:
    - **Mapa 2D de Saturação e Brilho:** Gradiente contínuo com cursor de arrasto tátil de alta precisão.
    - **Slider Arco-Íris de Matriz (Hue):** Espectro 360° para seleção infinita de tonalidades.
    - **Entrada HEX Direta:** Sincronização bidirecional instantânea entre código hexadecimal e cor escolhida.
    - **32 Cores Rápidas (Swatches):** Coleção curada das tonalidades mais populares para seleção com um clique.

- 🖌️ **Ferramentas de Desenho Completas:**
  - **Pincel (41 Formatos e Ajuste Livre de Tamanho):**
    - Novos pincéis orgânicos: **Arbustos (*Bushes*)** para folhagens, **Aquarela (*Watercolor*)** com saturação translúcida e borda úmida, e **Tinta Espalhável (*Spread Paint*)** para misturas cremosas.
    - Formatos geométricos, estrelas, coração, Cruz Latina tradicional (✝), Sinal de Mais (+), polígonos, florzinha, gotas, lua, raio, seta, caligrafia chanfrada, anel, círculo duplo, alvo, spray/aerógrafo, folha, patinha pet, sol radiante, coleção musical completa (♪, ♫, 𝄞, ♯, ♭, ♩), cerdas peludas e barras direcionais.
  - **Carimbos (139+ Assets com 60 Carimbos Coloríveis):**
    - 60 carimbos dinâmicos em SVG que adaptam sua cor instantaneamente à cor selecionada na paleta.
    - Categorias completas: *Coloríveis, Tux, Animais, Veículos, Natureza, Comidas, HQ/Fantasia e Emojis*.
  - **Formas Geométricas (16 Tipos):** Retângulo, Círculo, Triângulo, Losango, Estrela, Coração, Balões de Fala e Pensamento, Nuvem, Polígonos (5, 6, 8 lados), Seta, Raio e Lua com rotação 360° e modos Preenchido/Borda.
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

### Key Innovations & Features

- 📄 **Authentic Drawing Paper (Zero Border-Radius):**
  - The drawing canvas and sheet feature crisp, strictly straight corners (`border-radius: 0`), accurately reflecting the physical experience of drawing on real art paper with zero artificial rounding.

- 📱 **All-New Mobile Architecture (Single Action Bar & Fullscreen Drawers):**
  - **Unified Top Action Bar:** Direct access to essential actions with no hidden or clipped dropdowns:
    - `[ 🛠️ Tools ]` (with dynamic active tool badge)
    - `[ ↩️ Undo ]` and `[ ↪️ Redo ]`
    - `[ ➕ New ]` and `[ 💾 Save ]`
    - `[ 🎵 Sound Mode ]` and `[ 🇧🇷 Language PT/EN ]`
    - `[ 🎨 Tool Options ]`
  - **Fullscreen Overlays (100vw × 100dvh):** Sidebars open as full-screen smooth drawers with clean layouts:
    - **Tools Drawer:** 3-column ergonomic grid with compact buttons and a clear close button at the top.
    - **Options Drawer:** Dense sticker-book grid (up to 7 columns), brush size slider, and S/M/L/XL quick buttons.
  - **Unobstructed Canvas:** 100% free drawing space without floating docks over the canvas.
  - **Swipeable Color Palette:** Touch-friendly swatches with smooth horizontal swipe gestures.
  - **Interactive Tux Mascot:** Floating mascot responding with animated tips and playful audio on tap.
  - **Touch Gesture Protection:** Prevents unwanted pull-to-refresh and native scroll during brush strokes.

- 🎨 **Custom Retux Color Picker:**
  - Fully replaces the native OS color dialog with an integrated, kid-friendly palette:
    - **2D Saturation / Value Canvas:** Real-time tactile pointer with crosshair indicator.
    - **Rainbow 360° Hue Slider:** Continuous spectrum covering all visible colors.
    - **Direct Hex Input:** Real-time two-way synchronization.
    - **32 Quick Swatches:** Curated grid of the most popular creative colors.

- 🖌️ **Comprehensive Drawing Tools:**
  - **Paint Brush (41 Shapes & Free Sizing):** Organic **Bushes**, glazed **Watercolor**, creamy **Spread Paint**, alongside 38 geometric, musical, and procedural shapes.
  - **Stamps (139+ Total Assets with 60 Dynamic Colorable Stamps):** 60 SVGs that adapt in real time to any chosen color from the palette.
  - **Shapes (16 Types):** Full rotation control, 1:1 proportion lock, and dual fill/stroke modes.
  - **Magic Effects (60 Procedural Tools & Filters):** From classic Rainbow and Neon to Tornado, Calligraphy, Fire, Galaxy, Chrome Metal, Ivy Vines, Pop-Art Halftone, Frosted Glass, Symmetry Mirrors, and Floating Hearts.
  - **Draggable Text Engine:** Place, freely drag, rotate, recolor, and edit multiple texts directly on canvas.
  - **Dual Audio Suite:** Authentic Tux Paint sound effects paired with an offline Web Audio synthesizer fallback.
