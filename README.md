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
O **Retux Paint** é uma recriação moderna, elegante e 100% responsiva para a web do clássico e premiado **Tux Paint**. Desenvolvido com tecnologias modernas da Web (HTML5 Canvas 2D, Web Audio API e Vanilla JavaScript), o aplicativo é auto-contido em um único arquivo, não necessita de frameworks pesados e roda instantaneamente em qualquer navegador moderno (desktop, tablets e lousas digitais).

### Principais Funcionalidades

- 🖌️ **Ferramentas Clássicas de Desenho:**
  - **Pincel (33 Formatos e Ajuste Livre de Tamanho):** Círculos (fino, médio, grosso, gigante), quadrado, triângulo, losango, estrelas (5 e 8 pontas), coração, cruz, mais, polígonos (pentágono, hexágono, octógono), florzinha, gotas/respingos, lua, raio, seta, caligrafia chanfrada (esquerda e direita), anel, círculo duplo, alvo, spray/aerógrafo, folha, patinha pet, sol radiante, nota musical, cerdas peludas, barras horizontal e vertical. Controle contínuo de tamanho (de 2px a 100px) com atalhos de tamanho rápido (P, M, G, GG).
  - **Carimbos (79+ Assets):** Coleção vetorial em 8 categorias (*Coloríveis, Tux, Animais, Veículos, Natureza, Comidas, HQ/Fantasia e Emojis*).
  - **Carimbos Coloríveis:** Silhuetas que mudam de cor em tempo real de acordo com a paleta selecionada.
  - **Linhas Retas:** Desenho guiado com espessura variável.
  - **Formas Geométricas (16 Tipos):** Retângulo, Círculo, Triângulo, Losango, Estrela, Coração, Balões de Fala e Pensamento, Nuvem, Polígonos (5, 6, 8 lados), Seta, Raio e Lua. Suporte a proporção 1:1 (Shift) e modo Borda + Recheio.
  - **Preenchimento (Balde de Tinta):** Algoritmo de *Flood Fill* ultrarrápido com tolerância suave.
  - **Mágicas (37 Efeitos Procedurais e Filtros):** Arco-íris, Laser Neon, Florescer, Bolhas, Brilhos, Grama, Giz, Gotejar, Confete, Calidoscópio, Tijolos (Bricks), Trilhos de Trem (Rails), Flocos de Neve, Chuva, Raios Elétricos, Fogos de Artifício, Mosaico Vitral, Tabuleiro de Xadrez, Pêlos Macios, Fios (String Art), Luz Neon, TV Retrô Scanlines, Pixelizar, Inverter Cores, Desfoque (Blur), Escurecer, Clarear, Tingir (Tint), Preto & Branco (Grayscale), Sépia Vintage, Relevo 3D (Emboss), Bordas Neon (Edges), Olho de Peixe (Fisheye), Redemoinho (Twirl), Ondas Senoidais, Nitidez (Sharpen) e Borrar (Smudge).
  - **Borracha:** 4 tamanhos diferentes para correções rápidas.

- ✍️ **Editor de Texto Interativo & Múltiplos Textos Arrastáveis:**
  - Digitação direta no papel (sem caixas de diálogo `prompt()` invasivas).
  - **Arrasto de Qualquer Texto:** Qualquer texto criado pode ser selecionado e arrastado livremente pela tela a qualquer momento!
  - Edição ao vivo: altere cor na paleta, tamanho de fonte (slider), rotação (360°), negrito, itálico ou dê dois cliques para editar o conteúdo de qualquer texto criado.
  - Botão de exclusão rápida (`✕`) e edição inline (`✎`) para cada texto individualmente.

- 🔄 **Controle Total de Rotação:**
  - Rotação livre de 0° a 360° com atalhos de ±45° para **Carimbos**, **Textos** e **Formas**.

- 🎵 **Áudio Duplo (Oficial & Sintético):**
  - **Sons Oficiais do Tux Paint:** Integração com os arquivos de som originais (`.wav` e `.ogg`) do mascote Tux.
  - **Sintetizador Web Audio API:** Geração procedural de sons sintetizados para uso 100% autônomo offline.

- 📥 **Importador de Carimbos Personalizados:**
  - Importe qualquer arquivo SVG, PNG ou JPG do seu computador ou através de links da Web.
  - Opção para converter imagens importadas em carimbos coloríveis.
  - Armazenamento persistente local na aba "Meus Carimbos".

- 🌐 **Internacionalização (i18n):**
  - Alternância instantânea de idioma entre **Português (pt-BR)** e **Inglês (en-US)** com um clique no cabeçalho.

- 💾 **Salvamento e Exportação:**
  - Suporte à API nativa de arquivos do Windows (*File System Access API*), permitindo salvar diretamente na Área de Trabalho com escolha de formato (PNG ou JPG).
  - Cópia com 1 clique para a Área de Transferência (`Ctrl+C` para colar no WhatsApp, Word, etc.).

---

## 🇺🇸 English

### About the Project
**Retux Paint** is a modern, responsive web reimplementation of the classic and award-winning **Tux Paint**. Built with standard modern Web technologies (HTML5 Canvas 2D, Web Audio API, and Vanilla JavaScript), the application is self-contained in a single file, requiring zero external build tools and running smoothly on desktop browsers, tablets, and interactive whiteboards.

### Key Features

- 🖌️ **Classic Drawing Tools:**
  - **Paint Brush (33 Shapes & Free Size Adjustment):** Circles (fine, medium, thick, huge), square, triangle, diamond, stars (5 and 8 points), heart, cross, plus, polygons (pentagon, hexagon, octagon), flower, splatters, moon, lightning, arrow, calligraphy chisel (left and right), ring, double ring, bullseye target, airbrush/spray, leaf, pet paw, sunburst, music note, bristle brush, horizontal and vertical bars. Continuous size slider (2px to 100px) with quick size presets (S, M, L, XL).
  - **Stamps (79+ Assets):** Curated vector stamps in 8 categories (*Colorable, Tux, Animals, Vehicles, Nature, Food, Comics, and Emojis*).
  - **Colorable Stamps:** Silhouette assets that react in real-time to the active color palette.
  - **Lines:** Guided straight lines with adjustable thickness.
  - **Shapes (16 Types):** Rectangle, Circle, Triangle, Diamond, Star, Heart, Speech & Thought Bubbles, Cloud, Polygons (Pentagon, Hexagon, Octagon), Arrow, Lightning, and Moon. 1:1 proportion lock and Dual-color (Border + Fill) mode.
  - **Paint Bucket (Fill):** Fast scanline flood fill with soft color tolerance.
  - **Magic Effects (37 Generative Effects & Filters):** Rainbow, Neon Laser, Blooming Flowers, Bubbles, Sparkles, Grass, Chalk, Drip, Confetti, Kaleidoscope, Classic Bricks, Train Tracks, Snowflakes, Raindrops, Electric Lightning, Fireworks, Stained Glass Mosaic, Checkerboard, Soft Fur, String Art, Soft Glow, Retro CRT Scanlines, Pixelate, Invert Colors, Blur, Darken, Lighten, Color Tint, Grayscale, Vintage Sepia, 3D Emboss, Neon Edges, Fisheye Lens, Swirl/Twirl, Sine Waves, Sharpen, and Finger Smudge.
  - **Eraser:** 4 sizes with smooth erasing.

- ✍️ **Interactive On-Canvas Text & Multi-Text Dragging Engine:**
  - Live typing directly over the canvas paper (replacing disruptive modal prompts).
  - **Drag Any Created Text:** Every placed text can be selected and dragged freely across the canvas at any time!
  - Real-time editing: change color via palette, font size slider, 360° rotation slider, bold, italic, or double-click to edit text contents.
  - Quick inline delete (`✕`) and edit (`✎`) action buttons on each text element.

- 🔄 **Universal Rotation Engine:**
  - 360° rotation slider with ±45° presets for **Stamps**, **Text**, and **Shapes**.

- 🎵 **Dual Audio Engine:**
  - **Official Tux Paint Audio:** Authentic `.wav` and `.ogg` sound effects from the original Tux Paint suite.
  - **Web Audio API Synthesizer:** Real-time procedural audio fallback for 100% offline standalone usage.

- 📥 **Custom Stamp Importer:**
  - Import any SVG, PNG, or JPG from your computer or via direct Web URLs.
  - Convert custom graphics into palette-tinted stamps.
  - Persistent local storage under "My Stamps".

- 🌐 **Internationalization (i18n):**
  - Instant one-click language toggle between **Portuguese (pt-BR)** and **English (en-US)**.

- 💾 **Export & Save:**
  - Native Windows File System Access picker to save directly to Desktop or Pictures as PNG or JPG.
  - One-click "Copy Drawing" to system clipboard (`Ctrl+C` to paste into Discord, WhatsApp, Word, etc.).

---

## 🚀 Como Executar / How to Run

### Online Demo
Acesse diretamente via GitHub Pages:  
👉 **[https://uzielweb.github.io/retux-paint/](https://uzielweb.github.io/retux-paint/)**

### Localmente / Locally
Basta abrir o arquivo [`index.html`](index.html) em qualquer navegador moderno, ou servi-lo através do Laragon, Apache ou Live Server:
```bash
# Clone the repository
git clone https://github.com/uzielweb/retux-paint.git
cd retux-paint

# Simply open index.html in your browser!
start index.html
```

---

## 📄 Licença / License
Este projeto é distribuído sob a licença GNU GPL v2+ em homenagem e conformidade com o projeto original Tux Paint (criado por Bill Kendrick e a comunidade New Breed Software).
