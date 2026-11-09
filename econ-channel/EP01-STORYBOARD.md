# EP01 — Storyboard: «¿Por qué todo está más caro?» (8:00)

**Canal:** El Precio de Todo · **Idioma:** Español · **Duración:** ≈8:00 · **Formato:** faceless, VO + motion graphics
**Estado:** APROBADO (2026-11-09) — marca cerrada (@elprecio_detodo · Opción B). En build: VO ES por audition, luego composiciones y render.
**VO:** voz por audition (se auditionan 2 candidatas ES en el paso de producción; tú eliges). Registro: storyteller de aula — frases cortas, cero jerga sin imagen.
**Sistema visual (Opción B “El Precio de Todo”):**
- Fondo: pizarra verde oscuro `#10312B` con líneas de ledger al 4% · texto tiza crema `#EDE6D3` · **acento tiza amarillo** `#FFD84D` (números, slabs de énfasis) · **tiza coral** `#FF6B57` (alertas, flechas de subida)
- Anton para display/titulares, Archivo para cuerpo; números siempre en amarillo tiza con tabulares
- Anotaciones dibujadas a mano (círculos, subrayados, flechas) — técnica de marker-draw reutilizable del pipeline
- Episodio con motivo de **tique/recibo** y monedas de tiza; sin stock footage salvo 1–2 hero shots (recibo macro)
- Cada número con chip de fuente (`BLS` · `Eurostat` · `BCE` · `FRED`); tarjetas “no es consejo financiero” donde aplique

---

## Verificado (Nov 2026) — fact pack

| # | Dato | Fuente |
|---|---|---|
| F1 | IPC EE. UU. alcanzó **+9,1% interanual** en jun-2022 (máximo en 40 años) | BLS |
| F2 | IPCA zona euro alcanzó **+10,6% interanual** en oct-2022 | Eurostat |
| F3 | La Fed hizo el ciclo de subidas más rápido desde los 80, hasta **5,25–5,50%** (jul-2023); **primera subida desde 2023 en sep-2026**, hasta **3,75–4,00%** | FOMC / CBS |
| F4 | IPC EE. UU. **3,7%** (sep-2026; ago 3,4% · jul 3,4% · dic-2025 2,7%); subyacente **2,6%** | BLS (14-oct-2026) |
| F5 | EE. UU. energía **+20,4% interanual**; gasolina **+34,2% interanual** (sep-2026; la gasolina explicó más de la mitad de la subida mensual) | BLS / CBS |
| F6 | Zona euro **4,0%** (flash oct-2026; sep 3,8% · ago 3,2%); **energía +20,8% interanual** (componente más alto) · servicios 3,3% · alimentos 1,6% · NEIG 1,2% · **ex-energía 2,3%** | Eurostat (4-nov-2026) |
| F7 | **Países Bajos: CPI 3,7% en oct-2026** (snelle raming 4-nov; sep 3,4 · ago 3,3 · jul 3,2 · jun 2,9 · may 3,5; +0,7% m/m vs media 10 años de 0,5%); **HICP 3,3%** (desde 3,0%); **energía +14,4%** (sep 13,8%); **gas +52,5% interanual** (de 34,9%); electricidad +23,7%; servicios 3,9%; alimentación −0,6%. Definitivo: 10-nov-2026 | CBS NL |
| F7b | Déficit gobiernos zona euro **3,0% del PIB**; renta real hogares +0,1% t/t (2T-2026) | Eurostat |
| F10b | **Guerra en Irán desde el 28-feb-2026**: tráfico por Ormuz colapsó de ~20M b/d a **2,7M b/d** (mar–may, IEA); crudo de $78 a **$131 en 8 días** ($88 en el día 35); >1.300M barriles perdidos acumulados; bypass saudí+emiratí ~6,5M b/d; ~20% del LNG mundial también pasa por Ormuz; 84% del crudo → Asia | EIA / IEA / CBS News |
| F8 | Renta real de los hogares por habitante en la zona euro **+0,1% trimestral** (2T-2026); consumo real +0,3% | Eurostat (21-oct-2026) |
| F9 | Expectativas de inflación del consumidor en EE. UU. **3,9%** (sep-2026; desde 3,6%) | Trading Economics / encuestas BLS |
| F10 | Desencadenante: **guerra en Irán** (shock energético) sobre el legado de Rusia–Ucrania | CBS / Eurostat |

_Los gráficos con ejemplos cotidianos (recibo, cesta, depósito) son “ilustrativos” y se etiquetan así en pantalla; todo número de carga lleva su chip de fuente del fact pack._

---

## Ritmo (9 beats · timecode · contenido)

### 0:00–0:25 — FRÍO: EL TICKET
- **Visual:** recibo de supermercado desenrollándose (ilustrativo); líneas en Anton sobre papel térmico amarillo-paja: *Gasolina +34,2% (EE. UU., F5)* · *Energía +20,8% (EA, F6)* · *Tu cesta* (ilustrativa, se encoge). Después, sello a toda pantalla, tinta roja: **«MISMA CESTA. OTRO PRECIO.»**
- **VO (registro anécdota):** «Tu café. Tu gasolina. Tu alquiler. Todos cuentan la misma historia… y no ha terminado.»
- **Movimiento:** desenrollado con count-ups; sello con golpe seco + sub-bass; chips de fuente parpadean.
- **SFX:** un solo *stamp thud* (numpy). Nada de ruido de multitudes.

### 0:25–1:05 — LA PREGUNTA + LA RESPUESTA EN UNA FRASE
- **Visual:** tarjeta-definición en tiza: **«Inflación = la transferencia silenciosa de poder adquisitivo.»** Luego una línea de IPC 40 años (EE. UU. y zona euro) con 3 zonas sombreadas: 2010s «1–2%, la normalidad» · 2021–22 «la explosión» · 2023–25 «el enfriamiento largo» · 2026 «la segunda ola».
- **VO:** «La inflación es un robo sin pistola: te coge el dinero sin que lo notes. Hoy te cuento las tres olas… y la tercera acaba de llegar.»
- **Datos:** F1, F2. Gráfico: IPC interanual US & EA 2016–2026 (curva SVG dibujada en runtime, sin librerías externas).

### 1:05–2:05 — OLA 1: LA PITA (2020–22)
- **Visual:** tritríptico de culpables, cada uno con mini-gráfico:
  1. **Los cheques** — transferencias 2020–21 → exceso de demanda
  2. **El atasco** — cadenas de suministro / chips → picos de bienes
  3. **El misil** — Rusia invade Ucrania (feb-2022) → energía (EA >40% pico en 2022)
- **VO:** «No hace falta un villano. Hacen falta tres cerillas.»
- **Nota de diseño:** tres paneles en pizarra con dibujo de cerilla que se enciende uno a uno.

### 2:05–3:00 — OLA 2: EL MANGUERAZO (2022–25)
- **Visual:** dial gigante de tipos 0 → 5,25–5,50% (jul-2023, F3); BCE hasta 4,00% (sep-2023): las subidas más rápidas en 40 años; barras de hipoteca subiendo; luego el glide-down a <3% en 2025 y principios de 2026 (EE. UU. dic-2025: 2,7%).
- **VO:** «Una manguera contra un incendio. Pero el agua tarda un año y medio en llegar al fuego.»
- **Detalle de guion:** «Los tipos tardan 18 meses en encontrarte. Por eso el alquiler y la hipoteca se enfrían el último.»

### 3:00–3:45 — EL GIRO: NADIE TE DEVOLVIÓ EL DINERO
- **Visual:** la línea famosa que NO vuelve: **el nivel de precios**. Texto tiza: «Los precios no bajaron. Bajó la *velocidad* a la que subían.» A la derecha: salarios vs precios 2021→2026 (EA renta real +0,1% t/t 2T-2026, F8).
- **Microcosmos real:** cesta de 100 € en 2020 → poder de compra erosionado ~15–20% acumulado — carrito ilustrativo que se encoge (sin cifras inventadas; chip: «IPCA acumulado, Eurostat»).
- **VO:** «La desinflación no es el ladrón devolviendo la cartera. Es el ladrón caminando más despacio.»

### 3:45–5:15 — OLA 3 (EL PRESENTE): LA SEGUNDA CERILLA
- **Visual:** mapa — **Irán / Estrecho de Ormuz** (guerra desde el 28-feb-2026); petroleros detenidos; ticker de petróleo: **$78 → $131 en 8 días**, ahora ~$88; muro de titulares: «sep-2026: la Fed sube tipos por primera vez desde 2023» (F3).
- **Columna vertebral de datos (todos con chip en pantalla):**
  - Zona euro **4,0%** flash oct-2026 (F6) · EE. UU. **3,7%** sep-2026 (F4) · subyacente EE. UU. 2,6% → **es la energía otra vez**
  - EA energía **+20,8%** · alimentos +1,6% · servicios +3,3% · ex-energía **2,3%**
- **VO:** «Dos años enfriándose. Seis semanas para volver a arder. Bienvenido a la tercera ola.»
- **Ángulo euros/NL (canal ES/EU-first):** Países Bajos **3,7%** en oct-2026 (más alto del año; gas **+52,5%** interanual) · HICP 3,3% · TTF como indicador en pantalla · déficit EU 3,0% PIB.

### 5:15–6:15 — LOS DOS NÚMEROS QUE DECIDEN EL PRÓXIMO AÑO
- **Visual:** panel doble de dashboard:
  1. **La prima de energía** — Brent/TTF vs baseline preguerra ($78 → $131 en 8 días, ahora ~$88); por Ormuz pasa ~20% del petróleo mundial y ~20% del LNG; el tráfico cayó a 2,7M b/d (F10b) (~20% LNG; verificar EIA — YA VERIFICADO)
  2. **Las expectativas** — EE. UU. 3,9% y subiendo (F9)
- **VO:** «La inflación vive en lo que la gente *espera*, no solo en lo que pasó. Si tu jefe cree que habrá 4% de inflación, te sube el sueldo un 4%. Y la serpiente se muerde la cola.»
- **3 tarjetas-escenario** (animación de pase de cartas): *Aterrizaje suave ≈2,5%* · *Más alta y por más tiempo ≈4%* · *Segunda descarga → 5%+* — cada una con «qué la mata / qué la alimenta».

### 6:15–7:20 — QUÉ SIGNIFICA PARA TU DINERO (3 reglas)
- **Visual:** tres tarjetas de tiza:
  1. **El efectivo es un cubito de hielo al sol** — mejor un depósito que rinde que un colchón; el interés vuelve a ser positivo
  2. **La deuda a tipo fijo se devuelve con dinero más barato** — el banco no celebra
  3. **Pide el aumento en términos nominales** — una subida del 4% con 4% de inflación = estar quieto
- **VO:** empoderamiento sin consejo; cada tarjeta lleva micro-print «Contenido educativo, no consejo financiero».

### 7:20–7:45 — REPASO EN 3 LÍNEAS
1. 2021–22: la cerilla (COVID + Ucrania) → inflación del 10%
2. 2022–25: la manguera (las subidas más rápidas de la historia) → enfriamiento, sin devolución
3. 2026: la segunda cerilla (energía de Irán) → 4% otra vez — mantén el escudo

### 7:45–8:00 — OUTRO
- **Visual:** end card Opción B — avatar tiza-coin, botón suscribir, teaser del próximo episodio: **«Próximo: ¿quién paga realmente los aranceles — el importador, el exportador… o tú?»**
- **VO:** frase de despedida + «te veo en el próximo precio».

---

## Títulos (español; escoge en la revisión)

1. **«¿Por qué todo está más caro? La historia del impuesto invisible»**
2. «La segunda ola de inflación: lo que cambió en 2026»
3. «Nadie te devolvió tu dinero: la verdad de la inflación»

## Miniaturas (tres candidatas, fórmula B)

1. **«+4,0%»** gigante tiza amarillo + surtidor dibujado + recibo asomando; eslogan corto «OTRA VEZ»
2. **«NADIE TE DEVOLVIÓ»** 3 palabras + mano abierta con billete arrugado
3. **«€2,50 → €4,10»** tira de recibo con flecha coral
4. **«+52% TU GAS»** (Países Bajos, gas natural oct-2026, CBS) — variante NL/EU; slab tiza «EN 12 MESES»

## Descripción lista para pegar (fuentes)

- BLS — CPI News Release (14-oct-2026): via cpiinflationcalculator.com · tradingeconomics.com
- CBS News — «September CPI report…» (14-oct-2026)
- Eurostat — Euro indicators flash de octubre 2026 (4-nov-2026) · Inflation in the euro area · renta real de los hogares (21-oct-2026)
- CBS NL — Inflatie in oktober 3,7% bij snelle raming (4-nov-2026); definitivo 10-nov-2026
- EIA / IEA — Strait of Hormuz: ~20% del consumo mundial de crudo; tráfico 20→2,7M b/d (feb-2026→); $78→$131 (8 días); ~20% LNG

## Notas de producción (para el paso de construcción — no ahora)

- 9 beats → 9 sub-composiciones (`compositions/01-ticket.html` … `09-outro.html`), stage dead-centre 1920×1080, count-ups en cada número.
- Datos: líneas HICP/IPC 2016–2026 desde CSV embebido (SVG en runtime); cada gráfico lleva su chip de fuente.
- Paleta B: pizarra `#10312B` · crema `#EDE6D3` · amarillo `#FFD84D` · coral `#FF6B57`; subrayados y círculos de tiza en precio clave.
- SFX mínimos: page-flip, stamp, sub-bass thud (numpy). Nada de crowd noises.
- Aprobación previa a render: VO (voz ES elegida por ti) → ajustes de diseño aquí → luego build.
